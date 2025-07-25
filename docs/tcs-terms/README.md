# Taxon Concept Standard (TCS) term list

**Title**: Taxon Concept Standard (TCS) term list

**Date version created**: yyyy-mm-dd

**Part of TDWG standard**: 

**This version**:

**Latest version**:

**Abstract**: The Taxon Concept Standard (TCS) is the TDWG standard specifically
for sharing taxonomic and nomenclatural data. TCS provides TaxonConcept and
TaxonName classes for information about taxon concepts and taxon names,
respectively, as well as a TaxonConceptMapping class for taxon concept
alignments and a NomenclaturalType class for information on typification of
taxon names. TCS offers a semantic framework for, and facilitates more accurate
exchange of, taxonomic and nomenclatural data.

**Contributors**: Niels Klazenga, Greg Whitbread, Vijay Barve, Thierry Bourgoin,
Markus Döring, Anne Fuchs, Jeff Gerbracht, Johan Liljeblad, Carlos Martínez
Muñoz, Mieke Strong, William Ulate, Cam Webb 

**Creator**: TDWG Taxon Concept Schema (TCS) 2 Task Group

**Bibliographic citation**: Taxon Concept Standard Maintenance Group (2024).
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
this has been indicated in the notes.

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
possible. As because of this the examples take up a lot of space only one
example per term has been reproduced in this document. Links are provided for
other examples.

The examples in this document are in TurTLe. This format has been chosen because
it is very terse and still easy to read and, most importantly, allows comments.
The fact that the examples are in a serialization of RDF should not be taken to
mean that TCS data has to be RDF, just that it can be RDF. All examples are also
provided in JSON-LD.

The following namespace aliases are used in the examples:

| alias | namespace |
|-|-|
| tcs | http://rs.tdwg.org/tcs/terms/ |
| address | http://schemas.talis.com/2005/address/schema# |
| bibo | http://purl.org/ontology/bibo/ |
| dcterms | http://purl.org/dc/terms/ |
| dwc | http://rs.tdwg.org/dwc/terms/ |
| dwciri | http://rs.tdwg.org/dwc/iri/ |
| dsw | http://purl.org/dsw/ |
| foaf | http://xmlns.com/foaf/0.1/ |
| gbif | http://rs.gbif.org/terms/1.0/ |
| oa | http://www.w3.org/ns/oa# |
| rdf | http://www.w3.org/1999/02/22-rdf-syntax-ns# |
| rdfs | http://www.w3.org/2000/01/rdf-schema# |
| skosxl | http://www.w3.org/2008/05/skos-xl# |

## 2. Namespace

The namespace for TCS terms is `http://rs.tdwg.org/tcs/terms/`. The recommended
alias for this namespace is `tcs`.

## 3. Borrowed terms

As much as possible TCS uses already existing terms rather than define new
terms. Thus, many terms have been borrowed from Darwin Core and Dublin Core.

| standard | namespace | alias |
|-|-|-|
| Darwin Core | http://rs.tdwg.org/dwc/terms/ | dwc |
| Dublin Core | http://purl.org/dc/terms/ | dcterms |
## 4. Index of terms

**Taxon Concept**

