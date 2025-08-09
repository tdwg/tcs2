# SSSOM Mapping


## TaxonConcept


### tcs:TaxonConcept

| predicate | IRI or XPATH | remarks |
|-|-|-|
| skos:exactMatch | /DataSet/TaxonConcepts/TaxonConcept |  |
| skos:exactMatch | http://rs.tdwg.org/ontology/voc/TaxonConcept#TaxonConcept |  |
| skos:relatedMatch | http://rs.tdwg.org/dwc/terms/Taxon | The dwc:Taxon is hard to categorise. as it can be implemented in a way that a Taxon is equivalent to a TaxonConcept, but if either `taxonomicStatus` or `acceptedNameUsage` terms are used, both `accepted` and `synonym` uses are data artefacts that are not TaxonConcepts. |
| skos:exactMatch | http://openbiodiv.net/TaxonomicConcept |  |
| skos:broadMatch | http://openbiodiv.net/OperationalTaxonomicUnit |  |
| skos:broadMatch | http://www.w3.org/2004/02/skos/core#Concept |  |
| skos:broadMatch | http://purl.org/spar/frbr/Work |  |

### tcs:accordingTo

| predicate | IRI or XPATH | remarks |
|-|-|-|
| skos:exactMatch | /DataSet/TaxonConcepts/TaxonConcept/AccordingTo/AccordingToDetailed |  |
| skos:exactMatch | http://rs.tdwg.org/ontology/voc/TaxonName#accordingTo |  |
| skos:exactMatch | http://rs.tdwg.org/dwc/terms/nameAccordingTo | The TCS term is the IRI equivalent of the Darwin Core term. |
| skos:narrowMatch | http://purl.org/spar/frbr/realization | In OpenBiodiv-O, the `frbr:realization` is the `openbiodiv-o:Treatment` of that particular taxon. `tcs:accordingTo` can also point to the `openbiodiv-o:TaxonomicArticle`. In OpenBiodiv-O the `TaxonomicArticle` `openbiodiv-o:contains` the `Treatment`s. |
| skos:closeMatch | http://www.w3.org/2004/02/skos/core#inScheme | Both the subject and object in this relationship have a broader meaning in SKOS, but if the subject is a TaxonConcept, the meaning of the term is the same. |

### tcs:taxonName

| predicate | IRI or XPATH | remarks |
|-|-|-|
| skos:exactMatch | /DataSet/TaxonConcepts/TaxonConcept/Name/@ref |  |
| skos:exactMatch | http://rs.tdwg.org/ontology/voc/TaxonName#hasName |  |
| skos:narrowMatch | http://rs.tdwg.org/dwc/terms/scientificName | In Darwin Core records that do not have a `scientificName` but do have a `vernacularName`, the `vernacularName` is the `taxonName`. Also note `dwc:scientificName` is a string and `tcs:taxonName` an IRI. |
| skos:narrowMatch | http://rs.tdwg.org/dwc/terms/vernacularName |  |
| skos:closeMatch | http://openbiodiv.net/taxonomicName |  |

### tcs:synonym

| predicate | IRI or XPATH | remarks |
|-|-|-|
| skos:broadMatch | /DataSet/TaxonConcepts/TaxonConcept/TaxonRelationships/TaxonRelationship[@type='has synonym'] | The 'has synonym' relationship from TCS 1 has been split into `synonym` for relations between TaxonConcept and TaxonName and `intersects` for relationships between TaxonConcepts. Also note that the object of `has synonym` is a TaxonConcept and the object of `synonym` a TaxonName. |
| skos:broadMatch | http://rs.tdwg.org/ontology/voc/TaxonConcept#hasSynonym |  |
| skos:closeMatch | http://www.w3.org/2008/05/skos-xl#hiddenLabel | A synonym is an alternative label that is not used for the TaxonConcept. |

### tcs:vernacularName

| predicate | IRI or XPATH | remarks |
|-|-|-|
| skos:exactMatch | /DataSet/TaxonConcepts/TaxonConcept/TaxonRelationships/TaxonRelationship[@type='has vernacular'] | Note that the object of `has vernacular` is a TaxonConcept while the object of `vernacularName` is a TaxonName. |
| skos:exactMatch | http://rs.tdwg.org/ontology/voc/TaxonConcept#hasVernacular |  |
| skos:exactMatch | http://rs.tdwg.org/dwc/terms/vernacularName | The TCS term is the IRI equivalent of the Darwin Core term. |
| skos:closeMatch | http://openbiodiv.net/vernacularName |  |
| skos:closeMatch | http://www.w3.org/2008/05/skos-xl#altLabel |  |

