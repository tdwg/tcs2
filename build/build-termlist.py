#!/usr/bin/env python

# import libraries
import yaml
import vocab_build_tools as tools

# import configuration
stream = open('./config.yaml', 'r')

documents = yaml.load_all(stream, Loader=yaml.FullLoader)

# create markdown documents
for config in documents:
    print(config['outFileName'])

    merged_df = tools.create_df(config['termLists'])
    term_index = tools.create_index(config, merged_df)
    vocab = tools.create_vocab(config, merged_df)
    text = term_index + vocab

    headerObject = open(config['headerFileName'], 'rt', encoding='utf-8')
    header = headerObject.read()
    headerObject.close()

    footerObject = open(config['footerFileName'], 'rt', encoding='utf-8')
    footer = footerObject.read()
    footerObject.close()

    output = header + text + footer
    outputObject = open(config['outFileName'], 'wt', encoding='utf-8')
    outputObject.write(output)
    outputObject.close()