[tcs:TaxonConcept](#tcstaxonconcept) | [tcs:accordingTo](#tcsaccordingto) | [tcs:taxonName](#tcstaxonname) | [tcs:synonym](#tcssynonym) | [tcs:vernacularName](#tcsvernacularname) | [tcs:taxonRank](#tcstaxonrank) | [tcs:parentTaxonConcept](#tcsparenttaxonconcept) | [tcs:childTaxonConcept](#tcschildtaxonconcept) | [tcs:isCongruentWith](#tcsiscongruentwith) | [tcs:includes](#tcsincludes) | [tcs:isIncludedIn](#tcsisincludedin) | [tcs:partiallyOverlaps](#tcspartiallyoverlaps) | [tcs:isDisjointFrom](#tcsisdisjointfrom) | [tcs:intersects](#tcsintersects) | [dwc:scientificName](#dwcscientificname) | [dwc:vernacularName](#dwcvernacularname) | [dwc:verbatimTaxonRank](#dwcverbatimtaxonrank) | [dcterms:title](#dctermstitle)

**Taxon Concept Mapping**

[tcs:TaxonConceptMapping](#tcstaxonconceptmapping) | [tcs:mappingAccordingTo](#tcsmappingaccordingto) | [tcs:mappingRelation](#tcsmappingrelation) | [tcs:subjectTaxonConcept](#tcssubjecttaxonconcept) | [tcs:objectTaxonConcept](#tcsobjecttaxonconcept)

**Taxon Name**

[tcs:TaxonName](#tcstaxonname) | [tcs:nameString](#tcsnamestring) | [tcs:namePublishedIn](#tcsnamepublishedin) | [tcs:microreference](#tcsmicroreference) | [tcs:nomenclaturalCode](#tcsnomenclaturalcode) | [tcs:nomenclaturalStatus](#tcsnomenclaturalstatus) | [tcs:typification](#tcstypification) | [tcs:typificationLiteral](#tcstypificationliteral) | [tcs:basionym](#tcsbasionym) | [tcs:replacedName](#tcsreplacedname) | [tcs:basedOn](#tcsbasedon) | [tcs:laterHomonymOf](#tcslaterhomonymof) | [tcs:conservedAgainst](#tcsconservedagainst) | [tcs:combinationAuthor](#tcscombinationauthor) | [tcs:combinationAuthorLiteral](#tcscombinationauthorliteral) | [tcs:basionymAuthor](#tcsbasionymauthor) | [tcs:basionymAuthorLiteral](#tcsbasionymauthorliteral) | [tcs:combinationAscribedAuthor](#tcscombinationascribedauthor) | [tcs:combinationAscribedAuthorLiteral](#tcscombinationascribedauthorliteral) | [tcs:basionymAscribedAuthor](#tcsbasionymascribedauthor) | [tcs:basionymAscribedAuthorLiteral](#tcsbasionymascribedauthorliteral) | [dwc:scientificNameAuthorship](#dwcscientificnameauthorship) | [dwc:namePublishedIn](#dwcnamepublishedin) | [dwc:namePublishedInYear](#dwcnamepublishedinyear) | [dwc:genericName](#dwcgenericname) | [dwc:infragenericEpithet](#dwcinfragenericepithet) | [dwc:specificEpithet](#dwcspecificepithet) | [dwc:infraspecificEpithet](#dwcinfraspecificepithet) | [dwc:cultivarEpithet](#dwccultivarepithet)

**Nomenclatural Type**

[tcs:NomenclaturalType](#tcsnomenclaturaltype) | [tcs:typifiedName](#tcstypifiedname) | [tcs:typeOfType](#tcstypeoftype) | [tcs:typeName](#tcstypename) | [tcs:typeSpecimen](#tcstypespecimen) | [tcs:typePublishedIn](#tcstypepublishedin)

## 5. Vocabulary

### Taxon Concept

#### tcs:TaxonConcept

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
			<td><p>An identifiable taxonomic position that can be aligned to other such  positions through TCS concept mapping relations.</p></td>
		</tr>
		<tr>
			<td>Usage</td>
			<td><p>A <code>TaxonConcept</code> MUST have <code>taxonName</code> and <code>accordingTo</code> properties. </p></td>
		</tr>
		<tr>
			<td>Comments</td>
			<td><p>A taxonomic position is an opinion about the definition of a taxonomic group. A Taxon Concept is identifiable, because it combines a label – <code>taxonName</code> in TCS – with a source – <code>accordingTo</code>. Both the <code>taxonName</code> and <code>accordingTo</code> properties are REQUIRED on a <code>tcs:TaxonConcept</code>. When mentioning a taxon concept, the label and the source are combined, separated by 'sec.' (from, 'secundus', meaning 'according to') or 'sensu' (meaning the same). The term <code>dcterms:title</code> has been borrowed from Dublin Core to provide this taxon concept label. Because of the context provided by the source, taxon concepts are in principle also alignable to other Taxon Concepts using TCS concept mapping statements. The concept mapping properties in TCS are <code>isCongruentWith</code>, <code>includes</code>, <code>isIncludedIn</code>, <code>partiallyOverlaps</code>, <code>isDisjointFrom</code> and <code>intersects</code>. These properties can be used directly on a <code>TaxonConcept</code> object or as the value of the <code>tcs:mappingRelation</code> property in a <code>tcs:TaxonConceptMapping</code> object.</p>
<p>The TCS Taxon Concept is applied more broadly than the term is used in science (e.g. Franz &amp; Peet 2009 <a href="../bibliography/#franz_perspectives_2009">[franz_perspectives_2009]</a>). On the one hand, things that are not generally considered to be biological taxa, e.g. hybrids and cultivars, can be casted as TCS Taxon Concepts. Also Operational Taxonomic Units (OTUs) <a href="../bibliography/#sokal_principles_1963">[sokal_principles_1963]</a> can be exchanged as Taxon Concepts, if there is a reason to do so, e.g. if one wants to align them with other Taxon Concepts later. On the other hand, entries from treatments that are considered to cite concepts from other treatments can be formulated as Taxon Concepts. Every taxon concept from a treatment that is likely to be referenced as the source of taxonomic context, for example a field guide for a determination of a specimen or a national census for an ecological study, can – and it would be very nice if they would – be stated as a Taxon Concept, so they can be aligned with other Taxon Concepts that may provide more or different taxonomic context.</p>
<p>By contrast, entries in the nomenclature section of treatments ('TaxonomicNameUsage's sensu Senderov et al. 2018 &#91;<a href="#senderov_openbiodiv-o_2018">senderov_openbiodiv-o_2018</a>&#93;) and in lists of nomenclatural types are not Taxon Concepts.</p></td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>

```turtle
[] a tcs:TaxonConcept ;
    dcterms:title "Dicranoloma blumei sec. Klazenga 1999" ;
    tcs:accordingTo <https://www.tropicos.org/reference/9020903> 
    tcs:taxonName <https://www.tropicos.org/name/35121475> .

<https://www.tropicos.org/name/35121475> a tcs:TaxonName ;
    tcs:nameString "Dicranoloma blumei" ;
    dwc:scientificNameAuthorship "(Nees) Renauld" .

<https://www.tropicos.org/reference/9020903> a bibo:AcademicArticle ;
    dcterms:bibliographicCitation """Klazenga, N. (1999). A revision of the 
            Malesian species of Dicranoloma (Dicranaceae, Musci). Journal of the 
            Hattori Botanical Laboratory 87: 1-130.""" .
```


[&lsqb;TaxonConcept-example-1.ttl&rsqb;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonConcept-example-1.ttl)&nbsp;[&lsqb;TaxonConcept-example-1.jsonld&rsqb;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonConcept-example-1.jsonld)


[&lsqb;TaxonConcept-example-2.ttl&rsqb;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonConcept-example-2.ttl)&nbsp;[&lsqb;TaxonConcept-example-2.jsonld&rsqb;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonConcept-example-2.jsonld)


[&lsqb;TaxonConcept-example-3.ttl&rsqb;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonConcept-example-3.ttl)&nbsp;[&lsqb;TaxonConcept-example-3.jsonld&rsqb;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonConcept-example-3.jsonld)


[&lsqb;TaxonConcept-example-4.ttl&rsqb;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonConcept-example-4.ttl)&nbsp;[&lsqb;TaxonConcept-example-4.jsonld&rsqb;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonConcept-example-4.jsonld)


[&lsqb;TaxonConcept-example-5.ttl&rsqb;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonConcept-example-5.ttl)&nbsp;[&lsqb;TaxonConcept-example-5.jsonld&rsqb;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonConcept-example-5.jsonld)


[&lsqb;TaxonConcept-example-6.ttl&rsqb;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonConcept-example-6.ttl)&nbsp;[&lsqb;TaxonConcept-example-6.jsonld&rsqb;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonConcept-example-6.jsonld)


[&lsqb;TaxonConcept-example-7.ttl&rsqb;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonConcept-example-7.ttl)&nbsp;[&lsqb;TaxonConcept-example-7.jsonld&rsqb;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonConcept-example-7.jsonld)

</td>
		</tr>
		<tr>
			<td>GitHub issue</td>
			<td>https://github.com/tdwg/tcs2/issues/213</td>
		</tr>
	</tbody>
</table>

#### tcs:accordingTo

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
			<td>Definition</td>
			<td><p>Reference to the treatment or other source in which a Taxon Concept is  established or used. </p></td>
		</tr>
		<tr>
			<td>Usage</td>
			<td><p><code>accordingTo</code> is an IRI term and is REQUIRED on a Taxon Concept. A  Taxon Concept can have only one <code>accordingTo</code>. </p></td>
		</tr>
		<tr>
			<td></td>
			<td><b>required:</b> Yes — <b>repeatable:</b> No</td>
		</tr>
		<tr>
			<td>Comments</td>
			<td><p>Every Taxon Concept is in some sort of treatment and this treatment  provides important context without which we do not know what a taxon name  really means and therefore the <code>accordingTo</code> property is REQUIRED for a TCS  Taxon Concept. In TCS 2, <code>accordingTo</code> has to be a reference to some sort  of resource rather than just a person's name. However, TCS is lenient about  the nature of this resource and, apart from references to bibliographic  resources, references to personal communications and determinations are  also acceptable, if there is value in supplying taxon concepts from such  communications as Taxon Concepts.</p>
<p>The value of <code>accordingTo</code> has to be an object or IRI. This object can  contain as little as a bibliographic reference but it is much more useful  to provide it in a format that can be understood by reference managers  such as Zotero or Mendeley.</p></td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>

```turtle
# Taxonomic article (object of property only)
<https://doi.org/10.1080/14772000.2013.806371> a bibo:AcademicArticle ;
    dcterms:creator <https://orcid.org/0000-0001-7089-7018>,
            <https://orcid.org/0000-0002-2469-8162> ;
    bibo:authorList ( <https://orcid.org/0000-0001-7089-7018> 
        	<https://orcid.org/0000-0002-2469-8162> ) ;
    dcterms:title """Description of two new species and phylogenetic reassessment of 
            Perelleschus O’Brien & Wibmer, 1986 (Coleoptera: Curculionidae), with 
            a complete taxonomic concept history of Perelleschus sec. Franz & 
            Cardona-Duque, 2013""" ;
    bibo:shortTitle """Description of two new species and phylogenetic reassessment 
            of Perelleschus O’Brien & Wibmer, 1986 (Coleoptera""" ;
    dcterms:isPartOf [ a bibo:Issue ;
        dcterms:date "June 1, 2013" ;
        dcterms:isPartOf [ a bibo:Journal ;
                dcterms:title "Systematics and Biodiversity" ;
                bibo:issn "1477-2000" ] ;
                dcterms:publisher [ a foaf:Organization ;
                    foaf:name "Taylor & Francis" ] ;
            bibo:volume "11" ;
            bibo:issue "2" ] ;
    bibo:pages "209-236" ;
    bibo:doi "10.1080/14772000.2013.806371" ;
    bibo:uri "https://doi.org/10.1080/14772000.2013.806371" .

<https://orcid.org/0000-0001-7089-7018> a foaf:Person ;
    foaf:givenName "Nico M." ;
    foaf:surname "Franz" .

<https://orcid.org/0000-0002-2469-8162> a foaf:Person ;
    foaf:givenName "Juliana" ;
    foaf:surname "Cardona-Duque*" .
```


[&lsqb;TaxonConcept-accordingTo-example-1.ttl&rsqb;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonConcept-accordingTo-example-1.ttl)&nbsp;[&lsqb;TaxonConcept-accordingTo-example-1.jsonld&rsqb;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonConcept-accordingTo-example-1.jsonld)


[&lsqb;TaxonConcept-accordingTo-example-2.ttl&rsqb;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonConcept-accordingTo-example-2.ttl)&nbsp;[&lsqb;TaxonConcept-accordingTo-example-2.jsonld&rsqb;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonConcept-accordingTo-example-2.jsonld)


[&lsqb;TaxonConcept-accordingTo-example-3.ttl&rsqb;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonConcept-accordingTo-example-3.ttl)&nbsp;[&lsqb;TaxonConcept-accordingTo-example-3.jsonld&rsqb;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonConcept-accordingTo-example-3.jsonld)

</td>
		</tr>
		<tr>
			<td>GitHub issue</td>
			<td>https://github.com/tdwg/tcs2/issues/4</td>
		</tr>
	</tbody>
</table>

#### tcs:taxonName

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
			<td>Taxon name</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td><p>The accepted name for the taxonomic group.</p></td>
		</tr>
		<tr>
			<td>Usage</td>
			<td><p><code>taxonName</code> is an IRI term and is REQUIRED on a TCS TaxonConcept. A TaxonConcept MUST NOT have more than one <code>taxonName</code>.</p></td>
		</tr>
		<tr>
			<td></td>
			<td><b>required:</b> Yes — <b>repeatable:</b> No</td>
		</tr>
		<tr>
			<td>Comments</td>
			<td><p>The <code>taxonName</code> can be anything from a well-formed scientific name to an  informal name, vernacular name, indigenous knowledge label, or even a label  containing numbers and/or special symbols, such as are often used for OTUs. </p>
<p>The object of <code>taxonName</code> is an object or IRI, so that it can be reused in  other Taxon Concepts. TCS has got the Taxon Name class, which can be used  for any type of name, but people are free to use alternatives, e.g.  <code>skosxl:Label</code>, if they want to restrict the use of the Taxon Name class to  scientific (or scientific-y) names only.</p></td>
		</tr>
		<tr>
			<td>GitHub issue</td>
			<td>https://github.com/tdwg/tcs2/issues/2</td>
		</tr>
	</tbody>
</table>

#### tcs:synonym

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
			<td>Definition</td>
			<td><p>Name considered to apply to the same taxon as the accepted name.</p></td>
		</tr>
		<tr>
			<td>Usage</td>
			<td><p><code>synonym</code> is a Taxon Name; a Taxon Concept can have multiple synonyms.</p></td>
		</tr>
		<tr>
			<td></td>
			<td><b>required:</b> No — <b>repeatable:</b> Yes</td>
		</tr>
		<tr>
			<td>Comments</td>
			<td><p>A synonym is an alternative label for a taxon, so <code>synonym</code>, like <code>taxonName</code>, is a relation between a <code>TaxonConcept</code> and a <code>TaxonName</code>, not a relationship between different taxonomic entities.</p>
<p>The terms 'heterotypic synonym' and 'homotypic synonym' from the nomenclatural codes ('subjective synonym' and 'objective synonym', respectively, in the Zoological Code) are, in the context of Taxon Concepts and Taxon Names, best understood as synonyms (relations between Taxon Concepts and Taxon Names) and combinations (relations between Taxon Names), respectively. In TCS, combinations are dealt with using properties of the <code>TaxonName</code> class, <em>e.g.</em> <code>basionym</code> and <code>replacedName</code> (note that 'combination' is used here in a broader sense that what the term actually means). This has the advantage that people do not need to separate heterotypic and homotypic synonyms, or generally deal with nomenclature, which adds a degree of complexity that not all systems need or want. Avoiding terms that are too strictly defined in the nomenclatural codes also has the advantage that the term can, in principle, be applied to things that cannot be heterotypic or homotypic synonyms, e.g., to names that are not validly published under the relevant code, and avoids inappropriate use of the terms defined in the nomenclatural codes.</p></td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>

```turtle
[]  a tcs:TaxonConcept ;
    dcterms:title "Dicranoloma blumei sec. Klazenga 1999" ;
    tcs:accordingTo <https://www.tropicos.org/reference/9020903> ;
    tcs:taxonName <https://www.tropicos.org/name/35121475> ;
    tcs:synonym <https://www.tropicos.org/name/35121973> , 
            <https://www.tropicos.org/name/35121477> ,
            <https://www.tropicos.org/name/35121484> ,
            <https://www.tropicos.org/name/35188177> .

<https://www.tropicos.org/name/35121475> a tcs:TaxonName ;
    tcs:nameString "Dicranoloma blumei" ;
    dwc:scientificNameAuthorship "(Nees) Renauld" ;
    dwc:namePublishedIn "Rev. Bryol. 28(4): 69 (1901)" ;
    tcs:basionym <https://www.tropicos.org/name/35121972> .

<https://www.tropicos.org/name/35121972> a tcs:TaxonName ;
    tcs:nameString "Dicranum blumei" ;
    dwc:scientificNameAuthorship "Nees" ; 
    dwc:namePublishedIn """Nova Acta Phys.-Med. Acad. Caes. Leop.-Carol. Nat. 
            Cur. 11(1): 131 (1823)""" .

<https://www.tropicos.org/name/35154856> a tcs:TaxonName ;
    tcs:nameString "Leucoloma blumei" ;
    dwc:scientificNameAuthorship "(Nees) Broth." ; 
    dwc:namePublishedIn "Nat. Pflanzenfam. I(3): 322 (1901)" ;
    tcs:basionym <https://www.tropicos.org/name/35121972> .

<https://www.tropicos.org/name/35121973> a tcs:TaxonName ;
    tcs:nameString "Dicranum blumei var. laxifolium" ;
    dwc:scientificNameAuthorship "Broth. & Geh." ;
    dwc:namePublishedIn "Biblioth. Bot. 44: 4 (1898)" .

<https://www.tropicos.org/name/35121477> a tcs:TaxonName ;
    tcs:nameString "Dicranoloma blumei var. papillisetum" ;
    dwc:scientificNameAuthorship "M. Fleisch." ;
    dwc:namePublishedIn "Nova Guinea 12(2): 112 (1914)" .

<https://www.tropicos.org/name/35188177> a tcs:TaxonName ;
    tcs:nameString "Dicranoloma blumei f. subintegrum" ;
    dwc:scientificNameAuthorship "Dixon" ;
    dwc:namePublishedIn "J. Bot. 80: 4 (1942)" .

<https://www.tropicos.org/name/35121484> a tcs:TaxonName ;
    tcs:nameString "Dicranoloma braunfelsioides" ;
    dwc:scientificNameAuthorship "Herzog" ;
    dwc:namePublishedIn "Hedwigia 61: 288 (1919)" . 

<https://www.tropicos.org/reference/9020903> a bibo:AcademicArticle ;
    dcterms:bibliographicCitation """Klazenga, N. (1999). A revision of the 
            Malesian species of Dicranoloma (Dicranaceae, Musci). Journal of the 
            Hattori Botanical Laboratory 87: 1-130.""" .

# Example shows both homotypic and heterotypic synonyms:
# 
# Dicranoloma blumei, Dicranum blumei and Leucoloma blumei are homotypic 
# synonyms and are linked through the basionym (Dicranum blumei is the basionym 
# of Dicranoloma blumei and Leucoloma blumei).
# 
# Dicranum blumei var. laxifolium, Dicranoloma blumei var. papillisetum, 
# Dicranoloma braunfelsioides and Dicranoloma blumei f. subintegrum are 
# heterotypic synonyms of Dicranoloma blumei (according to this publication) and 
# are provided using the `synonym` property.
```


[&lsqb;TaxonConcept-synonym-example-1.ttl&rsqb;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonConcept-synonym-example-1.ttl)&nbsp;[&lsqb;TaxonConcept-synonym-example-1.jsonld&rsqb;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonConcept-synonym-example-1.jsonld)


[&lsqb;TaxonConcept-synonym-example-2.ttl&rsqb;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonConcept-synonym-example-2.ttl)&nbsp;[&lsqb;TaxonConcept-synonym-example-2.jsonld&rsqb;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonConcept-synonym-example-2.jsonld)


[&lsqb;TaxonConcept-synonym-example-3.ttl&rsqb;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonConcept-synonym-example-3.ttl)&nbsp;[&lsqb;TaxonConcept-synonym-example-3.jsonld&rsqb;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonConcept-synonym-example-3.jsonld)

</td>
		</tr>
		<tr>
			<td>GitHub issue</td>
			<td>https://github.com/tdwg/tcs2/issues/65</td>
		</tr>
	</tbody>
</table>

#### tcs:vernacularName

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
			<td>Definition</td>
			<td><p>Name for a taxon in a language used for general purposes.</p></td>
		</tr>
		<tr>
			<td>Usage</td>
			<td><p><code>vernacularName</code> is an IRI term; a Taxon Concept can have more than one  <code>vernacularName</code>.</p></td>
		</tr>
		<tr>
			<td></td>
			<td><b>required:</b> No — <b>repeatable:</b> Yes</td>
		</tr>
		<tr>
			<td>Comments</td>
			<td><p>The <code>vernacularName</code> property can be used when a vernacular name is used alongside a scientific name, which is the <code>taxonName</code>. If a vernacular name is the only name, the <code>taxonName</code> property SHOULD be used. The object of the <code>vernacularName</code> property can be a Taxon Name, but another label object, such as the GBIF <a href="https://rs.gbif.org/extension/gbif/1.0/vernacularname.xml">Vernacular Name</a>, might be preferrable, especially if there can be multiple vernacular names for a concept.</p></td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>

```turtle
[] a tcs:TaxonConcept ;
    dcterms:title "Graphium macleayanum sec. Orr & Kitching 2010" ;
    tcs:accordingTo <urn:isbn:978-1-74175-108-6> ;
    tcs:taxonName [ a tcs:TaxonName ;
            tcs:nameString "Graphium macleayanum" ] ;
    tcs:vernacularName [ a gbif:VernacularName ;
            dwc:vernacularName "Macleay's Swallowtail" ;
            dcterms:language: "en" ] .

<urn:isbn:978-1-74175-108-6> a bibo:Book ; 
    dcterms:bibliographicCitation """Orr, A. & Kitching, R. (2010). The 
            butterflies of Australia. Jacana Books, Crows Nest, Australia.""" .
```


[&lsqb;TaxonConcept-vernacularName-example-1.ttl&rsqb;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonConcept-vernacularName-example-1.ttl)&nbsp;[&lsqb;TaxonConcept-vernacularName-example-1.jsonld&rsqb;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonConcept-vernacularName-example-1.jsonld)


[&lsqb;TaxonConcept-vernacularName-example-2.ttl&rsqb;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonConcept-vernacularName-example-2.ttl)&nbsp;[&lsqb;TaxonConcept-vernacularName-example-2.jsonld&rsqb;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonConcept-vernacularName-example-2.jsonld)


[&lsqb;TaxonConcept-vernacularName-example-3.ttl&rsqb;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonConcept-vernacularName-example-3.ttl)&nbsp;[&lsqb;TaxonConcept-vernacularName-example-3.jsonld&rsqb;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonConcept-vernacularName-example-3.jsonld)

</td>
		</tr>
		<tr>
			<td>GitHub issue</td>
			<td>https://github.com/tdwg/tcs2/issues/10</td>
		</tr>
	</tbody>
</table>

#### tcs:taxonRank

<table style="width:100%;">
	<tbody>
		<tr>
			<td>Identifier</td>
			<td>http://rs.tdwg.org/tcs/terms/taxonRank</td>
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
			<td>Definition</td>
			<td><p>The rank at which a taxon is classified.</p></td>
		</tr>
		<tr>
			<td>Usage</td>
			<td><p><code>taxonRank</code> is an IRI property; a TaxonConcept or TaxonName MUST NOT have more than one <code>taxonRank</code>.</p></td>
		</tr>
		<tr>
			<td></td>
			<td><b>required:</b> No — <b>repeatable:</b> No</td>
		</tr>
		<tr>
			<td>Comments</td>
			<td><p>This property takes an object or IRI and it is RECOMMENDED to use a value from an existing controlled vocabulary. While there is no TDWG vocabulary yet, the GBIF Taxonomic Rank Vocabulary (https://rs.gbif.org/vocabulary/gbif/rank_2015-04-24.xml) is RECOMMENDED.</p>
<p>A taxon name takes its rank from the taxon it is applied to, so this property can also be used on a (stand-alone) <code>TaxonName</code> object.</p></td>
		</tr>
		<tr>
			<td>GitHub issue</td>
			<td>https://github.com/tdwg/tcs2/issues/32</td>
		</tr>
	</tbody>
</table>

#### tcs:parentTaxonConcept

<table style="width:100%;">
	<tbody>
		<tr>
			<td>Identifier</td>
			<td>http://rs.tdwg.org/tcs/terms/parentTaxonConcept</td>
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
			<td>Definition</td>
			<td><p>The immediately next higher taxon in a hierarchical classification.</p></td>
		</tr>
		<tr>
			<td>Usage</td>
			<td><p><code>parentTaxonConcept</code> is another TaxonConcept; a TaxonConcept can have only one <code>parentTaxonConcept</code>.</p></td>
		</tr>
		<tr>
			<td></td>
			<td><b>required:</b> No — <b>repeatable:</b> No</td>
		</tr>
		<tr>
			<td>Comments</td>
			<td><p>This is the parent as indicated in  the <code>accordingTo</code> reference, rather than a third-party classification. The  <code>accordingTo</code> of the parent will generally, but not necessarily, be the  same as that of the child. </p></td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>

```turtle
<https://www.catalogueoflife.org/data/taxon/6DBT> a tcs:TaxonConcept ;
    dcterms:title "Panthera sec. Catalogue of Life 2024-01-24" ;
    tcs:accordingTo <https://doi.org/10.48580/dfrdl> ;
    tcs:taxonName: [ a tcs:TaxonName ;
            tcs:nameString: "Panthera" ;
            dwc:scientificNameAuthorship: "Oken, 1816" ] .

<https://www.catalogueoflife.org/data/taxon/4CGXP> a tcs:TaxonConcept ;
    dcterms:title "Panthera leo sec. Catalogue of Life 2024-01-24" ;
    tcs:accordingTo <https://doi.org/10.48580/dfrdl> ;
    tcs:taxonName: [ a tcs:TaxonName ;
            tcs:nameString: "Panthera leo" ;
            dwc:scientificNameAuthorship: "(Linnaeus, 1758)" ] ;
    tcs:parentTaxonConcept <https://www.catalogueoflife.org/data/taxon/6DBT> .

<https://www.catalogueoflife.org/data/taxon/4CGXQ> a tcs:TaxonConcept ;
    dcterms:title "Panthera onca sec. Catalogue of Life 2024-01-24" ;
    tcs:accordingTo <https://doi.org/10.48580/dfrdl> ;
    tcs:taxonName: [ a tcs:TaxonName ;
            tcs:nameString: "Panthera onca" ;
            dwc:scientificNameAuthorship: "(Linnaeus, 1758)" ] ;
    tcs:parentTaxonConcept <https://www.catalogueoflife.org/data/taxon/6DBT> .

<https://www.catalogueoflife.org/data/taxon/4CGXR> a tcs:TaxonConcept ;
    dcterms:title "Panthera pardus sec. Catalogue of Life 2024-01-24" ;
    tcs:accordingTo <https://doi.org/10.48580/dfrdl> ;
    tcs:taxonName: [ a tcs:TaxonName ;
            tcs:nameString: "Panthera pardus" ;
            dwc:scientificNameAuthorship: "(Linnaeus, 1758)" ] ;
    tcs:parentTaxonConcept <https://www.catalogueoflife.org/data/taxon/6DBT> .

<https://www.catalogueoflife.org/data/taxon/4CGXS> a tcs:TaxonConcept ;
    dcterms:title "Panthera tigris sec. Catalogue of Life 2024-01-24" ;
    tcs:accordingTo <https://doi.org/10.48580/dfrdl> ;
    tcs:taxonName: [ a tcs:TaxonName ;
            tcs:nameString: "Panthera tigris" ;
            dwc:scientificNameAuthorship: "(Linnaeus, 1758)" ] ;
    tcs:parentTaxonConcept <https://www.catalogueoflife.org/data/taxon/6DBT> .
```


[&lsqb;TaxonConcept-parent-example-1.ttl&rsqb;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonConcept-parent-example-1.ttl)&nbsp;[&lsqb;TaxonConcept-parent-example-1.jsonld&rsqb;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonConcept-parent-example-1.jsonld)

</td>
		</tr>
		<tr>
			<td>GitHub issue</td>
			<td>https://github.com/tdwg/tcs2/issues/9</td>
		</tr>
	</tbody>
</table>

#### tcs:childTaxonConcept

<table style="width:100%;">
	<tbody>
		<tr>
			<td>Identifier</td>
			<td>http://rs.tdwg.org/tcs/terms/childTaxonConcept</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>http://www.w3.org/1999/02/22-rdf-syntax-ns#Property</td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Child</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td><p>A direct subordinate in a hierarchical classification.</p></td>
		</tr>
		<tr>
			<td>Usage</td>
			<td><p><code>childTaxonConcept</code> is another TaxonConcept; a TaxonConcept can have more than one <code>childTaxonConcept</code>.</p></td>
		</tr>
		<tr>
			<td></td>
			<td><b>required:</b> No — <b>repeatable:</b> Yes</td>
		</tr>
		<tr>
			<td>Comments</td>
			<td><p>This is a child as indicated in the <code>accordingTo</code> reference, rather than a third-party classification. The <code>accordingTo</code> of the child will generally, but not necessarily, be the same as that of the parent.</p></td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>

```turtle
<https://www.catalogueoflife.org/data/taxon/6DBT> a tcs:TaxonConcept ;
    dcterms:title "Panthera sec. Catalogue of Life 2024-01-24" ;
    tcs:accordingTo <https://doi.org/10.48580/dfrdl> ;
    tcs:taxonName: [ a tcs:TaxonName ;
            tcs:nameString: "Panthera" ;
            dwc:scientificNameAuthorship: "Oken, 1816" ]  ;
    tcs:childTaxonConcept <https://www.catalogueoflife.org/data/taxon/4CGXP> ,
            <https://www.catalogueoflife.org/data/taxon/4CGXQ> ,
            <https://www.catalogueoflife.org/data/taxon/4CGXR> ,
            <https://www.catalogueoflife.org/data/taxon/4CGXS> .

<https://www.catalogueoflife.org/data/taxon/4CGXP> a tcs:TaxonConcept ;
    dcterms:title "Panthera leo sec. Catalogue of Life 2024-01-24" ;
    tcs:accordingTo <https://doi.org/10.48580/dfrdl> ;
    tcs:taxonName: [ a tcs:TaxonName ;
            tcs:nameString: "Panthera leo" ;
            dwc:scientificNameAuthorship: "(Linnaeus, 1758)" ] .

<https://www.catalogueoflife.org/data/taxon/4CGXQ> a tcs:TaxonConcept ;
    dcterms:title "Panthera onca sec. Catalogue of Life 2024-01-24" ;
    tcs:accordingTo <https://doi.org/10.48580/dfrdl> ;
    tcs:taxonName: [ a tcs:TaxonName ;
            tcs:nameString: "Panthera onca" ;
            dwc:scientificNameAuthorship: "(Linnaeus, 1758)" ] .

<https://www.catalogueoflife.org/data/taxon/4CGXR> a tcs:TaxonConcept ;
    dcterms:title "Panthera pardus sec. Catalogue of Life 2024-01-24" ;
    tcs:accordingTo <https://doi.org/10.48580/dfrdl> ;
    tcs:taxonName: [ a tcs:TaxonName ;
            tcs:nameString: "Panthera pardus" ;
            dwc:scientificNameAuthorship: "(Linnaeus, 1758)" ] .

<https://www.catalogueoflife.org/data/taxon/4CGXS> a tcs:TaxonConcept ;
    dcterms:title "Panthera tigris sec. Catalogue of Life 2024-01-24" ;
    tcs:accordingTo <https://doi.org/10.48580/dfrdl> ;
    tcs:taxonName: [ a tcs:TaxonName ;
            tcs:nameString: "Panthera tigris" ;
            dwc:scientificNameAuthorship: "(Linnaeus, 1758)" ] .
```


[&lsqb;TaxonConcept-child-example-1.ttl&rsqb;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonConcept-child-example-1.ttl)&nbsp;[&lsqb;TaxonConcept-child-example-1.jsonld&rsqb;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonConcept-child-example-1.jsonld)

</td>
		</tr>
		<tr>
			<td>GitHub issue</td>
			<td>https://github.com/tdwg/tcs2/issues/232</td>
		</tr>
	</tbody>
</table>

#### tcs:isCongruentWith

<table style="width:100%;">
	<tbody>
		<tr>
			<td>Identifier</td>
			<td>http://rs.tdwg.org/tcs/terms/isCongruentWith</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>http://www.w3.org/1999/02/22-rdf-syntax-ns#Property</td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Is Congruent With</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td><p>The subject and object taxon concepts have a congruent taxonomic meaning,  i.e. there is no conflict between the concepts</p></td>
		</tr>
		<tr>
			<td>Usage</td>
			<td><p><code>isCongruentWith</code> can be used as a property on a Taxon Concept object, or as the value of the <code>mappingRelation</code> property on a Taxon Concept Mapping object. In both cases both the subject and object are Taxon Concepts.</p></td>
		</tr>
		<tr>
			<td></td>
			<td><b>required:</b> No — <b>repeatable:</b> Yes</td>
		</tr>
		<tr>
			<td>Comments</td>
			<td><p>The <code>isCongruentWith</code> relation is symmetrical, so if A <code>isCongruentWith</code> B then B <code>isCongruentWith</code> A, as well as transitive, so if A <code>isCongruentWith</code> B and B <code>isCongruentWith</code> C it follows that A <code>isCongruentWith</code> C.</p>
<p><img alt="" src="../media/mapping-relation-is-congruent-with.drawio.svg" /></p>
<p>This relation can also be written as the formula <strong>A &cong; B</strong> or <strong>A == B</strong>.</p></td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>

```turtle
[] a tcs:TaxonConcept ;
    dcterms:title "Aspleniaceae sec. Rothfels & al. 2012" ;
    tcs:accordingTo <https://doi.org/10.1002/tax.613003> ;
    tcs:taxonName <https://ipni.org/n/30001382-2> ;
    tcs:isCongruentWith [ a tcs:TaxonConcept ;
            dcterms:title "Aspleniaceae sec. Christenhusz & al. 2011" ;
            tcs:accordingTo <https://doi.org/10.11646/phytotaxa.19.1.2> ;
            tcs:taxonName <https://ipni.org/n/30001382-2> ] ,
        [ a tcs:TaxonConcept ;
            dcterms:title "Aspleniaceae sec. Smith & al. 2006" ;
            tcs:accordingTo <https://doi.org/10.2307/25065646> ;
            tcs:acceptedName <https://ipni.org/n/30001382-2> ] ,
        [ a tcs:TaxonConcept ;
            dcterms:title "Aspleniaceae sec. Pichi Sermolli 1977" ;
            tcs:accordingTo <https://doi.org/10.1080/00837792.1977.10670077> ;
            tcs:taxonName <https://ipni.org/n/30001382-2> ] ,
        [ a tcs:TaxonConcept ;
            dcterms:title "Aspleniaceae sec. Nayar 1970" ;
            tcs:accordingTo <https://doi.org/10.2307/1217958> ;
            tcs:taxonName <https://ipni.org/n/30001382-2> ] .
```


[&lsqb;TaxonConcept-isCongruentWith-example-1.ttl&rsqb;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonConcept-isCongruentWith-example-1.ttl)&nbsp;[&lsqb;TaxonConcept-isCongruentWith-example-1.jsonld&rsqb;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonConcept-isCongruentWith-example-1.jsonld)


[&lsqb;TaxonConceptMapping-isCongruentWith-example-2.ttl&rsqb;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonConceptMapping-isCongruentWith-example-2.ttl)&nbsp;[&lsqb;TaxonConceptMapping-isCongruentWith-example-2.jsonld&rsqb;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonConceptMapping-isCongruentWith-example-2.jsonld)


[&lsqb;TaxonConcept-isCongruentWith-example-3.ttl&rsqb;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonConcept-isCongruentWith-example-3.ttl)&nbsp;[&lsqb;TaxonConcept-isCongruentWith-example-3.jsonld&rsqb;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonConcept-isCongruentWith-example-3.jsonld)


[&lsqb;TaxonConceptMapping-isCongruentWith-example-1.ttl&rsqb;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonConceptMapping-isCongruentWith-example-1.ttl)&nbsp;[&lsqb;TaxonConceptMapping-isCongruentWith-example-1.jsonld&rsqb;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonConceptMapping-isCongruentWith-example-1.jsonld)

</td>
		</tr>
		<tr>
			<td>GitHub issue</td>
			<td>https://github.com/tdwg/tcs2/issues/52</td>
		</tr>
	</tbody>
</table>

#### tcs:includes

<table style="width:100%;">
	<tbody>
		<tr>
			<td>Identifier</td>
			<td>http://rs.tdwg.org/tcs/terms/includes</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>http://www.w3.org/1999/02/22-rdf-syntax-ns#Property</td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Includes</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td><p>The subject taxon concept has a more inclusive taxonomic meaning than the object taxon concept</p></td>
		</tr>
		<tr>
			<td>Usage</td>
			<td><p><code>includes</code> can be used as a property on a Taxon Concept object, or as the value of the <code>mappingRelation</code> property on a Taxon Concept Mapping object. In both cases both the subject and object are Taxon Concepts.</p></td>
		</tr>
		<tr>
			<td></td>
			<td><b>required:</b> No — <b>repeatable:</b> Yes</td>
		</tr>
		<tr>
			<td>Comments</td>
			<td><p>The <code>includes</code> relation is not symmetric, its inverse relation being <code>isIncludedIn</code>, so if A <code>includes</code> B then B <code>isIncludedIn</code> A. The <code>includes</code> relation  is transitive, so if A <code>includes</code> B and B <code>includes</code> C it follows that A <code>includes</code> C.</p>
<p><img alt="" src="../media/mapping-relation-includes.drawio.svg" /></p>
<p>This relation can also be written as the formula <strong>A &gt; B</strong>.</p></td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>

```turtle
[] a tcs:TaxonConcept ;
    dcterms:title "Diplaziopsidaceae sec. Rothfels & al. 2012" ;
    tcs:accordingTo <https://doi.org/10.1002/tax.613003> ;
    tcs:taxonName <https://ipni.org/n/77110538-1> ;
    tcs:includes [ a tcs:TaxonConcept ;
            dcterms:title "Diplaziopsidaceae sec. Christenhusz & al. 2011" ;
            tcs:accordingTo <https://doi.org/10.11646/phytotaxa.19.1.2> ;
            tcs:taxonName <https://ipni.org/n/77110538-1> ] .
```


[&lsqb;TaxonConcept-includes-example-1.ttl&rsqb;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonConcept-includes-example-1.ttl)&nbsp;[&lsqb;TaxonConcept-includes-example-1.jsonld&rsqb;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonConcept-includes-example-1.jsonld)


[&lsqb;TaxonConceptMapping-includes-example-2.ttl&rsqb;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonConceptMapping-includes-example-2.ttl)&nbsp;[&lsqb;TaxonConceptMapping-includes-example-2.jsonld&rsqb;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonConceptMapping-includes-example-2.jsonld)


[&lsqb;TaxonConceptMapping-includes-example-1.ttl&rsqb;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonConceptMapping-includes-example-1.ttl)&nbsp;[&lsqb;TaxonConceptMapping-includes-example-1.jsonld&rsqb;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonConceptMapping-includes-example-1.jsonld)

</td>
		</tr>
		<tr>
			<td>GitHub issue</td>
			<td>https://github.com/tdwg/tcs2/issues/53</td>
		</tr>
	</tbody>
</table>

#### tcs:isIncludedIn

<table style="width:100%;">
	<tbody>
		<tr>
			<td>Identifier</td>
			<td>http://rs.tdwg.org/tcs/terms/isIncludedIn</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>http://www.w3.org/1999/02/22-rdf-syntax-ns#Property</td>
		</tr>
		<tr>
			<td>Label</td>
			<td>is included in</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td><p>The subject taxon concept has a less inclusive taxonomic meaning than the  object taxon concept</p></td>
		</tr>
		<tr>
			<td>Usage</td>
			<td><p><code>isIncludedIn</code> can be used as a property on a Taxon Concept object, or as the value of the <code>mappingRelation</code> property on a Taxon Concept Mapping object. In both cases both the subject and object are Taxon Concepts.</p></td>
		</tr>
		<tr>
			<td></td>
			<td><b>required:</b> No — <b>repeatable:</b> Yes</td>
		</tr>
		<tr>
			<td>Comments</td>
			<td><p>The <code>isIncludedIn</code> relation is not symmetric, its inverse relation being <code>includes</code>, so if A <code>isIncludedIn</code> B then B <code>includes</code> A. The <code>isIncludedIn</code> relation  is transitive, so if A <code>isIncludedIn</code> B and B <code>isIncludedIn</code> C it follows that A <code>isIncludedIn</code> C.</p>
<p><img alt="" src="../media/mapping-relation-is-included-in.drawio.svg" /></p>
<p>This relation can also be written as the formula <strong>A &lt; B</strong>.</p></td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>

```turtle
[] a tcs:TaxonConcept ;
    dcterms:title "Athyriaceae sec. Rothfels & al. 2012" ;
    tcs:accordingTo <https://doi.org/10.1002/tax.613003> ;
    tcs:taxonName <https://ipni.org/n/30000361-2> ;
    tcs:isIncludedIn [ a tcs:TaxonConcept ;
            dcterms:title "Athyriaceae sec. Christenhusz & al. 2011" ;
            tcs:accordingTo <https://doi.org/10.11646/phytotaxa.19.1.2> ;
            tcs:taxonName <https://ipni.org/n/30000361-2> ] ,
        [ a tcs:TaxonConcept ;
            dcterms:title "Woodsiaceae sec. Smith & al. 2006" ;
            tcs:accordingTo <https://doi.org/10.2307/25065646> ;
            tcs:taxonName <https://ipni.org/n/30000455-2> ] ,
        [ a tcs:TaxonConcept ;
            dcterms:title "Dryopteridaceae sec. Nayar 1970" ;
            tcs:accordingTo <https://doi.org/10.2307/1217958> ;
            tcs:taxonName <https://ipni.org/n/30014148-2> ] ,
        [ a tcs:TaxonConcept ;
            dcterms:title "Dennstaedtiaceae sec. Holttum 1947" ;
            tcs:accordingTo [ a dcterms:BibliographicResource ;
                    dcterms:bibliographicCitation """Holttum, R.E. (1947). A 
                            revised classification of leptosporangiate ferns. 
                            Journal of the Linnean Society. Botany 53: 123–155.""" ] ;
            tcs:taxonName <https://ipni.org/n/17434830-1> ] .
```


[&lsqb;TaxonConcept-isIncludedIn-example-1.ttl&rsqb;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonConcept-isIncludedIn-example-1.ttl)&nbsp;[&lsqb;TaxonConcept-isIncludedIn-example-1.jsonld&rsqb;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonConcept-isIncludedIn-example-1.jsonld)


[&lsqb;TaxonConceptMapping-isIncludedIn-example-2.ttl&rsqb;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonConceptMapping-isIncludedIn-example-2.ttl)&nbsp;[&lsqb;TaxonConceptMapping-isIncludedIn-example-2.jsonld&rsqb;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonConceptMapping-isIncludedIn-example-2.jsonld)


[&lsqb;TaxonConceptMapping-isIncludedIn-example-1.ttl&rsqb;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonConceptMapping-isIncludedIn-example-1.ttl)&nbsp;[&lsqb;TaxonConceptMapping-isIncludedIn-example-1.jsonld&rsqb;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonConceptMapping-isIncludedIn-example-1.jsonld)

</td>
		</tr>
		<tr>
			<td>GitHub issue</td>
			<td>https://github.com/tdwg/tcs2/issues/54</td>
		</tr>
	</tbody>
</table>

#### tcs:partiallyOverlaps

<table style="width:100%;">
	<tbody>
		<tr>
			<td>Identifier</td>
			<td>http://rs.tdwg.org/tcs/terms/partiallyOverlaps</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>http://www.w3.org/1999/02/22-rdf-syntax-ns#Property</td>
		</tr>
		<tr>
			<td>Label</td>
			<td>partially overlaps</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td><p>The subject and object taxon concepts have partially overlapping taxonomic  meanings, <em>i.e.</em> they have some members in common, but each concept in  addition has members that are not included in the other concept</p></td>
		</tr>
		<tr>
			<td>Usage</td>
			<td><p><code>partiallyOverlaps</code> can be used as a property on a Taxon Concept object, or as the value of the <code>mappingRelation</code> property on a Taxon Concept Mapping object. In both cases both the subject and object are Taxon Concepts.</p></td>
		</tr>
		<tr>
			<td></td>
			<td><b>required:</b> No — <b>repeatable:</b> Yes</td>
		</tr>
		<tr>
			<td>Comments</td>
			<td><p>The <code>partiallyOverlaps</code> relation is symmetrical, so if A <code>partiallyOverlaps</code> B then B <code>partiallyOverlaps</code> A, but not transitive, so, if A <code>partiallyOverlaps</code> B and B <code>partiallyOverlaps</code> C, it does not follow that A <code>partiallyOverlaps</code> C.</p>
<p><img alt="" src="../media/mapping-relation-partially-overlaps.drawio.svg" /></p>
<p>This relation can also be written as the formula <strong>A &gt;&lt; B</strong>.</p></td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>

```turtle
[] a tcs:TaxonConcept ;
    dcterms:title "Diplaziopsidaceae sec. Rothfels & al. 2012" ;
    tcs:accordingTo <https://doi.org/10.1002/tax.613003> ;
    tcs:taxonName <https://ipni.org/n/77110538-1> ;
    tcs:partiallyOverlaps [ a tcs:TaxonConcept ;
            dcterms:title "Athyriaceae sec. Christenhusz & al. 2011" ;
            tcs:accordingTo <https://doi.org/10.11646/phytotaxa.19.1.2> ;
            tcs:taxonName <https://ipni.org/n/30000361-2> ] .
```


[&lsqb;TaxonConcept-partiallyOverlaps-example-1.ttl&rsqb;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonConcept-partiallyOverlaps-example-1.ttl)&nbsp;[&lsqb;TaxonConcept-partiallyOverlaps-example-1.jsonld&rsqb;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonConcept-partiallyOverlaps-example-1.jsonld)


[&lsqb;TaxonConceptMapping-partiallyOverlaps-example-2.ttl&rsqb;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonConceptMapping-partiallyOverlaps-example-2.ttl)&nbsp;[&lsqb;TaxonConceptMapping-partiallyOverlaps-example-2.jsonld&rsqb;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonConceptMapping-partiallyOverlaps-example-2.jsonld)


[&lsqb;TaxonConceptMapping-partiallyOverlaps-example-1.ttl&rsqb;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonConceptMapping-partiallyOverlaps-example-1.ttl)&nbsp;[&lsqb;TaxonConceptMapping-partiallyOverlaps-example-1.jsonld&rsqb;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonConceptMapping-partiallyOverlaps-example-1.jsonld)

</td>
		</tr>
		<tr>
			<td>GitHub issue</td>
			<td>https://github.com/tdwg/tcs2/issues/55</td>
		</tr>
	</tbody>
</table>

#### tcs:isDisjointFrom

<table style="width:100%;">
	<tbody>
		<tr>
			<td>Identifier</td>
			<td>http://rs.tdwg.org/tcs/terms/isDisjointFrom</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>http://www.w3.org/1999/02/22-rdf-syntax-ns#Property</td>
		</tr>
		<tr>
			<td>Label</td>
			<td>is disjoint from</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td><p>The subject and object taxon concepts have non-overlapping taxonomic  meanings, <em>i.e.</em> they do not have any members in common</p></td>
		</tr>
		<tr>
			<td>Usage</td>
			<td><p><code>isDisjointFrom</code> can be used as a property on a Taxon Concept object, or as the value of the <code>mappingRelation</code> property on a Taxon Concept Mapping object. In both cases both the subject and object are Taxon Concepts.</p></td>
		</tr>
		<tr>
			<td></td>
			<td><b>required:</b> No — <b>repeatable:</b> Yes</td>
		</tr>
		<tr>
			<td>Comments</td>
			<td><p>The <code>isDisjointFrom</code>  relation is symmetrical, so if A <code>isDisjointFrom</code>  B then B <code>isDisjointFrom</code> A, but not transitive, so, if A <code>isDisjointFrom</code>  B and B <code>isDisjointFrom</code> C, it does not follow that A <code>isDisjointFrom</code> C.</p>
<p><img alt="" src="../media/mapping-relations-is-disjoint-from.drawio.svg" /></p>
<p>This relation can also be written as the formula <strong>A | B</strong>.</p></td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>

```turtle
[] a tcs:TaxonConcept 
    dcterms:title "Campylopus introflexus sec. Koperski & al. 2000" ; 
    tcs:accordingTo <https://www.tropicos.org/reference/9022656> ;
    tcs:taxonName <https://www.tropicos.org/name/35156181> ;
    tcs:isDisjointFrom [ rdf:value [ a tcs:TaxonConcept ;
                    dcterms:title "Campylopus introflexus sec. Mönkemeyer 1927" ;
                    tcs:accordingTo <https://www.tropicos.org/publication/700> ;
                    tcs:taxonName <https://www.tropicos.org/name/35156181> ] ;
            rdfs:comment """Mit dem Taxon in Mönkemeyer ist der Beschreibung 
                    nach eindeutig *C. pilifer Brid. (C. polytrichoides De 
                    Not.), eine ozeanisch-submediterrane Art, gemeint. In 
                    älteren Floren wird C. introflexus, bevor diese Art von 
                    Störmer (1958) für Europa nachgewiesen wurde, regelmäßig als 
                    Synonym von C. polytrichoides aufgeführt oder in diesem 
                    Sinne verwendet (vgl. u. a. Demaret & Castagne 1961: 
                    203)""" ] .

# Because of the comment it is better to use a Taxon Concept Mapping object
# here.
```


[&lsqb;TaxonConcept-isDisjointFrom-example-1.ttl&rsqb;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonConcept-isDisjointFrom-example-1.ttl)&nbsp;[&lsqb;TaxonConcept-isDisjointFrom-example-1.jsonld&rsqb;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonConcept-isDisjointFrom-example-1.jsonld)


[&lsqb;TaxonConceptMapping-isDisjointFrom-example-2.ttl&rsqb;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonConceptMapping-isDisjointFrom-example-2.ttl)&nbsp;[&lsqb;TaxonConceptMapping-isDisjointFrom-example-2.jsonld&rsqb;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonConceptMapping-isDisjointFrom-example-2.jsonld)


[&lsqb;TaxonConceptMapping-isDisjointFrom-example-1.ttl&rsqb;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonConceptMapping-isDisjointFrom-example-1.ttl)&nbsp;[&lsqb;TaxonConceptMapping-isDisjointFrom-example-1.jsonld&rsqb;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonConceptMapping-isDisjointFrom-example-1.jsonld)

</td>
		</tr>
		<tr>
			<td>GitHub issue</td>
			<td>https://github.com/tdwg/tcs2/issues/56</td>
		</tr>
	</tbody>
</table>

#### tcs:intersects

<table style="width:100%;">
	<tbody>
		<tr>
			<td>Identifier</td>
			<td>http://rs.tdwg.org/tcs/terms/intersects</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>http://www.w3.org/1999/02/22-rdf-syntax-ns#Property</td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Intersects</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td><p>The taxonomic meanings of the subject and object taxon concepts intersect,  <em>i.e.</em> they have at least one member in common.</p></td>
		</tr>
		<tr>
			<td>Usage</td>
			<td><p><code>intersects</code> can be used as a property on a Taxon Concept object, or as the value of the <code>mappingRelation</code> property on a Taxon Concept Mapping object. In both cases both the subject and object are Taxon Concepts.</p></td>
		</tr>
		<tr>
			<td></td>
			<td><b>required:</b> No — <b>repeatable:</b> Yes</td>
		</tr>
		<tr>
			<td>Comments</td>
			<td><p><code>intersects</code> is the opposite of <code>isDisjointFrom</code> and the union of <code>isCongruentWith</code>, <code>includes</code>, <code>isIncludedIn</code> and <code>partiallyOverlaps</code>, meaning it can be any of these relations. This relation can be used when the more precise nature of the relationship is not known.</p>
<p>Quasi-nomenclatural statements like 'pro parte synonym', 'partial synonym' and 'misapplication', are Taxon Concept Mappings, no matter how imperfect, and, in TCS, are best dealt with using the <code>intersects</code> relation. In fact, all 'traditional synonymy' relationships, cf. Berendsohn &amp; al. (2000 <a href="../bibliography/#berendsohn_berlin_2003">[berendsohn_berlin_2003]</a>), can be accommodated using <code>intersects</code>. Also, citations of references in treatments are, in the context of TCS, best accommodated using the <code>intersects</code> relation.</p></td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>

```turtle
[] a tcs:TaxonConcept ;
    dcterms:title "Begonia salaziensis sec. Klazenga & al. 1994" ;
    tcs:accordingTo <https://doi/org/10.2307/3668252> ;
    tcs:taxonName <https://ipni.org/n/105644-1> ;
    tcs:intersects [ a tcs:TaxonConcept ;
            dcterms:title "Begonia salaziensis sec. Warburg 1894" ;
            tcs:accordingTo [ a bibo:Chapter ;
                    dcterms:bibliographicCitation """Warburg, O. (1894). Begoniaceae, 
                            in Engler, A. & K. Prantl, Nat. Pflanzenfam. 3(6a): 
                            121-150.""" ] ;
            tcs:taxonName <https://ipni.org/n/105644-1> ] ,
        [ a tcs:TaxonConcept ;
            dcterms:title "Begonia salaziensis sec. Irmscher 1925" ;
            tcs:accordingTo [ a bibo:Chapter ;
                    dcterms:bibliographicCitation """Irmscher, E. (1925). Begoniaceae, 
                            in Engler, A. & K. Prantl, Nat. Pflanzenfam. ed. 2, 21: 
                            548-588.""" ] ;
            tcs:taxonName <https://ipni.org/n/105644-1> ] .

[] a tcs:TaxonConcept ;
    dcterms:title "Begonia seychellensis sec. Klazenga & al. 1994" ;
    tcs:accordingTo <https://doi/org/10.2307/3668252> ;
    tcs:taxonName <https://ipni.org/n/105731-1> ;
    tcs:intersects [ a tcs:TaxonConcept ;
        dcterms:title "Begonia comorensis sec. Keraudren-Aymonin 1983" ;
        tcs:accordingTo [ a bibo:Book ;
                dcterms:bibliographicCitation """Keraudren-Aymonin, M. (1983). Flore 
                        de Madagascar et des Comores. Famille 144 – Begoniacées: 7-108""" ] ;
        tcs:taxonName <https://ipni.org/n/104440-1> ;
        tcs:synonym <https://ipni.org/n/105731-1> ] .
```


[&lsqb;TaxonConcept-intersects-example-1.ttl&rsqb;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonConcept-intersects-example-1.ttl)&nbsp;[&lsqb;TaxonConcept-intersects-example-1.jsonld&rsqb;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonConcept-intersects-example-1.jsonld)


[&lsqb;TaxonConcept-intersects-example-2.ttl&rsqb;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonConcept-intersects-example-2.ttl)&nbsp;[&lsqb;TaxonConcept-intersects-example-2.jsonld&rsqb;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonConcept-intersects-example-2.jsonld)


[&lsqb;TaxonConceptMapping-intersects-example-1.ttl&rsqb;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonConceptMapping-intersects-example-1.ttl)&nbsp;[&lsqb;TaxonConceptMapping-intersects-example-1.jsonld&rsqb;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonConceptMapping-intersects-example-1.jsonld)


[&lsqb;TaxonConcept-intersects-example-3.ttl&rsqb;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonConcept-intersects-example-3.ttl)&nbsp;[&lsqb;TaxonConcept-intersects-example-3.jsonld&rsqb;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonConcept-intersects-example-3.jsonld)

</td>
		</tr>
		<tr>
			<td>GitHub issue</td>
			<td>https://github.com/tdwg/tcs2/issues/57</td>
		</tr>
	</tbody>
</table>

#### dwc:scientificName

<table style="width:100%;">
	<tbody>
		<tr>
			<td>Identifier</td>
			<td>http://rs.tdwg.org/dwc/terms/scientificName</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>http://www.w3.org/1999/02/22-rdf-syntax-ns#Property</td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Scientific Name</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td><p>The full scientific name, with authorship and date information if known.  When forming part of an Identification, this should be the name in lowest  level taxonomic rank that can be determined. This term should not contain  identification qualifications, which should instead be supplied in the  IdentificationQualifier term.</p></td>
		</tr>
		<tr>
			<td></td>
			<td><b>required:</b> No — <b>repeatable:</b> No</td>
		</tr>
		<tr>
			<td>Comments</td>
			<td><p><code>scientificName</code> can be used in addition to the <code>taxonName</code> property on a TaxonConcept object or the <code>nameString</code> property on a TaxonName object.</p></td>
		</tr>
		<tr>
			<td>GitHub issue</td>
			<td>https://github.com/tdwg/tcs2/issues/17</td>
		</tr>
	</tbody>
</table>

#### dwc:vernacularName

<table style="width:100%;">
	<tbody>
		<tr>
			<td>Identifier</td>
			<td>http://rs.tdwg.org/dwc/terms/vernacularName</td>
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
			<td>Definition</td>
			<td><p>A common or vernacular name.</p></td>
		</tr>
		<tr>
			<td></td>
			<td><b>required:</b> No — <b>repeatable:</b> No</td>
		</tr>
		<tr>
			<td>GitHub issue</td>
			<td>https://github.com/tdwg/tcs2/issues/235</td>
		</tr>
	</tbody>
</table>

#### dwc:verbatimTaxonRank

<table style="width:100%;">
	<tbody>
		<tr>
			<td>Identifier</td>
			<td>http://rs.tdwg.org/dwc/terms/verbatimTaxonRank</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>http://www.w3.org/1999/02/22-rdf-syntax-ns#Property</td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Verbatim taxon rank</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td><p>The taxonomic rank of the most specific name in the dwc:scientificName as it appears in the original record.</p></td>
		</tr>
		<tr>
			<td></td>
			<td><b>required:</b> No — <b>repeatable:</b> No</td>
		</tr>
		<tr>
			<td>Comments</td>
			<td><p>This term may be used for taxonomic rank designations that are not in the controlled vocabulary that is used. Implementations can decide for themselves if it makes more sense to use this term on a TaxonConcept object or a TaxonName object, or both.</p></td>
		</tr>
		<tr>
			<td>GitHub issue</td>
			<td>https://github.com/tdwg/tcs2/issues/6</td>
		</tr>
	</tbody>
</table>

#### dcterms:title

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
			<td>Definition</td>
			<td><p>A name given to the resource.</p></td>
		</tr>
		<tr>
			<td></td>
			<td><b>required:</b> No — <b>repeatable:</b> No</td>
		</tr>
		<tr>
			<td>Comments</td>
			<td><p>In TCS <code>dcterms:title</code> is used for the taxonomic concept label <a href="../bibliography#senderov_openbiodiv-o_2018">[senderov_openbiodiv-o_2018]</a>, which consists of the Taxon Name and a reference to  the publication where the concept is circumscribed, separated by 'sec.',  which stands for 'secundus' ('according to'). It is used to indicate one  specific meaning of a name – a Taxon Concept – rather than the cumulative  nomenclatural and taxonomic legacy associated with the name.</p></td>
		</tr>
		<tr>
			<td>Examples</td>
			<td><ul>
<li><code>Dicranoloma assimile sec. Klazenga 1999</code></li>
<li><code>Euphrasia gibbsiae sec. Barker 1982</code></li>
<li><code>Megalorhipida leucodactylus sec. Gielis &amp; Hobern 2020-07-16</code></li>
<li><code>Circus cyaneus sec. Clements 2021</code></li>
<li><code>Circus cyaneus sec. Howard &amp; Moore 2013</code></li>
<li><code>Circus [cyaneus or hudsonius] sec. AviBase #82745BAA</code></li>
</ul></td>
		</tr>
		<tr>
			<td>GitHub issue</td>
			<td>https://github.com/tdwg/tcs2/issues/222</td>
		</tr>
	</tbody>
</table>

### Taxon Concept Mapping

#### tcs:TaxonConceptMapping

<table style="width:100%;">
	<tbody>
		<tr>
			<td>Identifier</td>
			<td>http://rs.tdwg.org/tcs/terms/TaxonConceptMapping</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>http://www.w3.org/2000/01/rdf-schema#Class</td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Taxon concept mapping</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td><p>Alignment or mapping of two Taxon Concepts in different taxonomies or different versions of a taxonomy</p></td>
		</tr>
		<tr>
			<td>Usage</td>
			<td><p>When using this class the <code>subjectTaxonConcept</code>, <code>mappingRelation</code> and <code>objectTaxonConcept</code> are REQUIRED </p></td>
		</tr>
		<tr>
			<td>Comments</td>
			<td><p>The Taxon Concept Mapping class allows for adding extra data to a taxon concept mapping statement. As it allows for adding an 'according to' to a concept mapping it can be used for third-party mappings. While structurally very similar to the Darwin Core Resource Relationship class, it is different in that instances of the Taxon Concept Mapping class are meaningful as standalone objects.</p></td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>

```turtle
# Andropogon capillipes sec. BONAP 2014 is congruent with Andropogon capillipes sec. Weakley 2006
[] a tcs:TaxonConceptMapping ;
    tcs:mappingAccordingTo <https://doi.org/10.3233/SW-160220> ;
    tcs:mappingRelation tcs:isCongruentWith ;
    tcs:subjectTaxonConcept [ a tcs:TaxonConcept ;
        dcterms:title "Andropogon capillipes sec. BONAP 2014" ;
        tcs:taxonName <https://ipni.org/n/12781-2> ;
        tcs:accordingTo <http://bonap.net/napa#2014> ] ;
    tcs:objectTaxonConcept [ a tcs:TaxonConcept ;
        dcterms:title "Andropogon capillipes sec. Weakley 2006" ;
        tcs:taxonName <https://ipni.org/n/12781-2> ;
        tcs:accordingTo <http://www.herbarium.unc.edu/FloraArchives/WeakleyFlora_2006-Jan.pdf> ] .
```


[&lsqb;TaxonConceptMapping-isCongruentWith-example-1.ttl&rsqb;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonConceptMapping-isCongruentWith-example-1.ttl)&nbsp;[&lsqb;TaxonConceptMapping-isCongruentWith-example-1.jsonld&rsqb;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonConceptMapping-isCongruentWith-example-1.jsonld)


[&lsqb;TaxonConceptMapping-isCongruentWith-example-2.ttl&rsqb;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonConceptMapping-isCongruentWith-example-2.ttl)&nbsp;[&lsqb;TaxonConceptMapping-isCongruentWith-example-2.jsonld&rsqb;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonConceptMapping-isCongruentWith-example-2.jsonld)


[&lsqb;TaxonConceptMapping-includes-example-1.ttl&rsqb;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonConceptMapping-includes-example-1.ttl)&nbsp;[&lsqb;TaxonConceptMapping-includes-example-1.jsonld&rsqb;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonConceptMapping-includes-example-1.jsonld)


[&lsqb;TaxonConceptMapping-includes-example-2.ttl&rsqb;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonConceptMapping-includes-example-2.ttl)&nbsp;[&lsqb;TaxonConceptMapping-includes-example-2.jsonld&rsqb;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonConceptMapping-includes-example-2.jsonld)


[&lsqb;TaxonConceptMapping-isIncludedIn-example-1.ttl&rsqb;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonConceptMapping-isIncludedIn-example-1.ttl)&nbsp;[&lsqb;TaxonConceptMapping-isIncludedIn-example-1.jsonld&rsqb;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonConceptMapping-isIncludedIn-example-1.jsonld)


[&lsqb;TaxonConceptMapping-isIncludedIn-example-2.ttl&rsqb;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonConceptMapping-isIncludedIn-example-2.ttl)&nbsp;[&lsqb;TaxonConceptMapping-isIncludedIn-example-2.jsonld&rsqb;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonConceptMapping-isIncludedIn-example-2.jsonld)


[&lsqb;TaxonConceptMapping-partiallyOverlaps-example-1.ttl&rsqb;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonConceptMapping-partiallyOverlaps-example-1.ttl)&nbsp;[&lsqb;TaxonConceptMapping-partiallyOverlaps-example-1.jsonld&rsqb;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonConceptMapping-partiallyOverlaps-example-1.jsonld)


[&lsqb;TaxonConceptMapping-partiallyOverlaps-example-2.ttl&rsqb;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonConceptMapping-partiallyOverlaps-example-2.ttl)&nbsp;[&lsqb;TaxonConceptMapping-partiallyOverlaps-example-2.jsonld&rsqb;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonConceptMapping-partiallyOverlaps-example-2.jsonld)


[&lsqb;TaxonConceptMapping-isDisjointFrom-example-1.ttl&rsqb;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonConceptMapping-isDisjointFrom-example-1.ttl)&nbsp;[&lsqb;TaxonConceptMapping-isDisjointFrom-example-1.jsonld&rsqb;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonConceptMapping-isDisjointFrom-example-1.jsonld)


[&lsqb;TaxonConceptMapping-isDisjointFrom-example-2.ttl&rsqb;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonConceptMapping-isDisjointFrom-example-2.ttl)&nbsp;[&lsqb;TaxonConceptMapping-isDisjointFrom-example-2.jsonld&rsqb;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonConceptMapping-isDisjointFrom-example-2.jsonld)


[&lsqb;TaxonConceptMapping-intersects-example-1.ttl&rsqb;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonConceptMapping-intersects-example-1.ttl)&nbsp;[&lsqb;TaxonConceptMapping-intersects-example-1.jsonld&rsqb;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonConceptMapping-intersects-example-1.jsonld)


[&lsqb;TaxonConceptMapping-intersects-example-2.ttl&rsqb;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonConceptMapping-intersects-example-2.ttl)&nbsp;[&lsqb;TaxonConceptMapping-intersects-example-2.jsonld&rsqb;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonConceptMapping-intersects-example-2.jsonld)

</td>
		</tr>
		<tr>
			<td>GitHub issue</td>
			<td>https://github.com/tdwg/tcs2/issues/43</td>
		</tr>
	</tbody>
</table>

#### tcs:mappingAccordingTo

<table style="width:100%;">
	<tbody>
		<tr>
			<td>Identifier</td>
			<td>http://rs.tdwg.org/tcs/terms/mappingAccordingTo</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>http://www.w3.org/1999/02/22-rdf-syntax-ns#Property</td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Mapping according to</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td><p>Reference to the source of the taxon concept mapping.</p></td>
		</tr>
		<tr>
			<td>Usage</td>
			<td><p><code>mappingAccordingTo</code> is an IRI term; a Taxon  Concept Mapping can have only one <code>mappingAccordingTo</code>.</p></td>
		</tr>
		<tr>
			<td></td>
			<td><b>required:</b> No — <b>repeatable:</b> No</td>
		</tr>
		<tr>
			<td>GitHub issue</td>
			<td>https://github.com/tdwg/tcs2/issues/47</td>
		</tr>
	</tbody>
</table>

#### tcs:mappingRelation

<table style="width:100%;">
	<tbody>
		<tr>
			<td>Identifier</td>
			<td>http://rs.tdwg.org/tcs/terms/mappingRelation</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>http://www.w3.org/1999/02/22-rdf-syntax-ns#Property</td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Mapping relation</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td><p>The kind of mapping relation between the two concepts</p></td>
		</tr>
		<tr>
			<td>Usage</td>
			<td><p>This property is REQUIRED; one MUST use one of the mapping properties <code>isCongruentWith</code>, <code>includes</code>, <code>isIncludedIn</code>, <code>partiallyOverlaps</code>, <code>isDisjointFrom</code> or <code>intersects</code>.</p></td>
		</tr>
		<tr>
			<td></td>
			<td><b>required:</b> Yes — <b>repeatable:</b> No</td>
		</tr>
		<tr>
			<td>GitHub issue</td>
			<td>https://github.com/tdwg/tcs2/issues/44</td>
		</tr>
	</tbody>
</table>

#### tcs:subjectTaxonConcept

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
			<td>Definition</td>
			<td><p>Taxon Concept that is the subject in the mapping statement.</p></td>
		</tr>
		<tr>
			<td>Usage</td>
			<td><p><code>subjectTaxonConcept</code> is a TCS Taxon Concept; a Taxon Concept Mapping  statement can have only one <code>subjectTaxonConcept</code>.</p></td>
		</tr>
		<tr>
			<td></td>
			<td><b>required:</b> Yes — <b>repeatable:</b> No</td>
		</tr>
		<tr>
			<td>Comments</td>
			<td><p>This is the Taxon Concept at the left-hand side of the statement.</p></td>
		</tr>
		<tr>
			<td>GitHub issue</td>
			<td>https://github.com/tdwg/tcs2/issues/45</td>
		</tr>
	</tbody>
</table>

#### tcs:objectTaxonConcept

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
			<td>Definition</td>
			<td><p>Taxon Concept that is the object in the mapping statement.</p></td>
		</tr>
		<tr>
			<td>Usage</td>
			<td><p><code>objectTaxonConcept</code> is a TCS Taxon Concept; a Taxon Concept Mapping  statement can have only one <code>objectTaxonConcept</code>.</p></td>
		</tr>
		<tr>
			<td></td>
			<td><b>required:</b> Yes — <b>repeatable:</b> No</td>
		</tr>
		<tr>
			<td>Comments</td>
			<td><p>This is the Taxon Concept at the right-hand side of the statement.</p></td>
		</tr>
		<tr>
			<td>GitHub issue</td>
			<td>https://github.com/tdwg/tcs2/issues/46</td>
		</tr>
	</tbody>
</table>

### Taxon Name

#### tcs:TaxonName

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
			<td><p>A TCS Taxon Name MUST have a <code>nameString</code>.</p></td>
		</tr>
		<tr>
			<td>Comments</td>
			<td><p>The word 'name' here is taken in its dictionary meaning and not in the sense of a particular nomenclatural code. This means that the Taxon Name class can, in principle, be used for any type of name, not just names that are validly published under the relevant nomenclatural code.</p></td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>

```turtle
<urn:lsid:zoobank.org:act:355AAA50-D89F-466E-A216-96B7A17D5AD4> a tcs:TaxonName ;
    tcs:nameString "Carabus nitens" ;
    dwc:scientificNameAuthorship "Linnaeus, 1758" .
```


[&lsqb;TaxonName-example-1.ttl&rsqb;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonName-example-1.ttl)&nbsp;[&lsqb;TaxonName-example-1.jsonld&rsqb;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonName-example-1.jsonld)


[&lsqb;TaxonName-example-2.ttl&rsqb;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonName-example-2.ttl)&nbsp;[&lsqb;TaxonName-example-2.jsonld&rsqb;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonName-example-2.jsonld)


[&lsqb;TaxonName-example-3.ttl&rsqb;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonName-example-3.ttl)&nbsp;[&lsqb;TaxonName-example-3.jsonld&rsqb;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonName-example-3.jsonld)


[&lsqb;TaxonName-example-4.ttl&rsqb;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonName-example-4.ttl)&nbsp;[&lsqb;TaxonName-example-4.jsonld&rsqb;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonName-example-4.jsonld)

</td>
		</tr>
		<tr>
			<td>GitHub issue</td>
			<td>https://github.com/tdwg/tcs2/issues/15</td>
		</tr>
	</tbody>
</table>

#### tcs:nameString

<table style="width:100%;">
	<tbody>
		<tr>
			<td>Identifier</td>
			<td>http://rs.tdwg.org/tcs/terms/nameString</td>
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
			<td>Definition</td>
			<td><p>The complete name string without any authority or year components.</p></td>
		</tr>
		<tr>
			<td>Usage</td>
			<td><p><code>nameString</code> is a literal. The <code>nameString</code> property is REQUIRED on a TCS Taxon Name and a Taxon Name can have only one <code>nameString</code>.</p></td>
		</tr>
		<tr>
			<td></td>
			<td><b>required:</b> No — <b>repeatable:</b> No</td>
		</tr>
		<tr>
			<td>Comments</td>
			<td><p>The <code>nameString</code> property differs from the <code>scientificName</code> property  in Darwin Core in that all kinds of names are allowed. Also, in the case of  scientific names, contrary to the <code>dwc:scientificName</code>, <code>nameString</code>  does not include the authorship. In botanical names, it does include the  rank prefixes for infrageneric and infraspecific epithets as they are  considered part of the name.</p></td>
		</tr>
		<tr>
			<td>GitHub issue</td>
			<td>https://github.com/tdwg/tcs2/issues/16</td>
		</tr>
	</tbody>
</table>

#### tcs:namePublishedIn

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
			<td>Definition</td>
			<td><p>Reference to the publication in which the name was first published.</p></td>
		</tr>
		<tr>
			<td></td>
			<td><b>required:</b> No — <b>repeatable:</b> No</td>
		</tr>
		<tr>
			<td>Comments</td>
			<td><p>In botany, this would be the protologue. This is the IRI counterpart of  the Darwin Core <code>namePublishedIn</code>, which TCS borrows.</p></td>
		</tr>
		<tr>
			<td>GitHub issue</td>
			<td>https://github.com/tdwg/tcs2/issues/29</td>
		</tr>
	</tbody>
</table>

#### tcs:microreference

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
			<td>Definition</td>
			<td><p>Specifies any minor reference parts, e.g. page number.</p></td>
		</tr>
		<tr>
			<td>Usage</td>
			<td><p><code>microreference</code> is a string literal; a Taxon Name can have only one  <code>microreference</code> and only when <code>namePublishedIn</code> is used as well.</p></td>
		</tr>
		<tr>
			<td></td>
			<td><b>required:</b> No — <b>repeatable:</b> No</td>
		</tr>
		<tr>
			<td>Comments</td>
			<td><p>In taxonomic works it is convention to cite the exact location in a work  where a new name is published. The <code>microreference</code> property lets one do  that on the Taxon Name object, so that the <code>namePublishedIn</code> reference can  be reused.</p></td>
		</tr>
		<tr>
			<td>GitHub issue</td>
			<td>https://github.com/tdwg/tcs2/issues/30</td>
		</tr>
	</tbody>
</table>

#### tcs:nomenclaturalCode

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
			<td>Definition</td>
			<td><p>Nomenclatural code that applies to the group of organisms the taxonomic name  is for.</p></td>
		</tr>
		<tr>
			<td>Usage</td>
			<td><p><code>nomenclaturalCode</code> takes an IRI or object; a Taxon Name can have only one  <code>nomenclaturalCode</code>.</p></td>
		</tr>
		<tr>
			<td></td>
			<td><b>required:</b> No — <b>repeatable:</b> No</td>
		</tr>
		<tr>
			<td>Comments</td>
			<td><p>This is the IRI equivalent of the Darwin Core <code>nomenclaturalCode</code>. In the  absence of a TDWG vocabulary, it is RECOMMENDED to use a value from the GBIF  Nomenclatural Codes Vocabulary  (https://rs.gbif.org/vocabulary/gbif/nomenclatural_code.xml).</p></td>
		</tr>
		<tr>
			<td>GitHub issue</td>
			<td>https://github.com/tdwg/tcs2/issues/33</td>
		</tr>
	</tbody>
</table>

#### tcs:nomenclaturalStatus

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
			<td>Definition</td>
			<td><p>Status related to the original publication of the name and its conformance to the relevant rules of nomenclature.</p></td>
		</tr>
		<tr>
			<td>Usage</td>
			<td><p><code>nomenclaturalStatus</code> takes an IRI or object; a Taxon Name can have only one  <code>nomenclaturalStatus</code>.</p></td>
		</tr>
		<tr>
			<td></td>
			<td><b>required:</b> No — <b>repeatable:</b> No</td>
		</tr>
		<tr>
			<td>Comments</td>
			<td><p>This is the IRI equivalent of the Darwin Core <code>nomenclaturalStatus</code>. In the  absence of a TDWG vocabulary, it is RECOMMENDED to use a value from the GBIF  Nomenclatural Status Vocabulary  (https://rs.gbif.org/vocabulary/gbif/nomenclatural_status_2019-02-08.xml).</p></td>
		</tr>
		<tr>
			<td>GitHub issue</td>
			<td>https://github.com/tdwg/tcs2/issues/35</td>
		</tr>
	</tbody>
</table>

#### tcs:typification

<table style="width:100%;">
	<tbody>
		<tr>
			<td>Identifier</td>
			<td>http://rs.tdwg.org/tcs/terms/typification</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>http://www.w3.org/1999/02/22-rdf-syntax-ns#Property</td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Typification</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td><p>Designation of a nomenclatural type for a name</p></td>
		</tr>
		<tr>
			<td>Usage</td>
			<td><p>The <code>typification</code> property takes a <code>tcs:NomenclaturalType</code> or array of <code>tcs:NomenclaturalType</code>s.</p></td>
		</tr>
		<tr>
			<td></td>
			<td><b>required:</b> No — <b>repeatable:</b> Yes</td>
		</tr>
		<tr>
			<td>Comments</td>
			<td><p><code>tcs:typification</code> is the inverse of <code>tcs:typifiedName</code>.</p></td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>

```turtle
<https://ipni.org/n/105731-1> a tcs:TaxonName ;
    tcs:nameString "Begonia seychellensis" ;
    dwc:scientificNameAuthorship "Hemsl." ;
    dwc:namePublishedIn "J. Bot. 54(Suppl. 2): 15 (1916)" ;
    tcs:typification [ a tcs:NomenclaturalType ;
            tcs:typifiedName <https://ipni.org/n/105731-1> ;
            tcs:typeSpecimen [ a dwc:MaterialCitation ;
                    dwc:country "Seychelles" ;
                    dwc:island "Mahé" ;
                    dwc:recordedBy "Horne" ;
                    dwc:recordNumber "s.n." ;
                    dwc:institutionCode "G" ] ;
            tcs:typeOfType <http://rs.gbif.org/vocabulary/gbif/type_status/isolectotype> ] ,
        [ a tcs:NomenclaturalType ;
            tcs:typifiedName <https://ipni.org/n/105731-1> ;
            tcs:typeSpecimen [ a dwc:MaterialCitation ;
                    dwc:country "Seychelles" ;
                    dwc:island "Mahé" ;
                    dwc:recordedBy "Horne" ;
                    dwc:recordNumber "245" ;
                    dwc:institutionCode "K" ] ;
            tcs:typeOfType <http://rs.gbif.org/vocabulary/gbif/type_status/lectotype> ]  ,
        [ a tcs:NomenclaturalType ;
            tcs:typifiedName <https://ipni.org/n/105731-1> ;
            tcs:typeSpecimen [ a dwc:MaterialCitation ;
                    dwc:country "Seychelles" ;
                    dwc:island "Mahé" ;
                    dwc:recordedBy "Gardiner" ;
                    dwc:recordNumber "s.n." ;
                    dwc:institutionCode "K" ] ;
            tcs:typeOfType <http://rs.gbif.org/vocabulary/gbif/type_status/syntype> ]  ,
        [ a tcs:NomenclaturalType ;
            tcs:typifiedName <https://ipni.org/n/105731-1> ;
            tcs:typeSpecimen [ a dwc:MaterialCitation ;
                    dwc:country "Seychelles" ;
                    dwc:island "Silhouette" ;
                    dwc:recordedBy "Gardiner" ;
                    dwc:recordNumber "111" ;
                    dwc:institutionCode "K" ] ;
            tcs:typeOfType <http://rs.gbif.org/vocabulary/gbif/type_status/syntype> ]  ,
        [ a tcs:NomenclaturalType ;
            tcs:typifiedName <https://ipni.org/n/105731-1> ;
            tcs:typeSpecimen [ a dwc:MaterialCitation ;
                    dwc:country "Seychelles" ;
                    dwc:island "Mahé and Silhouette" ;
                    dwc:recordedBy "Neville" ;
                    dwc:recordNumber "s.n." ;
                    dwc:institutionCode "K" ] ;
            tcs:typeOfType <http://rs.gbif.org/vocabulary/gbif/type_status/syntype> ]  .
```


[&lsqb;TaxonName-typification-example-1.ttl&rsqb;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonName-typification-example-1.ttl)&nbsp;[&lsqb;TaxonName-typification-example-1.jsonld&rsqb;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonName-typification-example-1.jsonld)


[&lsqb;TaxonName-typification-example-2.ttl&rsqb;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonName-typification-example-2.ttl)&nbsp;[&lsqb;TaxonName-typification-example-2.jsonld&rsqb;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonName-typification-example-2.jsonld)

</td>
		</tr>
		<tr>
			<td>GitHub issue</td>
			<td>https://github.com/tdwg/tcs2/issues/238</td>
		</tr>
	</tbody>
</table>

#### tcs:typificationLiteral

<table style="width:100%;">
	<tbody>
		<tr>
			<td>Identifier</td>
			<td>http://rs.tdwg.org/tcs/terms/typificationLiteral</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>http://www.w3.org/1999/02/22-rdf-syntax-ns#Property</td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Typification</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td><p>Designation of a nomenclatural type for a name</p></td>
		</tr>
		<tr>
			<td>Usage</td>
			<td><p>The <code>typificationLiteral</code> property takes a literal value.</p></td>
		</tr>
		<tr>
			<td></td>
			<td><b>required:</b> No — <b>repeatable:</b> No</td>
		</tr>
		<tr>
			<td>Comments</td>
			<td><p>The <code>typificationLiteral</code> property can be used for citation of a type (or types) as written in the publication in which the typified name was published. </p></td>
		</tr>
		<tr>
			<td>GitHub issue</td>
			<td>https://github.com/tdwg/tcs2/issues/223</td>
		</tr>
	</tbody>
</table>

#### tcs:basionym

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
			<td>Definition</td>
			<td><p>Epithet- or name-bringing synonym.</p></td>
		</tr>
		<tr>
			<td>Usage</td>
			<td><p>A <code>basionym</code> is another Taxon Name; a Taxon Name can have only one <code>basionym</code>.</p></td>
		</tr>
		<tr>
			<td></td>
			<td><b>required:</b> No — <b>repeatable:</b> No</td>
		</tr>
		<tr>
			<td>Comments</td>
			<td><p>The term <code>basionym</code> is in the draft BioCode (<a href="../bibliography/#greuter_draft_2011">[greuter_draft_2011]</a>), so can be used for all organisms. The <code>basionym</code> property is only used for new combinations ('comb. nov.'). If the new name is a replacement name ('nom. nov.') the <code>replacedName</code> property SHOULD be used instead. It SHOULD be noted that a basionym is always a different name or combination: a name cannot be its own basionym.</p></td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>

```turtle
<https://id.biodiversity.org.au/name/apni/166271> a tcs:TaxonName ;
    rdf:seeAlso <https://ipni.org/n/17571690-1> ;
    tcs:nameString "Doodia australis" ;
    dwc:scientificNameAuthorship "(Parris) Parris" ;
    dwc:namePublishedIn "Fl. Australia 48: 710 (1998)" ;
    tcs:basionym <https://id.biodiversity.org.au/name/apni/117170> .

<https://id.biodiversity.org.au/name/apni/117170> a tcs:TaxonName ;
    rdf:seeAlso <https://ipni.org/n/17567870-1> ;
    tcs:nameString "Doodia media subsp. australis" ;
    dwc:scientificNameAuthorship "Parris" ;
    dwc:namePublishedIn "New Zealand J. Bot. 10(4): 593 (1972)" .
```


[&lsqb;TaxonName-basionym-example-1.ttl&rsqb;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonName-basionym-example-1.ttl)&nbsp;[&lsqb;TaxonName-basionym-example-1.jsonld&rsqb;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonName-basionym-example-1.jsonld)


[&lsqb;TaxonName-basionym-example-2.ttl&rsqb;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonName-basionym-example-2.ttl)&nbsp;[&lsqb;TaxonName-basionym-example-2.jsonld&rsqb;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonName-basionym-example-2.jsonld)

</td>
		</tr>
		<tr>
			<td>GitHub issue</td>
			<td>https://github.com/tdwg/tcs2/issues/36</td>
		</tr>
	</tbody>
</table>

#### tcs:replacedName

<table style="width:100%;">
	<tbody>
		<tr>
			<td>Identifier</td>
			<td>http://rs.tdwg.org/tcs/terms/replacedName</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>http://www.w3.org/1999/02/22-rdf-syntax-ns#Property</td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Replaced name</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td><p>The legitimate or illegitimate, previously published name on which a  replacement name (nomen novum) is based.</p></td>
		</tr>
		<tr>
			<td>Usage</td>
			<td><p><code>replacedName</code> is another Taxon Name; a Taxon Name can have only one  <code>replacedName</code>.</p></td>
		</tr>
		<tr>
			<td></td>
			<td><b>required:</b> No — <b>repeatable:</b> No</td>
		</tr>
		<tr>
			<td>Comments</td>
			<td><p>'replaced name' is used in the draft BioCode (<a href="../bibliography/#greuter_draft_2011">[greuter_draft_2011]</a>). In the Botanical Code the term 'replaced synonym' is used for the same thing. A 'replacement name' is a name that is published as a substitute for an earlier published name that is either illegitimate or for which a new combination cannot be created in the place a taxon is transferred to because of an older blocking name.</p></td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>

```turtle
<https://www.tropicos.org/name/35183593> a tcs:TaxonName ;
    tcs:nameString "Dicranum bartramianum" ;
    dwc:scientificNameAuthorship "B.H.Allen" ;
    dwc:namePublishedIn "Cryptog. Bryol. Lichénol. 8: 323" ;
    dwc:namePublishedInYear "1987" ;
    tcs:replacedName <https://www.tropicos.org/name/35120798> .

<https://www.tropicos.org/name/35120798> a tcs:TaxonName ;
    tcs:nameString "Dicnemon robustum" ;
    dwc:scientificNameAuthorship "E.B.Bartram" ;
    dwc:namePublishedIn "Bryologist 48: 112" ;
    dwc:namePublishedInYear "1945" .

# blocking name
<https://www.tropicos.org/name/35124067> a tcs:TaxonName ;
    tcs:nameString "Dicranum robustum" ;
    dwc:scientificNameAuthorship "Hook.f. & Wilson" ;
    dwc:namePublishedIn "London J. Bot. 3: 542" ;
    dwc:namePublishedInYear "1844" .

# combination of Dicnemon robustum
<https://www.tropicos.org/name/35162373> a tcs:TaxonName ;
    tcs:nameString "Eucamptodon robustum" ;
    dwc:scientificNameAuthorship "(E.B.Bartram) E.B.Bartram" ;
    dwc:namePublishedIn "Brittonia 11: 88" ;
    dwc:namePublishedInYear "1959" ;
    tcs:basionym <https://www.tropicos.org/name/35120798> .

# combination of Dicranum bartramianum
<https://www.tropicos.org/name/35204723> a tcs:TaxonName ;
    tcs:nameString "Dicranoloma bartramianum" ;
    dwc:scientificNameAuthorship "(B.H.Allen) Klazenga" ;
    dwc:namePublishedIn "J. Hattory Bot. Lab. 87: 57" ;
    dwc:namePublishedInYear "1999" ;
    tcs:basionym <https://www.tropicos.org/name/35183593> .
```


[&lsqb;TaxonName-replacedName-example-1.ttl&rsqb;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonName-replacedName-example-1.ttl)&nbsp;[&lsqb;TaxonName-replacedName-example-1.jsonld&rsqb;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonName-replacedName-example-1.jsonld)


[&lsqb;TaxonName-replacedName-example-2.ttl&rsqb;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonName-replacedName-example-2.ttl)&nbsp;[&lsqb;TaxonName-replacedName-example-2.jsonld&rsqb;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonName-replacedName-example-2.jsonld)


[&lsqb;TaxonName-replacedName-example-3.ttl&rsqb;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonName-replacedName-example-3.ttl)&nbsp;[&lsqb;TaxonName-replacedName-example-3.jsonld&rsqb;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonName-replacedName-example-3.jsonld)


[&lsqb;TaxonName-replacedName-example-4.ttl&rsqb;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonName-replacedName-example-4.ttl)&nbsp;[&lsqb;TaxonName-replacedName-example-4.jsonld&rsqb;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonName-replacedName-example-4.jsonld)

</td>
		</tr>
		<tr>
			<td>GitHub issue</td>
			<td>https://github.com/tdwg/tcs2/issues/37</td>
		</tr>
	</tbody>
</table>

#### tcs:basedOn

<table style="width:100%;">
	<tbody>
		<tr>
			<td>Identifier</td>
			<td>http://rs.tdwg.org/tcs/terms/basedOn</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>http://www.w3.org/1999/02/22-rdf-syntax-ns#Property</td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Based on</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td><p>Earlier name on which this name is based</p></td>
		</tr>
		<tr>
			<td>Usage</td>
			<td><p><code>basedOn</code> is another Taxon Name; a Taxon Name can have only one <code>basedOn</code>. The term SHOULD only be used in situations where the semantically more meaningful <code>basionym</code> and <code>replacedName</code> cannot be used.</p></td>
		</tr>
		<tr>
			<td></td>
			<td><b>required:</b> No — <b>repeatable:</b> No</td>
		</tr>
		<tr>
			<td>Comments</td>
			<td><p>The <code>basedOn</code> property can be used to associate a name to a homotypic group of names in situations where the <code>basionym</code> and <code>replacedName</code> properties cannot be used. Therefore the property can be useful for (1) linking an autonym to a species name, (2) linking a valid name to an earlier invalid name and (3) linking an invalid name to a later valid name.</p></td>
		</tr>
		<tr>
			<td>GitHub issue</td>
			<td>https://github.com/tdwg/tcs2/issues/38</td>
		</tr>
	</tbody>
</table>

#### tcs:laterHomonymOf

<table style="width:100%;">
	<tbody>
		<tr>
			<td>Identifier</td>
			<td>http://rs.tdwg.org/tcs/terms/laterHomonymOf</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>http://www.w3.org/1999/02/22-rdf-syntax-ns#Property</td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Later homonym of</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td><p>An older legitimate name with the same spelling but a different nomenclatural type</p></td>
		</tr>
		<tr>
			<td>Usage</td>
			<td><p><code>laterHomonymOf</code> is another Taxon Name object</p></td>
		</tr>
		<tr>
			<td></td>
			<td><b>required:</b> No — <b>repeatable:</b> No</td>
		</tr>
		<tr>
			<td>Comments</td>
			<td><p>If there are more than two homonyms, the oldest name SHOULD be given here. In zoology, this is the <em>senior homonym</em>.</p></td>
		</tr>
		<tr>
			<td>GitHub issue</td>
			<td>https://github.com/tdwg/tcs2/issues/229</td>
		</tr>
	</tbody>
</table>

#### tcs:conservedAgainst

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
			<td>Definition</td>
			<td><p>Name(s) against which this name is conserved.</p></td>
		</tr>
		<tr>
			<td>Usage</td>
			<td><p>The <code>conservedAgainst</code> property takes another Taxon Name; a Taxon Name can  be conserved against more than one other Taxon Names.</p></td>
		</tr>
		<tr>
			<td></td>
			<td><b>required:</b> No — <b>repeatable:</b> Yes</td>
		</tr>
		<tr>
			<td>Comments</td>
			<td><p>A scientific name below the rank of family is not conserved against all  other names, but only against one or more names that in turn are rejected  against the conserved name. A name can be conserved against more than one  other name, so this property is repeatable.</p></td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>

```turtle
<https://www.tropicos.org/name/35000378> a tcs:TaxonName ;
    tcs:nameString "Dicranoloma" ;
    dwc:scientificNameAuthorship "(Renauld) Renauld" ;
    tcs:namePublishedInYear "1909" ;
    tcs:conservedAgainst <https://www.tropicos.org/name/35000771> ,
            <https://www.tropicos.org/name/35000146> .

<https://www.tropicos.org/name/35000771> a tcs:TaxonName ;
    tcs:nameString "Megalostylium" ;
    dwc:scientificNameAuthorship "Dozy & Molk." ;
    dwc:namePublishedInYear "1848" . 

<https://www.tropicos.org/name/35000146> a tcs:TaxonName ;
    tcs:nameString "Braunfelsia" ;
    dwc:scientificNameAuthorship "Paris" ;
    dwc:namePublishedInYear "1894" .
```


[&lsqb;TaxonName-conservedAgainst-example-1.ttl&rsqb;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonName-conservedAgainst-example-1.ttl)&nbsp;[&lsqb;TaxonName-conservedAgainst-example-1.jsonld&rsqb;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonName-conservedAgainst-example-1.jsonld)

</td>
		</tr>
		<tr>
			<td>GitHub issue</td>
			<td>https://github.com/tdwg/tcs2/issues/39</td>
		</tr>
	</tbody>
</table>

#### tcs:combinationAuthor

<table style="width:100%;">
	<tbody>
		<tr>
			<td>Identifier</td>
			<td>http://rs.tdwg.org/tcs/terms/combinationAuthor</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>http://www.w3.org/1999/02/22-rdf-syntax-ns#Property</td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Combination author</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td><p>Author of the combination</p></td>
		</tr>
		<tr>
			<td>Usage</td>
			<td><p><code>combinationAuthor</code> is an IRI property. It can be a person or a list of persons.</p></td>
		</tr>
		<tr>
			<td></td>
			<td><b>required:</b> No — <b>repeatable:</b> Yes</td>
		</tr>
		<tr>
			<td>Comments</td>
			<td><p>'combination' is taken here to be a different name with the same nomenclatural type.</p></td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>

```turtle
<https://ipni.org/n/316069-1> a tcs:TaxonName ;
    tcs:nameString "Rafflesia arnoldi" ;
    dwc:scientificNameAuthorship "R.Br." ;
    tcs:combinationAuthor <https://ipni.org/a/1192-1> ;
    tcs:combinationAuthorLiteral "R.Br." .

<https://ipni.org/a/1192-1> a foaf:Person ;
    foaf:givenName "Robert" ;
    foaf:surname "Brown" .
```


[&lsqb;TaxonName-combinationAuthor-example-1.ttl&rsqb;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonName-combinationAuthor-example-1.ttl)&nbsp;[&lsqb;TaxonName-combinationAuthor-example-1.jsonld&rsqb;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonName-combinationAuthor-example-1.jsonld)

</td>
		</tr>
		<tr>
			<td>GitHub issue</td>
			<td>https://github.com/tdwg/tcs2/issues/239</td>
		</tr>
	</tbody>
</table>

#### tcs:combinationAuthorLiteral

<table style="width:100%;">
	<tbody>
		<tr>
			<td>Identifier</td>
			<td>http://rs.tdwg.org/tcs/terms/combinationAuthorLiteral</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>http://www.w3.org/1999/02/22-rdf-syntax-ns#Property</td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Combination author literal</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td><p>Author of the combination</p></td>
		</tr>
		<tr>
			<td>Usage</td>
			<td><p><code>combinationAuthorLiteral</code> is a Literal property.</p></td>
		</tr>
		<tr>
			<td></td>
			<td><b>required:</b> No — <b>repeatable:</b> No</td>
		</tr>
		<tr>
			<td>Comments</td>
			<td><p>'combination' is taken here to be a different name with the same nomenclatural type.</p></td>
		</tr>
		<tr>
			<td>GitHub issue</td>
			<td>https://github.com/tdwg/tcs2/issues/239</td>
		</tr>
	</tbody>
</table>

#### tcs:basionymAuthor

<table style="width:100%;">
	<tbody>
		<tr>
			<td>Identifier</td>
			<td>http://rs.tdwg.org/tcs/terms/basionymAuthor</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>http://www.w3.org/1999/02/22-rdf-syntax-ns#Property</td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Basionym author</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td><p>Author of the basionym of the name</p></td>
		</tr>
		<tr>
			<td>Usage</td>
			<td><p><code>basionymAuthor</code> is an IRI property. It can be a person or a list of persons.</p></td>
		</tr>
		<tr>
			<td></td>
			<td><b>required:</b> No — <b>repeatable:</b> Yes</td>
		</tr>
		<tr>
			<td>Comments</td>
			<td><p><code>basionymAuthor</code> (or its literal counterpart) is the bit in parentheses in the <code>dwc:scientificNameAuthorship</code>.</p></td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>

```turtle
<https://tropicos.org/name/35121611> a tcs:taxonName ;
    tcs:nameString "Dicranoloma robustum" ;
    dwc:scientificNameAuthorship "(Hook.f. & Wilson) Paris" ;
    tcs:combinationAuthor <https://tropicos.org/person/2011> ;
    tcs:combinationAuthorLiteral "Paris" 
    tcs:basionymAuthor _:b1 ;
    tcs:basionymAuthorLiteral "Hook.f. & Wilson" ;
    tcs:basionym <https://tropicos.org/name/35124067> .

<https://tropicos.org/name/35124067> a tcs:TaxonName ;
    tcs:nameString "Dicranum robustum" ;
    dwc:scientificNameAuthorship ;
    tcs:combinationAuthor _:b1 ;
    tcs:combinationAuthorLiteral "Hook.f. & Wilson" .

<https://tropicos.org/person/2011> a foaf:Person ;
    foaf:givenName "Jean Édouard Gabriel Narcisse" ;
    foaf:surname "Paris" .

_:b1 a rdf:Seq ;
    rdf:_1 <https://tropicos.org/person/3> ;
    rdf:_2 <https://tropicos.org/person/10481> .

<https://tropicos.org/person/3> a foaf:Person ;
    foaf:givenName "Joseph Dalton" ;
    foaf:surname "Hooker" .

<https://tropicos.org/person/10481> a foaf:Person ;
    foaf:givenName "William" ;
    foaf:surname "Wilson" .
```


[&lsqb;TaxonName-basionymAuthor-example-1.ttl&rsqb;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonName-basionymAuthor-example-1.ttl)&nbsp;[&lsqb;TaxonName-basionymAuthor-example-1.jsonld&rsqb;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonName-basionymAuthor-example-1.jsonld)

</td>
		</tr>
		<tr>
			<td>GitHub issue</td>
			<td>https://github.com/tdwg/tcs2/issues/239</td>
		</tr>
	</tbody>
</table>

#### tcs:basionymAuthorLiteral

<table style="width:100%;">
	<tbody>
		<tr>
			<td>Identifier</td>
			<td>http://rs.tdwg.org/tcs/terms/basionymAuthorLiteral</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>http://www.w3.org/1999/02/22-rdf-syntax-ns#Property</td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Basionym author literal</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td><p>Author of the basionym of the name</p></td>
		</tr>
		<tr>
			<td>Usage</td>
			<td><p><code>basionymAuthorLiteral</code> is a Literal property.</p></td>
		</tr>
		<tr>
			<td></td>
			<td><b>required:</b> No — <b>repeatable:</b> No</td>
		</tr>
		<tr>
			<td>Comments</td>
			<td><p><code>basionymAuthorLiteral</code> is the bit in parentheses in the <code>dwc:scientificNameAuthorship</code>.</p></td>
		</tr>
		<tr>
			<td>GitHub issue</td>
			<td>https://github.com/tdwg/tcs2/issues/239</td>
		</tr>
	</tbody>
</table>

#### tcs:combinationAscribedAuthor

<table style="width:100%;">
	<tbody>
		<tr>
			<td>Identifier</td>
			<td>http://rs.tdwg.org/tcs/terms/combinationAscribedAuthor</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>http://www.w3.org/1999/02/22-rdf-syntax-ns#Property</td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Combination ascribed author</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td><p>Ascribed author of the present name</p></td>
		</tr>
		<tr>
			<td>Usage</td>
			<td><p><code>combinationAscribedAuthor</code> is an IRI property. It can be a person or a list of persons.</p></td>
		</tr>
		<tr>
			<td></td>
			<td><b>required:</b> No — <b>repeatable:</b> Yes</td>
		</tr>
		<tr>
			<td>Comments</td>
			<td><p>'Ascribed author' is a person (or group of people) who a name is ascribed to in a publication, but who is not the author of the name according to the rules of the nomenclatural codes, because they did not contribute to the validating description of the name. In the <code>dwc:scientificNameAuthorship</code> these authors are indicated with 'ex', the ascribed author coming before the 'ex' and the author the name is attributed to after. Note that the 'ex' construction that is sometimes used with zoological names has got nothing to do with attribution or ascription, but is used to indicate a concept, much like we do here with 'sec.' or 'sensu' in taxon concept labels.</p></td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>

```turtle
<https://tropicos.org/name/35153928> a tcs:TaxonName ;
    tcs:nameString "Calymperes serratum" ;
    dwc:scientificNameAuthorship "A.Braun ex Müll.Hal." ;
    tcs:combinationAuthor <https://tropicos.org/person/2> ;
    tcs:combinationAuthorLiteral "Müll.Hal." ;
    tcs:combinationAscribedAuthor <https://tropicos.org/person/973> ;
    tcs:combinationAscribedAuthorLiteral "A.Braun" .

<https://tropicos.org/person/2> a foaf:Person ;
    foaf:givenName "Johann Karl (Carl) August (Friedrich Wilhelm)" ;
    foaf:surname "Müller" .

<https://tropicos.org/person/973> a foaf:Person ;
    foaf:givenName "Alexander Karl (Carl) Heinrich" ;
    foaf:surname "Braun" .
```


[&lsqb;TaxonName-combinationAscribedAuthor-example-1.ttl&rsqb;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonName-combinationAscribedAuthor-example-1.ttl)&nbsp;[&lsqb;TaxonName-combinationAscribedAuthor-example-1.jsonld&rsqb;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonName-combinationAscribedAuthor-example-1.jsonld)

</td>
		</tr>
		<tr>
			<td>GitHub issue</td>
			<td>https://github.com/tdwg/tcs2/issues/239</td>
		</tr>
	</tbody>
</table>

#### tcs:combinationAscribedAuthorLiteral

<table style="width:100%;">
	<tbody>
		<tr>
			<td>Identifier</td>
			<td>http://rs.tdwg.org/tcs/terms/combinationAscribedAuthorLiteral</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>http://www.w3.org/1999/02/22-rdf-syntax-ns#Property</td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Combination ascribed author literal</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td><p>Ascribed author of the present name</p></td>
		</tr>
		<tr>
			<td>Usage</td>
			<td><p><code>combinationAscribedAuthorLiteral</code> is a Literal property.</p></td>
		</tr>
		<tr>
			<td></td>
			<td><b>required:</b> No — <b>repeatable:</b> No</td>
		</tr>
		<tr>
			<td>Comments</td>
			<td><p>'Ascribed author' is a person (or group of people) who a name is ascribed to in a publication, but who is not the author of the name according to the rules of the nomenclatural codes, because they did not contribute to the validating description of the name. In the <code>dwc:scientificNameAuthorship</code> these authors are indicated with 'ex', the ascribed author coming before the 'ex' and the author the name is attributed to after. Note that the 'ex' construction that is sometimes used with zoological names has got nothing to do with attribution or ascription, but is used to indicate a concept, much like we do here with 'sec.' or 'sensu' in taxon concept labels.</p></td>
		</tr>
		<tr>
			<td>GitHub issue</td>
			<td>https://github.com/tdwg/tcs2/issues/239</td>
		</tr>
	</tbody>
</table>

#### tcs:basionymAscribedAuthor

<table style="width:100%;">
	<tbody>
		<tr>
			<td>Identifier</td>
			<td>http://rs.tdwg.org/tcs/terms/basionymAscribedAuthor</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>http://www.w3.org/1999/02/22-rdf-syntax-ns#Property</td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Basionym author</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td><p>Ascribed author of the basionym of the name</p></td>
		</tr>
		<tr>
			<td>Usage</td>
			<td><p><code>basionymAscribedAuthor</code> is an IRI property. It can be a person or a list of persons.</p></td>
		</tr>
		<tr>
			<td></td>
			<td><b>required:</b> No — <b>repeatable:</b> Yes</td>
		</tr>
		<tr>
			<td>Comments</td>
			<td><p>'Ascribed author' is a person (or group of people) who a name is ascribed to in a publication, but who is not the author of the name according to the rules of the nomenclatural codes, because they did not contribute to the validating description of the name. In the <code>dwc:scientificNameAuthorship</code> these authors are indicated with 'ex', the ascribed author coming before the 'ex' and the author the name is attributed to after. Note that the 'ex' construction that is sometimes used with zoological names has got nothing to do with attribution or ascription, but is used to indicate a concept, much like we do here with 'sec.' or 'sensu' in taxon concept labels.</p></td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>

```turtle
<https://ipni.org/n/3007069-1> a tcs:TaxonName ;
    tcs:nameString "Senna artemisioides" ;
    dwc:scientificNameAuthorship "(Gaudich. ex DC.) Isely)" ;
    tcs:combinationAuthor <https://ipni.org/a/4317-1> ;
    tcs:combinationAuthorLiteral "Isely" ;
    tcs:basionymAuthor <https://ipni.org/a/16855-1> ;
    tcs:basionymAuthorLiteral "DC." ;
    tcs:basionymAscribedAuthor <https://ipni.org/a/3050-1> ;
    tcs:basionymAscribedAuthorLiteral "Gaudich." ;
    tcs:basionym <https://ipni.org/n/484142-1> .

<https://ipni.org/n/484142-1> a tcs:TaxonName ;
    tcs:nameString "Cassia artemisioides" ;
    dwc:scientificNameAuthorship "Gaudich. ex DC." ;
    tcs:combinationAuthor <https://ipni.org/a/16855-1> ;
    tcs:combinationAuthorLiteral "DC." ;
    tcs:combinationAscribedAuthor <https://ipni.org/a/3050-1> ;
    tcs:combinationAscribedAuthorLiteral "Gaudich." .

<https://ipni.org/a/4317-1> a foaf:Person ;
    foaf:givenName "Duane" ;
    foaf:surname "Isely" .

<https://ipni.org/a/16855-1> a foaf:Person ;
    foaf:givenName "Augustin Pyramus" ;
    foaf:surname "De Candolle" .

<https://ipni.org/a/3050-1> a foaf:Person ;
    foaf:givenName "Charles" ;
    foaf:surname "Gaudichaud-Beaupré" .
```


[&lsqb;TaxonName-basionymAscribedAuthor-example-1.ttl&rsqb;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonName-basionymAscribedAuthor-example-1.ttl)&nbsp;[&lsqb;TaxonName-basionymAscribedAuthor-example-1.jsonld&rsqb;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonName-basionymAscribedAuthor-example-1.jsonld)

</td>
		</tr>
		<tr>
			<td>GitHub issue</td>
			<td>https://github.com/tdwg/tcs2/issues/239</td>
		</tr>
	</tbody>
</table>

#### tcs:basionymAscribedAuthorLiteral

<table style="width:100%;">
	<tbody>
		<tr>
			<td>Identifier</td>
			<td>http://rs.tdwg.org/tcs/terms/basionymAscribedAuthorLiteral</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>http://www.w3.org/1999/02/22-rdf-syntax-ns#Property</td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Basionym author literal</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td><p>Ascribed author of the basionym of the name</p></td>
		</tr>
		<tr>
			<td>Usage</td>
			<td><p><code>basionymAscribedAuthorLiteral</code> is a Literal property.</p></td>
		</tr>
		<tr>
			<td></td>
			<td><b>required:</b> No — <b>repeatable:</b> No</td>
		</tr>
		<tr>
			<td>Comments</td>
			<td><p>'Ascribed author' is a person (or group of people) who a name is ascribed to in a publication, but who is not the author of the name according to the rules of the nomenclatural codes, because they did not contribute to the validating description of the name. In the <code>dwc:scientificNameAuthorship</code> these authors are indicated with 'ex', the ascribed author coming before the 'ex' and the author the name is attributed to after. Note that the 'ex' construction that is sometimes used with zoological names has got nothing to do with attribution or ascription, but is used to indicate a concept, much like we do here with 'sec.' or 'sensu' in taxon concept labels.</p></td>
		</tr>
		<tr>
			<td>GitHub issue</td>
			<td>https://github.com/tdwg/tcs2/issues/239</td>
		</tr>
	</tbody>
</table>

#### dwc:scientificNameAuthorship

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
			<td>Definition</td>
			<td><p>The authorship information for the <code>scientificName</code> formatted according to  the conventions of the applicable <code>nomenclaturalCode</code>.</p></td>
		</tr>
		<tr>
			<td>Usage</td>
			<td><p><code>scientificNameAuthorship</code> can be used if the <code>nameString</code> is a  scientific name.</p></td>
		</tr>
		<tr>
			<td></td>
			<td><b>required:</b> No — <b>repeatable:</b> No</td>
		</tr>
		<tr>
			<td>GitHub issue</td>
			<td>https://github.com/tdwg/tcs2/issues/24</td>
		</tr>
	</tbody>
</table>

#### dwc:namePublishedIn

<table style="width:100%;">
	<tbody>
		<tr>
			<td>Identifier</td>
			<td>http://rs.tdwg.org/dwc/terms/namePublishedIn</td>
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
			<td>Definition</td>
			<td><p>A reference for the publication in which the dwc:scientificName was  originally established under the rules of the associated  dwc:nomenclaturalCode.</p></td>
		</tr>
		<tr>
			<td></td>
			<td><b>required:</b> No — <b>repeatable:</b> No</td>
		</tr>
		<tr>
			<td>Comments</td>
			<td><p>This is the string equivalent of the TCS <code>namePublishedIn</code>. It can be used if one wants to give the protologue as a string, as in many botanical publications.</p></td>
		</tr>
		<tr>
			<td>GitHub issue</td>
			<td>https://github.com/tdwg/tcs2/issues/237</td>
		</tr>
	</tbody>
</table>

#### dwc:namePublishedInYear

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
			<td>Definition</td>
			<td><p>The four-digit year in which the <code>scientificName</code> was published.</p></td>
		</tr>
		<tr>
			<td>Usage</td>
			<td><p>This is the publication year for the present name combination, not the basionym should this be a new combination.</p></td>
		</tr>
		<tr>
			<td></td>
			<td><b>required:</b> No — <b>repeatable:</b> No</td>
		</tr>
		<tr>
			<td>GitHub issue</td>
			<td>https://github.com/tdwg/tcs2/issues/31</td>
		</tr>
	</tbody>
</table>

#### dwc:genericName

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
			<td>Definition</td>
			<td><p>The genus part of the <code>scientificName</code> without authorship.</p></td>
		</tr>
		<tr>
			<td>Usage</td>
			<td><p>This property should only be used for names below the rank of genus.</p></td>
		</tr>
		<tr>
			<td></td>
			<td><b>required:</b> No — <b>repeatable:</b> No</td>
		</tr>
		<tr>
			<td>GitHub issue</td>
			<td>https://github.com/tdwg/tcs2/issues/19</td>
		</tr>
	</tbody>
</table>

#### dwc:infragenericEpithet

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
			<td>Definition</td>
			<td><p>The infrageneric part of combinations at ranks above species but below  genus.</p></td>
		</tr>
		<tr>
			<td>Usage</td>
			<td><p>Names at ranks between species and genus, e.g. subgenera and sections, are  composed of two parts; the genus and the infrageneric epithet. This property  should therefore always be accompanied by the <code>genericName</code> property. If the  <code>infragenericEpithet</code> property is present, the <code>specificEpithet</code> and  <code>infraspecificEpithet</code> properties should not be present. </p></td>
		</tr>
		<tr>
			<td></td>
			<td><b>required:</b> No — <b>repeatable:</b> No</td>
		</tr>
		<tr>
			<td>GitHub issue</td>
			<td>https://github.com/tdwg/tcs2/issues/20</td>
		</tr>
	</tbody>
</table>

#### dwc:specificEpithet

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
			<td>Definition</td>
			<td><p>The name of the first or species epithet of the scientificName.</p></td>
		</tr>
		<tr>
			<td>Usage</td>
			<td><p>Names at ranks of species and below are composed of two or three words; the  genus name, the specific epithet and possibly an infraspecific epithet.  This property should therefore always be accompanied by the <code>genus</code> property.  If the <code>specificEpithet</code> property is present the <code>infragenericEpithet</code>  property should not be present.</p></td>
		</tr>
		<tr>
			<td></td>
			<td><b>required:</b> No — <b>repeatable:</b> No</td>
		</tr>
		<tr>
			<td>GitHub issue</td>
			<td>https://github.com/tdwg/tcs2/issues/21</td>
		</tr>
	</tbody>
</table>

#### dwc:infraspecificEpithet

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
			<td>Definition</td>
			<td><p>The name of the lowest or terminal infraspecific epithet of the  <code>scientificName</code>, excluding any rank designation.</p></td>
		</tr>
		<tr>
			<td>Usage</td>
			<td><p>Names at ranks below species are composed of three words; the genus name,  the specific epithet and an infraspecific epithet. This property should  therefore always be accompanied by the <code>genus</code> and <code>specificEpithet</code>  properties. If the <code>infraspecificEpithet</code> property is present the  <code>infragenericEpithet</code> property should not be present.</p></td>
		</tr>
		<tr>
			<td></td>
			<td><b>required:</b> No — <b>repeatable:</b> No</td>
		</tr>
		<tr>
			<td>GitHub issue</td>
			<td>https://github.com/tdwg/tcs2/issues/22</td>
		</tr>
	</tbody>
</table>

#### dwc:cultivarEpithet

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
			<td>Definition</td>
			<td><p>Part of the name of a cultivar, cultivar group or grex that follows the  scientific name.</p></td>
		</tr>
		<tr>
			<td>Usage</td>
			<td><p>The cultivar epithet follows a well-formed botanical name. Only include the string of the epithet. i.e. omit the single quotes around cultivar  names, the word 'Group' that denotes cultivar group, the + sign  used in chimeras and the 'gx' suffix in greges.</p></td>
		</tr>
		<tr>
			<td></td>
			<td><b>required:</b> No — <b>repeatable:</b> No</td>
		</tr>
		<tr>
			<td>GitHub issue</td>
			<td>https://github.com/tdwg/tcs2/issues/23</td>
		</tr>
	</tbody>
</table>

### Nomenclatural Type

#### tcs:NomenclaturalType

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
			<td><p>A Nomenclatural Type requires a <code>typifiedName</code>, <code>typeOfType</code> and either a <code>typeName</code> or <code>typeSpecimen</code>.</p></td>
		</tr>
		<tr>
			<td>Comments</td>
			<td><p>A nomenclatural type fixes the usage of a name to the taxonomic group that  contains the type. One or more Nomenclatural Types make up the typification  of a Taxon Name. In Darwin Core, NomenclaturalType can be used as object  with <code>dwciri:typeStatus</code>.</p></td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>

```turtle
# Examples from TCS 1
[] a tcs:NomenclaturalType ;
    tcs:typifiedName <https://ipni.org/n/50985479-1> ;
    tcs:typeOfType <http://rs.gbif.org/vocabulary/gbif/type_status/lectotype> ;
    tcs:typeName <https://ipni.org/n/333193-1> ;
    tcs:typePublishedIn [ a bibo:Article ;
    	  dcterms:bibliographicCitation """Copeland, H.F. (1943). A study, anatomical and 
                taxonomic, of the genera of Rhododendroideae. Am. Midl. Nat. 30: 533-625""" ] .

[] a tcs:NomenclaturalType ;
    tcs:typifiedName <https://ipni.org/n/333193-1> ;
    tcs:typeOfType <http://rs.gbif.org/vocabulary/gbif/type_status/lectotype> ;
    tcs:typeSpecimen [ a dwc:MaterialCitation ;
        dwc:verbatimLocality "Japan, Honshu, Nikko" ;
        dwc:recordedBy "Bisset" ;
        dwc:recordNumber "233" ;
        dwc:eventDate "1876-05-23" ;
        dwc:institutionCode "E" ] ;
    tcs:typePublishedIn [ a bibo:Article ; 
        dcterms:bibliographicCitation """Judd, W.S.; Kron, K.A. (1995). A revision of Rhododendron 
                VI. Subgenus Pentanthera (sections Sciadorhodon, Rhodora and Viscidula). Edinburgh 
                Journal of Botany 52: 1-54.""" ] .

# name used in TaxonName examples; more data there
<https://ipni.org/n/50985479-1> a tcs:TaxonName ;
    tcs:nameString "Rhododendron sect. Sciadorhodion" ;
    dwc:scientificNameAuthorship "Rehder & Wilson" .

<https://ipni.org/n/333193-1> a tcs:TaxonName ;
    tcs:nameString "Rhododendron quinquefolium" ;
    dwc:scientificNameAuthorship "Bisset & S.Moore" .
```


[&lsqb;NomenclaturalType-example-1.ttl&rsqb;](https://github.com/tdwg/tcs2/blob/master/examples/NomenclaturalType-example-1.ttl)&nbsp;[&lsqb;NomenclaturalType-example-1.jsonld&rsqb;](https://github.com/tdwg/tcs2/blob/master/examples/NomenclaturalType-example-1.jsonld)

</td>
		</tr>
		<tr>
			<td>GitHub issue</td>
			<td>https://github.com/tdwg/tcs2/issues/58</td>
		</tr>
	</tbody>
</table>

#### tcs:typifiedName

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
			<td>Definition</td>
			<td><p>The scientific name for which the specimen or other name is the type.</p></td>
		</tr>
		<tr>
			<td>Usage</td>
			<td><p><code>typifiedName</code> is a Taxon Name and is REQUIRED; a Nomenclatural Type can  typify only one Taxon Name.</p></td>
		</tr>
		<tr>
			<td></td>
			<td><b>required:</b> Yes — <b>repeatable:</b> No</td>
		</tr>
		<tr>
			<td>Comments</td>
			<td><p>The <code>typifiedName</code> property links the Nomenclatural Type back to the Taxon  Name. Also, when coming from the Preserved Specimen, the typified name is  the most important piece of information, because there is no point in  knowing what kind of type a specimen is without knowing for what name it  is the type. Therefore, <code>typifiedName</code> is a REQUIRED property.</p></td>
		</tr>
		<tr>
			<td>GitHub issue</td>
			<td>https://github.com/tdwg/tcs2/issues/59</td>
		</tr>
	</tbody>
</table>

#### tcs:typeOfType

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
			<td>Definition</td>
			<td><p>The kind of type this specimen is, e.g. holotype, isotype etc.</p></td>
		</tr>
		<tr>
			<td>Usage</td>
			<td><p><code>typeOfType</code> is an IRI term and SHOULD take its value from a controlled  vocabulary. A Nomenclatural Type can have only one <code>typeOfType</code></p></td>
		</tr>
		<tr>
			<td></td>
			<td><b>required:</b> Yes — <b>repeatable:</b> No</td>
		</tr>
		<tr>
			<td>Comments</td>
			<td><p>This is an IRI property. In the absence of a TDWG controlled vocabulary,  it is RECOMMENDED to use a value from the GBIF Nomenclatural Type Status  Vocabulary (https://rs.gbif.org/vocabulary/gbif/type_status_2021-01-18.xml).</p></td>
		</tr>
		<tr>
			<td>GitHub issue</td>
			<td>https://github.com/tdwg/tcs2/issues/60</td>
		</tr>
	</tbody>
</table>

#### tcs:typeName

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
			<td>Definition</td>
			<td><p>The name that is the type.</p></td>
		</tr>
		<tr>
			<td>Usage</td>
			<td><p><code>typeName</code> is a Taxon Name. A nomenclatural type can have only one  <code>typeName</code>.</p></td>
		</tr>
		<tr>
			<td></td>
			<td><b>required:</b> No — <b>repeatable:</b> No</td>
		</tr>
		<tr>
			<td>Comments</td>
			<td><p>Taxon names at ranks above species level can be typified by the name of a  lower taxon. Ultimately, by following the chain of type names, all names  resolve to a type species and thus a type specimen. </p></td>
		</tr>
		<tr>
			<td>GitHub issue</td>
			<td>https://github.com/tdwg/tcs2/issues/61</td>
		</tr>
	</tbody>
</table>

#### tcs:typeSpecimen

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
			<td>Definition</td>
			<td><p>The specimen that is the type.</p></td>
		</tr>
		<tr>
			<td>Usage</td>
			<td><p><code>typeSpecimen</code> takes an IRI – or object – that refers to a specimen. A  NomenclaturalType MUST NOT have more than one <code>typeSpecimen</code>.</p></td>
		</tr>
		<tr>
			<td></td>
			<td><b>required:</b> No — <b>repeatable:</b> No</td>
		</tr>
		<tr>
			<td>Comments</td>
			<td><p>Names at ranks of species and below are typified by a specimen. This property is mutually exclusive with <code>typeName</code>. This is an IRI property. One could use the Darwin Core Preserved Specimen or Material Citation. While a Taxon Name can have more than one type specimens, each of these type specimens requires its own Nomenclatural Type record, so a Nomenclatural Type can have only one <code>typeSpecimen</code>.</p></td>
		</tr>
		<tr>
			<td>GitHub issue</td>
			<td>https://github.com/tdwg/tcs2/issues/62</td>
		</tr>
	</tbody>
</table>

#### tcs:typePublishedIn

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
			<td>Definition</td>
			<td><p>Publication where the type was nominated</p></td>
		</tr>
		<tr>
			<td>Usage</td>
			<td><p><code>typePublishedIn</code> is an IRI term. A Nomenclatural Type can have at most one  <code>typePublishedIn</code>. </p></td>
		</tr>
		<tr>
			<td></td>
			<td><b>required:</b> No — <b>repeatable:</b> No</td>
		</tr>
		<tr>
			<td>Comments</td>
			<td><p><code>typePublishedIn</code> is relevant for lectotypes, neotypes, epitypes and  conserved types. For other kinds of type the publication where the type is  designated is the publication the name was published in.</p></td>
		</tr>
		<tr>
			<td>GitHub issue</td>
			<td>https://github.com/tdwg/tcs2/issues/63</td>
		</tr>
	</tbody>
</table>

<!-- footer -->