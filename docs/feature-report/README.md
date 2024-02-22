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
class. The data may dictate the use of a relationship object, but the terms have
the same meaning, regardless of the syntax.

We currently recognise the following relations between the major objects in TCS:

### Relationships between taxa

#### Hierarchical relationships

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

- tcs:taxonName
- tcs:synonym
- tcs:vernacularName

### Relationships between names

- tcs:basionym
- tcs:replacedSynonym
- tcs:spellingCorrectionOf
- tcs:conservedAgainst
- tcs:laterHomonymOf

<br/>

![](../media/context-tcs.jpg)

## Left out for now


## Context: SKOS and OpenBiodiv-O

![](../media/context-skos.jpg)

<br/>

**Table 1**: Mapping of TCS relations to SKOS terms

| TCS | SKOS|
|-|-|
| **tcs:TaxonConcept** | **skos:Concept** |
| tcs:accordingTo | skos:inScheme |
| | |
| tcs:taxonName | skosxl:prefLabel |
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
| tcs:laterHomonymOf | skosxl:labelRelation |

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

  > A **Work** is the product of an intellectual process of one or more persons,
  yet only indirect evidence about it is at our hands.

- At the same time the OpenBiodiv-O Taxonomic Concept is a SKOS Concept.

## Appendix 1: Mapping of TCS 1 and TDWG Ontology terms

### Taxon Concept