### tcs:taxonRank

| predicate | IRI or XPATH | remarks |
|-|-|-|
| skos:exactMatch | /DataSet/TaxonConcepts/TaxonConcept/Rank/@code |  |
| skos:exactMatch | http://rs.tdwg.org/ontology/voc/TaxonConcept#taxonomicRank |  |
| skos:exactMatch | http://rs.tdwg.org/dwc/terms/taxonRank | The TCS term is the IRI equivalent of the Darwin Core term. |

### tcs:parentTaxonConcept

| predicate | IRI or XPATH | remarks |
|-|-|-|
| skos:exactMatch | /DataSet/TaxonConcepts/TaxonConcept/TaxonRelationships/TaxonRelationship[@type='is child taxon of'] |  |
| skos:exactMatch | http://rs.tdwg.org/ontology/voc/TaxonConcept#isChildTaxonOf |  |
| skos:exactMatch | http://rs.tdwg.org/dwc/terms/parentNameUsage | The TCS term is the IRI equivalent of the Darwin Core term. |
| skos:closeMatch | http://www.w3.org/2004/02/skos/core#broader |  |

### tcs:childTaxonConcept

| predicate | IRI or XPATH | remarks |
|-|-|-|
| skos:exactMatch | /DataSet/TaxonConcepts/TaxonConcept/TaxonRelationships/TaxonRelationship[@type='is parent taxon of'] |  |
| skos:exactMatch | http://rs.tdwg.org/ontology/voc/TaxonConcept#isParentTaxonOf |  |
| skos:closeMatch | http://www.w3.org/2004/02/skos/core#narrower |  |

### tcs:isCongruentWith

| predicate | IRI or XPATH | remarks |
|-|-|-|
| skos:exactMatch | /DataSet/TaxonConcepts/TaxonConcept/TaxonRelationships/TaxonRelationship[@type='is congruent to'] |  |
| skos:exactMatch | http://rs.tdwg.org/ontology/voc/TaxonConcept#isCongruentTo |  |
| skos:narrowMatch | http://openbiodiv.net/Equal_INT | OpenBiodiv-O distinguishes between RCC5 Relation statements based on the ostensive component of the concepts and those based on the intensional component. |
| skos:narrowMatch | http://openbiodiv.net/Equal_OST |  |
| skos:closeMatch | http://www.w3.org/2004/02/skos/core#closeMatch |  |

### tcs:includes

| predicate | IRI or XPATH | remarks |
|-|-|-|
| skos:exactMatch | /DataSet/TaxonConcepts/TaxonConcept/TaxonRelationships/TaxonRelationship[@type='includes'] |  |
| skos:exactMatch | http://rs.tdwg.org/ontology/voc/TaxonConcept#includes |  |
| skos:narrowMatch | http://openbiodiv.net/InverseProperPart_INT |  |
| skos:narrowMatch | http://openbiodiv.net/InverseProperPart_OST |  |
| skos:closeMatch | http://www.w3.org/2004/02/skos/core#broadMatch |  |

### tcs:isIncludedIn

| predicate | IRI or XPATH | remarks |
|-|-|-|
| skos:exactMatch | /DataSet/TaxonConcepts/TaxonConcept/TaxonRelationships/TaxonRelationship[@type='is included in'] |  |
| skos:exactMatch | http://rs.tdwg.org/ontology/voc/TaxonConcept#isIncludedIn |  |
| skos:narrowMatch | http://openbiodiv.net/ProperPart_INT | OpenBiodiv-O distinguishes between RCC5 Relation statements based on the ostensive component of the concepts and those based on the intensional component. |
| skos:narrowMatch | http://openbiodiv.net/ProperPart_OST |  |
| skos:closeMatch | http://www.w3.org/2004/02/skos/core#narrowMatch |  |

### tcs:partiallyOverlaps

