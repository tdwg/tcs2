# TCS Term List
### Index of terms

**classes**

[tcs:TaxonConcept](#tcs_TaxonConcept) | [tcs:TaxonRelationship](#tcs_TaxonRelationship) | [tcs:TaxonName](#tcs_TaxonName) | [tcs:NomenclaturalType](#tcs_NomenclaturalType)

**Taxon Concept**

[tcs:taxonConceptCategory](#tcs_taxonConceptCategory) | [tcs:taxonName](#tcs_taxonName) | [tcs:accordingTo](#tcs_accordingTo) | [tcs:accordingToString](#tcs_accordingToString) | [tcs:parent](#tcs_parent) | [tcs:synonym](#tcs_synonym) | [tcs:vernacularName](#tcs_vernacularName) | [tcs:characterCircumscription](#tcs_characterCircumscription) | [tcs:specimenCircumscription](#tcs_specimenCircumscription)

**Taxon Relationship**

[tcs:relationshipType](#tcs_relationshipType) | [tcs:subjectTaxonConcept](#tcs_subjectTaxonConcept) | [tcs:objectTaxonConcept](#tcs_objectTaxonConcept) | [tcs:relationshipAccordingTo](#tcs_relationshipAccordingTo)

**Taxon Name**

[tcs:taxonNameString](#tcs_taxonNameString) | [tcs:uninomial](#tcs_uninomial) | [tcs:taxonNameAuthorship](#tcs_taxonNameAuthorship) | [tcs:combinationAuthoship](#tcs_combinationAuthoship) | [tcs:basionymAuthorship](#tcs_basionymAuthorship) | [tcs:namePublishedIn](#tcs_namePublishedIn) | [tcs:microreference](#tcs_microreference) | [tcs:nomenclaturalCode](#tcs_nomenclaturalCode) | [tcs:nomenclaturalStatus](#tcs_nomenclaturalStatus) | [tcs:basionym](#tcs_basionym) | [tcs:replacedName](#tcs_replacedName) | [tcs:basedOn](#tcs_basedOn) | [tcs:conservedAgainst](#tcs_conservedAgainst) | [tcs:sanctionedBy](#tcs_sanctionedBy)

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
			<td><p>The underlying meaning, or referential extension, of a scientific name  as  stated by a particular author in a particular publication. It represents the  author's full-blown view of how the name reaches out to observed or  unobserved objects in nature (beyond statements about type specimens). It is  a direct reflection of what has been written, illustrated, and deposited by  a taxonomist, regardless of his or her theoretical orientation (Franz &amp; Peet  2009).</p></td>
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
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="tcs_taxonConceptCategory"></a>Property tcs:taxonConceptCategory</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
			<td>http://rs.tdwg.org/tcs/terms/taxonConceptCategory</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>http://www.w3.org/1999/02/22-rdf-syntax-ns#Property</td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Taxon Concept Category</td>
		</tr>
		<tr>
			<td></td>
			<td><b>required:</b> No — <b>repeatable:</b> No</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td><p>The category of Taxon Concept</p></td>
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
			<td><p>The Taxon Name for this Taxonomic Name Usage</p></td>
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
			<td><p>Reference to the source of this concept, which uses the Taxon Name in this sense (i.e. secundum, sensu).</p></td>
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
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="tcs_accordingToString"></a>Property tcs:accordingToString</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
			<td>http://rs.tdwg.org/tcs/terms/accordingToString</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>http://www.w3.org/1999/02/22-rdf-syntax-ns#Property</td>
		</tr>
		<tr>
			<td>Label</td>
			<td>According To String</td>
		</tr>
		<tr>
			<td></td>
			<td><b>required:</b> No — <b>repeatable:</b> No</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td><p>String representation of accordingTo</p></td>
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
			<td><p>The direct, most proximate higher-rank parent (in a classification).</p></td>
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
			<td><p>Name considered to apply to the same taxon as the accepted name (taxonName)</p></td>
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
			<td><p>Common or vernacular name, used as an alternative to the taxonomic name.</p></td>
		</tr>
		<tr>
			<td>Usage</td>
			<td></td>
		</tr>
		<tr>
			<td>Comments</td>
			<td><p>A name is only a vernacular name if it is used as an alternative to another name.</p></td>
		</tr>
		<tr>
			<td>Examples</td>
			<td></td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="tcs_characterCircumscription"></a>Property tcs:characterCircumscription</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
			<td>http://rs.tdwg.org/tcs/terms/characterCircumscription</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>http://www.w3.org/1999/02/22-rdf-syntax-ns#Property</td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Character Circumscription</td>
		</tr>
		<tr>
			<td></td>
			<td><b>required:</b> No — <b>repeatable:</b> Yes</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td><p>A set of taxonomic descriptions used to define this concept. May potentially hold descriptions according to the TDWG SDD schema, or any other, format.</p></td>
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
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="tcs_specimenCircumscription"></a>Property tcs:specimenCircumscription</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
			<td>http://rs.tdwg.org/tcs/terms/specimenCircumscription</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>http://www.w3.org/1999/02/22-rdf-syntax-ns#Property</td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Specimen Circumscription</td>
		</tr>
		<tr>
			<td></td>
			<td><b>required:</b> No — <b>repeatable:</b> Yes</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td><p>A set of specimens that are used to define the concept.</p></td>
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
	</tbody>
</table>

#### Taxon Relationship

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="tcs_TaxonRelationship"></a>Class tcs:TaxonRelationship</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
			<td>http://rs.tdwg.org/tcs/terms/TaxonRelationship</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>http://www.w3.org/2000/01/rdf-schema#Class</td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Taxon Relationship</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td><p>Assertion of a relationship between two taxa</p></td>
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
			<td><p>The type of relationship that is asserted.</p></td>
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
			<td><p>The subject Taxon Concept in this relationship.</p></td>
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
			<td><p>The object or target Taxon Concept in this relationship.</p></td>
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
			<td><p>Reference for the taxon relationship assertion</p></td>
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
			<td><p>A name used as a label for a taxon or taxonomic group.</p></td>
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
			<td><p>The complete uninomial, binomial or trinomial name without any authority or  year components.</p></td>
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
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="tcs_uninomial"></a>Property tcs:uninomial</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
			<td>http://rs.tdwg.org/tcs/terms/uninomial</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>http://www.w3.org/1999/02/22-rdf-syntax-ns#Property</td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Uninomial</td>
		</tr>
		<tr>
			<td></td>
			<td><b>required:</b> No — <b>repeatable:</b> No</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td><p>Single-word name string for a name of generic or higher rank</p></td>
		</tr>
		<tr>
			<td>Usage</td>
			<td><p>This property should be used for any single word names. These include  family, genus, infrafamilial, and suprafamilial names. Note that this  property should be used for generic names. The genus property should only  be used for names below rank of genus.</p></td>
		</tr>
		<tr>
			<td>Comments</td>
			<td></td>
		</tr>
		<tr>
			<td>Examples</td>
			<td></td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="tcs_taxonNameAuthorship"></a>Property tcs:taxonNameAuthorship</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
			<td>http://rs.tdwg.org/tcs/terms/taxonNameAuthorship</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>http://www.w3.org/1999/02/22-rdf-syntax-ns#Property</td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Taxon Name Authorship</td>
		</tr>
		<tr>
			<td></td>
			<td><b>required:</b> No — <b>repeatable:</b> No</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td><p>The full code-appropriate authorship string for the Taxon Name.</p></td>
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
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="tcs_combinationAuthoship"></a>Property tcs:combinationAuthoship</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
			<td>http://rs.tdwg.org/tcs/terms/combinationAuthoship</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>http://www.w3.org/1999/02/22-rdf-syntax-ns#Property</td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Combination Authorship</td>
		</tr>
		<tr>
			<td></td>
			<td><b>required:</b> No — <b>repeatable:</b> No</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td><p>The full code-appropriate authorship string for the Taxon Name.</p></td>
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
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="tcs_basionymAuthorship"></a>Property tcs:basionymAuthorship</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
			<td>http://rs.tdwg.org/tcs/terms/basionymAuthorship</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>http://www.w3.org/1999/02/22-rdf-syntax-ns#Property</td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Basionym Authorship</td>
		</tr>
		<tr>
			<td></td>
			<td><b>required:</b> No — <b>repeatable:</b> No</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td><p>Authorship of the basionym</p></td>
		</tr>
		<tr>
			<td>Usage</td>
			<td><p>Note that the basionym is another name (Taxon Name) and that names cannot be their own basionym. The basionym authorship is always in parentheses in  both botanical and zoological names.</p></td>
		</tr>
		<tr>
			<td>Comments</td>
			<td></td>
		</tr>
		<tr>
			<td>Examples</td>
			<td></td>
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
			<td><p>Publication where the taxonomic name was first published.</p></td>
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
			<td><p>Refers to precise location within a larger work.</p></td>
		</tr>
		<tr>
			<td>Comments</td>
			<td></td>
		</tr>
		<tr>
			<td>Examples</td>
			<td></td>
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
			<td></td>
		</tr>
		<tr>
			<td>Examples</td>
			<td></td>
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
			<td></td>
		</tr>
		<tr>
			<td>Examples</td>
			<td></td>
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
			<td></td>
		</tr>
		<tr>
			<td>Examples</td>
			<td></td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="tcs_replacedName"></a>Property tcs:replacedName</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
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
			<td></td>
		</tr>
		<tr>
			<td>Examples</td>
			<td></td>
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
			<td><p>Name(s) against which this name is conserved</p></td>
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
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="tcs_sanctionedBy"></a>Property tcs:sanctionedBy</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
			<td>http://rs.tdwg.org/tcs/terms/sanctionedBy</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>http://www.w3.org/1999/02/22-rdf-syntax-ns#Property</td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Sanctioned By</td>
		</tr>
		<tr>
			<td></td>
			<td><b>required:</b> No — <b>repeatable:</b> No</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td><p>Reference to the work in which this name was sanctioned.</p></td>
		</tr>
		<tr>
			<td>Usage</td>
			<td></td>
		</tr>
		<tr>
			<td>Comments</td>
			<td><p>This is a reference to a publication, not a person.</p></td>
		</tr>
		<tr>
			<td>Examples</td>
			<td></td>
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
			<td><p>Element to which <code>TaxonName</code> permanently attached</p></td>
		</tr>
		<tr>
			<td>Usage</td>
			<td></td>
		</tr>
		<tr>
			<td>Comments</td>
			<td><p>One or more <code>NomenclaturalType</code>s make up the typification of a <code>TaxonName</code>.</p></td>
		</tr>
		<tr>
			<td>Examples</td>
			<td></td>
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
			<td><b>required:</b> No — <b>repeatable:</b> No</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td><p>The <code>TaxonName</code> for which this is <code>NomenclaturalType</code></p></td>
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
			<td><p>The kind of type this specimen is e.g. paratype, isotype, holotype etc.</p></td>
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
			<td><p>TaxonNames at ranks above species level are typified by the name of a lower taxon. Ultimately, by following the chain of type names, all names resolve  to a type species and so a type specimen.</p></td>
		</tr>
		<tr>
			<td>Examples</td>
			<td></td>
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
			<td><p>TaxonNames at ranks of family and below are typified by a specimen. This property is mutually exclusive with typeName.</p></td>
		</tr>
		<tr>
			<td>Comments</td>
			<td></td>
		</tr>
		<tr>
			<td>Examples</td>
			<td></td>
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
			<td><p>This is relevant for <code>lectotype</code>, <code>neotype</code>, <code>epitype</code> and conserved types. For other types of type the publication where the type is nominated is the  publication where the name was published.</p></td>
		</tr>
		<tr>
			<td>Comments</td>
			<td></td>
		</tr>
		<tr>
			<td>Examples</td>
			<td></td>
		</tr>
	</tbody>
</table>

<!-- termlist-footer.md ==>
