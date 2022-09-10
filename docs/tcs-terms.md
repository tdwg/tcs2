# TCS Term List

**Note:** The content below is created dynamically from the
[tcs.yaml](./tcs.yaml) and [dwc-for-tcs.yaml](./dwc-for-tcs.yaml) files.
Please do not edit the markdown directly, but make any changes in the YAML
files.

### Index of terms

**classes**

[tcs:TaxonConcept](#tcs_TaxonConcept) | [tcs:TaxonConceptRelationship](#tcs_TaxonConceptRelationship) | [tcs:TaxonName](#tcs_TaxonName) | [tcs:NomenclaturalType](#tcs_NomenclaturalType)

**Taxon Concept**

[tcs:taxonName](#tcs_taxonName) | [tcs:accordingTo](#tcs_accordingTo) | [tcs:verbatimNameString](#tcs_verbatimNameString) | [tcs:taxonomicRank](#tcs_taxonomicRank) | [tcs:parent](#tcs_parent) | [tcs:synonym](#tcs_synonym) | [tcs:vernacularName](#tcs_vernacularName)

**Taxon Concept Relationship**

[tcs:relationshipType](#tcs_relationshipType) | [tcs:subjectTaxonConcept](#tcs_subjectTaxonConcept) | [tcs:objectTaxonConcept](#tcs_objectTaxonConcept) | [tcs:relationshipAccordingTo](#tcs_relationshipAccordingTo) | [tcs:traditionalSynonymyRelationshipType](#tcs_traditionalSynonymyRelationshipType)

**Taxon Name**

[tcs:taxonNameString](#tcs_taxonNameString) | [tcs:namePublishedIn](#tcs_namePublishedIn) | [tcs:microreference](#tcs_microreference) | [tcs:nomenclaturalCode](#tcs_nomenclaturalCode) | [tcs:nomenclaturalStatus](#tcs_nomenclaturalStatus) | [tcs:basionym](#tcs_basionym) | [tcs:replacementNameFor](#tcs_replacementNameFor) | [tcs:basedOn](#tcs_basedOn) | [tcs:conservedAgainst](#tcs_conservedAgainst) | [dwc:scientificNameAuthorship](#dwc_scientificNameAuthorship) | [dwc:namePublishedInYear](#dwc_namePublishedInYear) | [dwc:genericName](#dwc_genericName) | [dwc:infragenericEpithet](#dwc_infragenericEpithet) | [dwc:specificEpithet](#dwc_specificEpithet) | [dwc:infraspecificEpithet](#dwc_infraspecificEpithet) | [dwc:cultivarEpithet](#dwc_cultivarEpithet)

**Nomenclatural Type**

[tcs:typifiedName](#tcs_typifiedName) | [tcs:typeOfType](#tcs_typeOfType) | [tcs:typeName](#tcs_typeName) | [tcs:typeSpecimen](#tcs_typeSpecimen) | [tcs:typePublishedIn](#tcs_typePublishedIn)

### Vocabulary

#### Taxon Concept

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="tcs_TaxonConcept"></a>Class tcs:TaxonConcept</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
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
			<td><p>An identifiable taxonomic position, a conception about the delimitation of  a taxonomic group, that can be aligned to other such positions through TCS  Taxon Concept Relationships.</p></td>
		</tr>
		<tr>
			<td>Usage</td>
			<td></td>
		</tr>
		<tr>
			<td>Comments</td>
			<td><p>A Taxon Concept is identifiable, because it combines a label – <code>taxonName</code> in TCS – with a source – <code>accordingTo</code>. Both these properties are required.  When mentioning a taxon concept, the label and the source are also combined,  separated by 'sec.' (from, 'secundus', meaning 'according to') or 'sensu'  (meaning the same). Because of the context provided by the source, taxon  concepts are in principle also alignable to other Taxon Concepts using the  TCS Taxon Concept Alignments.</p>
<p>The TCS Taxon Concept is a data object and is applied more broadly than the  term is used in science (e.g. Franz &amp; Peet 2009). On the one hand, things  that are not generally considered to be biological taxa, e.g. hybrids and  cultivars, can be casted as TCS Taxon Concepts. Also Operational Taxonomic  Units (OTUs, cf. Sokal &amp; Sneath 1963) can be exchanged as Taxon Concepts,  if there is a reason to do so, e.g. if one wants to align them with other  Taxon Concepts later. On the other hand, entries from treatments that are  considered to cite concepts from other treatments can be formulated as  Taxon Concepts. Every taxon concept from a treatment that is likely to be  referenced as the source of taxonomic context, for example a field guide  for a determination of a specimen or a national census for an ecological  study, can – and it would be very nice if they would – be stated as a Taxon  Concept, so they can be aligned with other Taxon Concepts that may provide  more or different taxonomic context.</p></td>
		</tr>
		<tr>
			<td>Examples</td>
			<td></td>
		</tr>
		<tr>
			<td>GitHub issue</td>
			<td>https://github.com/tdwg/tcs2/issues/1</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="tcs_taxonName"></a>Property tcs:taxonName</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
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
			<td><b>required:</b> No — <b>repeatable:</b> No</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td><p>The name that is given to the taxonomic group.</p></td>
		</tr>
		<tr>
			<td>Usage</td>
			<td></td>
		</tr>
		<tr>
			<td>Comments</td>
			<td><p>The <code>taxonName</code> can be anything from a well-formed scientific name to an  informal name, vernacular name, indigenous knowledge label, or even a label  containing numbers and/or special symbols, such as are often used for OTUs.  The object of <code>taxonName</code> is an object or IRI, so that it can be reused in  other Taxon Concepts. TCS has got the Taxon Name class, which can be used  for any type of name, but people are free to use alternatives, e.g.  <code>skosxl:Label</code>, if they want to restrict the use of the Taxon Name class to  scientific (or scientific-y) names only.</p></td>
		</tr>
		<tr>
			<td>Examples</td>
			<td></td>
		</tr>
		<tr>
			<td>GitHub issue</td>
			<td>https://github.com/tdwg/tcs2/issues/2</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="tcs_accordingTo"></a>Property tcs:accordingTo</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
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
			<td><b>required:</b> No — <b>repeatable:</b> No</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td><p>Reference to the treatment in which a Taxon Concept is established or used. </p></td>
		</tr>
		<tr>
			<td>Usage</td>
			<td></td>
		</tr>
		<tr>
			<td>Comments</td>
			<td><p>Every Taxon Concept is in some sort of treatment and this treatment  provides important context without which we do not know what a taxon name  really means and therefore the <code>accordingTo</code> property is required for a TCS  Taxon Concept. In TCS 2, <code>accordingTo</code> has to be a reference to some sort  of resource rather than just a person's name. However, TCS is lenient about  the nature of this resource and, apart from references to bibliographic  resources, references to personal communications and determinations are  also acceptable, if there is value in supplying taxon concepts from such  communications as Taxon Concepts.</p>
<p>The value of <code>accordingTo</code> has to be an object or IRI. This object can  contain as little as a bibliographic reference but it is much more useful  to provide it in a format that can be understood by reference managers  such as Zotero or Mendeley.</p></td>
		</tr>
		<tr>
			<td>Examples</td>
			<td></td>
		</tr>
		<tr>
			<td>GitHub issue</td>
			<td>https://github.com/tdwg/tcs2/issues/4</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="tcs_verbatimNameString"></a>Property tcs:verbatimNameString</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
			<td>http://rs.tdwg.org/tcs/terms/verbatimNameString</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>http://www.w3.org/1999/02/22-rdf-syntax-ns#Property</td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Verbatim Name String</td>
		</tr>
		<tr>
			<td></td>
			<td><b>required:</b> No — <b>repeatable:</b> No</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td><p>&lt;- The verbatim name string as used in the particular treatment.</p></td>
		</tr>
		<tr>
			<td>Usage</td>
			<td></td>
		</tr>
		<tr>
			<td>Comments</td>
			<td><p>The name string used in the treatment may be somewhat different from the  currently accepted spelling of the Taxon Name. The 'verbatim' does not  need to be taken too literally: it is permissible to write out abbreviated  generic names, or only provide the final epithet where the difference is.  It is also up to the user whether this term is used all the time when there  is a difference in spelling, only for nomenclatural novelties, only for the  original publication of original combinations, or not at all. Systems  cannot require this term and cannot use a default. </p></td>
		</tr>
		<tr>
			<td>Examples</td>
			<td></td>
		</tr>
		<tr>
			<td>GitHub issue</td>
			<td>https://github.com/tdwg/tcs2/issues/3</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="tcs_taxonomicRank"></a>Property tcs:taxonomicRank</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
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
			<td></td>
		</tr>
		<tr>
			<td>Comments</td>
			<td><p>The rank is an attribute of elements in a classification and <code>taxonomicRank</code>  can be applied to Taxon Concepts as well Taxon Names, as the rank of a  taxon is reflected in its name. This property takes an object or IRI and it  is recommended to use a value from an existing controlled vocabulary.  While there is no TDWG vocabulary yet, the GBIF Taxonomic Rank Vocabulary  (https://rs.gbif.org/vocabulary/gbif/rank.xml) is recommended.</p></td>
		</tr>
		<tr>
			<td>Examples</td>
			<td></td>
		</tr>
		<tr>
			<td>GitHub issue</td>
			<td>https://github.com/tdwg/tcs2/issues/32</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="tcs_parent"></a>Property tcs:parent</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
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
			<td></td>
		</tr>
		<tr>
			<td>Comments</td>
			<td><p>The <code>parent</code> is another Taxon Concept. This is the parent as indicated in  the <code>accordingTo</code> reference, rather than a third-party classification. The  <code>accordingTo</code> of the parent will generally, but not necessarily, be the  same as that of the child.</p></td>
		</tr>
		<tr>
			<td>Examples</td>
			<td></td>
		</tr>
		<tr>
			<td>GitHub issue</td>
			<td>https://github.com/tdwg/tcs2/issues/8</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="tcs_synonym"></a>Property tcs:synonym</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
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
			<td></td>
		</tr>
		<tr>
			<td>Comments</td>
			<td><p>Synonymy is between names but, if the names have different types, a Taxon  Concept is required. Therefore, <code>synonym</code> is a property of the Taxon Concept  class. <code>synonym</code> is used here in the stricter sense that only indicates that  the type of a name falls within a Taxon Concept and has the same  relationship to Taxon Concept as <code>taxonName</code>. This allows one to dispose of  names without having to deal with the Taxon Concepts that were realised  along with the publication of these names. If one wants to include these  “original concepts” and indicate a relationship between Taxon Concepts, the  <code>intersects</code> Taxon Concept Relationship can be used instead, optionally in  combination with the <code>traditionalSynonymyRelationshipType</code> property. The  <code>synonym</code> property can be used for both homotypic and heterotypic synonyms,  although for homotypic synonyms it is preferable to use the <code>basionym</code> or  <code>replacementNameFor</code> properties on the Taxon Name object.</p></td>
		</tr>
		<tr>
			<td>Examples</td>
			<td></td>
		</tr>
		<tr>
			<td>GitHub issue</td>
			<td>https://github.com/tdwg/tcs2/issues/65</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="tcs_vernacularName"></a>Property tcs:vernacularName</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
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
			<td></td>
		</tr>
		<tr>
			<td>Comments</td>
			<td><p>The <code>vernacularName</code> property can be used when a vernacular name is used  alongside a scientific name, which is the <code>taxonName</code>. If a vernacular name  is the only name, the <code>taxonName</code> property should be used.</p></td>
		</tr>
		<tr>
			<td>Examples</td>
			<td></td>
		</tr>
		<tr>
			<td>GitHub issue</td>
			<td>https://github.com/tdwg/tcs2/issues/10</td>
		</tr>
	</tbody>
</table>

#### Taxon Concept Relationship

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="tcs_TaxonConceptRelationship"></a>Class tcs:TaxonConceptRelationship</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
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
			<td></td>
		</tr>
		<tr>
			<td>Comments</td>
			<td><p>Taxon Concept Relationships are a set of relationships that allow for the  alignment of Taxon Concepts – or taxon concept mapping. The main  relationship types coincide with topological relationships that are widely  used in spatial analysis, analysis of computer networks, artificial  intelligence, etc. In particular, they are the relationships that are used  in RCC-5 Region Connection Calculus, which allows for reasoning.</p>
<p>An extra controlled term <code>intersects</code> has been added to the Taxon Concept  Relationship Type Vocabulary to accommodate Taxon Concept Relationship  statements between Taxon Concepts of which we know that they have at least  one member in common, but where the more specific topological relationship  is not easily inferred. Also, a property  <code>traditionalSynonymyRelationshipType</code> has been added to refine the  <code>intersects</code> relationship type for terms that are in use in traditional  synonymy and are better dealt with as Taxon Concept Relationships than  nomenclatural relationships.</p>
<p>Taxon Concept Relationship statements can be made in the treatment of the  subject Taxon Concept or by third parties.</p></td>
		</tr>
		<tr>
			<td>Examples</td>
			<td></td>
		</tr>
		<tr>
			<td>GitHub issue</td>
			<td>https://github.com/tdwg/tcs2/issues/43</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="tcs_relationshipType"></a>Property tcs:relationshipType</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
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
			<td></td>
		</tr>
		<tr>
			<td>Comments</td>
			<td><p>This is an IRI term. One should use a value from the TDWG Taxon Concept  Relationship Type Vocabulary.</p></td>
		</tr>
		<tr>
			<td>Examples</td>
			<td></td>
		</tr>
		<tr>
			<td>GitHub issue</td>
			<td>https://github.com/tdwg/tcs2/issues/44</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="tcs_subjectTaxonConcept"></a>Property tcs:subjectTaxonConcept</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
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
			<td></td>
		</tr>
		<tr>
			<td>Comments</td>
			<td><p>This is the Taxon Concept at the left-hand side of the relationship  statement.</p></td>
		</tr>
		<tr>
			<td>Examples</td>
			<td></td>
		</tr>
		<tr>
			<td>GitHub issue</td>
			<td>https://github.com/tdwg/tcs2/issues/45</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="tcs_objectTaxonConcept"></a>Property tcs:objectTaxonConcept</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
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
			<td></td>
		</tr>
		<tr>
			<td>Comments</td>
			<td><p>This is the Taxon Concept at the right-hand side of the relationship  statement.</p></td>
		</tr>
		<tr>
			<td>Examples</td>
			<td></td>
		</tr>
		<tr>
			<td>GitHub issue</td>
			<td>https://github.com/tdwg/tcs2/issues/46</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="tcs_relationshipAccordingTo"></a>Property tcs:relationshipAccordingTo</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
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
			<td></td>
		</tr>
		<tr>
			<td>Comments</td>
			<td><p>In the case of Taxon Concept Relationships from traditional synonymy, the  <code>relationshipAccordingTo</code> is the same as the <code>accordingTo</code> of the Taxon  Concept that is the <code>subjectTaxonConcept</code>.</p></td>
		</tr>
		<tr>
			<td>Examples</td>
			<td></td>
		</tr>
		<tr>
			<td>GitHub issue</td>
			<td>https://github.com/tdwg/tcs2/issues/47</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="tcs_traditionalSynonymyRelationshipType"></a>Property tcs:traditionalSynonymyRelationshipType</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
			<td>http://rs.tdwg.org/tcs/terms/traditionalSynonymyRelationshipType</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>http://www.w3.org/1999/02/22-rdf-syntax-ns#Property</td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Traditional Synonymy Relationship Type</td>
		</tr>
		<tr>
			<td></td>
			<td><b>required:</b> Yes — <b>repeatable:</b> No</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td><p>Type of relationship that is used in traditional synonymy, e.g. 'pro parte synonym' or 'misapplication'.</p></td>
		</tr>
		<tr>
			<td>Usage</td>
			<td></td>
		</tr>
		<tr>
			<td>Comments</td>
			<td><p>This is an IRI term. One should use a value from the TDWG Taxon Concept  Relationship Type Vocabulary. In the case of Taxon Concept Relationships  from traditional synonymy, the <code>relationshipAccordingTo</code> is the same as the  <code>accordingTo</code> of the Taxon Concept that is the <code>subjectTaxonConcept</code>.</p></td>
		</tr>
		<tr>
			<td>Examples</td>
			<td></td>
		</tr>
		<tr>
			<td>GitHub issue</td>
			<td>https://github.com/tdwg/tcs2/issues/200</td>
		</tr>
	</tbody>
</table>

#### Taxon Name

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="tcs_TaxonName"></a>Class tcs:TaxonName</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
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
			<td></td>
		</tr>
		<tr>
			<td>Comments</td>
			<td><p>The word 'name' here is taken in its dictionary meaning and not in the  sense of a particular nomenclatural code. This means that the Taxon Name  class can be used for any type of name, not just names that are validly  published under the relevant nomenclatural code.</p></td>
		</tr>
		<tr>
			<td>Examples</td>
			<td></td>
		</tr>
		<tr>
			<td>GitHub issue</td>
			<td>https://github.com/tdwg/tcs2/issues/15</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="tcs_taxonNameString"></a>Property tcs:taxonNameString</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
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
			<td></td>
		</tr>
		<tr>
			<td>Comments</td>
			<td><p>The <code>taxonNameString</code> property differs from the <code>scientificName</code> property  in Darwin Core in that all kinds of names are allowed. Also, in the case of  scientific names, contrary to the <code>dwc:scientificName</code>, <code>taxonNameString</code>  does not include the authorship. In botanical names, it does include the  rank prefixes for infrageneric and infraspecific epithets as they are  considered part of the name.</p></td>
		</tr>
		<tr>
			<td>Examples</td>
			<td></td>
		</tr>
		<tr>
			<td>GitHub issue</td>
			<td>https://github.com/tdwg/tcs2/issues/16</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="tcs_namePublishedIn"></a>Property tcs:namePublishedIn</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
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
			<td></td>
		</tr>
		<tr>
			<td>Comments</td>
			<td><p>In botany, this would be the protologue. This is the IRI counterpart of  the Darwin Core <code>namePublishedIn</code>.</p></td>
		</tr>
		<tr>
			<td>Examples</td>
			<td></td>
		</tr>
		<tr>
			<td>GitHub issue</td>
			<td>https://github.com/tdwg/tcs2/issues/29</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="tcs_microreference"></a>Property tcs:microreference</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
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
			<td></td>
		</tr>
		<tr>
			<td>Comments</td>
			<td><p>In taxonomic works it is convention to cite the exact location in a work  where a new name is published. The <code>microreference</code> property lets one do  that on the Taxon Name object, so that the <code>namePublishedIn</code> reference can  be reused.</p></td>
		</tr>
		<tr>
			<td>Examples</td>
			<td></td>
		</tr>
		<tr>
			<td>GitHub issue</td>
			<td>https://github.com/tdwg/tcs2/issues/30</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="tcs_nomenclaturalCode"></a>Property tcs:nomenclaturalCode</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
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
			<td></td>
		</tr>
		<tr>
			<td>Comments</td>
			<td><p>This is the IRI equivalent of the Darwin Core <code>nomenclaturalCode</code>. In the  absence of a TDWG vocabulary, it is recommended to use a value from the GBIF  Nomenclatural Codes Vocabulary  (https://rs.gbif.org/vocabulary/gbif/nomenclatural_code.xml).</p></td>
		</tr>
		<tr>
			<td>Examples</td>
			<td></td>
		</tr>
		<tr>
			<td>GitHub issue</td>
			<td>https://github.com/tdwg/tcs2/issues/33</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="tcs_nomenclaturalStatus"></a>Property tcs:nomenclaturalStatus</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
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
			<td></td>
		</tr>
		<tr>
			<td>Comments</td>
			<td><p>This is the IRI equivalent of the Darwin Core <code>nomenclaturalStatus</code>. In the  absence of a TDWG vocabulary, it is recommended to use a value from the GBIF  Nomenclatural Status Vocabulary  (https://rs.gbif.org/vocabulary/gbif/nomenclatural_status.xml).</p></td>
		</tr>
		<tr>
			<td>Examples</td>
			<td></td>
		</tr>
		<tr>
			<td>GitHub issue</td>
			<td>https://github.com/tdwg/tcs2/issues/35</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="tcs_basionym"></a>Property tcs:basionym</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
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
			<td></td>
		</tr>
		<tr>
			<td>Comments</td>
			<td><p>A basionym is the epithet-bringing name.  The <code>basionym</code> property is only  used for new combinations (<code>comb. nov.'). If the new name is an avowed  substitute ('nom. nov.') the</code>replacementNameFor` property should be used  instead.</p></td>
		</tr>
		<tr>
			<td>Examples</td>
			<td></td>
		</tr>
		<tr>
			<td>GitHub issue</td>
			<td>https://github.com/tdwg/tcs2/issues/36</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="tcs_replacementNameFor"></a>Property tcs:replacementNameFor</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
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
			<td></td>
		</tr>
		<tr>
			<td>Comments</td>
			<td><p>This is the 'replaced synonym' of the Botanical Code, which is to an avowed  substitute ('nom. nov.') what 'basionym' is to a new combination  ('comb. nov.')</p></td>
		</tr>
		<tr>
			<td>Examples</td>
			<td></td>
		</tr>
		<tr>
			<td>GitHub issue</td>
			<td>https://github.com/tdwg/tcs2/issues/37</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="tcs_basedOn"></a>Property tcs:basedOn</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
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
			<td></td>
			<td><b>required:</b> No — <b>repeatable:</b> No</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td><p>Invalidly published or illegitimate name for which this name is the  validation.</p></td>
		</tr>
		<tr>
			<td>Usage</td>
			<td></td>
		</tr>
		<tr>
			<td>Comments</td>
			<td></td>
		</tr>
		<tr>
			<td>Examples</td>
			<td></td>
		</tr>
		<tr>
			<td>GitHub issue</td>
			<td>https://github.com/tdwg/tcs2/issues/38</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="tcs_conservedAgainst"></a>Property tcs:conservedAgainst</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
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
			<td></td>
		</tr>
		<tr>
			<td>Comments</td>
			<td><p>A scientific name is not conserved against all other names, but only  against one or more names that in turn are rejected against the conserved  name. A name can be conserved against more than one other name, so this  property is repeatable.</p></td>
		</tr>
		<tr>
			<td>Examples</td>
			<td></td>
		</tr>
		<tr>
			<td>GitHub issue</td>
			<td>https://github.com/tdwg/tcs2/issues/39</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="dwc_scientificNameAuthorship"></a>Property dwc:scientificNameAuthorship</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
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
			<td>Comments</td>
			<td></td>
		</tr>
		<tr>
			<td>Examples</td>
			<td></td>
		</tr>
		<tr>
			<td>GitHub issue</td>
			<td>https://github.com/tdwg/tcs2/issues/24</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="dwc_namePublishedInYear"></a>Property dwc:namePublishedInYear</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
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
			<td><p>The authorship information for the <code>scientificName</code> formatted according to  the conventions of the applicable <code>nomenclaturalCode</code>.</p></td>
		</tr>
		<tr>
			<td>Usage</td>
			<td><p>This is the publication year for the present name combination, not the basionym should this be a new combination.</p></td>
		</tr>
		<tr>
			<td>Comments</td>
			<td></td>
		</tr>
		<tr>
			<td>Examples</td>
			<td></td>
		</tr>
		<tr>
			<td>GitHub issue</td>
			<td>https://github.com/tdwg/tcs2/issues/31</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="dwc_genericName"></a>Property dwc:genericName</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
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
			<td>Comments</td>
			<td></td>
		</tr>
		<tr>
			<td>Examples</td>
			<td></td>
		</tr>
		<tr>
			<td>GitHub issue</td>
			<td>https://github.com/tdwg/tcs2/issues/19</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="dwc_infragenericEpithet"></a>Property dwc:infragenericEpithet</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
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
			<td>Comments</td>
			<td></td>
		</tr>
		<tr>
			<td>Examples</td>
			<td></td>
		</tr>
		<tr>
			<td>GitHub issue</td>
			<td>https://github.com/tdwg/tcs2/issues/20</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="dwc_specificEpithet"></a>Property dwc:specificEpithet</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
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
			<td>Comments</td>
			<td></td>
		</tr>
		<tr>
			<td>Examples</td>
			<td></td>
		</tr>
		<tr>
			<td>GitHub issue</td>
			<td>https://github.com/tdwg/tcs2/issues/21</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="dwc_infraspecificEpithet"></a>Property dwc:infraspecificEpithet</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
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
			<td><p>Names at ranks below species are composed of three words; the genus name,  the specific epithet and an infraspecific epithet. This property should  therefore always be accompanied by the <code>genus</code> and <code>specificEpithet</code>  properties. If the <code>specificEpithet</code> property is present the <code>uninomial</code> and  <code>infragenericEpithet</code> properties should be absent.</p></td>
		</tr>
		<tr>
			<td>Comments</td>
			<td></td>
		</tr>
		<tr>
			<td>Examples</td>
			<td></td>
		</tr>
		<tr>
			<td>GitHub issue</td>
			<td>https://github.com/tdwg/tcs2/issues/22</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="dwc_cultivarEpithet"></a>Property dwc:cultivarEpithet</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
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
			<td><p>The cultivar epithet follows a well-formed botanical name. Only include the string of the epithet. i.e. omit the single quotes around cultivar  names, the word nullGroupnull that denotes cultivar group and the + sign  used in chimeras.</p></td>
		</tr>
		<tr>
			<td>Comments</td>
			<td></td>
		</tr>
		<tr>
			<td>Examples</td>
			<td></td>
		</tr>
		<tr>
			<td>GitHub issue</td>
			<td>https://github.com/tdwg/tcs2/issues/23</td>
		</tr>
	</tbody>
</table>

#### Nomenclatural Type

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="tcs_NomenclaturalType"></a>Class tcs:NomenclaturalType</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
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
			<td></td>
		</tr>
		<tr>
			<td>Comments</td>
			<td><p>A nomenclatural type fixes the usage of a name to the taxonomic group that  contains the type. One or more Nomenclatural Types make up the typification  of a Taxon Name. The Nomenclatural Type class is a decomposition of the  Darwin Core <code>typeStatus</code> into its individual components. It is the  intention that instances of this class can be referenced from both Taxon  Name (TCS) and Preserved Specimen (Darwin Core) records.</p></td>
		</tr>
		<tr>
			<td>Examples</td>
			<td></td>
		</tr>
		<tr>
			<td>GitHub issue</td>
			<td>https://github.com/tdwg/tcs2/issues/58</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="tcs_typifiedName"></a>Property tcs:typifiedName</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
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
			<td></td>
		</tr>
		<tr>
			<td>Comments</td>
			<td><p>The <code>typifiedName</code> property links the Nomenclatural Type back to the Taxon  Name. Also, when coming from the Preserved Specimen, the typified name is  the most important piece of information, because there is no point in  knowing what kind of type a specimen is without knowing for what name it  is the type. Therefore, <code>typifiedName</code> is a required property.</p></td>
		</tr>
		<tr>
			<td>Examples</td>
			<td></td>
		</tr>
		<tr>
			<td>GitHub issue</td>
			<td>https://github.com/tdwg/tcs2/issues/59</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="tcs_typeOfType"></a>Property tcs:typeOfType</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
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
			<td></td>
		</tr>
		<tr>
			<td>Comments</td>
			<td><p>This is an IRI property. In the absence of a TDWG controlled vocabulary,  it is recommended to use a value from the GBIF Nomenclatural Type Status  Vocabulary (https://rs.gbif.org/vocabulary/gbif/type_status.xml).</p></td>
		</tr>
		<tr>
			<td>Examples</td>
			<td></td>
		</tr>
		<tr>
			<td>GitHub issue</td>
			<td>https://github.com/tdwg/tcs2/issues/60</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="tcs_typeName"></a>Property tcs:typeName</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
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
			<td></td>
		</tr>
		<tr>
			<td>Comments</td>
			<td><p>Taxon names at ranks above species level can be typified by the name of a  lower taxon. Ultimately, by following the chain of type names, all names  resolve to a type species and thus a type specimen. One of <code>typeName</code> or  <code>typeSpecimen</code> is required.</p></td>
		</tr>
		<tr>
			<td>Examples</td>
			<td></td>
		</tr>
		<tr>
			<td>GitHub issue</td>
			<td>https://github.com/tdwg/tcs2/issues/61</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="tcs_typeSpecimen"></a>Property tcs:typeSpecimen</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
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
			<td><p>Names at ranks of family and below are typified by a specimen. This property  is mutually exclusive with <code>typeName</code>. This is an IRI property. One could  use the Darwin Core Preserved Specimen. One of <code>typeSpecimen</code> or <code>typeName</code>  is required.</p></td>
		</tr>
		<tr>
			<td>Comments</td>
			<td></td>
		</tr>
		<tr>
			<td>Examples</td>
			<td></td>
		</tr>
		<tr>
			<td>GitHub issue</td>
			<td>https://github.com/tdwg/tcs2/issues/62</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="tcs_typePublishedIn"></a>Property tcs:typePublishedIn</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
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
			<td></td>
		</tr>
		<tr>
			<td>Comments</td>
			<td><p><code>typePublishedIn</code> is relevant for lectotypes, neotypes, epitypes and  conserved types. For other kinds of type the publication where the type is  designated is the publication where the name was published.</p></td>
		</tr>
		<tr>
			<td>Examples</td>
			<td></td>
		</tr>
		<tr>
			<td>GitHub issue</td>
			<td>https://github.com/tdwg/tcs2/issues/63</td>
		</tr>
	</tbody>
</table>

<!-- termlist-footer.md ==>
