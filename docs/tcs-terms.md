# TCS Term List

**Note:** The content below is created dynamically from the
`tcs.yaml` and `<other-standard>-for-tcs.yaml` files in the [`/master`](../master) folder.
Please do not edit the markdown directly, but make any changes in the YAML
files.

## Index of terms

**classes**

[tcs:TaxonConcept](#tcstaxonconcept) | [tcs:TaxonConceptRelationship](#tcstaxonconceptrelationship) | [tcs:TaxonName](#tcstaxonname) | [tcs:NomenclaturalType](#tcsnomenclaturaltype)

**Taxon Concept**

[tcs:taxonName](#tcstaxonname) | [tcs:accordingTo](#tcsaccordingto) | [tcs:taxonomicRank](#tcstaxonomicrank) | [tcs:parent](#tcsparent) | [tcs:synonym](#tcssynonym) | [tcs:vernacularName](#tcsvernacularname) | [dcterms:title](#dctermstitle)

**Taxon Concept Relationship**

[tcs:relationshipType](#tcsrelationshiptype) | [tcs:subjectTaxonConcept](#tcssubjecttaxonconcept) | [tcs:objectTaxonConcept](#tcsobjecttaxonconcept) | [tcs:relationshipAccordingTo](#tcsrelationshipaccordingto)

**Taxon Name**

[tcs:taxonNameString](#tcstaxonnamestring) | [tcs:namePublishedIn](#tcsnamepublishedin) | [tcs:microreference](#tcsmicroreference) | [tcs:nomenclaturalCode](#tcsnomenclaturalcode) | [tcs:nomenclaturalStatus](#tcsnomenclaturalstatus) | [tcs:basionym](#tcsbasionym) | [tcs:replacementNameFor](#tcsreplacementnamefor) | [tcs:conservedAgainst](#tcsconservedagainst) | [dwc:scientificNameAuthorship](#dwcscientificnameauthorship) | [dwc:namePublishedInYear](#dwcnamepublishedinyear) | [dwc:genericName](#dwcgenericname) | [dwc:infragenericEpithet](#dwcinfragenericepithet) | [dwc:specificEpithet](#dwcspecificepithet) | [dwc:infraspecificEpithet](#dwcinfraspecificepithet) | [dwc:cultivarEpithet](#dwccultivarepithet)

**Nomenclatural Type**

[tcs:typifiedName](#tcstypifiedname) | [tcs:typeOfType](#tcstypeoftype) | [tcs:typeName](#tcstypename) | [tcs:typeSpecimen](#tcstypespecimen) | [tcs:typePublishedIn](#tcstypepublishedin)

## Taxon Concept

### tcs:TaxonConcept

<table style="width:100%;">
	<tbody>
		<tr>
			<td>Identifier</td>
			<td>http://rs.tdwg.org/tcs/terms/TaxonConcept</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>http://www.w3.org/2000/01/rdf-schema#Class</td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Taxon Concept</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td><p>An identifiable taxonomic position that can be aligned to other such  positions through TCS Taxon Concept Relationships.</p></td>
		</tr>
		<tr>
			<td>Usage</td>
			<td><p>The <code>taxonName</code> and <code>accordingTo</code> properties are required.</p></td>
		</tr>
		<tr>
			<td>GitHub issue</td>
			<td>https://github.com/tdwg/tcs2/issues/1</td>
		</tr>
	</tbody>
</table>


**Comments**

A taxonomic position is an opinion about the definition of a taxonomic  group. A Taxon Concept is identifiable, because it combines a label –  `taxonName` in TCS – with a source – `accordingTo`. Both these properties  are required. When mentioning a taxon concept, the label and the source are  also combined, separated by 'sec.' (from, 'secundus', meaning 'according  to') or 'sensu' (meaning the same). Because of the context provided by the  source, taxon concepts are in principle also alignable to other Taxon  Concepts using the TCS Taxon Concept Relationship statements.

The TCS Taxon Concept is a data object and is applied more broadly than the  term is used in science (e.g. Franz & Peet 2009). On the one hand, things  that are not generally considered to be biological taxa, e.g. hybrids and  cultivars, can be casted as TCS Taxon Concepts. Also Operational Taxonomic  Units (OTUs, cf. Sokal & Sneath 1963) can be exchanged as Taxon Concepts,  if there is a reason to do so, e.g. if one wants to align them with other  Taxon Concepts later. On the other hand, entries from treatments that are  considered to cite concepts from other treatments can be formulated as  Taxon Concepts. Every taxon concept from a treatment that is likely to be  referenced as the source of taxonomic context, for example a field guide  for a determination of a specimen or a national census for an ecological  study, can – and it would be very nice if they would – be stated as a Taxon  Concept, so they can be aligned with other Taxon Concepts that may provide  more or different taxonomic context.

By contrast, assertions of synonymy or misapplication and entries in lists  of nomenclatural types are not Taxon Concepts.


**Examples**

Taxonomic treatment:

```turtle
[] :TaxonConcept ;
    dcterms:title "Dicranoloma blumei sec. Klazenga (1999)" ;
    :taxonName [ <https://www.tropicos.org/name/35121475> a :TaxonName ;
            :taxonNameString "Dicranoloma blumei" ;
            dwc:scientificNameAuthorship "(Nees) Renauld" ] ;
    :accordingTo [ <https://www.tropicos.org/reference/9020903> a bibo:AcademicArticle ;
            dcterms:bibliographicCitation """Klazenga, N. (1999). A revision of the Malesian 
                    species of Dicranoloma (Dicranaceae, Musci). Journal of the Hattori
                    Botanical Laboratory 87: 1-130.""" ] .
```

Field guide:

```turtle
[] a :TaxonConcept ;
        dcterms:title "Orthetrum caledonicum sec. Theischinger and Hawking (2010)" ;
        :taxonName [ a :TaxonName ; 
                :taxonNameString "Orthetrum caledonicum" ] ;
        :vernacularName [ a :TaxonName ;
                :taxonNameString "Blue Skimmer" ] ;
        :accordingTo [ <urn:isbn:978-0-643-09073-6> a bibo:Book ;
                dcterms:bibliographicCitation """Theischinger, G.; Hawking, J. (2010). The 
                        complete field guide to dragonflies of Australia. CSIRO Publishing, 
                        Collingwood, Australia.""" ] .

```

Checklist:

```turtle
[] a :TaxonConcept ;
    dcterms:title "Calymperes moluccense sec. Yong et al. (2013)" ;
    :taxonName [ <https://www.tropicos.org/name/35153806> a :TaxonName ;
            :taxonNameString "Calymperes moluccense" ;
            dwc:scientificNameAuthorship "Schwägr." ] ;
    :accordingTo [ <urn:isbn:978-967-5221-99-6> a bibo:Book ;
            dcterms:bibliographicCitation """Yong, K.T.; Tan, B.C.; Ho, B.C.; Ho, Q.Y.; Mohamed, H.
                    A revised Moss Checklist of Peninsular Malaysia and Singapore. Research 
                    Pamphlet no. 133, Forest Research Institute Malaysia, Kepong, Malaysia.""" ] .
```

Plants of the World Online:

```turtle
<https://powo.science.kew.org/taxon/urn:lsid:ipni.org:names:105644-1> a :TaxonConcept ;
    dcterms:title "Begonia salaziensis sec. POWO (2022)" ;
    :taxonName [ <https://www.ipni.org/n/105644-1> a :TaxonName ;
            :taxonNameString "Begonia salaziensis" ; 
            dwc:scientificNameAuthorship "Warb." ;
            dwc:namePublishedIn """Nat. Pflanzenfam. [Engler & Prantl] iii. 6 a. (1894) 139." ] ;
    :accordingTo [ <urn:lsid:ipni.org:publications:17755-2> a bibo:Book ;
        dcterms:bibliographicCitation "Govaerts, R. (1996). World Checklist of Seed Plants 2(1, 2): 
                1-492. MIM, Deurne.""" ] .
```

Catalogue of Life:

```turtle
<https://www.catalogueoflife.org/data/taxon/KF8T#v2022-11-14> a :TaxonConcept ;
    dcterms:title "Balaenoptera musculus sec. Catalogue of Life (v2022-11-14)" ;
    :taxonName [ a :TaxonName ;
            :taxonNameString "Balaenoptera musculus" ;
            dwc:scientificNameAuthorship """(Linnaeus, 1758)" ] ;
    :accordingTo [ <https://www.catalogueoflife.org#v2022-11-14> a bibo:Website ;
            dcterms:isVersionOf "https://www.catalogueoflife.org" ;
            dcterms:title "Catalogue of Life, version 2022-11-14" ;
            bibo:uri "https://www.catalogueoflife.org""" ] .
```




### tcs:taxonName

<table style="width:100%;">
	<tbody>
		<tr>
			<td>Identifier</td>
			<td>http://rs.tdwg.org/tcs/terms/taxonName</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>http://www.w3.org/1999/02/22-rdf-syntax-ns#Property</td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Taxon Name</td>
		</tr>
		<tr>
			<td></td>
			<td><b>required:</b> Yes — <b>repeatable:</b> No</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td><p>A name or label that is given to a taxonomic group.</p></td>
		</tr>
		<tr>
			<td>Usage</td>
			<td><p><code>taxonName</code> is an IRI term and is required on a TCS Taxon Concept. A Taxon  Concept can only have one <code>taxonName</code>.</p></td>
		</tr>
		<tr>
			<td>GitHub issue</td>
			<td>https://github.com/tdwg/tcs2/issues/2</td>
		</tr>
	</tbody>
</table>


**Comments**

The `taxonName` can be anything from a well-formed scientific name to an  informal name, vernacular name, indigenous knowledge label, or even a label  containing numbers and/or special symbols, such as are often used for OTUs. 

The object of `taxonName` is an object or IRI, so that it can be reused in  other Taxon Concepts. TCS has got the Taxon Name class, which can be used  for any type of name, but people are free to use alternatives, e.g.  `skosxl:Label`, if they want to restrict the use of the Taxon Name class to  scientific (or scientific-y) names only.

### tcs:accordingTo

<table style="width:100%;">
	<tbody>
		<tr>
			<td>Identifier</td>
			<td>http://rs.tdwg.org/tcs/terms/accordingTo</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>http://www.w3.org/1999/02/22-rdf-syntax-ns#Property</td>
		</tr>
		<tr>
			<td>Label</td>
			<td>According To</td>
		</tr>
		<tr>
			<td></td>
			<td><b>required:</b> Yes — <b>repeatable:</b> No</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td><p>Reference to the treatment or other source in which a Taxon Concept is  established or used. </p></td>
		</tr>
		<tr>
			<td>Usage</td>
			<td><p><code>accordingTo</code> is an IRI term and is required on a Taxon Concept. A  Taxon Concept can have only one <code>accordingTo</code>. </p></td>
		</tr>
		<tr>
			<td>GitHub issue</td>
			<td>https://github.com/tdwg/tcs2/issues/4</td>
		</tr>
	</tbody>
</table>


**Comments**

Every Taxon Concept is in some sort of treatment and this treatment  provides important context without which we do not know what a taxon name  really means and therefore the `accordingTo` property is required for a TCS  Taxon Concept. In TCS 2, `accordingTo` has to be a reference to some sort  of resource rather than just a person's name. However, TCS is lenient about  the nature of this resource and, apart from references to bibliographic  resources, references to personal communications and determinations are  also acceptable, if there is value in supplying taxon concepts from such  communications as Taxon Concepts.

The value of `accordingTo` has to be an object or IRI. This object can  contain as little as a bibliographic reference but it is much more useful  to provide it in a format that can be understood by reference managers  such as Zotero or Mendeley.

### tcs:taxonomicRank

<table style="width:100%;">
	<tbody>
		<tr>
			<td>Identifier</td>
			<td>http://rs.tdwg.org/tcs/terms/taxonomicRank</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>http://www.w3.org/1999/02/22-rdf-syntax-ns#Property</td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Taxonomic Rank</td>
		</tr>
		<tr>
			<td></td>
			<td><b>required:</b> No — <b>repeatable:</b> No</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td><p>The rank at which a taxon is classified.</p></td>
		</tr>
		<tr>
			<td>Usage</td>
			<td><p><code>taxonomicRank</code> is an IRI property; a Taxon Concept can have only one  <code>taxonomicRank</code>.</p></td>
		</tr>
		<tr>
			<td>GitHub issue</td>
			<td>https://github.com/tdwg/tcs2/issues/32</td>
		</tr>
	</tbody>
</table>


**Comments**

The rank is an attribute of elements in a classification and `taxonomicRank`  can be applied to Taxon Concepts as well Taxon Names, as the rank of a  taxon is reflected in its name. This property takes an object or IRI and it  is recommended to use a value from an existing controlled vocabulary.  While there is no TDWG vocabulary yet, the GBIF Taxonomic Rank Vocabulary  (https://rs.gbif.org/vocabulary/gbif/rank.xml) is recommended.

### tcs:parent

<table style="width:100%;">
	<tbody>
		<tr>
			<td>Identifier</td>
			<td>http://rs.tdwg.org/tcs/terms/parent</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>http://www.w3.org/1999/02/22-rdf-syntax-ns#Property</td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Parent</td>
		</tr>
		<tr>
			<td></td>
			<td><b>required:</b> No — <b>repeatable:</b> No</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td><p>The direct parent in a classification.</p></td>
		</tr>
		<tr>
			<td>Usage</td>
			<td><p><code>parent</code> is another Taxon Concept; a Taxon Concept can have only one  <code>parent</code>.</p></td>
		</tr>
		<tr>
			<td>GitHub issue</td>
			<td>https://github.com/tdwg/tcs2/issues/8</td>
		</tr>
	</tbody>
</table>


**Comments**

The `parent` is another Taxon Concept. This is the parent as indicated in  the `accordingTo` reference, rather than a third-party classification. The  `accordingTo` of the parent will generally, but not necessarily, be the  same as that of the child. 

### tcs:synonym

<table style="width:100%;">
	<tbody>
		<tr>
			<td>Identifier</td>
			<td>http://rs.tdwg.org/tcs/terms/synonym</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>http://www.w3.org/1999/02/22-rdf-syntax-ns#Property</td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Synonym</td>
		</tr>
		<tr>
			<td></td>
			<td><b>required:</b> No — <b>repeatable:</b> Yes</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td><p>Name considered to apply to the same taxon as the accepted name.</p></td>
		</tr>
		<tr>
			<td>Usage</td>
			<td><p><code>synonym</code> is a Taxon Name; a Taxon Concept can have multiple synonyms.</p></td>
		</tr>
		<tr>
			<td>GitHub issue</td>
			<td>https://github.com/tdwg/tcs2/issues/65</td>
		</tr>
	</tbody>
</table>


**Comments**

Synonymy is between names but, if the names have different nomenclatural types, a Taxon  Concept is required. Therefore, `synonym` is a property of the Taxon Concept  class. `synonym` is used here in the stricter sense that only indicates that  the type of a name falls within a Taxon Concept and has the same  relationship to Taxon Concept as `taxonName` (the accepted name). This  allows one to dispose of names without having to deal with the Taxon  Concepts that were realised along with the publication of these names. If  one wants to include these “original concepts” and indicate a relationship  between Taxon Concepts, the `intersects` Taxon Concept Relationship can be  used instead.


**Examples**

```turtle
[] a :TaxonConcept ;
    dcterms:title "Hebe imbricata sec. Bayly & Kellow (2006)" ;
    :taxonName [ <https://www.ipni.org/n/989261-1> a :TaxonName ;
            :taxonNameString "Hebe imbricata" ;
            dwc:scientificNameAuthorship "Cockayne & Allen" ;
            dwc:namePublishedIn "Trans. & Proc. New Zealand Inst. lvii. 42 (1927) (1927)" ] ;
    :synonym [ <https://www.ipni.org/n/812507-1> a :TaxonName ;
            :taxonNameString "Veronica poppelwellii" ;
            dwc:scientificNameAuthorship "Cockayne" ; 
            dwc:namePublishedIn "Trans. & Proc. New Zealand Inst. 1915, xlviii. 200 (1916)" ] ;
    :accordingTo [ <urn:isbn:978-0-909010-12-6> a bibo:Book ;
            dcterms:bibliographicCitation """Bayly, M.; Kellow, A. (2006). An illustrated guide to 
                    New Zealand Hebes. Te Papa Press, Wellington, New Zealand.""" ] .
```


### tcs:vernacularName

<table style="width:100%;">
	<tbody>
		<tr>
			<td>Identifier</td>
			<td>http://rs.tdwg.org/tcs/terms/vernacularName</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>http://www.w3.org/1999/02/22-rdf-syntax-ns#Property</td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Vernacular Name</td>
		</tr>
		<tr>
			<td></td>
			<td><b>required:</b> No — <b>repeatable:</b> Yes</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td><p>Common or vernacular name for a taxonomic group, when used besides the  <code>taxonName</code>.</p></td>
		</tr>
		<tr>
			<td>Usage</td>
			<td><p><code>vernacularName</code> is an IRI term; a Taxon Concept can have more than one  <code>vernacularName</code>.</p></td>
		</tr>
		<tr>
			<td>GitHub issue</td>
			<td>https://github.com/tdwg/tcs2/issues/10</td>
		</tr>
	</tbody>
</table>


**Comments**

The `vernacularName` property can be used when a vernacular name is used  alongside a scientific name, which is the `taxonName`. If a vernacular name  is the only name, the `taxonName` property should be used. The object of the  `vernacularName` property can be a Taxon Name, but another label  object, such as the GBIF [Vernacular Name](https://rs.gbif.org/extension/gbif/1.0/vernacularname.xml),  might be preferrable, especially if there can be multiple vernacular names  for a concept.


**Examples**

```turtle
[] a :TaxonConcept ;
    dcterms:title "Graphium macleayanum sec. Orr & Kitching (2010)"
    :taxonName [ a :TaxonName ;
            :taxonNameString "Graphium macleayanum" ] ;
    :vernacularName [ a gbif:VernacularName ;
            dwc:vernacularName "Macleay's Swallowtail" 
            dcterms:language: "en" ] ;
    :accordingTo <urn:isbn:978-1-74175-108-6> .

<urn:isbn:978-1-74175-108-6> a bibo:Book ; 
    dcterms:bibliographicCitation """Orr, A. & Kitching, R. (2010). The 
            butterflies of Australia. Jacana Books, Crows Nest, Australia.""" .
```

```turtle
[] a :TaxonConcept ;
    dcterms:title "Quercus robur sec. Duistermaat (2020)" ;
    :taxonName <https://www.ipni.org/n/304293-2> ;
    :vernacularName [ a gbif:VernacularName ;
            dwc:vernacularName "Zomereik" ;
            dcterms:language "nl" ] ;
    :accordingTo [ <urn:isbn:978-90-01-58956-1> a bibo:Book ;
            dcterms:bibliographicCitation """Duistermaat, H. (2020). Heukels 
                    Flora van Nederland, edn 24. Noordhoff, Groningen.""" ] .

<https://www.ipni.org/n/304293-2> a :TaxonName ;
    :taxonNameString "Quercus robur" .
```

```turtle
<https://vicflora.rbg.vic.gov.au/flora/taxon/93c88fde-ab15-4a9a-a61d-3830a57a0160#2023-03-02> 
    a :TaxonConcept ;
    dcterms:title "Callitris verrucosa sec. VicFlora (2023-03-22)" ;
    :taxonName <https://www.ipni.org/n/134460-3> ;
    :vernacularName [ a gbif:VernacularName ; 
            dwc:vernacularName "Scrub Cypress-pine" ;
            dcterms:language "en" ;
            gbif:isPreferredName: <http://rs.gbif.org/vocab/boolean/true> ] ;
    :vernacularName [ a gbif:VernacularName ; 
            dwc:vernacularName "Mallee Pine" ;
            dcterms:language "en" ;
            gbif:isPreferredName: <http://rs.gbif.org/vocab/boolean/false> ] ;
    :vernacularName [ a gbif:VernacularName ; 
            dwc:vernacularName "Cow Pine" ;
            dcterms:language "en" ;
            gbif:isPreferredName: <http://rs.gbif.org/vocab/boolean/false> ] ;
    :vernacularName [ a gbif:VernacularName ; 
            dwc:vernacularName "Turpentine Pine" ;
            dcterms:language "en" ;
            gbif:isPreferredName: <http://rs.gbif.org/vocab/boolean/false> ] ;
    :accordingTo [ a bibo:website ;
            dcterms:bibliographicCitation """VicFlora (2023). Flora of Victoria, 
                    Royal Botanic Gardens Victoria. Available online: 
                    https://vicflora.rbg.vic.gov.au (accessed on: 22 Mar. 2023).""" ].

<https://www.ipni.org/n/134460-3> a TaxonName ;
    :taxonNameString "Callitris verrucosa" .
```


### dcterms:title

<table style="width:100%;">
	<tbody>
		<tr>
			<td>Identifier</td>
			<td>http://purl.org/dc/terms/title</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>http://www.w3.org/1999/02/22-rdf-syntax-ns#Property</td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Taxon concept label</td>
		</tr>
		<tr>
			<td></td>
			<td><b>required:</b> No — <b>repeatable:</b> No</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td><p>A name given to the resource.</p></td>
		</tr>
		<tr>
			<td>GitHub issue</td>
			<td>https://github.com/tdwg/tcs2/issues/222</td>
		</tr>
	</tbody>
</table>


**Comments**

In TCS `dcterms:title` is used for the taxonomic concept label (cf.  Senderov et al., 2018), which consists of the Taxon Name and a reference to  the publication where the concept is circumscribed, separated by 'sec.',  which stands for 'secundus' ('according to'). It is used to indicate one  specific meaning of a name – a Taxon Concept – rather than the cumulative  nomenclatural and taxonomic legacy associated with the name.



**Examples**

```
Andropogon virginicus var. tenuis-patheus sec. Blomquist (1948)
Perelleschus sec. Franz & Cardona-Duque (2013)
```

## Taxon Concept Relationship

### tcs:TaxonConceptRelationship

<table style="width:100%;">
	<tbody>
		<tr>
			<td>Identifier</td>
			<td>http://rs.tdwg.org/tcs/terms/TaxonConceptRelationship</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>http://www.w3.org/2000/01/rdf-schema#Class</td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Taxon Concept Relationship</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td><p>Topological relationship between two Taxon Concepts.</p></td>
		</tr>
		<tr>
			<td>Usage</td>
			<td><p><code>relationshipType</code>, <code>subjectTaxonConcept</code>, <code>objectTaxonConcept</code> and  <code>relationshipAccordingTo</code> are all required.</p></td>
		</tr>
		<tr>
			<td>GitHub issue</td>
			<td>https://github.com/tdwg/tcs2/issues/43</td>
		</tr>
	</tbody>
</table>


**Comments**

Taxon Concept Relationships are a set of relationships that allow for the  alignment of Taxon Concepts – or taxon concept mapping. The main  relationship types coincide with topological relationships that are widely  used in spatial analysis, analysis of computer networks, artificial  intelligence, etc. In particular, they are the relationships that are used  in RCC-5 Region Connection Calculus, which allows for reasoning.

An extra controlled term `intersects` has been added to the Taxon Concept  Relationship Type Vocabulary to accommodate Taxon Concept Relationship  statements between Taxon Concepts of which we know that they have at least  one member in common, but where the more specific topological relationship  is not easily inferred.

Taxon Concept Relationship statements can be made in the treatment of the  subject Taxon Concept or by third parties.


**Examples**

```turtle
# Athyriaceae sec. Rothfels et al. (2012) is proper subset of Woodsiaceae sec. Smith et al. (2006)
[] a :TaxonRelationship ; 
    :relationshipType tcreltype:isProperSubsetOf ; 
    :subjectTaxonConcept [ a :TaxonConcept ; 
            dcterms:title "Athyriaceae sec. Rothfels et al. (2012)" ;
            :taxonName [ a :TaxonName ;
                    :taxonNameString "Athyriaceae" ] ;
            :accordingTo <https://doi.org/10.1002/tax.613003> ] ;
    :objectTaxonConcept [ a :TaxonConcept ;
            dcterms:title "Woodsiaceae sec. Smith et al. (2006)" ;
            :taxonName [ a :TaxonName ;
                    :taxonNameString "Woodsiaceae" ] ;
            :accordingTo <https://doi.org/10.2307/25065646> ] ;
    :relationshipAccordingTo <https://doi.org/10.1002/tax.613003> .

<https://doi.org/10.1002/tax.613003> a bibo:AcademicArticle ;
    dcterms:bibliographicCitation """Rothfels, Carl J.; Sundue, Michael A.; Kuo, Li-Yaung; Larsson, 
            Anders; Kato, Masahiro; Schuettpelz, Eric; Pryer, Kathleen M. (2012). A revised 
            family–level classification for eupolypod II ferns (Polypodiidae: Polypodiales). Taxon 
            61(3): 515-533.""" .

<https://doi.org/10.2307/25065646> a bibo:AcademicArticle ;
    dcterms:bibliographicCitation """Smith, Alan R.; Pryer, Kathleen M.; Schuettpelz, Eric; Korall, 
            Petra; Schneider, Harald; Wolf, Paul G. (2006). A classification for extant ferns. Taxon 
            55(3): 705-731.""" .
```

```turtle
# Dicranum fuscescens sec. Koperski et al. (2000) is congruent with Dicranum fuscescens sec. Corley 
# et al. (1981)
[] a :TaxonRelationship ;
        :relationshipType tcreltype:isCongruentWith ; 
        :subjectTaxonConcept [ a :TaxonConcept ;
                dcterms:title "Dicranum fuscescens sec. Koperski et al. (2000)" ;
                :taxonName <https://www.tropicos.org/name/35122385> ;
                :accordingTo <https://www.tropicos.org/reference/9022656> ] ;
        :objectTaxonConcept [ a :TaxonConcept ;
                dcterms:title "Dicranum fuscescens sec. Corley et al. (1981)" ;
                :taxonName <https://www.tropicos.org/name/35122385> ;
                :accordingTo <https://www.tropicos.org/reference/9004554> ] ;
        :raletionshipAccordingTo <https://www.tropicos.org/reference/9022656> .

<https://www.tropicos.org/name/35122385> a :TaxonName ;
    :taxonNameString "Dicranum fuscescens" ;
    dwc:scientificNameAuthorship "Turner" .        

<https://www.tropicos.org/reference/9022656> a bibo:Book ;
    dcterms:bibliographicCitation """Koperski, Monika; Sauer, Michael; Braun, Walter; Gradstein, S. 
            Rob (2000). Referenzliste der Moose Deuthschlands. Schriftenreihe für Vegetationskunde 
            34. Bundersamt für Naturschutz, Bonn-Bad Godesberg.""" .

<https://www.tropicos.org/reference/9004554> a bibo:AcademicArticle ;
    dcterms:bibliographicCitation """Corley, M.F.V.; Crundwell, A.C.; Düll, R.; Hill, M.O.; Smith, 
    A.J.E. (1981). Mosses of Europe and the Azores; an annotated list of species, with synonyms from 
    the recent literature. Journal of Bryology 11(4): 609-689.""" .
```

```turtle
# Phyllotrox sec. Franz & O'Brien (2001) partially overlaps Phyllotrox sec. Franz (2006)
[] a :TaxonRelationship ;
    :relationshipType tcreltype:partiallyOverlaps ;
    :subjectTaxonConcept [ a :TaxonConcept ;
            dcterms:title "Phyllotrox sec. Franz & O'Brien (2001)" ;
            :taxonName _:n1 ;
            :accordingTo <https://www.jstor.org/stable/25078744> ] ;
    :objectTaxonConcept [ a :TaxonConcept ; 
            dcterms:title "Phyllotrox sec. Franz (2006)" ;
            :taxonName _:n1 ;
            :accordingTo <https://doi.org/10.1111/j.1365-3113.2005.00308.x> ] ;
    :relationshipAccordingTo <https://doi.org/10.1111/cla.12042> .

_:n1 a :TaxonName ;
    :taxonNameString "Phyllotrox" ;
    dwc:scientificNameAuthorship "Schoenherr" .

<https://www.jstor.org/stable/25078744> a bibo:AcademicArticle ;
    dcterms:bibliographicCitation """Franz, Nico M.; O`Brien, Charles W. (2001). Revision and 
            phylogeny of Perelleschus (Coleoptera: Curculionidae) with notes on its Association with 
            Carludovica (Cyclanthaceae). Transactions of the American Entomological Society 127(2): 
            255-287""" .

<https://doi.org/10.1111/j.1365-3113.2005.00308.x> a bibo: AcademicArticle ;
    dcterms:bibliographicReference """Franz, Nico M. (2006). Towards a phylogenetic system of 
            derelomine flower weevils (Coleoptera: Curculionidae). Systematic Entomology 31(2): 
            220-287.""" .

<https://doi.org/10.1111/cla.12042> a bibo:AcademicArticle ;
    dcterms:bibliographicCitation """Franz, Nico M. (2014). Anatomy of a cladistic analysis. 
            Cladistics 30(3): 294-321.""" .
```


### tcs:relationshipType

<table style="width:100%;">
	<tbody>
		<tr>
			<td>Identifier</td>
			<td>http://rs.tdwg.org/tcs/terms/relationshipType</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>http://www.w3.org/1999/02/22-rdf-syntax-ns#Property</td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Relationship type</td>
		</tr>
		<tr>
			<td></td>
			<td><b>required:</b> Yes — <b>repeatable:</b> No</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td><p>The type of relationship.</p></td>
		</tr>
		<tr>
			<td>Usage</td>
			<td><p>This property is required; one MUST use a term from the Taxon Concept  Relationship Vocabulary.</p></td>
		</tr>
		<tr>
			<td>GitHub issue</td>
			<td>https://github.com/tdwg/tcs2/issues/44</td>
		</tr>
	</tbody>
</table>

### tcs:subjectTaxonConcept

<table style="width:100%;">
	<tbody>
		<tr>
			<td>Identifier</td>
			<td>http://rs.tdwg.org/tcs/terms/subjectTaxonConcept</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>http://www.w3.org/1999/02/22-rdf-syntax-ns#Property</td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Subject Taxon Concept</td>
		</tr>
		<tr>
			<td></td>
			<td><b>required:</b> Yes — <b>repeatable:</b> No</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td><p>Taxon Concept that is the subject in the relationship statement.</p></td>
		</tr>
		<tr>
			<td>Usage</td>
			<td><p><code>subjectTaxonConcept</code> is a TCS Taxon Concept; a Taxon Concept Relationship  statement can have only one <code>subjectTaxonConcept</code>.</p></td>
		</tr>
		<tr>
			<td>GitHub issue</td>
			<td>https://github.com/tdwg/tcs2/issues/45</td>
		</tr>
	</tbody>
</table>


**Comments**

This is the Taxon Concept at the left-hand side of the relationship  statement.

### tcs:objectTaxonConcept

<table style="width:100%;">
	<tbody>
		<tr>
			<td>Identifier</td>
			<td>http://rs.tdwg.org/tcs/terms/objectTaxonConcept</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>http://www.w3.org/1999/02/22-rdf-syntax-ns#Property</td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Object Taxon Concept</td>
		</tr>
		<tr>
			<td></td>
			<td><b>required:</b> Yes — <b>repeatable:</b> No</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td><p>Taxon Concept that is the object in the relationship statement.</p></td>
		</tr>
		<tr>
			<td>Usage</td>
			<td><p><code>objectTaxonConcept</code> is a TCS Taxon Concept; a Taxon Concept Relationship  statement can have only one <code>objectTaxonConcept</code>.</p></td>
		</tr>
		<tr>
			<td>GitHub issue</td>
			<td>https://github.com/tdwg/tcs2/issues/46</td>
		</tr>
	</tbody>
</table>


**Comments**

This is the Taxon Concept at the right-hand side of the relationship  statement.

### tcs:relationshipAccordingTo

<table style="width:100%;">
	<tbody>
		<tr>
			<td>Identifier</td>
			<td>http://rs.tdwg.org/tcs/terms/relationshipAccordingTo</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>http://www.w3.org/1999/02/22-rdf-syntax-ns#Property</td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Relationship According To</td>
		</tr>
		<tr>
			<td></td>
			<td><b>required:</b> Yes — <b>repeatable:</b> No</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td><p>Reference to the source of the taxon concept relationship statement.</p></td>
		</tr>
		<tr>
			<td>Usage</td>
			<td><p><code>relationshipAccordingTo</code> is an IRI term and is required; a Taxon  Relationship statement can have only one <code>relationshipAccordingTo</code>.</p></td>
		</tr>
		<tr>
			<td>GitHub issue</td>
			<td>https://github.com/tdwg/tcs2/issues/47</td>
		</tr>
	</tbody>
</table>


**Comments**

In the case of Taxon Concept Relationships from traditional synonymy, the  `relationshipAccordingTo` is the same as the `accordingTo` of the Taxon  Concept that is the `subjectTaxonConcept`.

## Taxon Name

### tcs:TaxonName

<table style="width:100%;">
	<tbody>
		<tr>
			<td>Identifier</td>
			<td>http://rs.tdwg.org/tcs/terms/TaxonName</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>http://www.w3.org/2000/01/rdf-schema#Class</td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Taxon Name</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td><p>A name or label applied to a taxon or taxonomic group.</p></td>
		</tr>
		<tr>
			<td>Usage</td>
			<td><p>A TCS Taxon Name only requires a <code>taxonNameString</code>.</p></td>
		</tr>
		<tr>
			<td>GitHub issue</td>
			<td>https://github.com/tdwg/tcs2/issues/15</td>
		</tr>
	</tbody>
</table>


**Comments**

The word 'name' here is taken in its dictionary meaning and not in the  sense of a particular nomenclatural code. This means that the Taxon Name  class can be used for any type of name, not just names that are validly  published under the relevant nomenclatural code.


**Examples**

```turtle
<urn:lsid:zoobank.org:act:355AAA50-D89F-466E-A216-96B7A17D5AD4> a :TaxonName ;
    :taxonNameString "Carabus nitens"
    dwc:scientificNameAuthorship "Linnaeus, 1758" .
```

```turtle
<https://www.ipni.org/n/316069-1> a :TaxonName ;
    :taxonNameString "Rafflesia arnoldii" ;
    dwc:scientificNameAuthorship "R.Br." ;
    dwc:namePublishedIn "Account Rafflesia 7, tt. 15-22 (1821)" .
```

```turtle
<http://www.indexfungorum.org/names/NamesRecord.asp?RecordID=178962> a :TaxonName ;
    :taxonNameString "Amanita phalloides" ;
    dwc:scientificNameAuthorship "(Vaill. ex Fr.) Link" ;
    dwc:namePublishedIn "Handb. Erk. Gew. 3: 272 (1833)" .
```


### tcs:taxonNameString

<table style="width:100%;">
	<tbody>
		<tr>
			<td>Identifier</td>
			<td>http://rs.tdwg.org/tcs/terms/taxonNameString</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>http://www.w3.org/1999/02/22-rdf-syntax-ns#Property</td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Taxon Name String</td>
		</tr>
		<tr>
			<td></td>
			<td><b>required:</b> Yes — <b>repeatable:</b> No</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td><p>The complete name string without any authority or year components.</p></td>
		</tr>
		<tr>
			<td>Usage</td>
			<td><p><code>taxonNameString</code> is a literal and is required on a TCS TAxon Name. A Taxon  Name can have only one <code>taxonNameString</code>.</p></td>
		</tr>
		<tr>
			<td>GitHub issue</td>
			<td>https://github.com/tdwg/tcs2/issues/16</td>
		</tr>
	</tbody>
</table>


**Comments**

The `taxonNameString` property differs from the `scientificName` property  in Darwin Core in that all kinds of names are allowed. Also, in the case of  scientific names, contrary to the `dwc:scientificName`, `taxonNameString`  does not include the authorship. In botanical names, it does include the  rank prefixes for infrageneric and infraspecific epithets as they are  considered part of the name.

### tcs:namePublishedIn

<table style="width:100%;">
	<tbody>
		<tr>
			<td>Identifier</td>
			<td>http://rs.tdwg.org/tcs/terms/namePublishedIn</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>http://www.w3.org/1999/02/22-rdf-syntax-ns#Property</td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Name Published In</td>
		</tr>
		<tr>
			<td></td>
			<td><b>required:</b> No — <b>repeatable:</b> No</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td><p>Reference to the publication in which the name was first published.</p></td>
		</tr>
		<tr>
			<td>Usage</td>
			<td><p><code>taxonNameString</code> is a literal; there can only be one <code>taxonNameString</code> on  a Taxon Name.</p></td>
		</tr>
		<tr>
			<td>GitHub issue</td>
			<td>https://github.com/tdwg/tcs2/issues/29</td>
		</tr>
	</tbody>
</table>


**Comments**

In botany, this would be the protologue. This is the IRI counterpart of  the Darwin Core `namePublishedIn`.

### tcs:microreference

<table style="width:100%;">
	<tbody>
		<tr>
			<td>Identifier</td>
			<td>http://rs.tdwg.org/tcs/terms/microreference</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>http://www.w3.org/1999/02/22-rdf-syntax-ns#Property</td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Microreference</td>
		</tr>
		<tr>
			<td></td>
			<td><b>required:</b> No — <b>repeatable:</b> No</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td><p>Specifies any minor reference parts, e.g. page number.</p></td>
		</tr>
		<tr>
			<td>Usage</td>
			<td><p><code>microreference</code> is a string literal; a Taxon Name can have only one  <code>microreference</code> and only when <code>namePublishedIn</code> is used as well.</p></td>
		</tr>
		<tr>
			<td>GitHub issue</td>
			<td>https://github.com/tdwg/tcs2/issues/30</td>
		</tr>
	</tbody>
</table>


**Comments**

In taxonomic works it is convention to cite the exact location in a work  where a new name is published. The `microreference` property lets one do  that on the Taxon Name object, so that the `namePublishedIn` reference can  be reused.

### tcs:nomenclaturalCode

<table style="width:100%;">
	<tbody>
		<tr>
			<td>Identifier</td>
			<td>http://rs.tdwg.org/tcs/terms/nomenclaturalCode</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>http://www.w3.org/1999/02/22-rdf-syntax-ns#Property</td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Nomenclatural Code</td>
		</tr>
		<tr>
			<td></td>
			<td><b>required:</b> No — <b>repeatable:</b> No</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td><p>Nomenclatural code that applies to the group of organisms the taxonomic name  is for.</p></td>
		</tr>
		<tr>
			<td>Usage</td>
			<td><p><code>nomenclaturalCode</code> takes an IRI or object; a Taxon Name can have only one  <code>nomenclaturalCode</code>.</p></td>
		</tr>
		<tr>
			<td>GitHub issue</td>
			<td>https://github.com/tdwg/tcs2/issues/33</td>
		</tr>
	</tbody>
</table>


**Comments**

This is the IRI equivalent of the Darwin Core `nomenclaturalCode`. In the  absence of a TDWG vocabulary, it is recommended to use a value from the GBIF  Nomenclatural Codes Vocabulary  (https://rs.gbif.org/vocabulary/gbif/nomenclatural_code.xml).

### tcs:nomenclaturalStatus

<table style="width:100%;">
	<tbody>
		<tr>
			<td>Identifier</td>
			<td>http://rs.tdwg.org/tcs/terms/nomenclaturalStatus</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>http://www.w3.org/1999/02/22-rdf-syntax-ns#Property</td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Nomenclatural Status</td>
		</tr>
		<tr>
			<td></td>
			<td><b>required:</b> No — <b>repeatable:</b> No</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td><p>Status related to the original publication of the name and its conformance to the relevant rules of nomenclature.</p></td>
		</tr>
		<tr>
			<td>Usage</td>
			<td><p><code>nomenclaturalStatus</code> takes an IRI or object; a Taxon Name can have only one  <code>nomenclaturalStatus</code>.</p></td>
		</tr>
		<tr>
			<td>GitHub issue</td>
			<td>https://github.com/tdwg/tcs2/issues/35</td>
		</tr>
	</tbody>
</table>


**Comments**

This is the IRI equivalent of the Darwin Core `nomenclaturalStatus`. In the  absence of a TDWG vocabulary, it is recommended to use a value from the GBIF  Nomenclatural Status Vocabulary  (https://rs.gbif.org/vocabulary/gbif/nomenclatural_status.xml).

### tcs:basionym

<table style="width:100%;">
	<tbody>
		<tr>
			<td>Identifier</td>
			<td>http://rs.tdwg.org/tcs/terms/basionym</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>http://www.w3.org/1999/02/22-rdf-syntax-ns#Property</td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Basionym</td>
		</tr>
		<tr>
			<td></td>
			<td><b>required:</b> No — <b>repeatable:</b> No</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td><p>Original name on which the present name is based.</p></td>
		</tr>
		<tr>
			<td>Usage</td>
			<td><p>A <code>basionym</code> is another Taxon Name; a Taxon Name can have only one  <code>basionym</code>.</p></td>
		</tr>
		<tr>
			<td>GitHub issue</td>
			<td>https://github.com/tdwg/tcs2/issues/36</td>
		</tr>
	</tbody>
</table>


**Comments**

A basionym is the epithet-bringing name.  The `basionym` property is only  used for new combinations ('comb. nov.'). If the new name is an avowed  substitute ('nom. nov.') the `replacementNameFor` property should be used  instead.


**Examples**

```turtle
<https://id.biodiversity.org.au/name/apni/166271> a TaxonName ;
    rdf:seeAlso <https://www.ipni.org/n/17571690-1> ;
    :taxonNameString "Doodia australis" ;
    dwc:scientificNameAuthorship "(Parris) Parris" ;
    dwc:namePublishedIn "Fl. Australia 48: 710 (1998)" ;
    :basionym [ <https://id.biodiversity.org.au/name/apni/117170> a :TaxonName ;
            rdf:seeAlso <https://www.ipni.org/n/17567870-1> ;
            :taxonNameString "Doodia media subsp. australis" ;
            dwc:scientificNameAuthorship "Parris" ;
            dwc:namePublishedIn "New Zealand J. Bot. 10(4): 593 (1972)" ] .
```


### tcs:replacementNameFor

<table style="width:100%;">
	<tbody>
		<tr>
			<td>Identifier</td>
			<td>http://rs.tdwg.org/tcs/terms/replacementNameFor</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>http://www.w3.org/1999/02/22-rdf-syntax-ns#Property</td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Replacement Name For</td>
		</tr>
		<tr>
			<td></td>
			<td><b>required:</b> No — <b>repeatable:</b> No</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td><p>Name for which this name is a replacement</p></td>
		</tr>
		<tr>
			<td>Usage</td>
			<td><p><code>replacementNameFor</code> is another Taxon Name; a Taxon Name can have only one  <code>replaccementNameFor</code>.</p></td>
		</tr>
		<tr>
			<td>GitHub issue</td>
			<td>https://github.com/tdwg/tcs2/issues/37</td>
		</tr>
	</tbody>
</table>


**Comments**

This is the 'replaced synonym' of the Botanical Code, which is to an avowed  substitute ('nom. nov.') what 'basionym' is to a new combination  ('comb. nov.')

### tcs:conservedAgainst

<table style="width:100%;">
	<tbody>
		<tr>
			<td>Identifier</td>
			<td>http://rs.tdwg.org/tcs/terms/conservedAgainst</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>http://www.w3.org/1999/02/22-rdf-syntax-ns#Property</td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Conserved Against</td>
		</tr>
		<tr>
			<td></td>
			<td><b>required:</b> No — <b>repeatable:</b> Yes</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td><p>Name(s) against which this name is conserved.</p></td>
		</tr>
		<tr>
			<td>Usage</td>
			<td><p>The <code>conservedAgainst</code> property takes another Taxon Name; a Taxon Name can  be conserved against more than one other Taxon Names.</p></td>
		</tr>
		<tr>
			<td>GitHub issue</td>
			<td>https://github.com/tdwg/tcs2/issues/39</td>
		</tr>
	</tbody>
</table>


**Comments**

A scientific name is not conserved against all other names, but only  against one or more names that in turn are rejected against the conserved  name. A name can be conserved against more than one other name, so this  property is repeatable.

### dwc:scientificNameAuthorship

<table style="width:100%;">
	<tbody>
		<tr>
			<td>Identifier</td>
			<td>http://rs.tdwg.org/dwc/terms/scientificNameAuthorship</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>http://www.w3.org/1999/02/22-rdf-syntax-ns#Property</td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Scientific Name Authorship</td>
		</tr>
		<tr>
			<td></td>
			<td><b>required:</b> No — <b>repeatable:</b> No</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td><p>The authorship information for the <code>scientificName</code> formatted according to  the conventions of the applicable <code>nomenclaturalCode</code>.</p></td>
		</tr>
		<tr>
			<td>Usage</td>
			<td><p><code>scientificNameAuthorship</code> can be used if the <code>taxonNameString</code> is a  scientific name.</p></td>
		</tr>
		<tr>
			<td>GitHub issue</td>
			<td>https://github.com/tdwg/tcs2/issues/24</td>
		</tr>
	</tbody>
</table>

### dwc:namePublishedInYear

<table style="width:100%;">
	<tbody>
		<tr>
			<td>Identifier</td>
			<td>http://rs.tdwg.org/dwc/terms/namePublishedInYear</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>http://www.w3.org/1999/02/22-rdf-syntax-ns#Property</td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Name Published In Year</td>
		</tr>
		<tr>
			<td></td>
			<td><b>required:</b> No — <b>repeatable:</b> No</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td><p>The four-digit year in which the <code>scientificName</code> was published.</p></td>
		</tr>
		<tr>
			<td>Usage</td>
			<td><p>This is the publication year for the present name combination, not the basionym should this be a new combination.</p></td>
		</tr>
		<tr>
			<td>GitHub issue</td>
			<td>https://github.com/tdwg/tcs2/issues/31</td>
		</tr>
	</tbody>
</table>

### dwc:genericName

<table style="width:100%;">
	<tbody>
		<tr>
			<td>Identifier</td>
			<td>http://rs.tdwg.org/dwc/terms/genericName</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>http://www.w3.org/1999/02/22-rdf-syntax-ns#Property</td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Generic Name</td>
		</tr>
		<tr>
			<td></td>
			<td><b>required:</b> No — <b>repeatable:</b> No</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td><p>The genus part of the <code>scientificName</code> without authorship.</p></td>
		</tr>
		<tr>
			<td>Usage</td>
			<td><p>This property should only be used for names below the rank of genus.</p></td>
		</tr>
		<tr>
			<td>GitHub issue</td>
			<td>https://github.com/tdwg/tcs2/issues/19</td>
		</tr>
	</tbody>
</table>

### dwc:infragenericEpithet

<table style="width:100%;">
	<tbody>
		<tr>
			<td>Identifier</td>
			<td>http://rs.tdwg.org/dwc/terms/infragenericEpithet</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>http://www.w3.org/1999/02/22-rdf-syntax-ns#Property</td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Infrageneric Epithet</td>
		</tr>
		<tr>
			<td></td>
			<td><b>required:</b> No — <b>repeatable:</b> No</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td><p>The infrageneric part of combinations at ranks above species but below  genus.</p></td>
		</tr>
		<tr>
			<td>Usage</td>
			<td><p>Names at ranks between species and genus, e.g. subgenera and sections, are  composed of two parts; the genus and the infrageneric epithet. This property  should therefore always be accompanied by the <code>genericName</code> property. If the  <code>infragenericEpithet</code> property is present, the <code>specificEpithet</code> and  <code>infraspecificEpithet</code> properties should be absent. </p></td>
		</tr>
		<tr>
			<td>GitHub issue</td>
			<td>https://github.com/tdwg/tcs2/issues/20</td>
		</tr>
	</tbody>
</table>

### dwc:specificEpithet

<table style="width:100%;">
	<tbody>
		<tr>
			<td>Identifier</td>
			<td>http://rs.tdwg.org/dwc/terms/specificEpithet</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>http://www.w3.org/1999/02/22-rdf-syntax-ns#Property</td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Specific Epithet</td>
		</tr>
		<tr>
			<td></td>
			<td><b>required:</b> No — <b>repeatable:</b> No</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td><p>The name of the first or species epithet of the scientificName.</p></td>
		</tr>
		<tr>
			<td>Usage</td>
			<td><p>Names at ranks of species and below are composed of two or three words; the  genus name, the specific epithet and possibly an infraspecific epithet.  This property should therefore always be accompanied by the <code>genus</code> property.  If the <code>specificEpithet</code> property is present the <code>uninomial</code> and  <code>infragenericEpithet</code> properties should be absent.</p></td>
		</tr>
		<tr>
			<td>GitHub issue</td>
			<td>https://github.com/tdwg/tcs2/issues/21</td>
		</tr>
	</tbody>
</table>

### dwc:infraspecificEpithet

<table style="width:100%;">
	<tbody>
		<tr>
			<td>Identifier</td>
			<td>http://rs.tdwg.org/dwc/terms/infraspecificEpithet</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>http://www.w3.org/1999/02/22-rdf-syntax-ns#Property</td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Infraspecific Epithet</td>
		</tr>
		<tr>
			<td></td>
			<td><b>required:</b> No — <b>repeatable:</b> No</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td><p>The name of the lowest or terminal infraspecific epithet of the  <code>scientificName</code>, excluding any rank designation.</p></td>
		</tr>
		<tr>
			<td>Usage</td>
			<td><p>Names at ranks below species are composed of three words; the genus name,  the specific epithet and an infraspecific epithet. This property should  therefore always be accompanied by the <code>genus</code> and <code>specificEpithet</code>  properties. If the <code>specificEpithet</code> property is present the <code>uninomial</code> and <code>infragenericEpithet</code> properties should be absent.</p></td>
		</tr>
		<tr>
			<td>GitHub issue</td>
			<td>https://github.com/tdwg/tcs2/issues/22</td>
		</tr>
	</tbody>
</table>

### dwc:cultivarEpithet

<table style="width:100%;">
	<tbody>
		<tr>
			<td>Identifier</td>
			<td>http://rs.tdwg.org/dwc/terms/cultivarEpithet</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>http://www.w3.org/1999/02/22-rdf-syntax-ns#Property</td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Cultivar Epithet</td>
		</tr>
		<tr>
			<td></td>
			<td><b>required:</b> No — <b>repeatable:</b> No</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td><p>Part of the name of a cultivar, cultivar group or grex that follows the  scientific name.</p></td>
		</tr>
		<tr>
			<td>Usage</td>
			<td><p>The cultivar epithet follows a well-formed botanical name. Only include the string of the epithet. i.e. omit the single quotes around cultivar  names, the word 'Group' that denotes cultivar group and the + sign  used in chimeras.</p></td>
		</tr>
		<tr>
			<td>GitHub issue</td>
			<td>https://github.com/tdwg/tcs2/issues/23</td>
		</tr>
	</tbody>
</table>

## Nomenclatural Type

### tcs:NomenclaturalType

<table style="width:100%;">
	<tbody>
		<tr>
			<td>Identifier</td>
			<td>http://rs.tdwg.org/tcs/terms/NomenclaturalType</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>http://www.w3.org/2000/01/rdf-schema#Class</td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Nomenclatural Type</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td><p>Element to which a scientific name is permanently attached.</p></td>
		</tr>
		<tr>
			<td>Usage</td>
			<td><p>A Nomenclatural Type requires a <code>typifiedName</code> and either a <code>typeName</code> or  <code>typeSpecimen</code>.</p></td>
		</tr>
		<tr>
			<td>GitHub issue</td>
			<td>https://github.com/tdwg/tcs2/issues/58</td>
		</tr>
	</tbody>
</table>


**Comments**

A nomenclatural type fixes the usage of a name to the taxonomic group that  contains the type. One or more Nomenclatural Types make up the typification  of a Taxon Name. In Darwin Core RDF, NomenclaturalType can be used as object  with `dwciri:typeStatus`.

### tcs:typifiedName

<table style="width:100%;">
	<tbody>
		<tr>
			<td>Identifier</td>
			<td>http://rs.tdwg.org/tcs/terms/typifiedName</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>http://www.w3.org/1999/02/22-rdf-syntax-ns#Property</td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Typified Name</td>
		</tr>
		<tr>
			<td></td>
			<td><b>required:</b> Yes — <b>repeatable:</b> No</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td><p>The scientific name for which the specimen or other name is the type.</p></td>
		</tr>
		<tr>
			<td>Usage</td>
			<td><p><code>typifiedName</code> is a Taxon Name and is required; a Nomenclatural Type can  typify only one Taxon Name.</p></td>
		</tr>
		<tr>
			<td>GitHub issue</td>
			<td>https://github.com/tdwg/tcs2/issues/59</td>
		</tr>
	</tbody>
</table>


**Comments**

The `typifiedName` property links the Nomenclatural Type back to the Taxon  Name. Also, when coming from the Preserved Specimen, the typified name is  the most important piece of information, because there is no point in  knowing what kind of type a specimen is without knowing for what name it  is the type. Therefore, `typifiedName` is a required property.

### tcs:typeOfType

<table style="width:100%;">
	<tbody>
		<tr>
			<td>Identifier</td>
			<td>http://rs.tdwg.org/tcs/terms/typeOfType</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>http://www.w3.org/1999/02/22-rdf-syntax-ns#Property</td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Type of Type</td>
		</tr>
		<tr>
			<td></td>
			<td><b>required:</b> No — <b>repeatable:</b> No</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td><p>The kind of type this specimen is, e.g. holotype, isotype etc.</p></td>
		</tr>
		<tr>
			<td>Usage</td>
			<td><p><code>typeOfType</code> is an IRI term and should take its value from a controlled  vocabulary. A Nomenclatural Type can have only one</p></td>
		</tr>
		<tr>
			<td>GitHub issue</td>
			<td>https://github.com/tdwg/tcs2/issues/60</td>
		</tr>
	</tbody>
</table>


**Comments**

This is an IRI property. In the absence of a TDWG controlled vocabulary,  it is recommended to use a value from the GBIF Nomenclatural Type Status  Vocabulary (https://rs.gbif.org/vocabulary/gbif/type_status.xml).

### tcs:typeName

<table style="width:100%;">
	<tbody>
		<tr>
			<td>Identifier</td>
			<td>http://rs.tdwg.org/tcs/terms/typeName</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>http://www.w3.org/1999/02/22-rdf-syntax-ns#Property</td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Type Name</td>
		</tr>
		<tr>
			<td></td>
			<td><b>required:</b> No — <b>repeatable:</b> No</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td><p>The name that is the type.</p></td>
		</tr>
		<tr>
			<td>Usage</td>
			<td><p><code>typeName</code> is a Taxon Name. A nomenclatural type can have only one  <code>typeName</code>.</p></td>
		</tr>
		<tr>
			<td>GitHub issue</td>
			<td>https://github.com/tdwg/tcs2/issues/61</td>
		</tr>
	</tbody>
</table>


**Comments**

Taxon names at ranks above species level can be typified by the name of a  lower taxon. Ultimately, by following the chain of type names, all names  resolve to a type species and thus a type specimen. 

### tcs:typeSpecimen

<table style="width:100%;">
	<tbody>
		<tr>
			<td>Identifier</td>
			<td>http://rs.tdwg.org/tcs/terms/typeSpecimen</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>http://www.w3.org/1999/02/22-rdf-syntax-ns#Property</td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Type Specimen</td>
		</tr>
		<tr>
			<td></td>
			<td><b>required:</b> No — <b>repeatable:</b> No</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td><p>The specimen that is the type.</p></td>
		</tr>
		<tr>
			<td>Usage</td>
			<td><p><code>typeSpecimen</code> takes an IRI – or object – that refers to a specimen. A  Nomenclatural Type can only have one <code>typeSpecimen</code>.</p></td>
		</tr>
		<tr>
			<td>GitHub issue</td>
			<td>https://github.com/tdwg/tcs2/issues/62</td>
		</tr>
	</tbody>
</table>


**Comments**

Names at ranks of family and below are typified by a specimen. This property  is mutually exclusive with `typeName`. This is an IRI property. One could  use the Darwin Core Preserved Specimen. While a Taxon Name can have more  than one type specimens, each of these type specimens requires its own  Nomenclatural Type record, so a Nomenclatural Type can have only one  `typeSpecimen`.

### tcs:typePublishedIn

<table style="width:100%;">
	<tbody>
		<tr>
			<td>Identifier</td>
			<td>http://rs.tdwg.org/tcs/terms/typePublishedIn</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>http://www.w3.org/1999/02/22-rdf-syntax-ns#Property</td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Type Published In</td>
		</tr>
		<tr>
			<td></td>
			<td><b>required:</b> No — <b>repeatable:</b> No</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td><p>Publication where the type was nominated</p></td>
		</tr>
		<tr>
			<td>Usage</td>
			<td><p><code>typePublishedIn</code> is an IRI term. A Nomenclatural Type can have at most one  <code>typePublishedIn</code>. </p></td>
		</tr>
		<tr>
			<td>GitHub issue</td>
			<td>https://github.com/tdwg/tcs2/issues/63</td>
		</tr>
	</tbody>
</table>


**Comments**

`typePublishedIn` is relevant for lectotypes, neotypes, epitypes and  conserved types. For other kinds of type the publication where the type is  designated is the publication where the name was published.

<!-- termlist-footer.md ==>
