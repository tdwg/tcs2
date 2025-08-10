# Taxon Concept Standard (TCS) Term List

**Title**
: Taxon Concept Standard (TCS) Term List

**Date version created**
: 2025-08-09

**Part of TDWG standard**
: http://www.tdwg.org/standards/117

**This version**
: http://rs.tdwg.org/tcs/doc/terms/2025-08-09

**Latest version**
: http://rs.tdwg.org/tcs/doc/terms

**Abstract**
: The Taxon Concept Standard (TCS) is the TDWG standard specifically
for sharing taxonomic and nomenclatural data. TCS provides TaxonConcept and
TaxonName classes for information about taxon concepts and taxon names,
respectively, as well as a TaxonConceptMapping class for taxon concept
alignments and a NomenclaturalType class for information on typification of
taxon names. TCS offers a semantic framework for, and facilitates more accurate
exchange of, taxonomic and nomenclatural data.

**Contributors**
: Niels Klazenga [![](../media/orcid_16x16.gif)](https://orcid.org/0000-0003-2224-6821) (Royal Botanic Gardens Victoria, Australia/Atlas of Living Australia, Australia),
Greg Whitbread [![](../media/orcid_16x16.gif)](https://orcid.org/0000-0002-2954-9027) (Taxamatics, Australia),
Vijay Barve  [![](../media/orcid_16x16.gif)](https://orcid.org/0000-0002-4852-2567) (Natural History Museum of Los Angeles County, USA),
Thierry Bourgoin [![](../media/orcid_16x16.gif)](https://orcid.org/0000-0001-9277-2478) (Museum national Histoire naturelle Paris, France),
Markus Döring [![](../media/orcid_16x16.gif)](https://orcid.org/0000-0001-7757-1889) (GBIF, Denmark/Catalogue of Life, The Netherlands),
Anne Fuchs [![](../media/orcid_16x16.gif)](https://orcid.org/0000-0001-5737-8803) (Centre for Australian National Biodiversity Research, Australia),
Jeff Gerbracht (Cornell Lab of Ornithology, USA),
Johan Liljeblad [![](../media/orcid_16x16.gif)](https://orcid.org/0000-0003-0442-8162) (Swedish Species Information Centre, Sweden),
Carlos Martínez Muñoz,
Mieke Strong [![](../media/orcid_16x16.gif)](https://orcid.org/0009-0004-5278-4238) (Gaia Resources, Australia),
William Ulate [![](../media/orcid_16x16.gif)](https://orcid.org/0000-0003-2863-2491) (Missouri Botanical Garden, USA),
Cam Webb [![](../media/orcid_16x16.gif)](https://orcid.org/0000-0003-1031-3249) (University of Alaska Museum of the North, USA)

**Creator**
: TDWG Taxon Concept Schema (TCS) 2 Task Group

**Bibliographic citation**
: Taxon Concept Standard Maintenance Group (2025).
Taxon Concept Standard Term List. Biodiversity Information Standards (TDWG).

## 1. Introduction

### 1.1. Status of this document and its content

The **Introduction** in this document is informative and the **Namespace** and
**Borrowed terms** sections are normative. Within the **Vocabulary** section the
Identifier, Type, Definition and Usage for terms are normative. For borrowed
terms Usage is normative only in the sense that it specifies how the term should
be used within TCS. All other parts, including Label, Comments and Examples, are
informative. The assignment of properties to classes is also informative,
although most properties can only reasonably be used in the class in which they
are organised. For the properties that can be used in more than one TCS class
this has been indicated in the comments.

### 1.2. RFC keywords

The key words “MUST”, “MUST NOT”, “REQUIRED”, “SHALL”, “SHALL NOT”, “SHOULD”, 
“SHOULD NOT”, “RECOMMENDED”, “MAY”, and “OPTIONAL” in this document are to be 
interpreted as described in BCP 14 [RFC 2119] and [RFC 8174] when, and only 
when, they appear in all capitals, as shown here.

### 1.3. Structure of TCS

TCS has four main classes, **TaxonConcept**, **TaxonConceptMapping**,
**TaxonName** and **NomenclaturalType**.

The **TaxonConcept** class provides terms to share information about taxon
concepts and is the class everything else in TCS revolves around. We have
defined a **TaxonConcept** as:

> An **identifiable** taxonomic position that can be **aligned** to other such positions
> through TCS concept mapping relations

The change from the earlier 'a name plus a description of a taxon' was necessary
because TCS has to deal with a wider variety of taxon concepts and today's taxon
concepts do not necessarily have a formal scientific name or a description. In
order for a taxon concept to be identifiable, however, it needs to have some
kind of label and it has to have some sort of treatment, so the `taxonName` and
`accordingTo` properties on the `TaxonConcept` are required.

The **TaxonConceptMapping** class is almost identical in structure to the Darwin
Core `ResourceRelationship` class. As a taxon concept mapping is a very specific
type of resource relationship and because Darwin Core does not define IRI
properties for `dwc:ResourceRelationship`, TCS defines its own class. The
`subjectTaxonConcept`, `mappingRelation` and `objectTaxonConcept` are required
on a `TaxonConceptMapping`. The value of `mappingRelation` has to be one of the
mapping properties from the `TaxonConcept` class.

The **TaxonName** class encapsulates all information about taxon names. Only the
`nameString` property is required. Currently, TCS only has the one class
that can be used for all types of names, including scientific named and
vernacular names, but it is envisaged that in future TCS will also have classes
for specific categories of names, e.g., 'ScientificName' and 'VernacularName'.
The use of the **TaxonName** class is not currently required in TCS: it can be
replaced by a [SKOS-XL Label](https://www.w3.org/TR/skos-reference/skos-xl.html)
or [GBIF VernacularName](http://rs.gbif.org/terms/1.0/VernacularName) (or any
other label object) if considered more appropriate.

The **NomenclaturalType** class can be used to share information about
nomenclatural types of names. It also shows similarity to the Darwin Core
`ResourceRelationship` class in the sense that a nomenclatural type is a
resource relationship between a `tcs:TaxonName` and either another
`tcs:TaxonName` or a Specimen (for which we use the Darwin Core
`PreservedSpecimen` or `MaterialCitation` in the examples). The `typifiedName`,
`typeOfType` and either the `typeSpecimen` or `typeName` properties are
required.

In contrast to Darwin Core, TCS does not define 'ID' and 'Remarks' properties on 
its classes. In accordance with the Darwin Core RDF Guide
(Darwin Core and RDF/OWL Task Groups 2015 [\[darwin_core_and_rdfowl_task_groups_darwin_2015\]](../bibliography/#darwin_core_and_rdfowl_task_groups_darwin_2015)), instances of TCS
classes SHOULD have a `rdf:id` and MAY have a `rdfs:comment`.

Information on **synonymy** can be shared using the `synonym` property of the
TaxonConcept and the `basionym` and `replacedName` properties of the TaxonName.
TCS does not use the terms 'homotypic synonym' and 'heterotypic synonym' because
these terms are rather strictly defined in the nomenclatural codes, which makes
them less useful for data exchange, but `synonym` can be used for heterotypic
synonyms and `basionym` and `replacedName` for homotypic synonyms. The `synonym`
property can be used for all synonyms and it is up to data providers or
application profiles whether or not synonyms are split into homotypic and
heterotypic synonyms.

The mapping properties in the TaxonConcept class, `isCongruentWith`, `includes`,
`isIncludedIn`, `partiallyOverlaps`, `intersects` and `isDisjointFrom` can be
used to align taxon concepts. These properties are equivalent to topological
properties in spatial analysis and can be used in reasoning. Taxon concept
mappings are currently not used very often in taxonomic treatments but, besides
being more expressive and more generally applicable than nomenclatural
relationships, they have the advantage that they can be made by third parties,
so they can be used to add information to the analysis that is not already
present in the data.

### 1.4. Examples

Examples are provided for most TCS terms. As almost all TCS properties are IRI
properties, significant context has been added to make the examples as useful as
possible. As because of this the examples take up a lot of space they have been
placed in separate documents, which are linked to from this document.

The examples referenced in this document are in TurTLe. This format has been
chosen because it is very terse and still easy to read and, most importantly,
allows comments. The fact that the examples are in a serialization of RDF should
not be taken to mean that TCS data has to be RDF, just that it can be RDF. All
examples are also provided in JSON-LD.

## 2. Namespace

The namespace for TCS terms is `http://rs.tdwg.org/tcs/terms/`. The recommended
alias for this namespace is `tcs`.

## 3. Borrowed terms

As much as possible TCS uses already existing terms rather than define new
terms. Thus, many terms have been borrowed from Darwin Core and Dublin Core.

| Standard | Namespace | Alias |
|----------|-----------|-------|
| Darwin Core | http://rs.tdwg.org/dwc/terms/ | dwc |
| Dublin Core | http://purl.org/dc/terms/ | dcterms |