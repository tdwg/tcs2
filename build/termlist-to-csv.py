import yaml
import re
import csv

"""
Removes images, converts double linebreaks to paragraph marks, converts
whitespace to single space and trims the string; used for definitions, usage and
notes
"""
def clean_up_text(text):
    text = re.sub(r"\!\[\]\([^\)]+\)", '', text)
    text = text.replace('\n\n', '¶')
    text = re.sub(r"\s+", ' ', text)
    return text.strip()

"""
Turns examples in a pipe-separated list of hyperlinks
"""
def process_examples(content, glue=' | '):
    examples = []
    for item in content:
        examples.append(f'https://tdwg.github.io/tcs2/examples/{item}.html')
    return glue.join(examples)


"""
Convert a single term list to a CSV file
"""
def convert_term_list_to_csv(filename):
    with open(f'../master/{filename}.yaml', 'r') as stream:
        terms = yaml.load(stream, Loader=yaml.FullLoader)

        csv_terms = []

        for term in terms:
            csv_terms.append({
                'term_localName': term['localName'],
                'label': term['label'],
                'definition': clean_up_text(term['definition']) if term['definition'] else None,
                'usage': clean_up_text(term['usage']) if term['usage'] else None,
                'notes': clean_up_text(term['notes']) if term['notes'] else None,
                'examples': process_examples(term['examples']) if 'examples' in term and term['examples'] else None,
                'definition_derived_from': None,
                'type': term['type'],
                'tdwgutility_organizedInClass': term['organizedInClass']
            })

    with open(f'rs.tdwg.org/{filename}.csv', 'w', newline='') as csvfile:
        fieldnames = [
            'term_localName',
            'label',
            'definition',
            'usage',
            'notes',
            'examples',
            'definition_derived_from',
            'type',
            'tdwgutility_organizedInClass'
        ]

        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for term in csv_terms:
            writer.writerow(term)


stream = open('./config.yaml', 'r')
config = yaml.load(stream, Loader=yaml.FullLoader)
for termList in config['termLists']:
    convert_term_list_to_csv(termList['filename'])
