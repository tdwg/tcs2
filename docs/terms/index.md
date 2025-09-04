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
for sharing taxonomic and nomenclatural data. TCS provides Taxon Concept and
Taxon Name classes for information about taxon concepts and taxon names,
respectively, as well as a Taxon Concept Mapping class for taxon concept
alignments and a Nomenclatural Type class for information on typification of
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

The Introduction in this document is informative and the Namespace and Borrowed
terms sections are normative. Within the Vocabulary section the Identifier,
Type, Definition and Usage for terms are normative. For borrowed terms Usage is
normative only in the sense that it specifies how the term should be used within
TCS. All other parts, including Label, Comments and Examples, are informative.
The assignment of properties to classes is also informative, although most
properties can only reasonably be used in the class in which they are organised.
For the properties that can be used in more than one TCS class this has been
indicated in the comments.

### 1.2. RFC keywords

The key words “MUST”, “MUST NOT”, “REQUIRED”, “SHALL”, “SHALL NOT”, “SHOULD”, 
“SHOULD NOT”, “RECOMMENDED”, “MAY”, and “OPTIONAL” in this document are to be 
interpreted as described in BCP 14 [RFC 2119] and [RFC 8174] when, and only 
when, they appear in all capitals, as shown here.

### 1.3. Structure of TCS

TCS has four main classes, **Taxon Concept**, **Taxon Concept Mapping**,
**Taxon Name** and **Nomenclatural Type**.

The **Taxon Concept** class provides terms to share information about taxon
concepts and is the class everything else in TCS revolves around. We have
defined a **Taxon Concept** as:

> An **identifiable** taxonomic position that can be **aligned** to other such positions
> through TCS concept mapping relations

The change from the earlier 'a name plus a description of a taxon' was necessary
because TCS has to deal with a wider variety of taxon concepts and today's taxon
concepts do not necessarily have a formal scientific name or a description. In
order for a taxon concept to be identifiable, however, it needs to have some
kind of label and it has to have some sort of treatment, so the `taxonName` and
`accordingTo` properties on the `TaxonConcept` are required.

The **Taxon Concept Mapping** class is almost identical in structure to the Darwin
Core `ResourceRelationship` class. As a taxon concept mapping is a very specific
type of resource relationship and because Darwin Core does not define IRI
properties for `dwc:ResourceRelationship`, TCS defines its own class. The
`subjectTaxonConcept`, `mappingRelation` and `objectTaxonConcept` are required
on a `TaxonConceptMapping`. The value of `mappingRelation` has to be one of the
mapping properties from the `TaxonConcept` class.