TCS 1 | TDWG Ontology | TCS 2
-|-|-
/DataSet/TaxonConcepts/TaxonConcept | [tc:TaxonConcept](https://github.com/tdwg/tnc/blob/5d3950009e2462e7d8c930dc08f4733738b9133d/tcs-docs/TaxonConcept.ttl#L36) | **[TaxonConcept](https://github.com/tdwg/tcs2/tree/master/docs/tcs-terms#tcstaxonconcept)**
/DataSet/TaxonConcepts/TaxonConcept/@type | &mdash; | &mdash;
/DataSet/TaxonConcepts/TaxonConcept/Rank | [tc:rankString](https://github.com/tdwg/tnc/blob/5d3950009e2462e7d8c930dc08f4733738b9133d/tcs-docs/TaxonConcept.ttl#L142) | [dwc:verbatimTaxonRank](https://github.com/tdwg/tcs2/tree/master/docs/tcs-terms#dwcverbatimtaxonrank)
/DataSet/TaxonConcepts/TaxonConcept/Rank/@code | [tc:rank](https://github.com/tdwg/tnc/blob/5d3950009e2462e7d8c930dc08f4733738b9133d/tcs-docs/TaxonConcept.ttl#L157) | [taxonomicRank](https://github.com/tdwg/tcs2/tree/master/docs/tcs-terms#tcstaxonomicrank)
/DataSet/TaxonConcepts/TaxonConcept/Name | [tc:nameString](https://github.com/tdwg/tnc/blob/5d3950009e2462e7d8c930dc08f4733738b9133d/tcs-docs/TaxonConcept.ttl#L72) | [dcterms:title](https://github.com/tdwg/tcs2/tree/master/docs/tcs-terms#dctermstitle) \| [dcterms:identifier](https://github.com/tdwg/tcs2/tree/master/docs/tcs-terms#dctermsidentifier) \| [dwc:scientificName](https://github.com/tdwg/tcs2/tree/master/docs/tcs-terms#dwcscientificname) \| [dwc:vernacularName](https://github.com/tdwg/tcs2/tree/master/docs/tcs-terms#dwcvernacularname)
/DataSet/TaxonConcepts/TaxonConcept/Name/@ref | [tc:hasName](https://github.com/tdwg/tnc/blob/5d3950009e2462e7d8c930dc08f4733738b9133d/tcs-docs/TaxonConcept.ttl#L65) | [taxonName](https://github.com/tdwg/tcs2/tree/master/docs/tcs-terms#tcstaxonname)
/DataSet/TaxonConcepts/TaxonConcept/AccordingTo/AccordingToDetailed | [  tc:accordingTo](https://github.com/tdwg/tnc/blob/5d3950009e2462e7d8c930dc08f4733738b9133d/tcs-docs/TaxonConcept.ttl#L50) | [accordingTo](https://github.com/tdwg/tcs2/tree/master/docs/tcs-terms#tcsaccordingto)
/DataSet/TaxonConcepts/TaxonConcept/AccordingTo/AccordingToSimple | [tc:accordingToString](https://github.com/tdwg/tnc/blob/5d3950009e2462e7d8c930dc08f4733738b9133d/tcs-docs/TaxonConcept.ttl#L58) | &mdash;
/DataSet/TaxonConcepts/TaxonConcept/SpecimenCircumscription | [tc:circumscribedBy](https://github.com/tdwg/tnc/blob/5d3950009e2462e7d8c930dc08f4733738b9133d/tcs-docs/TaxonConcept.ttl#L80) | &mdash;
/DataSet/TaxonConcepts/TaxonConcept/CharacterCircumscription | [tc:describedBy](https://github.com/tdwg/tnc/blob/5d3950009e2462e7d8c930dc08f4733738b9133d/tcs-docs/TaxonConcept.ttl#L87) | &mdash;

### Taxon Relationship / Taxon Relationship Assertion

TCS 1 | TDWG Ontology | TCS 2 
-|-|-
/DataSet/TaxonConcepts/TaxonConcept/TaxonRelationships/TaxonRelationship \| /DataSet/TaxonRelationshipAssertions/TaxonRelationshipAssertion | [tc:Relationship](https://github.com/tdwg/tnc/blob/5d3950009e2462e7d8c930dc08f4733738b9133d/tcs-docs/TaxonConcept.ttl#L42) | [dwc:ResourceRelationship](http://rs.tdwg.org/dwc/terms/ResourceRelationship)
/DataSet/TaxonConcepts/TaxonConcept/Relationships/Relationship/@type \| /DataSet/TaxonRelationshipAssertions/TaxonRelationshipAssertion/@type | [tc:relationshipCategory](https://github.com/tdwg/tnc/blob/5d3950009e2462e7d8c930dc08f4733738b9133d/tcs-docs/TaxonConcept.ttl#L128) | &mdash;
/DataSet/TaxonRelationshipAssertions/TaxonRelationshipAssertion/FromTaxonConcept | [tc:fromTaxon](https://github.com/tdwg/tnc/blob/5d3950009e2462e7d8c930dc08f4733738b9133d/tcs-docs/TaxonConcept.ttl#L94) | &mdash;
/DataSet/TaxonRelationshipAssertions/TaxonRelationshipAssertion/ToTaxonConcept \| /DataSet/TaxonConcepts/TaxonConcept/TaxonRelationships/TaxonRelationship/ToTaxonConcept | [tc:toTaxon](https://github.com/tdwg/tnc/blob/5d3950009e2462e7d8c930dc08f4733738b9133d/tcs-docs/TaxonConcept.ttl#L134) | &mdash;
/DataSet/TaxonRelationshipAssertions/TaxonRelationshipAssertion/AccordingTo | &mdash; | &mdash;

### Relationship Type vocabulary

TCS 1 | TDWG Ontology | TCS 2 
-|-|-
is congruent to | [tc:isCongruentTo](https://github.com/tdwg/tnc/blob/5d3950009e2462e7d8c930dc08f4733738b9133d/tcs-docs/TaxonConcept.ttl#L252) | [isCongruentWith](https://github.com/tdwg/tcs2/tree/master/docs/tcs-terms#tcsiscongruentwith)
is not congruent to | [tc:isNotCongruentTo](https://github.com/tdwg/tnc/blob/5d3950009e2462e7d8c930dc08f4733738b9133d/tcs-docs/TaxonConcept.ttl#L299) | &mdash;
includes | [tc:includes](https://github.com/tdwg/tnc/blob/5d3950009e2462e7d8c930dc08f4733738b9133d/tcs-docs/TaxonConcept.ttl#L222) | [includes](https://github.com/tdwg/tcs2/tree/master/docs/tcs-terms#tcsincludes)
does not include | [tc:doesNotInclude](https://github.com/tdwg/tnc/blob/5d3950009e2462e7d8c930dc08f4733738b9133d/tcs-docs/TaxonConcept.ttl#L178) | &mdash;
excludes | [tc:excludes](https://github.com/tdwg/tnc/blob/5d3950009e2462e7d8c930dc08f4733738b9133d/tcs-docs/TaxonConcept.ttl#L191) | [isDisjointFrom](https://github.com/tdwg/tcs2/tree/master/docs/tcs-terms#tcsisdisjointfrom)
is included in | [tc:isIncludedIn](https://github.com/tdwg/tnc/blob/5d3950009e2462e7d8c930dc08f4733738b9133d/tcs-docs/TaxonConcept.ttl#L286) | [isIncludedIn](https://github.com/tdwg/tcs2/tree/master/docs/tcs-terms#tcsisincludedin)
is not included in | [tc:isNotIncludedIn](https://github.com/tdwg/tnc/blob/5d3950009e2462e7d8c930dc08f4733738b9133d/tcs-docs/TaxonConcept.ttl#L306) | &mdash;
overlaps | [tc:overlaps](https://github.com/tdwg/tnc/blob/5d3950009e2462e7d8c930dc08f4733738b9133d/tcs-docs/TaxonConcept.ttl#L357) | [partiallyOverlaps](https://github.com/tdwg/tcs2/tree/master/docs/tcs-terms#tcspartiallyoverlaps)
does not overlap | [tc:doesNotOverlap](https://github.com/tdwg/tnc/blob/5d3950009e2462e7d8c930dc08f4733738b9133d/tcs-docs/TaxonConcept.ttl#L184) | &mdash;
 | | 
is child taxon of | [tc:isChildTaxonOf](https://github.com/tdwg/tnc/blob/5d3950009e2462e7d8c930dc08f4733738b9133d/tcs-docs/TaxonConcept.ttl#L245) | [parent](https://github.com/tdwg/tcs2/tree/master/docs/tcs-terms#tcsparent)
is parent taxon of | [tc:isParentTaxonOf](https://github.com/tdwg/tnc/blob/5d3950009e2462e7d8c930dc08f4733738b9133d/tcs-docs/TaxonConcept.ttl#L312) | &mdash;
 | | 
is anamorph of | [tc:isAnamorphOf](https://github.com/tdwg/tnc/blob/5d3950009e2462e7d8c930dc08f4733738b9133d/tcs-docs/TaxonConcept.ttl#L237) | &mdash;
is teleomorph of | [tc:isTeleomorphOf](https://github.com/tdwg/tnc/blob/5d3950009e2462e7d8c930dc08f4733738b9133d/tcs-docs/TaxonConcept.ttl#L340) | &mdash;
 | | 
is second parent of | [tc:isSecondParentOf](https://github.com/tdwg/tnc/blob/5d3950009e2462e7d8c930dc08f4733738b9133d/tcs-docs/TaxonConcept.ttl#L319) | &mdash;
is female parent of | [tc:isFemaleParentOf](https://github.com/tdwg/tnc/blob/5d3950009e2462e7d8c930dc08f4733738b9133d/tcs-docs/TaxonConcept.ttl#L259) | &mdash;
is first parent of | [tc:isFirstParentOf](https://github.com/tdwg/tnc/blob/5d3950009e2462e7d8c930dc08f4733738b9133d/tcs-docs/TaxonConcept.ttl#L265) | &mdash;
is male parent of | [tc:isMaleParentOf](https://github.com/tdwg/tnc/blob/5d3950009e2462e7d8c930dc08f4733738b9133d/tcs-docs/TaxonConcept.ttl#292) | &mdash;
is hybrid parent of | [tc:isHybridParentOf](https://github.com/tdwg/tnc/blob/5d3950009e2462e7d8c930dc08f4733738b9133d/tcs-docs/TaxonConcept.ttl#279) | &mdash;
is hybrid child of | [tc:isHybridChildOf](https://github.com/tdwg/tnc/blob/5d3950009e2462e7d8c930dc08f4733738b9133d/tcs-docs/TaxonConcept.ttl#272) | &mdash;
 | | 
is ambiregnal of | [tc:isAmbiregnalOf](https://github.com/tdwg/tnc/blob/5d3950009e2462e7d8c930dc08f4733738b9133d/tcs-docs/TaxonConcept.ttl#228) | &mdash;
 | | 
is vernacular for | [tc:isVernacularFor](https://github.com/tdwg/tnc/blob/5d3950009e2462e7d8c930dc08f4733738b9133d/tcs-docs/TaxonConcept.ttl#348) | &mdash;
has vernacular | [tc:hasVernacular](https://github.com/tdwg/tnc/blob/5d3950009e2462e7d8c930dc08f4733738b9133d/tcs-docs/TaxonConcept.ttl#212) | [vernacularName](https://github.com/tdwg/tcs2/tree/master/docs/tcs-terms#tcsvernacularname)
has synonym | [tc:HasSynonym](https://github.com/tdwg/tnc/blob/5d3950009e2462e7d8c930dc08f4733738b9133d/tcs-docs/TaxonConcept.ttl#L198) | [synonym](https://github.com/tdwg/tcs2/tree/master/docs/tcs-terms#tcssynonym) \| [intersects](https://github.com/tdwg/tcs2/tree/master/docs/tcs-terms#tcsintersects)

### Taxon Concept type vocabulary

TCS 1 | TDWG Ontology | TCS 2
-|-|-
original | &mdash; | &mdash;
revision | &mdash; | &mdash;
incomplete | &mdash; | &mdash;
aggregate | &mdash; | &mdash;
nominal | &mdash; | &mdash;

### Taxonomic Rank vocabulary

#### TaxonomicRankAboveSuperfamilyEnum

TCS 1 | TDWG Ontology | TCS 2
-|-|-
infraord | &mdash; | &mdash;
subord | &mdash; | &mdash;
ord | &mdash; | &mdash;
superord | &mdash; | &mdash;
infracl | &mdash; | &mdash;
subcl | &mdash; | &mdash;
cl | &mdash; | &mdash;
supercl | &mdash; | &mdash;
infraphyl_div | &mdash; | &mdash;
subphyl_div | &mdash; | &mdash;
phyl_div | &mdash; | &mdash;
superphyl_div | &mdash; | &mdash;
infrareg | &mdash; | &mdash;
subreg | &mdash; | &mdash;
reg | &mdash; | &mdash;
superreg | &mdash; | &mdash;
dom | &mdash; | &mdash;
taxsupragen | &mdash; | &mdash;

#### TaxonomicRankFamilyGroupEnum

TCS 1 | TDWG Ontology | TCS 2
-|-|-
infrafam | &mdash; | &mdash;
subfam | &mdash; | &mdash;
fam | &mdash; | &mdash;
superfam | &mdash; | &mdash;

#### TaxonomicRankFamilySubdivisionEnum

TCS 1 | TDWG Ontology | TCS 2
-|-|-
infratrib | &mdash; | &mdash;
subtrib | &mdash; | &mdash;
trib | &mdash; | &mdash;
supertrib | &mdash; | &mdash;

#### TaxonomicRankGenusGroupEnum

TCS 1 | TDWG Ontology | TCS 2
-|-|-
infragen | &mdash; | &mdash;
subgen | &mdash; | &mdash;
gen | &mdash; | &mdash;

#### TaxonomicRankGenusSubdivisionEnum

TCS 1 | TDWG Ontology | TCS 2
-|-|-
aggr | &mdash; | &mdash;
taxinfragen | &mdash; | &mdash;
subser | &mdash; | &mdash;
ser | &mdash; | &mdash;
subsect | &mdash; | &mdash;
sect | &mdash; | &mdash;

#### TaxonomicRankSpeciesGroupEnum

TCS 1 | TDWG Ontology | TCS 2
-|-|-
subsp_aggr | &mdash; | &mdash;
subsp | &mdash; | &mdash;
sp | &mdash; | &mdash;

#### TaxonomicRankBelowSubspeciesEnum

TCS 1 | TDWG Ontology | TCS 2
-|-|-
cand | &mdash; | &mdash;
taxinfrasp | &mdash; | &mdash;
fsp | &mdash; | &mdash;
subsubfm | &mdash; | &mdash;
subfm | &mdash; | &mdash;
fm | &mdash; | &mdash;
subsubvar | &mdash; | &mdash;
subvar | &mdash; | &mdash;
var | &mdash; | &mdash;
pv | &mdash; | &mdash;
bv | &mdash; | &mdash;
infrasp | &mdash; | &mdash;

#### TaxonomicRankCultivatedPlants

TCS 1 | TDWG Ontology | TCS 2
-|-|-
cv | &mdash; | &mdash;
convar | &mdash; | &mdash;
grex | &mdash; | &mdash;
cvgroup | &mdash; | &mdash;
graftchimaera | &mdash; | &mdash;
denomclass | &mdash; | &mdash;

### Taxon Name

TCS 1 | TDWG Ontology | TCS 2 
-|-|-
/DataSet/TaxonNames/TaxonName | [tn:TaxonName](https://github.com/tdwg/tnc/blob/5d3950009e2462e7d8c930dc08f4733738b9133d/tcs-docs/TaxonName.ttl#L29) | **[TaxonName](https://github.com/tdwg/tcs2/tree/master/docs/tcs-terms#tcstaxonname)**
/DataSet/TaxonNames/TaxonName/@nomenclaturalCode | [tn:nomenclaturalCode](https://github.com/tdwg/tnc/blob/5d3950009e2462e7d8c930dc08f4733738b9133d/tcs-docs/TaxonName.ttl#L173) | [nomenclaturalCode](https://github.com/tdwg/tcs2/tree/master/docs/tcs-terms#tcsnomenclaturalcode)
/DataSet/TaxonNames/TaxonName/@isAnamorphic | &mdash; | &mdash;
/DataSet/TaxonNames/TaxonName/Simple |   [tn:nameComplete](https://github.com/tdwg/tnc/blob/5d3950009e2462e7d8c930dc08f4733738b9133d/tcs-docs/TaxonName.ttl#L161) | [taxonNameString](https://github.com/tdwg/tcs2/tree/master/docs/tcs-terms#tcstaxonnamestring)
/DataSet/TaxonNames/TaxonName/Rank | [tn:rankString](https://github.com/tdwg/tnc/blob/5d3950009e2462e7d8c930dc08f4733738b9133d/tcs-docs/TaxonName.ttl#L321) | [dwc:verbatimTaxonRank](https://github.com/tdwg/tcs2/tree/master/docs/tcs-terms#dwcverbatimtaxonrank)
/DataSet/TaxonNames/TaxonName/Rank/@code | [tn:rank](https://github.com/tdwg/tnc/blob/5d3950009e2462e7d8c930dc08f4733738b9133d/tcs-docs/TaxonName.ttl#L309) | [taxonomicRank](https://github.com/tdwg/tcs2/tree/master/docs/tcs-terms#tcstaxonomicrank)
/DataSet/TaxonNames/TaxonName/CanonicalName/Uninomial | [tn:uninomial](https://github.com/tdwg/tnc/blob/5d3950009e2462e7d8c930dc08f4733738b9133d/tcs-docs/TaxonName.ttl#L257) | &mdash;
/DataSet/TaxonNames/TaxonName/CanonicalName/Genus | [  tn:genusPart](https://github.com/tdwg/tnc/blob/5d3950009e2462e7d8c930dc08f4733738b9133d/tcs-docs/TaxonName.ttl#L110) | [dwc:genericName](https://github.com/tdwg/tcs2/tree/master/docs/tcs-terms#dwcgenericname)
/DataSet/TaxonNames/TaxonName/CanonicalName/InfragenericEpithet | [tn:infragenericEpithet](https://github.com/tdwg/tnc/blob/5d3950009e2462e7d8c930dc08f4733738b9133d/tcs-docs/TaxonName.ttl#L133) | [dwc:infragenericEpithet](https://github.com/tdwg/tcs2/tree/master/docs/tcs-terms#dwcinfragenericepithet)
/DataSet/TaxonNames/TaxonName/CanonicalName/SpecificEpithet | [tn:specificEpithet](https://github.com/tdwg/tnc/blob/5d3950009e2462e7d8c930dc08f4733738b9133d/tcs-docs/TaxonName.ttl#L205) | [dwc:specificEpithet](https://github.com/tdwg/tcs2/tree/master/docs/tcs-terms#dwcspecificepithet)
/DataSet/TaxonNames/TaxonName/CanonicalName/InfraspecificEpithet | [tn:infraspecificEpithet](https://github.com/tdwg/tnc/blob/5d3950009e2462e7d8c930dc08f4733738b9133d/tcs-docs/TaxonName.ttl#L147) | [dwc:infraspecificEpithet](https://github.com/tdwg/tcs2/tree/master/docs/tcs-terms#dwcinfraspecificepithet)
/DataSet/TaxonNames/TaxonName/CanonicalName/CultivarNameGroup | [tn:cultivarNameGroup](https://github.com/tdwg/tnc/blob/5d3950009e2462e7d8c930dc08f4733738b9133d/tcs-docs/TaxonName.ttl#L97) | [dwc:cultivarEpithet](https://github.com/tdwg/tcs2/tree/master/docs/tcs-terms#dwccultivarepithet)
/DataSet/TaxonNames/TaxonName/CanonicalAuthorship/Simple | [tn:authorship](https://github.com/tdwg/tnc/blob/5d3950009e2462e7d8c930dc08f4733738b9133d/tcs-docs/TaxonName.ttl#L72) | [dwc:scientificNameAuthorship](https://github.com/tdwg/tcs2/tree/master/docs/tcs-terms#dwcscientificnameauthorship)
/DataSet/TaxonNames/TaxonName/CanonicalAuthorship/Authorship/Simple | &mdash; | &mdash;
/DataSet/TaxonNames/TaxonName/CanonicalAuthorship/Authorship/Authors | &mdash; | &mdash;
/DataSet/TaxonNames/TaxonName/CanonicalAuthorship/BasionymAuthorship/Simple | [  tn:basionymAuthorship](https://github.com/tdwg/tnc/blob/5d3950009e2462e7d8c930dc08f4733738b9133d/tcs-docs/TaxonName.ttl#L373) | &mdash;
/DataSet/TaxonNames/TaxonName/CanonicalAuthorship/BasionymAuthorship/Authors | &mdash; | &mdash;
/DataSet/TaxonNames/TaxonName/CanonicalAuthorship/CombinationAuthorship/Simple | [tn:combinationAuthorship](https://github.com/tdwg/tnc/blob/5d3950009e2462e7d8c930dc08f4733738b9133d/tcs-docs/TaxonName.ttl#L388) | &mdash;
/DataSet/TaxonNames/TaxonName/CanonicalAuthorship/CombinationAuthorship/Authors | &mdash; | &mdash;
/DataSet/TaxonNames/TaxonName/PublishedIn | &mdash; | [namePublishedIn](https://github.com/tdwg/tcs2/tree/master/docs/tcs-terms#tcsnamepublishedin)
/DataSet/TaxonNames/TaxonName/Year | [tn:year](https://github.com/tdwg/tnc/blob/5d3950009e2462e7d8c930dc08f4733738b9133d/tcs-docs/TaxonName.ttl#L269) | [dwc:namePublishedInYear](https://github.com/tdwg/tcs2/tree/master/docs/tcs-terms#dwcnamepublishedinyear)
/DataSet/TaxonNames/TaxonName/MicroReference \| //element(*,NomenclaturalNoteType)/MicroReference | &mdash; | [microReference](https://github.com/tdwg/tcs2/tree/master/docs/tcs-terms#tcsmicroreference)
/DataSet/TaxonNames/TaxonName/Typification/Simple | &mdash; | [typification](https://github.com/tdwg/tcs2/tree/master/docs/tcs-terms#tcstypification)
/DataSet/TaxonNames/TaxonName/SpellingCorrectionOf | [tn:spellingCorrection](https://github.com/tdwg/tnc/blob/5d3950009e2462e7d8c930dc08f4733738b9133d/tcs-docs/TaxonName.ttl#L647) | [spellingCorrectionOf](https://github.com/tdwg/tcs2/tree/master/docs/tcs-terms#tcsspellingcorrectionof)
/DataSet/TaxonNames/TaxonName/Basionym | [tn:hasBasionym](https://github.com/tdwg/tnc/blob/5d3950009e2462e7d8c930dc08f4733738b9133d/tcs-docs/TaxonName.ttl#L296) | [basionym](https://github.com/tdwg/tcs2/tree/master/docs/tcs-terms#tcsbasionym)
/DataSet/TaxonNames/TaxonName/BasedOn | [tn:BasedOn](https://github.com/tdwg/tnc/blob/5d3950009e2462e7d8c930dc08f4733738b9133d/tcs-docs/TaxonName.ttl#L427) | &mdash;
/DataSet/TaxonNames/TaxonName/ConservedAgainst | [tn:ConservedAgainst](https://github.com/tdwg/tnc/blob/5d3950009e2462e7d8c930dc08f4733738b9133d/tcs-docs/TaxonName.ttl#L433) | [conservedAgainst](https://github.com/tdwg/tcs2/tree/master/docs/tcs-terms#tcsconservedagainst)
/DataSet/TaxonNames/TaxonName/LaterHomonymOf | [tn:LaterHomonymOf](https://github.com/tdwg/tnc/blob/5d3950009e2462e7d8c930dc08f4733738b9133d/tcs-docs/TaxonName.ttl#L547) | [laterHomonymOf](https://github.com/tdwg/tcs2/tree/master/docs/tcs-terms#tcslaterhomonymof)
/DataSet/TaxonNames/TaxonName/Sanctioned | &mdash; | &mdash;
/DataSet/TaxonNames/TaxonName/ReplacementNameFor | [tn:ReplacementNameFor](https://github.com/tdwg/tnc/blob/5d3950009e2462e7d8c930dc08f4733738b9133d/tcs-docs/TaxonName.ttl#L630) | [replacedName](https://github.com/tdwg/tcs2/tree/master/docs/tcs-terms#tcsreplacedname)
/DataSet/TaxonNames/TaxonName/PublicationStatus | [tn:publicationStatus](https://github.com/tdwg/tnc/blob/5d3950009e2462e7d8c930dc08f4733738b9133d/tcs-docs/TaxonName.ttl#L624) | [nomenclaturalStatus](https://github.com/tdwg/tcs2/tree/master/docs/tcs-terms#tcsnomenclaturalstatus)

### Nomenclatural Code vocabulary

TCS 1 | TDWG Ontology | TCS 2
-|-|-
Viral | [tn:Viral](https://github.com/tdwg/tnc/blob/5d3950009e2462e7d8c930dc08f4733738b9133d/tcs-docs/TaxonName.ttl#L675) | &mdash;
Bacteriological | [tn:Bacteriological](https://github.com/tdwg/tnc/blob/5d3950009e2462e7d8c930dc08f4733738b9133d/tcs-docs/TaxonName.ttl#L422) | &mdash;
Botanical | [tn:ICBN](https://github.com/tdwg/tnc/blob/5d3950009e2462e7d8c930dc08f4733738b9133d/tcs-docs/TaxonName.ttl#L505) | &mdash;
Zoological | [tn:ICZN](https://github.com/tdwg/tnc/blob/5d3950009e2462e7d8c930dc08f4733738b9133d/tcs-docs/TaxonName.ttl#L515) | &mdash;
CultivatedPlant | [tn:ICNCP](https://github.com/tdwg/tnc/blob/5d3950009e2462e7d8c930dc08f4733738b9133d/tcs-docs/TaxonName.ttl#L510) | &mdash;
Indeterminate | &mdash; | &mdash;

### Typification

TCS 1 | TDWG Ontology | TCS 2 
-|-|-
/DataSet/TaxonNames/TaxonName/Typification/TypeVouchers/TypeVoucher \| /DataSet/TaxonNames/TaxonName/Typification/TypeName | [tn:NomenclaturalType](https://github.com/tdwg/tnc/blob/5d3950009e2462e7d8c930dc08f4733738b9133d/tcs-docs/TaxonName.ttl#L45) | **[NomenclaturalType](https://github.com/tdwg/tcs2/tree/master/docs/tcs-terms#tcsnomenclaturaltype)**
&mdash; | &mdash; | [typifiedName](https://github.com/tdwg/tcs2/tree/master/docs/tcs-terms#tcstypifiedname)
/DataSet/TaxonNames/TaxonName/Typification/TypeVouchers/TypeVoucher/@typeofType | [tn:typeOfType](https://github.com/tdwg/tnc/blob/5d3950009e2462e7d8c930dc08f4733738b9133d/tcs-docs/TaxonName.ttl#L241) | [typeOfType](https://github.com/tdwg/tcs2/tree/master/docs/tcs-terms#tcstypeoftype)
/DataSet/TaxonNames/TaxonName/Typification/TypeVouchers/TypeVoucher/VoucherReference | [tn:typeSpecimen](https://github.com/tdwg/tnc/blob/5d3950009e2462e7d8c930dc08f4733738b9133d/tcs-docs/TaxonName.ttl#L249) | [typeSpecimen](https://github.com/tdwg/tcs2/tree/master/docs/tcs-terms#tcstypespecimen)
/DataSet/TaxonNames/TaxonName/Typification/TypeVouchers/TypeVoucher/LectotypePublication \| /DataSet/TaxonNames/TaxonName/Typification/TypeName/LectotypePublication | &mdash; | [typePublishedIn](https://github.com/tdwg/tcs2/tree/master/docs/tcs-terms#tcstypepublishedin)
/DataSet/TaxonNames/TaxonName/Typification/TypeName/NameReference | [tn:typeName](https://github.com/tdwg/tnc/blob/5d3950009e2462e7d8c930dc08f4733738b9133d/tcs-docs/TaxonName.ttl#L233) | [typeName](https://github.com/tdwg/tcs2/tree/master/docs/tcs-terms#tcstypename)

### Type of Type vocabulary

TCS 1 | TDWG Ontology | TCS 2
-|-|-
allo | [tn:Allotype](https://github.com/tdwg/tnc/blob/5d3950009e2462e7d8c930dc08f4733738b9133d/tcs-docs/TaxonName.ttl#L416) | &mdash;
allolecto | [tn:Allolectotype](https://github.com/tdwg/tnc/blob/5d3950009e2462e7d8c930dc08f4733738b9133d/tcs-docs/TaxonName.ttl#L406) | &mdash;
alloneo | [tn:Alloneotype](https://github.com/tdwg/tnc/blob/5d3950009e2462e7d8c930dc08f4733738b9133d/tcs-docs/TaxonName.ttl#L411) | &mdash;
co | [tn:Cotype](https://github.com/tdwg/tnc/blob/5d3950009e2462e7d8c930dc08f4733738b9133d/tcs-docs/TaxonName.ttl#L439) | &mdash;
epi | [tn:Epitype](https://github.com/tdwg/tnc/blob/5d3950009e2462e7d8c930dc08f4733738b9133d/tcs-docs/TaxonName.ttl#L444) | &mdash;
ex | [tn:ExType](https://github.com/tdwg/tnc/blob/5d3950009e2462e7d8c930dc08f4733738b9133d/tcs-docs/TaxonName.ttl#L486) | &mdash;
exepi | [tn:ExEpitype](https://github.com/tdwg/tnc/blob/5d3950009e2462e7d8c930dc08f4733738b9133d/tcs-docs/TaxonName.ttl#L451) | &mdash;
exholo | [tn:ExHolotype](https://github.com/tdwg/tnc/blob/5d3950009e2462e7d8c930dc08f4733738b9133d/tcs-docs/TaxonName.ttl#L456) | &mdash;
exiso | [tn:ExIsotype](https://github.com/tdwg/tnc/blob/5d3950009e2462e7d8c930dc08f4733738b9133d/tcs-docs/TaxonName.ttl#L273) | &mdash;
exlecto | [tn:ExLectotype](https://github.com/tdwg/tnc/blob/5d3950009e2462e7d8c930dc08f4733738b9133d/tcs-docs/TaxonName.ttl#L466) | &mdash;
exneo | [tn:ExNeotype](https://github.com/tdwg/tnc/blob/5d3950009e2462e7d8c930dc08f4733738b9133d/tcs-docs/TaxonName.ttl#L471) | &mdash;
expara | [tn:ExParatype](https://github.com/tdwg/tnc/blob/5d3950009e2462e7d8c930dc08f4733738b9133d/tcs-docs/TaxonName.ttl#L476) | &mdash;
exsyn | [tn:ExSyntype](https://github.com/tdwg/tnc/blob/5d3950009e2462e7d8c930dc08f4733738b9133d/tcs-docs/TaxonName.ttl#L481) | &mdash;
hapanto | [tn:Hapantotype](https://github.com/tdwg/tnc/blob/5d3950009e2462e7d8c930dc08f4733738b9133d/tcs-docs/TaxonName.ttl#L491) | &mdash;
holo | [tn:Holotype](https://github.com/tdwg/tnc/blob/5d3950009e2462e7d8c930dc08f4733738b9133d/tcs-docs/TaxonName.ttl#L498) | &mdash;
icono | [tn:Iconotype](https://github.com/tdwg/tnc/blob/5d3950009e2462e7d8c930dc08f4733738b9133d/tcs-docs/TaxonName.ttl#L520) | &mdash;
iso | [tn:Isotype](https://github.com/tdwg/tnc/blob/5d3950009e2462e7d8c930dc08f4733738b9133d/tcs-docs/TaxonName.ttl#L541) | &mdash;
isolecto | [tn:IsoLectotype](https://github.com/tdwg/tnc/blob/5d3950009e2462e7d8c930dc08f4733738b9133d/tcs-docs/TaxonName.ttl#L526) | &mdash;
isoneo | [tn:Isoneotype](https://github.com/tdwg/tnc/blob/5d3950009e2462e7d8c930dc08f4733738b9133d/tcs-docs/TaxonName.ttl#L531) | &mdash;
isosyn | [tn:Isosyntype](https://github.com/tdwg/tnc/blob/5d3950009e2462e7d8c930dc08f4733738b9133d/tcs-docs/TaxonName.ttl#L536) | &mdash;
lecto | [tn:Lectotype](https://github.com/tdwg/tnc/blob/5d3950009e2462e7d8c930dc08f4733738b9133d/tcs-docs/TaxonName.ttl#L553) | &mdash;
neo | [tn:Neotype](https://github.com/tdwg/tnc/blob/5d3950009e2462e7d8c930dc08f4733738b9133d/tcs-docs/TaxonName.ttl#L560) | &mdash;
para | [tn:Paratype](https://github.com/tdwg/tnc/blob/5d3950009e2462e7d8c930dc08f4733738b9133d/tcs-docs/TaxonName.ttl#L582) | &mdash;
paralecto | [tn:Paralectotype](https://github.com/tdwg/tnc/blob/5d3950009e2462e7d8c930dc08f4733738b9133d/tcs-docs/TaxonName.ttl#L572) | &mdash;
paraneo | [tn:Paraneotype](https://github.com/tdwg/tnc/blob/5d3950009e2462e7d8c930dc08f4733738b9133d/tcs-docs/TaxonName.ttl#L577) | &mdash;
plasto | [tn:Plastotype](https://github.com/tdwg/tnc/blob/5d3950009e2462e7d8c930dc08f4733738b9133d/tcs-docs/TaxonName.ttl#L609) | &mdash;
plastoholo | [tn:Plastoholotype](https://github.com/tdwg/tnc/blob/5d3950009e2462e7d8c930dc08f4733738b9133d/tcs-docs/TaxonName.ttl#L589) | &mdash;
plastoiso | [tn:Plastoisotype](https://github.com/tdwg/tnc/blob/5d3950009e2462e7d8c930dc08f4733738b9133d/tcs-docs/TaxonName.ttl#L594) | &mdash;
plastolecto | [tn:Plastolectotype](https://github.com/tdwg/tnc/blob/5d3950009e2462e7d8c930dc08f4733738b9133d/tcs-docs/TaxonName.ttl#L599) | &mdash;
plastoneo | [tn:Plastoneotype](https://github.com/tdwg/tnc/blob/5d3950009e2462e7d8c930dc08f4733738b9133d/tcs-docs/TaxonName.ttl#L604) | &mdash;
plastopara | [tn:Plastoparatype](https://github.com/tdwg/tnc/blob/5d3950009e2462e7d8c930dc08f4733738b9133d/tcs-docs/TaxonName.ttl#L609) | &mdash;
plastosyn | [tn:Plastosyntype](https://github.com/tdwg/tnc/blob/5d3950009e2462e7d8c930dc08f4733738b9133d/tcs-docs/TaxonName.ttl#L614) | &mdash;
sec | [tn:SecondaryType](https://github.com/tdwg/tnc/blob/5d3950009e2462e7d8c930dc08f4733738b9133d/tcs-docs/TaxonName.ttl#L641) | &mdash;
supp | [tn:SupplementaryType](https://github.com/tdwg/tnc/blob/5d3950009e2462e7d8c930dc08f4733738b9133d/tcs-docs/TaxonName.ttl#L652) | &mdash;
syn | [tn:Syntype](https://github.com/tdwg/tnc/blob/5d3950009e2462e7d8c930dc08f4733738b9133d/tcs-docs/TaxonName.ttl#L657) | &mdash;
topo | [tn:Topotype](https://github.com/tdwg/tnc/blob/5d3950009e2462e7d8c930dc08f4733738b9133d/tcs-docs/TaxonName.ttl#L663) | &mdash;
type | [tn:Type](https://github.com/tdwg/tnc/blob/5d3950009e2462e7d8c930dc08f4733738b9133d/tcs-docs/TaxonName.ttl#L669) | &mdash;
not | [tn:NotAType](https://github.com/tdwg/tnc/blob/5d3950009e2462e7d8c930dc08f4733738b9133d/tcs-docs/TaxonName.ttl#L567) | &mdash;

