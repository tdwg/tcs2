# Implementation experience report

No new features have been added in this revision of TCS. One of the main
objectives of the current effort is to make TCS useful again and all terms in
the current release are widely implemented in applications that are out there.
Terms for which a clear use case could not be identified have been left out of
this release.

A recent important development, the Catalogue of Life Data Package (ColDP), has
a data model that is very similar to TCS and includes all TCS terms, the main
difference being that ColDP has a Synonym entity, which TCS does not. When TCS
is expressed in tabular form, a separate table is needed for synonyms, because
of the many-to-many relation between Taxon Concepts and Taxon Names (synonyms,
like accepted names (`taxonName`), are Taxon Names), but there should be no
identifiers for synonyms. This is the same way the Name Relation in the ColDP
schema works.

ColDP also offers a Name Usage entity "for simpler sharing". The "simpler
sharing" is probably because the ColDP Name Usage is essentially the Darwin Core
Taxon. When the names in a data set are unique, it is possible to roundtrip
between the two schemas of ColDP—i.e., the schema with Taxon and Name and the
schema with Name Usage—and between TCS and Darwin Core.

TCS can play the same role for the Darwin Core Taxon that the Darwin Core IRI
(`dwciri`) namespace has for the other Darwin Core entities. Moreover the TCS
Nomenclatural Type can be used as the object for the `dwciri:typeStatus`
property.