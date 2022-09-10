import markdown
import pandas as pd
import yaml


# convert YAML to CSV


def yaml_to_df(in_filepath):
    """Create data frame from YAML

    Args:
        in_filepath (string): path to the YAML file

    Returns:
        pandas.DataFrame: data frame
    """
    f = open(in_filepath, newline='')
    data = yaml.load(f, Loader=yaml.FullLoader)
    f.close()
    return pd.DataFrame.from_dict(data)


def yaml_to_csv(in_filepath, outfile_path):
    """Convert YAML to CSV

    Args:
        in_filepath ([type]): [description]
        outfile_path ([type]): [description]
    """
    df = yaml_to_df(in_filepath)
    df.to_csv(outfile_path, index=False)


# create dictionary with terms from YAML file


def dict_from_yaml(termLists):
    """Create Python dictionary from one or more YAML term list files

    Args:
        termLists (List<Dict>): list of dictionaries that, at a minimum, have 
            the 'filename', 'vann_preferredNamespaceUri' and 
            'vann_preferredNamespacePrefix' keys (from the config.)

    Returns:
        List<Dict>: List of terms: each term is a dictionary
    """
    dicts = []
    for index, list in enumerate(termLists):
        f = open(
            '../master/{filename}.yaml'.format(filename=list['filename']), newline='')
        data = yaml.load(f, Loader=yaml.FullLoader)
        data = [dict(item, namespace=list['vann_preferredNamespaceUri'])
                for item in data]
        data = [dict(item, namespaceAlias=list['vann_preferredNamespacePrefix'])
                for item in data]
        dicts += data
    return dicts

# create data frame from dictionary


def create_df(termLists):
    """Create Pandas data frame from list of dictionaries

    Args:
        termLists (List<Dict>): list of dictionaries that, at a minimum, have 
            the 'filename', 'vann_preferredNamespaceUri' and 
            'vann_preferredNamespacePrefix' keys (from the config.)

    Returns:
        pandas.DataFrame: data frame with terms
    """
    dict = dict_from_yaml(termLists)
    return pd.DataFrame.from_dict(dict)

# create index of terms


def create_index(categories, merged_df):
    """Create index of terms

    Args:
        categories (List<Dict>): categories from the config.
        merged_df (pandas.DataFrame): data frame with terms

    Returns:
        string: index of terms in Markdown format
    """
    text = '\n### Index of terms\n\n'

    if len(categories) > 1:
        text += '**classes**\n\n'

        items = []
        for index, row in merged_df[merged_df['type'].str.contains('Class')].iterrows():
            label = '{namespaceAlias}:{localName}'.format(
                namespaceAlias=row['namespaceAlias'], localName=row['localName'])
            anchor = '#{namespaceAlias}_{localName}'.format(
                namespaceAlias=row['namespaceAlias'], localName=row['localName'])
            item = '[{label}]({anchor})'.format(label=label, anchor=anchor)
            items.append(item)
        text += ' | '.join(items) + '\n\n'

    for category in categories:
        if len(categories) > 1:
            text += '**{label}**\n\n'.format(label=category['label'])
            filtered_df = merged_df[merged_df['organizedInClass']
                                    == category['namespace']]
        else:
            filtered_df = merged_df

        items = []
        for index, row in filtered_df.iterrows():
            if 'Class' in row['type'] or 'Property' in row['type']:
                label = '{namespaceAlias}:{localName}'.format(
                    namespaceAlias=row['namespaceAlias'],
                    localName=row['localName']
                )
            else:
                label = '{label}'.format(label=row['label'])

            anchor = '#{namespaceAlias}_{localName}'.format(
                namespaceAlias=row['namespaceAlias'], localName=row['localName'])

            if 'Class' not in row['type']:
                item = '[{label}]({anchor})'.format(label=label, anchor=anchor)
                items.append(item)
        text += ' | '.join(items) + '\n\n'

    return text

# create table cell


def table_cell(content, celltype='td', colspan=1):
    """Create HTML <td/> or </th> element

    Args:
        content (str): content to go into the cell
        celltype (str, optional): The type of cell: 'td' or 'th'. Defaults to 'td'.
        colspan (int, optional): Number of columns the cell should span. Defaults to 1.

    Returns:
        str: HTML table cell (<td)
    """
    if colspan == 1:
        return '\t\t\t<{celltype}>{content}</{celltype}>'.format(content=content, celltype=celltype)
    else:
        return '\t\t\t<{celltype} colspan="{colspan}">{content}</{celltype}>'.format(content=content, celltype=celltype, colspan=colspan)

