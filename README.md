# The Taxon Concept Standard

The Taxon Concept Standard (TCS), is the TDWG standard for exchange of taxonomic
and nomenclatural data. Formerly an XML Schema, and called Taxon Concept Schema,
TCS is now a vocabulary standard with terms that can be used in many formats,
including CSV, JSON and RDF, and for individual objects as well as entire data
sets. TCS can be used alongside or instead of the Darwin Core Taxon class. It
defines Taxon Concept, Taxon Name, Taxon Concept Mapping and Nomenclatural Type
classes, which provide a semantic framework for, and allow more accurate
transfer of, taxonomic and nomenclatural data.

TCS is maintained by the [Taxon Concept Standard Maintenance
Group](https://www.tdwg.org/standards/tcs/#maintenance-group) in this
repository.

## Getting started

- [TCS Term List](https://tdwg.github.io/tcs2/terms/) — The normative list of TCS terms. This document
  defines and describes all TCS terms and provides guidance on how to use them.

- [TCS 2 Feature report](https://tdwg.github.io/tcs2/feature-report/) — A Feature Report is one of two
  documents that have to accompany major enhancements to TDWG standards,
  according to the Vocabulary Maintenance Standard
  ([[vocabulary_maintenance_specification_task_group_vocabulary_2017](https://tdwg.github.io/tcs2/bibliography/#[vocabulary_maintenance_specification_task_group_2017])]).
  The _TCS 2 Feature Report_ sets out why TCS 2 was necessary and describes the
  changes from TCS 1 to TCS 2. It also places TCS in the TDWG ecosystem and
  broader context.

- [TCS 2 Implementation experience report](https://tdwg.github.io/tcs2/implementation-experience-report/)
  — The _TCS 2 Implementation Experience Report_ describes how parts of TCS have
  already been implemented and provides a worked out example that highlights the
  TCS Taxon Concept Mappings, a feature of TCS that is not used as often as we
  would like it to be.

- [Examples](https://tdwg.github.io/tcs2/examples/) — All the examples that are referenced in the _TCS
  Term List_. Examples are focused on individual terms, but do provide some
  context.

- [Recipes](https://tdwg.github.io/tcs2/recipes/) — Recipes are longer examples that focus on complete
  records and show how TCS can be applied to real-world situations. There are
  recipes for some taxonomic revisions, including the one example that shipped
  with TCS 1, a checklist, a page from the Catalogue of Life and entries from
  AviBase. Also, some examples of how to use TCS in combination with Darwin
  Core, for identifications and nomenclatural type designations, are included.

- [Bibliography](https://tdwg.github.io/tcs2/bibliography/) — The references cited on this website.

## Structure of this repository

In the structure below `:` means manually maintained and `+` means generated. Generated documents should not be edited manually. 

```
├── build
│   ├── static                           : Headers and footers for generated files
│   ├── build-termlist.py                : Main build script for the documentation
│   ├── config.yaml                      : Configuration for the build; sets locations for files, etc.
│   └── vocab_build_tools.py             : Functions used for building documentation
│
├── docs
│   ├── _data
│   │   ├── footer.yml
│   │   └── navigation.yml
│   ├── bibliography
│   │   └── index.md                     : Bibliography page
│   ├── examples                         + Examples folder
│   │   ├── index.md                     + Examples index                         
│   │   └── ....md                       + Example files
│   ├── feature-report
│   │   └── index.md                     : Feature Report page
│   ├── implementation-experience-report
│   │   ├── index.md                     : Implementation Experience Report page
│   │   └── media                        : Images used in Implementation Experience Report
│   ├── media
|   ├── recipes                          : Recipes folder
│   └── terms
│       └── index.md                     + Term List 
│
├── examples                             : Examples in TTL and JSON 
│
├── master                               : Master files from which all documentation is generated
|   ├── README.md
|   ├── dcterms-for-tcs.yaml             : Terms borrowed from Dublin Core                   
|   ├── dwc-for-tcs.yaml                 : Terms borrowed from Darwin Core 
|   └── tcs.yaml                         : Terms defined in TCS
│
└── recipes                              : Recipes in TTL and JSON     
```

