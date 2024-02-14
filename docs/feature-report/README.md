# Feature report 

## Why do we need TCS 2?

> However, the object properties necessary to relate dwc:Taxon instances to name
> entities, references, parent taxa, and child taxa do not exist and the exact
> relationship between taxonomic entities such as taxon concepts, protonyms,
> taxon name usages, etc. has not been established using RDF. So the creation of
> functional dwc:Taxon instances described using RDF is not possible at the
> present time.

## Parameters

- stick to terms that are already available in TCS 1.
- borrow what we can from Darwin Core and other specifications

## Changes

While the version of the standard we are replacing is an XML Schema (XSD), our
work was mainly based on the TDWG Taxon Concept and Taxon Name LSID Ontologies,
which form a rather honest translation of the TCS XML Schema into OWL
ontologies.

The most important change we made was to dismantle the Taxon Relationship object
that both TCS 1 and the Taxon Concept Ontology have. We want TCS to be a
vocabulary standard, i.e. a set of terms and definitions, so TCS should not
prescribe a certain syntax. 

Another problem with a relationship object is that it obscures the precise
nature of the relationship. Not all relationship types in TCS 1 are
relationships between Taxon Concepts, some are relationships between Taxon
Concepts and Taxon Names. Also, relationships between Taxon Names in TCS 1 are
elements (owl:objectProperty in the TDWG Taxon Name LSID Ontology), while
relationships between Taxon Concepts (and some between Taxon Concepts and Taxon
Names) are values in an enumeration (owl:Class in the TDWG Taxon Concept LSID
Ontology).

By elevating the values from the Taxon Relationship type enumeration to
first-class TCS properties and leaving the syntax out of the standard, people
can choose whether to hang them off the subject Taxon Concept, or use them in a
utility object outside TCS, for example the Darwin Core Resource Relationship
class. The terms have the same meaning, no matter what syntax is used.

We currently recognise the following relations between the major objects in TCS:

### Relationships between taxa

#### Hierachical relationships

- tcs:parent

#### Horizontal relationships 

- tcs:isCongruentWith
- tcs:includes
- tcs:isIncludedIn
- tcs:partiallyOverlaps
- tcs:isDisjointWith
- tcs:intersects

Horizontal relationships between Taxon Concepts are relationships between Taxon
Concepts in different taxonomies (or different versions of a taxonomy).

### Relationships between taxa and names

- tcs:acceptedName
- tcs:synonym
- tcs:vernacularName

### Relationships between names

- tcs:basionym
- tcs:replacedSynonym
- tcs:spellingCorrectionOf
- tcs:conservedAgainst

<br/>

![](../media/context-tcs.jpg)

## Left out for now


## Context: SKOS and OpenBiodiv-O

![](../media/context-skos.jpg)

<br/>

| TCS | SKOS|
|-|-|
| **tcs:TaxonConcept** | **skos:Concept** |
| tcs:accordingTo | skos:inScheme |
| | |
| tcs:acceptedName | skosxl:prefLabel |
| tcs:synonym | skosxl:hiddenLabel |
| tcs:vernacularName | skosxl:altLabel |
| | |
| tcs:parent | skos:broader |
| | |
| tcs:isCongruentWith | skos:closeMatch |
| tcs:includes | skos:narrowMatch |
| tcs:isIncludedIn | skos:broadMatch |
| tcs:partiallyOverlaps | skos:relatedMatch |
| tcs:isDisjointWith | skos:relatedMatch |
| tcs:intersects | skos:relatedMatch |
| | |
| **tcs:TaxonName** | **skosxl:Label** |
| tcs:taxonNameString | skosxl:literalForm |
| | |
| tcs:basionym | skosxl:labelRelation |
| tcs:replacedSynonym | skosxl:labelRelation |
| tcs:conservedAgainst | skosxl:labelRelation |
| tcs:spellingCorrectionOf | skosxl:labelRelation |

<br/>

- Relationships between taxa are anologous to `skos:semanticRelation` properties
- Horizontal relationships between taxa are also analogous to
  `skos:mappingRelation` properties
- Relationships between taxa and names are analogous to the SKOS-XL labeling
  properties, `skosxl:prefLabel`, `skosxl:altLabel` and `skosxl:hiddenLabel`
- Relationships between names are analogous to the `skosxl:labelRelation`
  property.

<br/><br/>

![](../media/context-openbiodiv-o.jpg)

- The OpenBiodiv Ontology (OpenBiodiv-O) establishes the Taxonomic Concept as a
  Work under the FRBR (Functional Requirements for Bibliographic Records) data
  model. The Expression that realises this Work is the Treatment. While in FRBR
  a Work can have more than one Expression, there is a one-to-one relationship
  between Taxonomic Concepts and Treatment.

- At the same time the OpenBiodiv-O Taxonomic Concept is a SKOS Concept.

## Mapping

