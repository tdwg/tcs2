import markdown
import pandas as pd
import yaml
import re


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
    text = '\n\n## 4. Index of terms\n\n'

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
                namespaceAlias=row['namespaceAlias'], localName=row['localName'].lower())

            item = f'[{label}]({anchor})'
            items.append(item)
        text += ' |\n'.join(items) + '\n\n'

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

    curie = '{namespaceAlias}:{localName}'.format(
        namespaceAlias=term['namespaceAlias'], localName=term['localName'])
    
    id = curie.replace(':', '_').lower()

    text += f"""
    <thead>
        <th colspan="2"><a id="{id}"></a>Term Name: {curie}</th>
    </thead>
    """


    text += '<tbody>\n'

    # Term IRI
    uri = '{namespace}{localName}'.format(
        namespace=term['namespace'], localName=term['localName'])
    text += table_row([
        table_cell('Identifier'),
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

    # Definition
    definition = term['definition'] if term['definition'] else ""
    text += table_row([
        table_cell('Definition'),
        table_cell(markdown.markdown(definition))])

    # Usage
    if 'usage' in term and isinstance(term['usage'], str):
        try: 
            usage = term['usage'] if term['usage'] else ""
            text += table_row([
                table_cell('Usage'),
                table_cell(markdown.markdown(usage))
            ])
        except: 
            print(term['localName'])
            print(term['usage'])

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

    # Controlled term
    if 'Concept' in term['type']:
        text += table_row([
            table_cell('Controlled value'),
            table_cell(term['controlled_value_string'])
        ])

    # Comments/Notes
    if term['notes']:
        comments = term['notes']
        text += table_row([
            table_cell('Comments'),
            table_cell(markdown.markdown(comments))
        ])
        
        

    # Examples
    if 'examples' in term: 
        if isinstance(term['examples'], list):
            examples = []
            # for ex in term['examples']:
            #     links = add_links(ex)
            #     examples.append(links)
            
            # examples_text = ''
            # for idx, ex in enumerate(term['examples']):
            #     if idx == 0:
            #         examples_text += '\n'
            #         examples_text += add_example(ex, False)
            #         examples_text += '\n'
            # examples_text += '\n'.join(examples)

            for ex in term['examples']:
                examples.append(add_example_link(ex))
            examples_text = '\n'.join(examples) 
                
            text += table_row([
                table_cell('Examples'),
                # table_cell(examples_text)
                table_cell(f"<ul>\n{examples_text}\n</ul>\n")
            ])
        elif isinstance(term['examples'], str):
            with open('../examples/' + term['examples'], 'r') as f:
                examples = f.read()
            text += table_row([
                table_cell('Examples'),
                table_cell(markdown.markdown(examples))
            ])
                

    # Github issue
    # if 'github' in term and not pd.isna(term['github']):
    #     text += table_row([
    #         table_cell('GitHub issue'),
    #         table_cell(
    #             'https://github.com/tdwg/tcs2/issues/{github}'.format(github=int(term['github'])))
    #     ])

    text += '\t</tbody>\n'
    text += '</table>\n\n'

    return text

def add_example(ex, links=True):
    file_name = '../examples/' + ex + '.ttl'
    with open(file_name, 'r') as examplefile:
        example = examplefile.read()
        example = re.sub(r'@.*> ?. *\n', '', example).strip()
    text = '\n```turtle\n'
    text += example
    text += '\n```\n\n'
    if (links):
        text += add_links(ex)
    return text

def add_links(ex):
    text = '[&#91;TurTLe&#93;](https://github.com/tdwg/tcs2/blob/master/examples/' + ex + '.ttl)&nbsp;'
    text += '[&#91;JSON-LD&#93;](https://github.com/tdwg/tcs2/blob/master/examples/' + ex + '.jsonld)\n\n'
    return text

def add_example_link(ex):
    return f"<li><a href=\"../examples/{ex}.html\">{ex}</a></li>\n"
    


# create vocabulary

def create_vocab(categories, merged_df):
    """Create vocabulary

    Args:
        categories (list<dict>): categories (from the config.)
        merged_df (pandas.DataFrame): data frame with terms

    Returns:
        str: vocabulary in HTML format
    """
    # vocab = '## Vocabulary\n\n'
    vocab = '## 5. Vocabulary\n\n'
    for index, category in enumerate(categories, start=1):
        if len(categories) > 1:
            vocab += '### 5.{index}. {label}\n\n'.format(label=category['label'], index=index)
            filtered_df = merged_df[merged_df['organizedInClass']
                                    == category['namespace']]
        else:
            filtered_df = merged_df
        for index, row in filtered_df.iterrows():
            vocab += term_table(row)
    return vocab


def create_examples_page(config):
    merged_df = create_df(config['termLists'])
    examples = merged_df[~merged_df['examples'].isna()]

    classes = ['TaxonConcept', 'TaxonConceptMapping', 'TaxonName', 'NomenclaturalType']
    
    with open('./static/examples-header.md', 'r') as f:
        header = f.read()

    with open('../docs/examples/README.md', 'w') as f:
        
        f.write(header)
        
        f.write('## Index\n\n')
        
        for cl in classes:
            egs = []
            for index, row in examples[examples['organizedInClass'] == 'http://rs.tdwg.org/tcs/terms/' + cl].iterrows():
                if type(row['examples']) == list:
                    egs.append({
                        'namespace': row['namespace'],
                        'localName': row['localName'],
                        'examples': row['examples']
                    })
            
            if len(egs):
                f.write('### ' + cl + '\n\n')
                
                terms = []
                for row in egs:
                    alias = [n['vann_preferredNamespacePrefix'] for n in config['termLists'] if n['vann_preferredNamespaceUri'] == row['namespace']][0]
                    localName = row['localName']
                    items = []
                    for ex in row['examples']:
                        items.append(f'[{ex}](#{ex})')
                    terms.append(f'**{alias}:{localName}:** ' + ' &bull; '.join(items))
                f.write(' | '.join(terms))
                f.write('\n\n')

        for cl in classes:
            
            egs = []
            for index, row in examples[examples['organizedInClass'] == 'http://rs.tdwg.org/tcs/terms/' + cl].iterrows():
                if type(row['examples']) == list:
                    egs.append({
                        'namespace': row['namespace'],
                        'localName': row['localName'],
                        'examples': row['examples']
                    })
            
            if len(egs):
                f.write("\n## " + cl + "\n\n")
                
                for row in egs:
                    alias = [n['vann_preferredNamespacePrefix'] for n in config['termLists'] if n['vann_preferredNamespaceUri'] == row['namespace']][0]
                    f.write("\n### " + alias + ":" + row['localName'] + "\n\n") 
                
                    for ex in row['examples']:
                        if ex[:len(cl)+1] == cl + '-':
                            f.write('#### ' + ex)
                            text = add_example(ex)
                            f.write(text)
                        
def create_sssom_page(config):
    merged_df = create_df(config['termLists'])
    mappings = merged_df[~merged_df['mappings'].isna()]

    classes = ['TaxonConcept', 'TaxonConceptMappings', 'TaxonName', 'NomenclaturalType']

    with open('./static/mappings-header.md', 'r') as f:
        header = f.read()

    with open('../docs/sssom_mappings/README.md', 'w') as f:
        
        f.write(header)
        
        for cl in classes:
            f.write("\n## " + cl + "\n\n")
            
            for index, row in mappings[mappings['organizedInClass'] == 'http://rs.tdwg.org/tcs/terms/' + cl].iterrows():
                alias = [n['vann_preferredNamespacePrefix'] for n in config['termLists'] if n['vann_preferredNamespaceUri'] == row['namespace']][0]
                f.write("\n### " + alias + ":" + row['localName'] + "\n\n") 
                
                f.write("| predicate | IRI or XPATH | remarks |\n")
                f.write("|-|-|-|\n")
                for m in row['mappings']:
                    f.write("| " + str(m['predicate']))
                    f.write(' | ' + str(m['iri'])\
                        .replace('tc:', 'http://rs.tdwg.org/ontology/voc/TaxonConcept#')\
                        .replace('tn:', 'http://rs.tdwg.org/ontology/voc/TaxonName#')\
                        .replace('dwc:', 'http://rs.tdwg.org/dwc/terms/')\
                        .replace('openbiodiv-o:', 'http://openbiodiv.net/')\
                        .replace('skos:', 'http://www.w3.org/2004/02/skos/core#')\
                        .replace('skosxl:', 'http://www.w3.org/2008/05/skos-xl#')\
                        .replace('frbr:', 'http://purl.org/spar/frbr/'))
                    if 'remarks' in m:
                        f.write(' | ' + str(m['remarks']))
                    else:
                        f.write(' | ')
                    f.write(' |\n')


def create_examples_index_page(config):
    merged_df = create_df(config['termLists'])
    examples = merged_df[~merged_df['examples'].isna()]

    classes = ['TaxonConcept', 'TaxonConceptMappings', 'TaxonName', 'NomenclaturalType']

    header_object = open('static/examples-header.md', 'rt', encoding='utf-8')
    header = header_object.read()
    header_object.close()

    with open('../docs/examples/index.md', 'w') as f:
        
        f.write(header)
        
        for cl in classes:
            f.write("\n## " + cl + "\n\n")
            
            for index, row in examples[examples['organizedInClass'] == 'http://rs.tdwg.org/tcs/terms/' + cl].iterrows():
                alias = [n['vann_preferredNamespacePrefix'] for n in config['termLists'] if n['vann_preferredNamespaceUri'] == row['namespace']][0]
                
                if type(row['examples']) == list:
                    f.write("\n### " + alias + ":" + row['localName'] + "\n\n")
                    for ex in row['examples']:
                        f.write(f"- [{ex}]({ex}.md)\n")

def create_example_pages(config):
    merged_df = create_df(config['termLists'])
    examples = merged_df[~merged_df['examples'].isna()]

    classes = ['TaxonConcept', 'TaxonConceptMappings', 'TaxonName', 'NomenclaturalType']

    for cl in classes:
        for index, row in examples[examples['organizedInClass'] == 'http://rs.tdwg.org/tcs/terms/' + cl].iterrows():
            alias = [n['vann_preferredNamespacePrefix'] for n in config['termLists'] if n['vann_preferredNamespaceUri'] == row['namespace']][0]
            
            if type(row['examples']) == list:
                for index, ex in enumerate(row['examples']):
                    with open('../docs/examples/' + ex + '.md', 'w') as f:
                        heading = ex.replace('-', ' ')
                        f.write('# ' + heading + '\n')
                        f.write('\n\n')
                        f.write('**Term:** ')
                        f.write('[' + alias + ':' + row['localName'] + '](../terms/#' + alias + '_' + row['localName'].lower() + ')')
                        f.write('\n\n')

                        if (len(row['examples']) > 1):
                            exs = []
                            for i, exx in enumerate(row['examples']):
                                if i == index:
                                    exs.append(exx)
                                else:
                                    exs.append(f'[{exx}](./{exx}.html)')
                            f.write(' | '.join(exs))

                        text = add_example(ex)
                        f.write(text)