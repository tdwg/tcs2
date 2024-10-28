# Implementation experience report

No new features have been added in this revision of TCS. One of the main
objectives of the current effort is to make TCS useful again and all terms in
the current release are widely implemented in applications that are out there.
Terms for which a clear use case could not be identified have been left out of
this release.

A recent important application, the Catalog of Life Data Package (ColDP), has a
data model that is very similar to TCS and includes all TCS terms, the main
difference being that ColDP has a Synonym entity, which TCS does not. When TCS
is expressed in tabular form, a separate table is needed for synonyms, because
of the one-to-many relation between Taxon Concepts and Taxon Names (synonyms are
Taxon Names, just like accepted names), but there will be no identifiers for
synonyms. This is the same way the Name Relation in the ColDP schema works.

ColDP also offers a Name Usage entity "for simpler sharing". The "simpler
sharing" is probably because the ColDP Name Usage is essentially the Darwin Core
Taxon. When the names in a data set are unique, it is possible to roundtrip
between the two schemas of ColDP—i.e., the schema with Taxon and Name and the
schema with Name usage—and between TCS and Darwin Core.

TCS can play the same role for the Darwin Core Taxon that the Darwin Core IRI
(`dwciri`) namespace has for the other Darwin Core entities. Moreover the TCS
Nomenclatural Type can be used as the object for the `dwciri:typeStatus`
property.

<br/>

![alt text](media/taxon-concepts.png)

**Fig. 1.** Taxon concepts (green dots) with their according-to (blue dots) and
all associated names (orange dots). Taxon Concepts are connected to names via
the `taxonName` and `synonym` properties and Taxon Names are connected to each
other through the `basionym` and `replacedName` properties. **A.** Dicranoloma
assimile sec. Klazenga 1999, **B.** Dicranum assimile sec. Norris & Koponen
1990, **C.** Dicranoloma assimile sec. Tan 1989, **D.** Dicranooloma assimile sec.
Eddy 1988, **E.** Dicranoloma assimile sec. Tan & Koponen 1983.

<hr/>

![](media/taxon-concepts-taxon-names-references.svg)

**Fig. 2.** Graph with all Taxon Concepts, Taxon Names and references.

<hr>

![](media/taxon-concepts-taxon-names.svg)

**Fig. 3.** Graph with all Taxon Concepts, Taxon Names and references.

<hr>

![alt text](media/taxon-name-relations.png)

**Fig. 4.** Taxon Names and their relationships. **A.** Name without other
combinations, **B.** basionym with two combinations, **C.** replacement name and
replaced name, both of which are the basionym of another combination, **D.**
replacement name of which the replaced name is the replacement name of another
name.

<hr>

![alt text](media/taxon-name-relations-2.png)

**Fig. 5.** Same Taxon Name graphs as in the previous figure, but with
`originalName` property connecting combinations to the same "original name".

<hr>

![alt text](media/mapping-by-name-examples.png)

**Fig. 6.** Examples of Taxon Concept Mappings using type specimens of names
that the concepts apply to. **==**: `isCongruentWith`; **>**: `includes`; **<**:
`isIncludedIn`; **><**: `partiallyOverlaps`. **A ∩ B**: specimens included in
both subject and object Taxon Concepts; **A – B**: specimens included in the
subject Taxon Concept but not in the object Taxon Concept; **B – A**: specimens
included in the object Taxon Concept but not in the subject Taxon Concept.

<hr>

![](media/ostensive-mappings.svg)

**Fig. 4** Taxon Concepts with mappings based on the type specimens of names
that are included in the concepts.

<hr>

![](media/intensional-mappings.svg)

**Fig. 5.** Taxon Concept with mappings that were added to the data set by the
author of the latest revision.

<hr>

![](media/intensional-mappings-groups.svg)

**Fig. 6.** Taxon Concepts with individual Taxon Concepts (green dots) connected
to "group concepts" (light-brown dots), which are representative for groups of
Taxon Concepts that are congruent with each other, through `isCongruentWith`
mappings and group concept are connected to each other by other intersecting
mapping relations.

<hr>

![alt text](media/taxon-concepts-treatments.png)

**Fig. 7.** Groups of TaxonConcepts connected by intensional mappings, with
concepts for each treatment highlighted in red. **A.** Tan & Koponen 1983,
**B.** Eddy 1988, **C.** Tan 1989, **D.** Norris & Koponen 1990, **E.** Klazenga
1999.

<hr>

![](media/intensional-mappings-higher-classification.svg)

**Fig. 8.** Intersecting groups of Taxon Concepts with the concepts in the
latest taxonomy (red dots) connected to higher-taxon concepts (yellow dots)
through `parent` relations.

<hr>

![alt text](media/ostensive-groups-classification.png)

**Fig. 9.** Groups of intersecting Taxon Concepts based on ostensive mappings,
without (**A**) and with (**B**) classification.

<hr>

![alt text](media/ostensive-groups-classification-corrected.png)

**Fig. 10.** As previous figure, but with intersections caused by
misidentifications removed.