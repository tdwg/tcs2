#!/usr/bin/env python

import yaml
import pandas as pd
import markdown

# create data frame with terms from YAML file


def yaml_to_df(filename):
    f = open('../master/{filename}.yaml'.format(filename=filename), newline='')
    data = yaml.load(f, Loader=yaml.FullLoader)
    f.close()
    return pd.DataFrame.from_dict(data)

# create merged data frame


def create_df(termLists):
    for index, list in enumerate(termLists):
        df = yaml_to_df(list['filename'])
        df['namespace'] = list['vann_preferredNamespaceUri']
        df['namespaceAlias'] = list['vann_preferredNamespacePrefix']
        if index == 0:
            merged_df = df
        else:
            merged_df = pd.concat([merged_df, df])
        return merged_df

# create index of terms


def create_index(config, merged_df):
    text = '### Index of terms\n\n'

    if len(config['categories']) > 1:
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

    for category in config['categories']:
        if len(config['categories']) > 1:
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
    if colspan == 1:
        return '\t\t\t<{celltype}>{content}</{celltype}>'.format(content=content, celltype=celltype)
    else:
        return '\t\t\t<{celltype} colspan="{colspan}">{content}</{celltype}>'.format(content=content, celltype=celltype, colspan=colspan)

# create table row


def table_row(cells):
    return '\t\t<tr>\n{cells}\n\t\t</tr>\n'.format(cells='\n'.join(cells))

# create term table


def term_table(term):
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
        table_cell(markdown.markdown(comments))
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

    text += '\t</tbody>\n'
    text += '</table>\n\n'
    return text

# create vocabulary


def create_vocab(config, merged_df):
    vocab = '### Vocabulary\n\n'
    for category in config['categories']:
        if len(config['categories']) > 1:
            vocab += '#### {label}\n\n'.format(label=category['label'])
            filtered_df = merged_df[merged_df['organizedInClass']
                                    == category['namespace']]
        else:
            filtered_df = merged_df
        for index, row in filtered_df.iterrows():
            vocab += term_table(row)
    return vocab