# create table row


def table_row(cells):
    """Create HTML <tr/> element

    Args:
        cells (List<str>): list of table cell elements

    Returns:
        str: HTML table row (</tr>)
    """
    return '\t\t<tr>\n{cells}\n\t\t</tr>\n'.format(cells='\n'.join(cells))

# create term table


def term_table(term):
    """Create HTML table for single term

    Args:
        term (dict): term dictionary (row from lerm list data frame)

    Returns:
        str: HTML table (<table/>) with term metadata
    """
    text = '<table>\n'

    # table header
    curie = '{namespaceAlias}:{localName}'.format(
        namespaceAlias=term['namespaceAlias'], localName=term['localName'])
    curieAnchor = curie.replace(':', '_')
    term_type = term['type'][term['type'].find('#')+1:]
    if term_type == 'Concept':
        tableHeader = '<a id="{anchor}"></a>{term_type} {curie} ({label})'.format(
            curie=curie, anchor=curieAnchor, term_type=term_type, label=term['label'])
    else:
        tableHeader = '<a id="{anchor}"></a>{term_type} {curie}'.format(
            curie=curie, anchor=curieAnchor, term_type=term_type)
    text += '\t<thead>\n'
    text += table_row([table_cell(tableHeader, celltype='th', colspan=2)])
    text += '\t</thead>\n'

    text += '\t<tbody>\n'

    # Term IRI
    uri = '{namespace}{localName}'.format(
        namespace=term['namespace'], localName=term['localName'])
    text += table_row([
        table_cell('Term IRI'),
        table_cell(uri)
    ])

    # Type
    text += table_row([
        table_cell('Type'),
        table_cell(term['type'])
    ])

    # Label
    text += table_row([
        table_cell('Label'),
        table_cell(term['label'])
    ])

    # Attributes
    if 'Property' in term['type']:
        required = "Yes" if term['required'] else "No"
        repeatable = "Yes" if term['repeatable'] else "No"
        attrs = '<b>required:</b> {required} — <b>repeatable:</b> {repeatable}'.format(
            required=required, repeatable=repeatable)
        text += table_row([
            table_cell(''),
            table_cell(attrs)
        ])

    # Definition
    definition = term['definition'] if term['definition'] else ""
    text += table_row([
        table_cell('Definition'),
        table_cell(markdown.markdown(definition))])

    # Usage
    usage = term['usage'] if term['usage'] else ""
    text += table_row([
        table_cell('Usage'),
        table_cell(markdown.markdown(usage))
    ])

    # Comments/Notes
    comments = term['notes'] if term['notes'] else ""
    text += table_row([
        table_cell('Comments'),
        table_cell(markdown.markdown(comments, extensions=['nl2br']))
    ])

    # Examples
    if 'examples' in term:
        examples = term['examples'] if term['examples'] else ""
        text += table_row([
            table_cell('Examples'),
            table_cell(markdown.markdown(examples))
        ])

    # Controlled term
    if 'Concept' in term['type']:
        text += table_row([
            table_cell('Controlled value'),
            table_cell(term['controlled_value_string'])
        ])

    # Github issue
    if 'github' in term and not pd.isna(term['github']):
        text += table_row([
            table_cell('GitHub issue'),
            table_cell(
                'https://github.com/tdwg/tcs2/issues/{github}'.format(github=int(term['github'])))
        ])

    text += '\t</tbody>\n'
    text += '</table>\n\n'
    return text

# create vocabulary


def create_vocab(categories, merged_df):
    """Create vocabulary

    Args:
        categories (list<dict>): categories (from the config.)
        merged_df (pandas.DataFrame): data frame with terms

    Returns:
        str: vocabulary in HTML format
    """
    vocab = '### Vocabulary\n\n'
    for category in categories:
        if len(categories) > 1:
            vocab += '#### {label}\n\n'.format(label=category['label'])
            filtered_df = merged_df[merged_df['organizedInClass']
                                    == category['namespace']]
        else:
            filtered_df = merged_df
        for index, row in filtered_df.iterrows():
            vocab += term_table(row)
    return vocab