| predicate | IRI or XPATH | remarks |
|-|-|-|
| skos:exactMatch | /DataSet/TaxonConcepts/TaxonConcept/TaxonRelationships/TaxonRelationship[@type='overlaps'] |  |
| skos:exactMatch | http://rs.tdwg.org/ontology/voc/TaxonConcept#overlaps |  |
| skos:narrowMatch | http://openbiodiv.net/PartiallyOverlaps_INT | OpenBiodiv-O distinguishes between RCC5 Relation statements based on the ostensive component of the concepts and those based on the intensional component. |
| skos:narrowMatch | http://openbiodiv.net/PartiallyOverlaps_OST |  |

### tcs:isDisjointFrom

| predicate | IRI or XPATH | remarks |
|-|-|-|
| skos:exactMatch | /DataSet/TaxonConcepts/TaxonConcept/TaxonRelationships/TaxonRelationship[@type='excludes'] |  |
| skos:exactMatch | http://rs.tdwg.org/ontology/voc/TaxonConcept#excludes |  |
| skos:narrowMatch | http://openbiodiv.net/Disjoint_INT | OpenBiodiv-O distinguishes between RCC5 Relation statements based on the ostensive component of the concepts and those based on the intensional component. |
| skos:narrowMatch | http://openbiodiv.net/Disjoint_OST |  |

### tcs:intersects

| predicate | IRI or XPATH | remarks |
|-|-|-|
| skos:broadMatch | /DataSet/TaxonConcepts/TaxonConcept/TaxonRelationships/TaxonRelationship[@type='has synonym'] | The TCS 1 `has synonym` relationship has been split into `synonym` for relations between TaxonConcept and TaxonName and `intersects` for relationships between TaxonConcepts. |
| skos:broadMatch | http://rs.tdwg.org/ontology/voc/TaxonConcept#hasSynonym |  |

### dwc:scientificName

| predicate | IRI or XPATH | remarks |
|-|-|-|
| skos:broadMatch | /DataSet/TaxonNames/TaxonName/Simple | TCS 1 uses the same element for vernacular names |
| skos:broadMatch | http://rs.tdwg.org/ontology/voc/TaxonName#nameComplete |  |

### dwc:verbatimTaxonRank

| predicate | IRI or XPATH | remarks |
|-|-|-|
| skos:exactMatch | /DataSet/TaxonConcepts/TaxonConcept/Rank |  |
| skos:exactMatch | http://rs.tdwg.org/ontology/voc/TaxonConcept#rankString |  |

### dcterms:title

| predicate | IRI or XPATH | remarks |
|-|-|-|
| skos:closeMatch | http://openbiodiv.net/taxonConceptLabel | TCS adopts the TaxonConceptLabel from OpenBiodiv-O. `dcterms:title` s good match for the string representation. |

## TaxonConceptMappings


## TaxonName


### tcs:TaxonName

| predicate | IRI or XPATH | remarks |
|-|-|-|
| skos:exactMatch | /DataSet/TaxonNames/TaxonName |  |
| skos:exactMatch | http://rs.tdwg.org/ontology/voc/TaxonName#TaxonName |  |
| skos:closeMatch | http://openbiodiv.net/TaxonomicName |  |
| skos:broadMatch | http://www.w3.org/2008/05/skos-xl#Label | The TaxonName is a special kind of SKOSXL Label |

### tcs:nameString

| predicate | IRI or XPATH | remarks |
|-|-|-|
| skos:exactMatch | /DataSet/TaxonNames/TaxonName/Simple |  |
| skos:exactMatch | http://rs.tdwg.org/ontology/voc/TaxonName#nameComplete |  |
| skos:closeMatch | http://www.w3.org/2008/05/skos-xl#literalForm |  |

### tcs:namePublishedIn

| predicate | IRI or XPATH | remarks |
|-|-|-|
| skos:exactMatch | /DataSet/TaxonNames/TaxonName/PublishedIn |  |
| skos:exactMatch | http://rs.tdwg.org/ontology/voc/TaxonName#namePublishedIn |  |
| skos:exactMatch | http://rs.tdwg.org/dwc/terms/namePublishedIn | The TCS term is the IRI equivalent of the Darwin Core term |

### tcs:microreference

| predicate | IRI or XPATH | remarks |
|-|-|-|
| skos:exactMatch | /DataSet/TaxonNames/TaxonName/MicroReference |  |
| None | http://rs.tdwg.org/ontology/voc/TaxonName#microReference |  |

