# TCS 2 Task Group

Welcome to the repository of the TCS 2 Task Group. The TCS 2 Task Group ([charter](https://github.com/tdwg/tnc/blob/master/charters/tcs-2-task-group-charter.md)) was established, under the Taxon Names and Concepts Interest Group, by the TDWG Executive in March 2021, in order to develop the new version of the Taxon Concept Schema (TCS).

The [Taxon Concept Schema](https://www.tdwg.org/standards/tcs/) is the TDWG standard for the exchange of information on the definition of taxa, or taxon concepts. It was ratified at the TDWG Conference in Leningrad in 2006. It is one of a group of TDWG standards, including also the [Access to Biological Collections Data Schema (ABCD)](https://www.tdwg.org/standards/abcd/) and the [Structured Descriptive Data Schema (SDD)](https://www.tdwg.org/standards/sdd/), ratified around the same time, that are based on an [XML Schema](https://www.w3.org/TR/xmlschema-0/). Unfortunately, TCS has never enjoyed much take-up, probably mainly because of the restrictions imposed by the XML Schema. The [Taxon Name](https://github.com/tdwg/ontology/blob/master/ontology/voc/TaxonName.rdf) and [Taxon Concept](https://github.com/tdwg/ontology/blob/master/ontology/voc/TaxonConcept.rdf) parts of the [TDWG LSID Ontology](https://github.com/tdwg/ontology/), which were a reframing of TCS in RDF, have found some more usage and were in fact considered the most useful parts of the TDWG Ontology. However, with the demise of the TDWG Ontology, and especially since the ratification of [Darwin Core](https://dwc.tdwg.org/), which allows for the exchange of taxon definition information in a variety of formats, including CSV, in 2010, most of the exchange of taxon definition information has been done in Darwin Core.

After the Interest Group meeting at the SPNHC–TDWG Joint Conference in Dunedin in 2018, where the shortcomings of Darwin Core with respect to the exchange of taxon definition information were discussed, the Taxon Name and Concept Interest Group started a review of TCS, which eventually led to the establishment of the TCS 2 Task Group.

The purpose of the Task Group is to recast TCS into a vocabulary standard, like Darwin Core and [Audubon Core](https://ac.tdwg.org/), that can be maintained and documented under the [Vocabulary Maintenance Standard](https://github.com/tdwg/vocab/tree/master/vms) and the [Standards Documentation Standard](https://github.com/tdwg/vocab/tree/master/sds). It is expected that TCS 2 will not replace the Darwin Core Taxon class, but rather complement Darwin Core. The tasks of the Task Group are:

- Turn the TCS XML Schema into a set of classes and properties
- Update, improve and/or provide definitions for all terms
- Provide controlled vocabularies for properties that would benefit from them.

While in principle we will not be adding new terms at this stage, we might come up with better names for terms if that does not change the meaning of the term significantly. We also might, at the discretion of the Task Group, add new terms if we can get agreement on them easily. On the other hand, we might leave out – for the moment – some terms that are currently in TCS, which are not straightforward and for which we do not have a strong use case yet. The objective is to get a standard that people can use and that can be maintained as soon as possible. Resolving any perceived problems in TCS, or making significant additions, will be much easier when they can be discussed in isolation and we have a framework to work within.

## Core members

- Vijay Barve, Natural History Museum, Los Angeles County, USA
- Thierry Bourgoin - Muséum national de l'Histoire naturelle, France
- Markus Döring - Global Biodiversity Information Facility, Germany
- Anne Fuchs - Centre for Australian National Biodiversity Research, Australia
- Niels Klazenga – Royal Botanic Gardens Victoria / Atlas of Living Australia, Australia (chair)
- Johan Liljeblad – SLU Swedish Species Information Centre, Sweden
- Carlos Martínez Muñoz - Senckenberg Gesellschaft für Naturforschung, Germany
- Mieke Strong - Gaia Resources, Australia
- Campbell Webb – University of Alaska Museum of the North, USA
- Greg Whitbread – Taxamatics, Australia

## Getting involved

All the work of the Task Group is done in this GitHub repository, especially in the [issues](https://github.com/tdwg/tcs2/issues), where we have created an issue for each term, so the best way of becoming involved in developing the next version of TCS is to watch this repository and participate in the discussions around each term. We also have meetings via WebEx, which we cannot announce as publicly as before, so, if you want to become even more involved, please contact the chair of the Task Group, so you'll receive the invitations.



![](assets/tcs_diagram.svg)



**Figure 1.** Mind model of what the new version of TCS might look like and how the classes could relate to each other and to external classes. Data types and connectors will not make it into the standard, so other relationships will be possible.