The **Taxon Name** class encapsulates all information about taxon names. Only the
`nameString` property is required. Currently, TCS only has the one class
that can be used for all types of names, including scientific names and
vernacular names, but it is envisaged that in future TCS will also have classes
for specific categories of names, e.g., 'ScientificName' and 'VernacularName'.
The use of the **Taxon Name** class is not currently required in TCS: it can be
replaced by a [SKOS-XL Label](https://www.w3.org/TR/skos-reference/skos-xl.html)
or [GBIF VernacularName](http://rs.gbif.org/terms/1.0/VernacularName) (or any
other label object) if considered more appropriate.

The **Nomenclatural Type** class can be used to share information about
nomenclatural types of names. It also shows similarity to the Darwin Core
`ResourceRelationship` class in the sense that a nomenclatural type is a
resource relationship between a `tcs:TaxonName` and either another
`tcs:TaxonName` or a Specimen (for which we use the Darwin Core
`PreservedSpecimen` or `MaterialCitation` in the examples). The `typifiedName`,
`typeOfType` and either the `typeSpecimen` or `typeName` properties are
required.

In contrast to Darwin Core, TCS does not define 'ID' and 'Remarks' properties on
its classes. In accordance with the Darwin Core RDF Guide (Darwin Core and
RDF/OWL Task Groups 2015
[\[darwin_core_and_rdfowl_task_groups_darwin_2015\]](../bibliography/#darwin_core_and_rdfowl_task_groups_darwin_2015)),
instances of TCS classes SHOULD have a `rdf:id` and MAY have a `rdfs:comment`.
Also, other terms from general-purpose standards like RDFS and Dublin Core MAY
be used—and have been freely used in the examples—when they add value to the
data. These terms have not been borrowed by TCS, as they have no special meaning
in TCS and are used with TCS the same way as everywhere else.

Information on **synonymy** can be shared using the `synonym` property of the
Taxon Concept and the `basionym` and `replacedName` properties of the TaxonName.
TCS does not use the terms 'homotypic synonym' and 'heterotypic synonym' because
these terms are rather strictly defined in the nomenclatural codes, which makes
them less useful for data exchange, but `synonym` can be used for heterotypic
synonyms and `basionym` and `replacedName` for homotypic synonyms. The `synonym`
property can be used for all synonyms and it is up to data providers or
application profiles whether or not synonyms are split into homotypic and
heterotypic synonyms.

The **mapping properties** in the Taxon Concept class, `isCongruentWith`,
`includes`, `isIncludedIn`, `partiallyOverlaps`, `intersects` and
`isDisjointFrom` can be used to align taxon concepts. These properties are
equivalent to topological properties in spatial analysis and can be used in
reasoning. Taxon concept mappings are currently not used very often in taxonomic
treatments but, besides being more expressive and more generally applicable than
nomenclatural relationships, they have the advantage that they can be made by
third parties, so they can be used to add information that is not already
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

## 4. Index of terms

**Taxon Concept**

[tcs:TaxonConcept](#tcs_taxonconcept) |
[tcs:accordingTo](#tcs_accordingto) |
[tcs:taxonName](#tcs_taxonname) |
[tcs:synonym](#tcs_synonym) |
[tcs:vernacularName](#tcs_vernacularname) |
[tcs:taxonRank](#tcs_taxonrank) |
[tcs:parentTaxonConcept](#tcs_parenttaxonconcept) |
[tcs:childTaxonConcept](#tcs_childtaxonconcept) |
[tcs:isCongruentWith](#tcs_iscongruentwith) |
[tcs:includes](#tcs_includes) |
[tcs:isIncludedIn](#tcs_isincludedin) |
[tcs:partiallyOverlaps](#tcs_partiallyoverlaps) |
[tcs:isDisjointFrom](#tcs_isdisjointfrom) |
[tcs:intersects](#tcs_intersects) |
[dwc:verbatimTaxonRank](#dwc_verbatimtaxonrank) |
[dcterms:title](#dcterms_title)

**Taxon Concept Mapping**

[tcs:TaxonConceptMapping](#tcs_taxonconceptmapping) |
[tcs:mappingAccordingTo](#tcs_mappingaccordingto) |
[tcs:mappingRelation](#tcs_mappingrelation) |
[tcs:subjectTaxonConcept](#tcs_subjecttaxonconcept) |
[tcs:objectTaxonConcept](#tcs_objecttaxonconcept)

**Taxon Name**

[tcs:TaxonName](#tcs_taxonname) |
[tcs:nameString](#tcs_namestring) |
[tcs:namePublishedIn](#tcs_namepublishedin) |
[tcs:microreference](#tcs_microreference) |
[tcs:nomenclaturalCode](#tcs_nomenclaturalcode) |
[tcs:nomenclaturalStatus](#tcs_nomenclaturalstatus) |
[tcs:typification](#tcs_typification) |
[tcs:typificationLiteral](#tcs_typificationliteral) |
[tcs:basionym](#tcs_basionym) |
[tcs:replacedName](#tcs_replacedname) |
[tcs:basedOn](#tcs_basedon) |
[tcs:laterHomonymOf](#tcs_laterhomonymof) |
[tcs:conservedAgainst](#tcs_conservedagainst) |
[tcs:combinationAuthor](#tcs_combinationauthor) |
[tcs:combinationAuthorLiteral](#tcs_combinationauthorliteral) |
[tcs:basionymAuthor](#tcs_basionymauthor) |
[tcs:basionymAuthorLiteral](#tcs_basionymauthorliteral) |
[tcs:combinationAscribedAuthor](#tcs_combinationascribedauthor) |
[tcs:combinationAscribedAuthorLiteral](#tcs_combinationascribedauthorliteral) |
[tcs:basionymAscribedAuthor](#tcs_basionymascribedauthor) |
[tcs:basionymAscribedAuthorLiteral](#tcs_basionymascribedauthorliteral) |
[dwc:scientificNameAuthorship](#dwc_scientificnameauthorship) |
[dwc:namePublishedIn](#dwc_namepublishedin) |
[dwc:namePublishedInYear](#dwc_namepublishedinyear) |
[dwc:genericName](#dwc_genericname) |
[dwc:infragenericEpithet](#dwc_infragenericepithet) |
[dwc:specificEpithet](#dwc_specificepithet) |
[dwc:infraspecificEpithet](#dwc_infraspecificepithet) |
[dwc:cultivarEpithet](#dwc_cultivarepithet)

**Nomenclatural Type**

[tcs:NomenclaturalType](#tcs_nomenclaturaltype) |
[tcs:typifiedName](#tcs_typifiedname) |
[tcs:typeOfType](#tcs_typeoftype) |
[tcs:typeName](#tcs_typename) |
[tcs:typeSpecimen](#tcs_typespecimen) |
[tcs:typePublishedIn](#tcs_typepublishedin)

## 5. Vocabulary

### 5.1. Taxon Concept

<table>

    <thead>
        <th colspan="2"><a id="tcs_taxonconcept"></a>Term Name: tcs:TaxonConcept</th>
    </thead>
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
			<td><ul>
<li><a href="../examples/TaxonConcept-example-1.html">TaxonConcept-example-1</a></li>

<li><a href="../examples/TaxonConcept-example-2.html">TaxonConcept-example-2</a></li>

<li><a href="../examples/TaxonConcept-example-3.html">TaxonConcept-example-3</a></li>

<li><a href="../examples/TaxonConcept-example-4.html">TaxonConcept-example-4</a></li>

<li><a href="../examples/TaxonConcept-example-5.html">TaxonConcept-example-5</a></li>

<li><a href="../examples/TaxonConcept-example-6.html">TaxonConcept-example-6</a></li>

<li><a href="../examples/TaxonConcept-example-7.html">TaxonConcept-example-7</a></li>

</ul>
</td>
		</tr>
	</tbody>
</table>

<table>

    <thead>
        <th colspan="2"><a id="tcs_accordingto"></a>Term Name: tcs:accordingTo</th>
    </thead>
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
			<td><b>Required:</b> Yes — <b>Repeatable:</b> No</td>
		</tr>
		<tr>
			<td>Comments</td>
			<td><p>Every Taxon Concept is in some sort of treatment and this treatment  provides important context without which we do not know what a taxon name  really means and therefore the <code>accordingTo</code> property is REQUIRED for a TCS  Taxon Concept. In TCS 2, <code>accordingTo</code> has to be a reference to some sort  of resource rather than just a person's name. However, TCS is lenient about  the nature of this resource and, apart from references to bibliographic  resources, references to personal communications and determinations are  also acceptable, if there is value in supplying taxon concepts from such  communications as Taxon Concepts.</p>
<p>The value of <code>accordingTo</code> has to be an object or IRI. This object can contain as little as a bibliographic reference but it is more useful to provide it in a format that can be understood by reference managers such as Zotero or Mendeley.</p></td>
		</tr>
		<tr>
			<td>Examples</td>
			<td><ul>
<li><a href="../examples/TaxonConcept-accordingTo-example-1.html">TaxonConcept-accordingTo-example-1</a></li>

<li><a href="../examples/TaxonConcept-accordingTo-example-2.html">TaxonConcept-accordingTo-example-2</a></li>

<li><a href="../examples/TaxonConcept-accordingTo-example-3.html">TaxonConcept-accordingTo-example-3</a></li>

</ul>
</td>
		</tr>
	</tbody>
</table>

<table>

    <thead>
        <th colspan="2"><a id="tcs_taxonname"></a>Term Name: tcs:taxonName</th>
    </thead>
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
			<td>Definition</td>
			<td><p>The accepted name for the taxonomic group.</p></td>
		</tr>
		<tr>
			<td>Usage</td>
			<td><p><code>taxonName</code> is an IRI term and is REQUIRED on a TCS Taxon Concept. A Taxon Concept MUST NOT have more than one <code>taxonName</code>.</p></td>
		</tr>
		<tr>
			<td></td>
			<td><b>Required:</b> Yes — <b>Repeatable:</b> No</td>
		</tr>
		<tr>
			<td>Comments</td>
			<td><p>The <code>taxonName</code> can be anything from a well-formed scientific name to an  informal name, vernacular name, indigenous knowledge label, or even a label  containing numbers and/or special symbols, such as are often used for OTUs. </p>
<p>The object of <code>taxonName</code> is an object or IRI, so that it can be reused in  other Taxon Concepts. TCS has got the Taxon Name class, which can be used  for any type of name, but people are free to use alternatives, e.g.  <code>skosxl:Label</code>, if they want to restrict the use of the Taxon Name class to  scientific names only.</p></td>
		</tr>
	</tbody>
</table>

<table>

    <thead>
        <th colspan="2"><a id="tcs_synonym"></a>Term Name: tcs:synonym</th>
    </thead>
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
			<td><b>Required:</b> No — <b>Repeatable:</b> Yes</td>
		</tr>
		<tr>
			<td>Comments</td>
			<td><p>A synonym is an alternative label for a taxon, so <code>synonym</code>, like <code>taxonName</code>, is a relation between a <code>TaxonConcept</code> and a <code>TaxonName</code>, not a relationship between different taxonomic entities.</p>
<p>The terms 'heterotypic synonym' and 'homotypic synonym' from the nomenclatural codes ('subjective synonym' and 'objective synonym', respectively, in the Zoological Code) are, in the context of Taxon Concepts and Taxon Names, best understood as synonyms (relations between Taxon Concepts and Taxon Names) and combinations (relations between Taxon Names), respectively. In TCS, combinations are dealt with using properties of the <code>TaxonName</code> class, <em>e.g.</em>, <code>basionym</code> and <code>replacedName</code> (note that 'combination' is used here in a broader sense than what the term actually means). This has the advantage that people do not need to separate heterotypic and homotypic synonyms, or generally deal with nomenclature, which adds a degree of complexity that not all systems need or want. Avoiding terms that are strictly defined in the nomenclatural codes also has the advantage that the term can, in principle, be applied to things that cannot be heterotypic or homotypic synonyms, e.g., to names that are not validly published under the relevant code, and avoids inappropriate use of the terms defined in the nomenclatural codes.</p></td>
		</tr>
		<tr>
			<td>Examples</td>
			<td><ul>
<li><a href="../examples/TaxonConcept-synonym-example-1.html">TaxonConcept-synonym-example-1</a></li>

<li><a href="../examples/TaxonConcept-synonym-example-2.html">TaxonConcept-synonym-example-2</a></li>

<li><a href="../examples/TaxonConcept-synonym-example-3.html">TaxonConcept-synonym-example-3</a></li>

</ul>
</td>
		</tr>
	</tbody>
</table>

<table>

    <thead>
        <th colspan="2"><a id="tcs_vernacularname"></a>Term Name: tcs:vernacularName</th>
    </thead>
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
			<td><b>Required:</b> No — <b>Repeatable:</b> Yes</td>
		</tr>
		<tr>
			<td>Comments</td>
			<td><p>The <code>vernacularName</code> property can be used when a vernacular name is used alongside a scientific name, which is the <code>taxonName</code>. If a vernacular name is the only name, the <code>taxonName</code> property SHOULD be used. The object of the <code>vernacularName</code> property can be a Taxon Name, but another label object, such as the GBIF <a href="https://rs.gbif.org/extension/gbif/1.0/vernacularname.xml">Vernacular Name</a>, might be preferrable, especially if there can be multiple vernacular names for a concept.</p></td>
		</tr>
		<tr>
			<td>Examples</td>
			<td><ul>
<li><a href="../examples/TaxonConcept-vernacularName-example-1.html">TaxonConcept-vernacularName-example-1</a></li>

<li><a href="../examples/TaxonConcept-vernacularName-example-2.html">TaxonConcept-vernacularName-example-2</a></li>

<li><a href="../examples/TaxonConcept-vernacularName-example-3.html">TaxonConcept-vernacularName-example-3</a></li>

<li><a href="../examples/TaxonConcept-vernacularName-example-4.html">TaxonConcept-vernacularName-example-4</a></li>

</ul>
</td>
		</tr>
	</tbody>
</table>

<table>

    <thead>
        <th colspan="2"><a id="tcs_taxonrank"></a>Term Name: tcs:taxonRank</th>
    </thead>
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
			<td>Taxon Rank</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td><p>The rank at which a taxon is classified.</p></td>
		</tr>
		<tr>
			<td>Usage</td>
			<td><p><code>taxonRank</code> is an IRI property; a Taxon Concept or Taxon Name MUST NOT have more than one <code>taxonRank</code>.</p></td>
		</tr>
		<tr>
			<td></td>
			<td><b>Required:</b> No — <b>Repeatable:</b> No</td>
		</tr>
		<tr>
			<td>Comments</td>
			<td><p>This term is the IRI equivalent of the Darwin Core <code>taxonRank</code>. This property takes an object or IRI and it is RECOMMENDED to use a value from an existing controlled vocabulary. While there is no TDWG vocabulary yet, the GBIF Taxonomic Rank Vocabulary (<a href="https://rs.gbif.org/vocabulary/gbif/rank_2015-04-24.xml">https://rs.gbif.org/vocabulary/gbif/rank_2015-04-24.xml</a>) is RECOMMENDED.</p>
<p>A taxon name takes its rank from the taxon it is applied to, so this property can also be used on a (stand-alone) <code>TaxonName</code> object.</p></td>
		</tr>
	</tbody>
</table>

<table>

    <thead>
        <th colspan="2"><a id="tcs_parenttaxonconcept"></a>Term Name: tcs:parentTaxonConcept</th>
    </thead>
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
			<td>Parent Taxon Concept</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td><p>The immediately next higher taxon in a hierarchical classification.</p></td>
		</tr>
		<tr>
			<td>Usage</td>
			<td><p><code>parentTaxonConcept</code> is another Taxon Concept; a Taxon Concept can have only one <code>parentTaxonConcept</code>.</p></td>
		</tr>
		<tr>
			<td></td>
			<td><b>Required:</b> No — <b>Repeatable:</b> No</td>
		</tr>
		<tr>
			<td>Comments</td>
			<td><p>This is the parent as indicated in the <code>accordingTo</code> reference, rather than a third-party classification. The <code>accordingTo</code> of the parent will generally, but not necessarily, be the same as that of the child. </p></td>
		</tr>
		<tr>
			<td>Examples</td>
			<td><ul>
<li><a href="../examples/TaxonConcept-parent-example-1.html">TaxonConcept-parent-example-1</a></li>

</ul>
</td>
		</tr>
	</tbody>
</table>

<table>

    <thead>
        <th colspan="2"><a id="tcs_childtaxonconcept"></a>Term Name: tcs:childTaxonConcept</th>
    </thead>
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
			<td>Child Taxon Concept</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td><p>A direct subordinate in a hierarchical classification.</p></td>
		</tr>
		<tr>
			<td>Usage</td>
			<td><p><code>childTaxonConcept</code> is another Taxon Concept; a Taxon Concept can have more than one <code>childTaxonConcept</code>.</p></td>
		</tr>
		<tr>
			<td></td>
			<td><b>Required:</b> No — <b>Repeatable:</b> Yes</td>
		</tr>
		<tr>
			<td>Comments</td>
			<td><p>This is a child as indicated in the <code>accordingTo</code> reference, rather than a third-party classification. The <code>accordingTo</code> of the child will generally, but not necessarily, be the same as that of the parent.</p></td>
		</tr>
		<tr>
			<td>Examples</td>
			<td><ul>
<li><a href="../examples/TaxonConcept-child-example-1.html">TaxonConcept-child-example-1</a></li>

</ul>
</td>
		</tr>
	</tbody>
</table>

<table>

    <thead>
        <th colspan="2"><a id="tcs_iscongruentwith"></a>Term Name: tcs:isCongruentWith</th>
    </thead>
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
			<td><b>Required:</b> No — <b>Repeatable:</b> Yes</td>
		</tr>
		<tr>
			<td>Comments</td>
			<td><p>The <code>isCongruentWith</code> relation is symmetrical, so if A <code>isCongruentWith</code> B then B <code>isCongruentWith</code> A, as well as transitive, so if A <code>isCongruentWith</code> B and B <code>isCongruentWith</code> C it follows that A <code>isCongruentWith</code> C. This relation can also be written as the formula <strong>A &cong; B</strong> or <strong>A == B</strong>.</p>
<p><img alt="" src="../media/mapping-relation-isCongruentWith.drawio.svg" /></p></td>
		</tr>
		<tr>
			<td>Examples</td>
			<td><ul>
<li><a href="../examples/TaxonConcept-isCongruentWith-example-1.html">TaxonConcept-isCongruentWith-example-1</a></li>

<li><a href="../examples/TaxonConceptMapping-isCongruentWith-example-2.html">TaxonConceptMapping-isCongruentWith-example-2</a></li>

<li><a href="../examples/TaxonConcept-isCongruentWith-example-3.html">TaxonConcept-isCongruentWith-example-3</a></li>

<li><a href="../examples/TaxonConceptMapping-isCongruentWith-example-1.html">TaxonConceptMapping-isCongruentWith-example-1</a></li>

</ul>
</td>
		</tr>
	</tbody>
</table>

<table>

    <thead>
        <th colspan="2"><a id="tcs_includes"></a>Term Name: tcs:includes</th>
    </thead>
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
			<td><b>Required:</b> No — <b>Repeatable:</b> Yes</td>
		</tr>
		<tr>
			<td>Comments</td>
			<td><p>The <code>includes</code> relation is not symmetric, its inverse relation being <code>isIncludedIn</code>, so if A <code>includes</code> B then B <code>isIncludedIn</code> A. The <code>includes</code> relation  is transitive, so if A <code>includes</code> B and B <code>includes</code> C it follows that A <code>includes</code> C. This relation can also be written as the formula <strong>A &gt; B</strong>.</p>
<p><img alt="" src="../media/mapping-relation-includes.drawio.svg" /></p></td>
		</tr>
		<tr>
			<td>Examples</td>
			<td><ul>
<li><a href="../examples/TaxonConcept-includes-example-1.html">TaxonConcept-includes-example-1</a></li>

<li><a href="../examples/TaxonConceptMapping-includes-example-2.html">TaxonConceptMapping-includes-example-2</a></li>

<li><a href="../examples/TaxonConceptMapping-includes-example-1.html">TaxonConceptMapping-includes-example-1</a></li>

</ul>
</td>
		</tr>
	</tbody>
</table>

<table>

    <thead>
        <th colspan="2"><a id="tcs_isincludedin"></a>Term Name: tcs:isIncludedIn</th>
    </thead>
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
			<td>Is Included In</td>
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
			<td><b>Required:</b> No — <b>Repeatable:</b> Yes</td>
		</tr>
		<tr>
			<td>Comments</td>
			<td><p>The <code>isIncludedIn</code> relation is not symmetric, its inverse relation being <code>includes</code>, so if A <code>isIncludedIn</code> B then B <code>includes</code> A. The <code>isIncludedIn</code> relation  is transitive, so if A <code>isIncludedIn</code> B and B <code>isIncludedIn</code> C it follows that A <code>isIncludedIn</code> C. This relation can also be written as the formula <strong>A &lt; B</strong>.</p>
<p><img alt="" src="../media/mapping-relation-isIncludedIn.drawio.svg" /></p></td>
		</tr>
		<tr>
			<td>Examples</td>
			<td><ul>
<li><a href="../examples/TaxonConcept-isIncludedIn-example-1.html">TaxonConcept-isIncludedIn-example-1</a></li>

<li><a href="../examples/TaxonConceptMapping-isIncludedIn-example-2.html">TaxonConceptMapping-isIncludedIn-example-2</a></li>

<li><a href="../examples/TaxonConceptMapping-isIncludedIn-example-1.html">TaxonConceptMapping-isIncludedIn-example-1</a></li>

</ul>
</td>
		</tr>
	</tbody>
</table>

<table>

    <thead>
        <th colspan="2"><a id="tcs_partiallyoverlaps"></a>Term Name: tcs:partiallyOverlaps</th>
    </thead>
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
			<td>Partially Overlaps</td>
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
			<td><b>Required:</b> No — <b>Repeatable:</b> Yes</td>
		</tr>
		<tr>
			<td>Comments</td>
			<td><p>The <code>partiallyOverlaps</code> relation is symmetrical, so if A <code>partiallyOverlaps</code> B then B <code>partiallyOverlaps</code> A, but not transitive, so, if A <code>partiallyOverlaps</code> B and B <code>partiallyOverlaps</code> C, it does not follow that A <code>partiallyOverlaps</code> C. This relation can also be written as the formula <strong>A &gt;&lt; B</strong>.</p>
<p><img alt="" src="../media/mapping-relation-partiallyOverlaps.drawio.svg" /></p></td>
		</tr>
		<tr>
			<td>Examples</td>
			<td><ul>
<li><a href="../examples/TaxonConcept-partiallyOverlaps-example-1.html">TaxonConcept-partiallyOverlaps-example-1</a></li>

<li><a href="../examples/TaxonConceptMapping-partiallyOverlaps-example-2.html">TaxonConceptMapping-partiallyOverlaps-example-2</a></li>

<li><a href="../examples/TaxonConceptMapping-partiallyOverlaps-example-1.html">TaxonConceptMapping-partiallyOverlaps-example-1</a></li>

</ul>
</td>
		</tr>
	</tbody>
</table>

<table>

    <thead>
        <th colspan="2"><a id="tcs_isdisjointfrom"></a>Term Name: tcs:isDisjointFrom</th>
    </thead>
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
			<td>Is Disjoint From</td>
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
			<td><b>Required:</b> No — <b>Repeatable:</b> Yes</td>
		</tr>
		<tr>
			<td>Comments</td>
			<td><p>The <code>isDisjointFrom</code>  relation is symmetrical, so if A <code>isDisjointFrom</code> B then B <code>isDisjointFrom</code> A, but not transitive, so, if A <code>isDisjointFrom</code> B and B <code>isDisjointFrom</code> C, it does not follow that A <code>isDisjointFrom</code> C. This relation can also be written as the formula <strong>A | B</strong>.</p>
<p><img alt="" src="../media/mapping-relation-isDisjointFrom.drawio.svg" /></p></td>
		</tr>
		<tr>
			<td>Examples</td>
			<td><ul>
<li><a href="../examples/TaxonConcept-isDisjointFrom-example-1.html">TaxonConcept-isDisjointFrom-example-1</a></li>

<li><a href="../examples/TaxonConceptMapping-isDisjointFrom-example-2.html">TaxonConceptMapping-isDisjointFrom-example-2</a></li>

<li><a href="../examples/TaxonConceptMapping-isDisjointFrom-example-1.html">TaxonConceptMapping-isDisjointFrom-example-1</a></li>

</ul>
</td>
		</tr>
	</tbody>
</table>

<table>

    <thead>
        <th colspan="2"><a id="tcs_intersects"></a>Term Name: tcs:intersects</th>
    </thead>
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
			<td><b>Required:</b> No — <b>Repeatable:</b> Yes</td>
		</tr>
		<tr>
			<td>Comments</td>
			<td><p><code>intersects</code> is the opposite of <code>isDisjointFrom</code> and the union of <code>isCongruentWith</code>, <code>includes</code>, <code>isIncludedIn</code> and <code>partiallyOverlaps</code>, meaning it can be any of these relations. This relation can be used when the more precise nature of the relationship is not known. Quasi-nomenclatural statements like 'pro parte synonym', 'partial synonym' and 'misapplication', are Taxon Concept Mappings, no matter how imperfect, and, in TCS, are best dealt with using the <code>intersects</code> relation. In fact, all 'traditional synonymy' relationships, cf. Berendsohn &amp; al. (2000 <a href="../bibliography/#berendsohn_berlin_2003">[berendsohn_berlin_2003]</a>), can be accommodated using <code>intersects</code>. Also, citations of references in treatments are, in the context of TCS, best accommodated using the <code>intersects</code> relation.</p></td>
		</tr>
		<tr>
			<td>Examples</td>
			<td><ul>
<li><a href="../examples/TaxonConcept-intersects-example-1.html">TaxonConcept-intersects-example-1</a></li>

<li><a href="../examples/TaxonConcept-intersects-example-2.html">TaxonConcept-intersects-example-2</a></li>

<li><a href="../examples/TaxonConceptMapping-intersects-example-1.html">TaxonConceptMapping-intersects-example-1</a></li>

<li><a href="../examples/TaxonConcept-intersects-example-3.html">TaxonConcept-intersects-example-3</a></li>

</ul>
</td>
		</tr>
	</tbody>
</table>

<table>

    <thead>
        <th colspan="2"><a id="dwc_verbatimtaxonrank"></a>Term Name: dwc:verbatimTaxonRank</th>
    </thead>
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
			<td>Verbatim Taxon Rank</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td><p>The taxonomic rank of the most specific name in the <code>dwc:scientificName</code> as it appears in the original record.</p></td>
		</tr>
		<tr>
			<td></td>
			<td><b>Required:</b> No — <b>Repeatable:</b> No</td>
		</tr>
		<tr>
			<td>Comments</td>
			<td><p>This term may be used for taxonomic rank designations that are not in the controlled vocabulary that is used. Implementations can decide for themselves if it makes more sense to use this term on a Taxon Concept object or a Taxon Name object, or both.</p></td>
		</tr>
	</tbody>
</table>

<table>

    <thead>
        <th colspan="2"><a id="dcterms_title"></a>Term Name: dcterms:title</th>
    </thead>
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
			<td>Taxon Concept Label</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td><p>A name given to the resource.</p></td>
		</tr>
		<tr>
			<td></td>
			<td><b>Required:</b> No — <b>Repeatable:</b> No</td>
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
	</tbody>
</table>

### 5.2. Taxon Concept Mapping

<table>

    <thead>
        <th colspan="2"><a id="tcs_taxonconceptmapping"></a>Term Name: tcs:TaxonConceptMapping</th>
    </thead>
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
			<td>Taxon Concept Mapping</td>
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
			<td><ul>
<li><a href="../examples/TaxonConceptMapping-isCongruentWith-example-1.html">TaxonConceptMapping-isCongruentWith-example-1</a></li>

<li><a href="../examples/TaxonConceptMapping-isCongruentWith-example-2.html">TaxonConceptMapping-isCongruentWith-example-2</a></li>

<li><a href="../examples/TaxonConceptMapping-includes-example-1.html">TaxonConceptMapping-includes-example-1</a></li>

<li><a href="../examples/TaxonConceptMapping-includes-example-2.html">TaxonConceptMapping-includes-example-2</a></li>

<li><a href="../examples/TaxonConceptMapping-isIncludedIn-example-1.html">TaxonConceptMapping-isIncludedIn-example-1</a></li>

<li><a href="../examples/TaxonConceptMapping-isIncludedIn-example-2.html">TaxonConceptMapping-isIncludedIn-example-2</a></li>

<li><a href="../examples/TaxonConceptMapping-partiallyOverlaps-example-1.html">TaxonConceptMapping-partiallyOverlaps-example-1</a></li>

<li><a href="../examples/TaxonConceptMapping-partiallyOverlaps-example-2.html">TaxonConceptMapping-partiallyOverlaps-example-2</a></li>

<li><a href="../examples/TaxonConceptMapping-isDisjointFrom-example-1.html">TaxonConceptMapping-isDisjointFrom-example-1</a></li>

<li><a href="../examples/TaxonConceptMapping-isDisjointFrom-example-2.html">TaxonConceptMapping-isDisjointFrom-example-2</a></li>

<li><a href="../examples/TaxonConceptMapping-intersects-example-1.html">TaxonConceptMapping-intersects-example-1</a></li>

<li><a href="../examples/TaxonConceptMapping-intersects-example-2.html">TaxonConceptMapping-intersects-example-2</a></li>

</ul>
</td>
		</tr>
	</tbody>
</table>

<table>

    <thead>
        <th colspan="2"><a id="tcs_mappingaccordingto"></a>Term Name: tcs:mappingAccordingTo</th>
    </thead>
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
			<td>Mapping According To</td>
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
			<td><b>Required:</b> No — <b>Repeatable:</b> No</td>
		</tr>
	</tbody>
</table>

<table>

    <thead>
        <th colspan="2"><a id="tcs_mappingrelation"></a>Term Name: tcs:mappingRelation</th>
    </thead>
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
			<td>Mapping Relation</td>
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
			<td><b>Required:</b> Yes — <b>Repeatable:</b> No</td>
		</tr>
	</tbody>
</table>

<table>

    <thead>
        <th colspan="2"><a id="tcs_subjecttaxonconcept"></a>Term Name: tcs:subjectTaxonConcept</th>
    </thead>
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
			<td><b>Required:</b> Yes — <b>Repeatable:</b> No</td>
		</tr>
		<tr>
			<td>Comments</td>
			<td><p>This is the Taxon Concept at the left-hand side of the statement.</p></td>
		</tr>
	</tbody>
</table>

<table>

    <thead>
        <th colspan="2"><a id="tcs_objecttaxonconcept"></a>Term Name: tcs:objectTaxonConcept</th>
    </thead>
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
			<td><b>Required:</b> Yes — <b>Repeatable:</b> No</td>
		</tr>
		<tr>
			<td>Comments</td>
			<td><p>This is the Taxon Concept at the right-hand side of the statement.</p></td>
		</tr>
	</tbody>
</table>

### 5.3. Taxon Name

<table>

    <thead>
        <th colspan="2"><a id="tcs_taxonname"></a>Term Name: tcs:TaxonName</th>
    </thead>
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
			<td><ul>
<li><a href="../examples/TaxonName-example-1.html">TaxonName-example-1</a></li>

<li><a href="../examples/TaxonName-example-2.html">TaxonName-example-2</a></li>

<li><a href="../examples/TaxonName-example-3.html">TaxonName-example-3</a></li>

<li><a href="../examples/TaxonName-example-4.html">TaxonName-example-4</a></li>

</ul>
</td>
		</tr>
	</tbody>
</table>

<table>

    <thead>
        <th colspan="2"><a id="tcs_namestring"></a>Term Name: tcs:nameString</th>
    </thead>
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
			<td>Name String</td>
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
			<td><b>Required:</b> Yes — <b>Repeatable:</b> No</td>
		</tr>
		<tr>
			<td>Comments</td>
			<td><p>The <code>nameString</code> property differs from the <code>scientificName</code> property  in Darwin Core in that all kinds of names are allowed. Also, in the case of  scientific names, contrary to the <code>dwc:scientificName</code>, <code>nameString</code>  does not include the authorship. In botanical names, it does include the  rank prefixes for infrageneric and infraspecific epithets as they are  considered part of the name.</p></td>
		</tr>
	</tbody>
</table>

<table>

    <thead>
        <th colspan="2"><a id="tcs_namepublishedin"></a>Term Name: tcs:namePublishedIn</th>
    </thead>
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
			<td><b>Required:</b> No — <b>Repeatable:</b> No</td>
		</tr>
		<tr>
			<td>Comments</td>
			<td><p>In botany, this would be the protologue. This is the IRI counterpart of  the Darwin Core <code>namePublishedIn</code>, which TCS borrows.</p></td>
		</tr>
	</tbody>
</table>

<table>

    <thead>
        <th colspan="2"><a id="tcs_microreference"></a>Term Name: tcs:microreference</th>
    </thead>
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
			<td><b>Required:</b> No — <b>Repeatable:</b> No</td>
		</tr>
		<tr>
			<td>Comments</td>
			<td><p>In taxonomic works it is convention to cite the exact location in a work  where a new name is published. The <code>microreference</code> property lets one do  that on the Taxon Name object, so that the <code>namePublishedIn</code> reference can  be reused.</p></td>
		</tr>
	</tbody>
</table>

<table>

    <thead>
        <th colspan="2"><a id="tcs_nomenclaturalcode"></a>Term Name: tcs:nomenclaturalCode</th>
    </thead>
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
			<td><b>Required:</b> No — <b>Repeatable:</b> No</td>
		</tr>
		<tr>
			<td>Comments</td>
			<td><p>This is the IRI equivalent of the Darwin Core <code>nomenclaturalCode</code>. In the absence of a TDWG vocabulary, it is RECOMMENDED to use a value from the GBIF Nomenclatural Codes Vocabulary (<a href="https://rs.gbif.org/vocabulary/gbif/nomenclatural_code.xml">https://rs.gbif.org/vocabulary/gbif/nomenclatural_code.xml</a>).</p></td>
		</tr>
	</tbody>
</table>

<table>

    <thead>
        <th colspan="2"><a id="tcs_nomenclaturalstatus"></a>Term Name: tcs:nomenclaturalStatus</th>
    </thead>
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
			<td><b>Required:</b> No — <b>Repeatable:</b> No</td>
		</tr>
		<tr>
			<td>Comments</td>
			<td><p>This is the IRI equivalent of the Darwin Core <code>nomenclaturalStatus</code>. In the  absence of a TDWG vocabulary, it is RECOMMENDED to use a value from the GBIF  Nomenclatural Status Vocabulary  (<a href="https://rs.gbif.org/vocabulary/gbif/nomenclatural_status_2019-02-08.xml">https://rs.gbif.org/vocabulary/gbif/nomenclatural_status_2019-02-08.xml</a>).</p></td>
		</tr>
	</tbody>
</table>

<table>

    <thead>
        <th colspan="2"><a id="tcs_typification"></a>Term Name: tcs:typification</th>
    </thead>
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
			<td><p>The <code>typification</code> property takes a TCS Nomenclatural Type or list of Nomenclatural Types.</p></td>
		</tr>
		<tr>
			<td></td>
			<td><b>Required:</b> No — <b>Repeatable:</b> Yes</td>
		</tr>
		<tr>
			<td>Comments</td>
			<td><p><code>tcs:typification</code> is the inverse of <code>tcs:typifiedName</code>.</p></td>
		</tr>
		<tr>
			<td>Examples</td>
			<td><ul>
<li><a href="../examples/TaxonName-typification-example-1.html">TaxonName-typification-example-1</a></li>

<li><a href="../examples/TaxonName-typification-example-2.html">TaxonName-typification-example-2</a></li>

</ul>
</td>
		</tr>
	</tbody>
</table>

<table>

    <thead>
        <th colspan="2"><a id="tcs_typificationliteral"></a>Term Name: tcs:typificationLiteral</th>
    </thead>
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
			<td><b>Required:</b> No — <b>Repeatable:</b> No</td>
		</tr>
		<tr>
			<td>Comments</td>
			<td><p>The <code>typificationLiteral</code> property can be used for citation of a type (or types) as written in the publication in which the typified name was published. </p></td>
		</tr>
	</tbody>
</table>

<table>

    <thead>
        <th colspan="2"><a id="tcs_basionym"></a>Term Name: tcs:basionym</th>
    </thead>
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
			<td><b>Required:</b> No — <b>Repeatable:</b> No</td>
		</tr>
		<tr>
			<td>Comments</td>
			<td><p>The term <code>basionym</code> is in the draft BioCode (<a href="../bibliography/#greuter_draft_2011">[greuter_draft_2011]</a>), so can be used for all organisms. The <code>basionym</code> property is only used for new combinations ('comb. nov.'). If the new name is a replacement name ('nom. nov.') the <code>replacedName</code> property SHOULD be used instead. It SHOULD be noted that a basionym is always a different name or combination: a name cannot be its own basionym.</p></td>
		</tr>
		<tr>
			<td>Examples</td>
			<td><ul>
<li><a href="../examples/TaxonName-basionym-example-1.html">TaxonName-basionym-example-1</a></li>

<li><a href="../examples/TaxonName-basionym-example-2.html">TaxonName-basionym-example-2</a></li>

</ul>
</td>
		</tr>
	</tbody>
</table>

<table>

    <thead>
        <th colspan="2"><a id="tcs_replacedname"></a>Term Name: tcs:replacedName</th>
    </thead>
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
			<td>Replaced Name</td>
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
			<td><b>Required:</b> No — <b>Repeatable:</b> No</td>
		</tr>
		<tr>
			<td>Comments</td>
			<td><p>'replaced name' is used in the draft BioCode (<a href="../bibliography/#greuter_draft_2011">[greuter_draft_2011]</a>). In the Botanical Code the term 'replaced synonym' is used for the same thing. A 'replacement name' is a name that is published as a substitute for an earlier published name that is either illegitimate or for which a new combination cannot be created in the place a taxon is transferred to because of an older blocking name.</p></td>
		</tr>
		<tr>
			<td>Examples</td>
			<td><ul>
<li><a href="../examples/TaxonName-replacedName-example-1.html">TaxonName-replacedName-example-1</a></li>

<li><a href="../examples/TaxonName-replacedName-example-2.html">TaxonName-replacedName-example-2</a></li>

<li><a href="../examples/TaxonName-replacedName-example-3.html">TaxonName-replacedName-example-3</a></li>

<li><a href="../examples/TaxonName-replacedName-example-4.html">TaxonName-replacedName-example-4</a></li>

</ul>
</td>
		</tr>
	</tbody>
</table>

<table>

    <thead>
        <th colspan="2"><a id="tcs_basedon"></a>Term Name: tcs:basedOn</th>
    </thead>
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
			<td>Based On</td>
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
			<td><b>Required:</b> No — <b>Repeatable:</b> No</td>
		</tr>
		<tr>
			<td>Comments</td>
			<td><p>The <code>basedOn</code> property can be used to associate a name to a homotypic group of names in situations where the <code>basionym</code> and <code>replacedName</code> properties cannot be used. Therefore the property can be useful for (1) linking an autonym to a species name, (2) linking a valid name to an earlier invalid name and (3) linking an invalid name to a later valid name.</p></td>
		</tr>
	</tbody>
</table>

<table>

    <thead>
        <th colspan="2"><a id="tcs_laterhomonymof"></a>Term Name: tcs:laterHomonymOf</th>
    </thead>
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
			<td>Later Homonym Of</td>
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
			<td><b>Required:</b> No — <b>Repeatable:</b> No</td>
		</tr>
		<tr>
			<td>Comments</td>
			<td><p>If there are more than two homonyms, the oldest name SHOULD be given here. In zoology, this is the <em>senior homonym</em>.</p></td>
		</tr>
	</tbody>
</table>

<table>

    <thead>
        <th colspan="2"><a id="tcs_conservedagainst"></a>Term Name: tcs:conservedAgainst</th>
    </thead>
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
			<td><b>Required:</b> No — <b>Repeatable:</b> Yes</td>
		</tr>
		<tr>
			<td>Comments</td>
			<td><p>A scientific name below the rank of family is not conserved against all  other names, but only against one or more names that in turn are rejected  against the conserved name. A name can be conserved against more than one  other name, so this property is repeatable.</p></td>
		</tr>
		<tr>
			<td>Examples</td>
			<td><ul>
<li><a href="../examples/TaxonName-conservedAgainst-example-1.html">TaxonName-conservedAgainst-example-1</a></li>

</ul>
</td>
		</tr>
	</tbody>
</table>

<table>

    <thead>
        <th colspan="2"><a id="tcs_combinationauthor"></a>Term Name: tcs:combinationAuthor</th>
    </thead>
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
			<td>Combination Author</td>
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
			<td><b>Required:</b> No — <b>Repeatable:</b> Yes</td>
		</tr>
		<tr>
			<td>Comments</td>
			<td><p>'combination' is taken here to be a different name with the same nomenclatural type.</p></td>
		</tr>
		<tr>
			<td>Examples</td>
			<td><ul>
<li><a href="../examples/TaxonName-combinationAuthor-example-1.html">TaxonName-combinationAuthor-example-1</a></li>

</ul>
</td>
		</tr>
	</tbody>
</table>

<table>

    <thead>
        <th colspan="2"><a id="tcs_combinationauthorliteral"></a>Term Name: tcs:combinationAuthorLiteral</th>
    </thead>
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
			<td>Combination Author</td>
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
			<td><b>Required:</b> No — <b>Repeatable:</b> No</td>
		</tr>
		<tr>
			<td>Comments</td>
			<td><p>'combination' is taken here to be a different name with the same nomenclatural type.</p></td>
		</tr>
	</tbody>
</table>

<table>

    <thead>
        <th colspan="2"><a id="tcs_basionymauthor"></a>Term Name: tcs:basionymAuthor</th>
    </thead>
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
			<td>Basionym Author</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td><p>Author of the basionym of the described name</p></td>
		</tr>
		<tr>
			<td>Usage</td>
			<td><p><code>basionymAuthor</code> is an IRI property. It can be a person or a list of persons.</p></td>
		</tr>
		<tr>
			<td></td>
			<td><b>Required:</b> No — <b>Repeatable:</b> Yes</td>
		</tr>
		<tr>
			<td>Comments</td>
			<td><p><code>basionymAuthor</code> (or its literal counterpart) is the bit in parentheses in the <code>dwc:scientificNameAuthorship</code>.</p></td>
		</tr>
		<tr>
			<td>Examples</td>
			<td><ul>
<li><a href="../examples/TaxonName-basionymAuthor-example-1.html">TaxonName-basionymAuthor-example-1</a></li>

</ul>
</td>
		</tr>
	</tbody>
</table>

<table>

    <thead>
        <th colspan="2"><a id="tcs_basionymauthorliteral"></a>Term Name: tcs:basionymAuthorLiteral</th>
    </thead>
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
			<td>Basionym Author</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td><p>Author of the basionym of the described name</p></td>
		</tr>
		<tr>
			<td>Usage</td>
			<td><p><code>basionymAuthorLiteral</code> is a Literal property.</p></td>
		</tr>
		<tr>
			<td></td>
			<td><b>Required:</b> No — <b>Repeatable:</b> No</td>
		</tr>
		<tr>
			<td>Comments</td>
			<td><p><code>basionymAuthorLiteral</code> is the bit in parentheses in the <code>dwc:scientificNameAuthorship</code>.</p></td>
		</tr>
	</tbody>
</table>

<table>

    <thead>
        <th colspan="2"><a id="tcs_combinationascribedauthor"></a>Term Name: tcs:combinationAscribedAuthor</th>
    </thead>
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
			<td>Combination Ascribed Author</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td><p>Ascribed author of the described name</p></td>
		</tr>
		<tr>
			<td>Usage</td>
			<td><p><code>combinationAscribedAuthor</code> is an IRI property. It can be a person or a list of persons.</p></td>
		</tr>
		<tr>
			<td></td>
			<td><b>Required:</b> No — <b>Repeatable:</b> Yes</td>
		</tr>
		<tr>
			<td>Comments</td>
			<td><p>An 'ascribed author' is a person (or group of people) who a name is ascribed to in a publication, but who is not the author of the name according to the rules of the nomenclatural codes, because they did not contribute to the validating description of the name. In the <code>dwc:scientificNameAuthorship</code> these authors are indicated with 'ex', the ascribed author coming before the 'ex' and the author the name is attributed to after. Note that the 'ex' (or 'Ex') construction that is sometimes used with zoological names has got nothing to do with attribution or ascription, but is used to denote a concept, much like we do here with 'sec.' or 'sensu' in taxon concept labels.</p></td>
		</tr>
		<tr>
			<td>Examples</td>
			<td><ul>
<li><a href="../examples/TaxonName-combinationAscribedAuthor-example-1.html">TaxonName-combinationAscribedAuthor-example-1</a></li>

</ul>
</td>
		</tr>
	</tbody>
</table>

<table>

    <thead>
        <th colspan="2"><a id="tcs_combinationascribedauthorliteral"></a>Term Name: tcs:combinationAscribedAuthorLiteral</th>
    </thead>
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
			<td>Combination Ascribed Author</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td><p>Ascribed author of the described name</p></td>
		</tr>
		<tr>
			<td>Usage</td>
			<td><p><code>combinationAscribedAuthorLiteral</code> is a Literal property.</p></td>
		</tr>
		<tr>
			<td></td>
			<td><b>Required:</b> No — <b>Repeatable:</b> No</td>
		</tr>
		<tr>
			<td>Comments</td>
			<td><p>An 'ascribed author' is a person (or group of people) who a name is ascribed to in a publication, but who is not the author of the name according to the rules of the nomenclatural codes, because they did not contribute to the validating description of the name. In the <code>dwc:scientificNameAuthorship</code> these authors are indicated with 'ex', the ascribed author coming before the 'ex' and the author the name is attributed to after. Note that the 'ex' (or 'Ex') construction that is sometimes used with zoological names has got nothing to do with attribution or ascription, but is used to denote a concept, much like we do here with 'sec.' or 'sensu' in taxon concept labels.</p></td>
		</tr>
	</tbody>
</table>

<table>

    <thead>
        <th colspan="2"><a id="tcs_basionymascribedauthor"></a>Term Name: tcs:basionymAscribedAuthor</th>
    </thead>
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
			<td>Basionym Ascribed Author</td>
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
			<td><b>Required:</b> No — <b>Repeatable:</b> Yes</td>
		</tr>
		<tr>
			<td>Comments</td>
			<td><p>An 'ascribed author' is a person (or group of people) who a name is ascribed to in a publication, but who is not the author of the name according to the rules of the nomenclatural codes, because they did not contribute to the validating description of the name. In the <code>dwc:scientificNameAuthorship</code> these authors are indicated with 'ex', the ascribed author coming before the 'ex' and the author the name is attributed to after. Note that the 'ex' (or 'Ex') construction that is sometimes used with zoological names has got nothing to do with attribution or ascription, but is used to denote a concept, much like we do here with 'sec.' or 'sensu' in taxon concept labels.</p></td>
		</tr>
		<tr>
			<td>Examples</td>
			<td><ul>
<li><a href="../examples/TaxonName-basionymAscribedAuthor-example-1.html">TaxonName-basionymAscribedAuthor-example-1</a></li>

</ul>
</td>
		</tr>
	</tbody>
</table>

<table>

    <thead>
        <th colspan="2"><a id="tcs_basionymascribedauthorliteral"></a>Term Name: tcs:basionymAscribedAuthorLiteral</th>
    </thead>
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
			<td>Basionym Ascribed Author</td>
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
			<td><b>Required:</b> No — <b>Repeatable:</b> No</td>
		</tr>
		<tr>
			<td>Comments</td>
			<td><p>An 'ascribed author' is a person (or group of people) who a name is ascribed to in a publication, but who is not the author of the name according to the rules of the nomenclatural codes, because they did not contribute to the validating description of the name. In the <code>dwc:scientificNameAuthorship</code> these authors are indicated with 'ex', the ascribed author coming before the 'ex' and the author the name is attributed to after. Note that the 'ex' (or 'Ex') construction that is sometimes used with zoological names has got nothing to do with attribution or ascription, but is used to denote a concept, much like we do here with 'sec.' or 'sensu' in taxon concept labels.</p></td>
		</tr>
	</tbody>
</table>

<table>

    <thead>
        <th colspan="2"><a id="dwc_scientificnameauthorship"></a>Term Name: dwc:scientificNameAuthorship</th>
    </thead>
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
			<td><b>Required:</b> No — <b>Repeatable:</b> No</td>
		</tr>
	</tbody>
</table>

<table>

    <thead>
        <th colspan="2"><a id="dwc_namepublishedin"></a>Term Name: dwc:namePublishedIn</th>
    </thead>
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
			<td><p>A reference for the publication in which the <code>dwc:scientificName</code> was  originally established under the rules of the associated  <code>dwc:nomenclaturalCode</code>.</p></td>
		</tr>
		<tr>
			<td></td>
			<td><b>Required:</b> No — <b>Repeatable:</b> No</td>
		</tr>
		<tr>
			<td>Comments</td>
			<td><p>This is the string literal equivalent of the TCS <code>namePublishedIn</code>. It can be used if one wants to give the protologue as a string, as in many botanical publications.</p></td>
		</tr>
	</tbody>
</table>

<table>

    <thead>
        <th colspan="2"><a id="dwc_namepublishedinyear"></a>Term Name: dwc:namePublishedInYear</th>
    </thead>
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
			<td><b>Required:</b> No — <b>Repeatable:</b> No</td>
		</tr>
	</tbody>
</table>

<table>

    <thead>
        <th colspan="2"><a id="dwc_genericname"></a>Term Name: dwc:genericName</th>
    </thead>
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
			<td><p>This property SHOULD only be used for names below the rank of genus.</p></td>
		</tr>
		<tr>
			<td></td>
			<td><b>Required:</b> No — <b>Repeatable:</b> No</td>
		</tr>
	</tbody>
</table>

<table>

    <thead>
        <th colspan="2"><a id="dwc_infragenericepithet"></a>Term Name: dwc:infragenericEpithet</th>
    </thead>
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
			<td><p>Names at ranks between species and genus, e.g. subgenera and sections, are  composed of two parts; the genus and the infrageneric epithet. This property  SHOULD therefore always be accompanied by the <code>genericName</code> property. If the  <code>infragenericEpithet</code> property is present, the <code>specificEpithet</code> and  <code>infraspecificEpithet</code> properties SHOULD not be present. </p></td>
		</tr>
		<tr>
			<td></td>
			<td><b>Required:</b> No — <b>Repeatable:</b> No</td>
		</tr>
	</tbody>
</table>

<table>

    <thead>
        <th colspan="2"><a id="dwc_specificepithet"></a>Term Name: dwc:specificEpithet</th>
    </thead>
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
			<td><p>Names at ranks of species and below are composed of two or three parts: the generic name, the specific epithet and possibly an infraspecific epithet. This property SHOULD therefore always be accompanied by the <code>genus</code> property. If the <code>specificEpithet</code> property is present the <code>infragenericEpithet</code> property SHOULD not be present.</p></td>
		</tr>
		<tr>
			<td></td>
			<td><b>Required:</b> No — <b>Repeatable:</b> No</td>
		</tr>
	</tbody>
</table>

<table>

    <thead>
        <th colspan="2"><a id="dwc_infraspecificepithet"></a>Term Name: dwc:infraspecificEpithet</th>
    </thead>
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
			<td><p>Names at ranks below species are composed of three parts; the genus name,  the specific epithet and an infraspecific epithet. This property SHOULD  therefore always be accompanied by the <code>genus</code> and <code>specificEpithet</code>  properties. If the <code>infraspecificEpithet</code> property is present the  <code>infragenericEpithet</code> property SHOULD not be present.</p></td>
		</tr>
		<tr>
			<td></td>
			<td><b>Required:</b> No — <b>Repeatable:</b> No</td>
		</tr>
	</tbody>
</table>

<table>

    <thead>
        <th colspan="2"><a id="dwc_cultivarepithet"></a>Term Name: dwc:cultivarEpithet</th>
    </thead>
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
			<td><b>Required:</b> No — <b>Repeatable:</b> No</td>
		</tr>
	</tbody>
</table>

### 5.4. Nomenclatural Type

<table>

    <thead>
        <th colspan="2"><a id="tcs_nomenclaturaltype"></a>Term Name: tcs:NomenclaturalType</th>
    </thead>
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
			<td><p>A nomenclatural type fixes the usage of a name to the taxonomic group that contains the type. One or more Nomenclatural Types make up the typification of a Taxon Name. In Darwin Core, a Nomenclatural Type object can be used as object with <code>dwciri:typeStatus</code>.</p></td>
		</tr>
		<tr>
			<td>Examples</td>
			<td><ul>
<li><a href="../examples/NomenclaturalType-example-1.html">NomenclaturalType-example-1</a></li>

</ul>
</td>
		</tr>
	</tbody>
</table>

<table>

    <thead>
        <th colspan="2"><a id="tcs_typifiedname"></a>Term Name: tcs:typifiedName</th>
    </thead>
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
			<td><b>Required:</b> Yes — <b>Repeatable:</b> No</td>
		</tr>
		<tr>
			<td>Comments</td>
			<td><p>The <code>typifiedName</code> property links the Nomenclatural Type back to the Taxon  Name. Also, when coming from the Preserved Specimen, the typified name is  the most important piece of information, because there is no point in  knowing what kind of type a specimen is without knowing for what name it  is the type. Therefore, <code>typifiedName</code> is a REQUIRED property.</p></td>
		</tr>
	</tbody>
</table>

<table>

    <thead>
        <th colspan="2"><a id="tcs_typeoftype"></a>Term Name: tcs:typeOfType</th>
    </thead>
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
			<td>Type Of Type</td>
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
			<td><b>Required:</b> Yes — <b>Repeatable:</b> No</td>
		</tr>
		<tr>
			<td>Comments</td>
			<td><p>This is an IRI property. In the absence of a TDWG controlled vocabulary,  it is RECOMMENDED to use a value from the GBIF Nomenclatural Type Status  Vocabulary (<a href="https://rs.gbif.org/vocabulary/gbif/type_status_2021-01-18.xml">https://rs.gbif.org/vocabulary/gbif/type_status_2021-01-18.xml</a>).</p></td>
		</tr>
	</tbody>
</table>

<table>

    <thead>
        <th colspan="2"><a id="tcs_typename"></a>Term Name: tcs:typeName</th>
    </thead>
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
			<td><b>Required:</b> No — <b>Repeatable:</b> No</td>
		</tr>
		<tr>
			<td>Comments</td>
			<td><p>Taxon names at ranks above species level can be typified by the name of a  lower taxon. Ultimately, by following the chain of type names, all names  resolve to a type species and thus a type specimen. </p></td>
		</tr>
	</tbody>
</table>

<table>

    <thead>
        <th colspan="2"><a id="tcs_typespecimen"></a>Term Name: tcs:typeSpecimen</th>
    </thead>
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
			<td><p><code>typeSpecimen</code> takes an IRI – or object – that refers to a specimen. A  Nomenclatural Type MUST NOT have more than one <code>typeSpecimen</code>.</p></td>
		</tr>
		<tr>
			<td></td>
			<td><b>Required:</b> No — <b>Repeatable:</b> No</td>
		</tr>
		<tr>
			<td>Comments</td>
			<td><p>Names at ranks of species and below are typified by a specimen. This property is mutually exclusive with <code>typeName</code>. This is an IRI property. One could use the Darwin Core Preserved Specimen or Material Citation. While a Taxon Name can have more than one type specimens, each of these type specimens requires its own Nomenclatural Type record, so a Nomenclatural Type can have only one <code>typeSpecimen</code>.</p></td>
		</tr>
	</tbody>
</table>

<table>

    <thead>
        <th colspan="2"><a id="tcs_typepublishedin"></a>Term Name: tcs:typePublishedIn</th>
    </thead>
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
			<td><b>Required:</b> No — <b>Repeatable:</b> No</td>
		</tr>
		<tr>
			<td>Comments</td>
			<td><p><code>typePublishedIn</code> is relevant for lectotypes, neotypes, epitypes and  conserved types. For other kinds of type the publication where the type is  designated is the publication the name was published in.</p></td>
		</tr>
	</tbody>
</table>

<!-- footer -->