### tcs:nomenclaturalCode

| predicate | IRI or XPATH | remarks |
|-|-|-|
| skos:exactMatch | /DataSet/TaxonNames/TaxonName/@nomenclaturalCode |  |
| skos:exactMatch | http://rs.tdwg.org/ontology/voc/TaxonName#nomenclaturalCode |  |
| skos:exactMatch | http://rs.tdwg.org/dwc/terms/nomenclaturalCode | The TCS term is the IRI equivalent of the Darwin Core term. |

### tcs:nomenclaturalStatus

| predicate | IRI or XPATH | remarks |
|-|-|-|
| skos:exactMatch | /DataSet/TaxonNames/TaxonName/PublicationStatus |  |
| skos:exactMatch | http://rs.tdwg.org/ontology/voc/TaxonName#publicationStatus |  |
| skos:exactMatch | http://rs.tdwg.org/dwc/terms/nomenclaturalCode | The TCS term is the IRI equivalent of the Darwin Core term. |

### tcs:typification

| predicate | IRI or XPATH | remarks |
|-|-|-|
| skos:exactMatch | /DataSet/TaxonNames/TaxonName/Typification |  |

### tcs:typificationLiteral

| predicate | IRI or XPATH | remarks |
|-|-|-|
| skos:exactMatch | /DataSet/TaxonNames/TaxonName/Typification/Simple |  |

### tcs:basionym

| predicate | IRI or XPATH | remarks |
|-|-|-|
| skos:exactMatch | /DataSet/TaxonNames/TaxonName/Basionym |  |
| skos:exactMatch | http://rs.tdwg.org/ontology/voc/TaxonName#hasBasionym |  |
| skos:broadMatch | http://rs.tdwg.org/dwc/terms/originalNameUsage | `originalNameUsage` can be a `basionym` or a `replacedName` or any older name with the same type. Also note that `originalNameUsage` is a string. |

### tcs:replacedName

| predicate | IRI or XPATH | remarks |
|-|-|-|
| skos:exactMatch | /DataSet/TaxonNames/TaxonName/ReplacementNameFor |  |
| skos:exactMatch | http://rs.tdwg.org/ontology/voc/TaxonName#ReplacementNameFor |  |
| skos:broadMatch | http://rs.tdwg.org/dwc/terms/originalNameUsage | `originalNameUsage` can be a `replacedName` or a `basionym` or any older name with the same type. Also note that `originalNameUsage` is a string. |

### tcs:laterHomonymOf

| predicate | IRI or XPATH | remarks |
|-|-|-|
| skos:exactMatch | /DataSet/TaxonNames/TaxonName/LaterHomonymOf |  |
| skos:exactMatch | http://rs.tdwg.org/ontology/voc/TaxonName#LaterHomonymOf |  |

### tcs:conservedAgainst

| predicate | IRI or XPATH | remarks |
|-|-|-|
| skos:exactMatch | /DataSet/TaxonNames/TaxonName/ConservedAgainst |  |
| skos:exactMatch | http://rs.tdwg.org/ontology/voc/TaxonName#ConservedAgainst |  |

### dwc:scientificNameAuthorship

| predicate | IRI or XPATH | remarks |
|-|-|-|
| skos:exactMatch | /DataSet/TaxonNames/TaxonName/CanonicalAuthorship/Simple |  |
| skos:exactMatch | http://rs.tdwg.org/ontology/voc/TaxonName#authorship |  |

### dwc:namePublishedIn

| predicate | IRI or XPATH | remarks |
|-|-|-|
| skos:exactMatch | /DataSet/TaxonNames/TaxonName/Simple | The TCS 1 element can be used with both a 'ref' attribute and a text node. |

### dwc:namePublishedInYear

| predicate | IRI or XPATH | remarks |
|-|-|-|
| skos:exactMatch | /DataSet/TaxonNames/TaxonName/Year |  |
| skos:exactMatch | http://rs.tdwg.org/ontology/voc/TaxonName#year |  |

### dwc:genericName

| predicate | IRI or XPATH | remarks |
|-|-|-|
| skos:exactMatch | /DataSet/TaxonNames/TaxonName/CanonicalName/Genus |  |
| skos:exactMatch | http://rs.tdwg.org/ontology/voc/TaxonName#genusPart |  |

### dwc:infragenericEpithet

