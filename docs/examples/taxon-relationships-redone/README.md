# Taxon Relationship Assertion redone

## Relationships in TCS

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

### Relationships between taxa and names

- tcs:acceptedName
- tcs:synonym
- tcs:vernacularName

### Relationships between names

- tcs:basionym
- tcs:replacedSynonym
- tcs:spellingCorrectionOf
- tcs:conservedAgainst


## Mapping to SKOS

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
| tcs:isCongruentWith | skos:closeMatch/skos:exactMatch |
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

- Relationships between taxa are anologous to `skos:semanticRelation` properties
- Horizontal relationships between taxa are also analogous to `skos:mappingRelation` properties
- Relationships between taxa and names are analogous to `skosxl:prefLabel`, `skosxl:altLabel` and `skosxl:hiddenLabel` properties
- Relationships between names are analogous to the `skosxl:labelRelation` property.