| predicate | IRI or XPATH | remarks |
|-|-|-|
| skos:exactMatch | /DataSet/TaxonNames/TaxonName/CanonicalName/InfragenericEpithet |  |
| skos:exactMatch | http://rs.tdwg.org/ontology/voc/TaxonName#infragenericEpithet |  |

### dwc:specificEpithet

| predicate | IRI or XPATH | remarks |
|-|-|-|
| skos:exactMatch | /DataSet/TaxonNames/TaxonName/CanonicalName/SpecificEpithet |  |
| skos:exactMatch | http://rs.tdwg.org/ontology/voc/TaxonName#specificEpithet |  |

### dwc:infraspecificEpithet

| predicate | IRI or XPATH | remarks |
|-|-|-|
| skos:exactMatch | /DataSet/TaxonNames/TaxonName/CanonicalName/InfraspecificEpithet |  |
| skos:exactMatch | http://rs.tdwg.org/ontology/voc/TaxonName#infraspecificEpithet |  |

### dwc:cultivarEpithet

| predicate | IRI or XPATH | remarks |
|-|-|-|
| skos:exactMatch | /DataSet/TaxonNames/TaxonName/CanonicalName/CultivarNameGroup |  |
| skos:exactMatch | http://rs.tdwg.org/ontology/voc/TaxonName#cultivarNameGroup |  |

## NomenclaturalType


### tcs:NomenclaturalType

| predicate | IRI or XPATH | remarks |
|-|-|-|
| skos:narrowMatch | /DataSet/TaxonNames/TaxonName/Typification/TypeVouchers/TypeVoucher/ | TCS 1 does not have an equivalent for NomenclaturalType, but has a choice between TypeName and TypeVouchers. Therefore, TypeVoucher does not include those NomenclaturalTypes that have a `typeName` rather than a `typeSpecimen`. |
| skos:broadMatch | http://rs.tdwg.org/dwc/terms/ResourceRelationship | A NomenclaturalType is in essence a special kind of ResourceRelationship connecting a name to a specimen or other name, with, depending on whether one comes from a tcs:TaxonName or a dwc:MaterialEntity, `typifiedName` being the `resourceID` and `typeSpecimen` or `typeName` the `relatedResourceID` and vice versa. |

### tcs:typifiedName

| predicate | IRI or XPATH | remarks |
|-|-|-|
|  |  | In TCS 1 there is no property relating a TypeVoucher to a TaxonName, as TypeVouchers are nested under the TaxonName. |

### tcs:typeOfType

| predicate | IRI or XPATH | remarks |
|-|-|-|
| skos:narrowMatch | /DataSet/TaxonNames/TaxonName/Typification/TypeVouchers/TypeVoucher/@typeofType | In TCS 1 only TypeVouchers have a `typeOfType`; TypeName does not. |
| skos:narrowMatch | http://rs.tdwg.org/ontology/voc/TaxonName#typeOfType |  |

### tcs:typeName

| predicate | IRI or XPATH | remarks |
|-|-|-|
| skos:exactMatch | /DataSet/TaxonNames/TaxonName/Typification/TypeName/NameReference |  |
| skos:exactMatch | http://rs.tdwg.org/ontology/voc/TaxonName#typeName |  |

### tcs:typeSpecimen

| predicate | IRI or XPATH | remarks |
|-|-|-|
| skos:exactMatch | /DataSet/TaxonNames/TaxonName/Typification/TypeVouchers/TypeVoucher/VoucherReference |  |
| skos:exactMatch | http://rs.tdwg.org/ontology/voc/TaxonName#typeSpecimen |  |

### tcs:typePublishedIn

| predicate | IRI or XPATH | remarks |
|-|-|-|
| skos:narrowMatch | /DataSet/TaxonNames/TaxonName/Typification/TypeName/LectotypePublication | Apart from TCS 1 having different elements for `LectotypePublication`for TypeName and TypeVoucher, the TCS 1 terms are ostensibly only to be used for lectotypifications, while designations of neotypes, epitypes and conserved types also takes place in different publications from the ones the names have been published in. The TCS 2 term can be used for all these typifications, as it could for typifications that are in the publication of the name. |
| skos:narrowMatch | /DataSet/TaxonNames/TaxonName/Typification/TypeVouchers/TypeVoucher/LectotypePublication |  |
