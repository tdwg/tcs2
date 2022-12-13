# TCS Taxon Concept Relationship Type Vocabulary

**Note:** The content below is created dynamically from the
[tcsTaxonConceptRelationshipType.yaml](./tcsTaxonConceptRelationshipType.yaml) file. Please
do not edit the markdown directly, but make any changes in the YAML file.

## Index of terms

[Taxon Concept Relationship Type Concept Scheme](##user-content-tcsreltypert) | [Is Congruent With](##user-content-tcsreltypert001) | [Has proper subset](##user-content-tcsreltypert002) | [Is proper subset of](##user-content-tcsreltypert003) | [partiallyOverlaps](##user-content-tcsreltypert004) | [Is disjoint from](##user-content-tcsreltypert005) | [Intersects](##user-content-tcsreltypert006)

### tcsreltype:rt

<table style="width:100%;">
	<tbody>
		<tr>
			<td>Identifier</td>
			<td>http://rs.tdwg.org/tcs-taxon-concept-relationship-type/values/rt</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>http://www.w3.org/2004/02/skos/core#ConceptScheme</td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Taxon Concept Relationship Type Concept Scheme</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td><p>A SKOS Concept Scheme for controlled values for  <code>tcs:taxonConceptRelationshipType</code></p></td>
		</tr>
		<tr>
			<td>Controlled value</td>
			<td>None</td>
		</tr>
	</tbody>
</table>

### tcsreltype:rt001

<table style="width:100%;">
	<tbody>
		<tr>
			<td>Identifier</td>
			<td>http://rs.tdwg.org/tcs-taxon-concept-relationship-type/values/rt001</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>http://www.w3.org/2004/02/skos/core#Concept</td>
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
			<td>Controlled value</td>
			<td>isCongruentWith</td>
		</tr>
	</tbody>
</table>


**Comments**

The `isCongruentWith` relationship is symmetrical, so if A `isCongruentWith`  B then B `isCongruentWith` A, as well as transitive, so if A  `isCongruentWith` B and B `isCongruentWith` C it follows that A  `isCongruentWith` C.

### tcsreltype:rt002

<table style="width:100%;">
	<tbody>
		<tr>
			<td>Identifier</td>
			<td>http://rs.tdwg.org/tcs-taxon-concept-relationship-type/values/rt002</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>http://www.w3.org/2004/02/skos/core#Concept</td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Has proper subset</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td><p>The subject taxon concept has a more inclusive taxonomic meaning than the object taxon concept</p></td>
		</tr>
		<tr>
			<td>Controlled value</td>
			<td>hasProperSubset</td>
		</tr>
	</tbody>
</table>


**Comments**

The `hasProperSubset` relationship is not symmetric, its inverse  relationship being  `isProperSubsetOf`, so if A `hasProperSubset` B then B  `isProperSubsetOf` A. The `hasProperSubset` relationship  is transitive, so  if A `hasProperSubset` B and B `hasProperSubset` C it follows that A  `hasProperSubset` C.

### tcsreltype:rt003

<table style="width:100%;">
	<tbody>
		<tr>
			<td>Identifier</td>
			<td>http://rs.tdwg.org/tcs-taxon-concept-relationship-type/values/rt003</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>http://www.w3.org/2004/02/skos/core#Concept</td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Is proper subset of</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td><p>The subject taxon concept has a less inclusive taxonomic meaning than the  object taxon concept</p></td>
		</tr>
		<tr>
			<td>Controlled value</td>
			<td>isProperSubsetOf</td>
		</tr>
	</tbody>
</table>


**Comments**

The `isProperSubsetOf` relationship is not symmetric, its inverse  relationship being  `hasProperSubset`, so if A `isProperSubsetOf` B then B  `hasProperSubset` A. The `isProperSubsetOf` relationship  is transitive, so  if A `isProperSubsetOf` B and B `isProperSubsetOf` C it follows that A  `isProperSubsetOf` C.

### tcsreltype:rt004

<table style="width:100%;">
	<tbody>
		<tr>
			<td>Identifier</td>
			<td>http://rs.tdwg.org/tcs-taxon-concept-relationship-type/values/rt004</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>http://www.w3.org/2004/02/skos/core#Concept</td>
		</tr>
		<tr>
			<td>Label</td>
			<td>partiallyOverlaps</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td><p>The subject and object taxon concepts have partially overlapping taxonomic  meanings, <em>i.e.</em> they have some members in common, but each concept in  addition has members that are not included in the other concept</p></td>
		</tr>
		<tr>
			<td>Controlled value</td>
			<td>partiallyOverlaps</td>
		</tr>
	</tbody>
</table>


**Comments**

The `partiallyOverlaps`  relationship is symmetrical, so if A  `partiallyOverlaps` B then B `partiallyOverlaps` A, but not transitive, so,  if A `partiallyOverlaps` B and B `partiallyOverlaps` C, it does not follow  that A `partiallyOverlaps` C.

### tcsreltype:rt005

<table style="width:100%;">
	<tbody>
		<tr>
			<td>Identifier</td>
			<td>http://rs.tdwg.org/tcs-taxon-concept-relationship-type/values/rt005</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>http://www.w3.org/2004/02/skos/core#Concept</td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Is disjoint from</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td><p>The subject and objects taxon concepts have non-overlapping taxonomic  meanings, <em>i.e.</em> they do not have any members in common</p></td>
		</tr>
		<tr>
			<td>Controlled value</td>
			<td>isDisjointFrom</td>
		</tr>
	</tbody>
</table>


**Comments**

The `isDisjointFrom`  relationship is symmetrical, so if A `isDisjointFrom`  B then B `isDisjointFrom` A, but not transitive, so, if A `isDisjointFrom`  B and B `isDisjointFrom` C, it does not follow that A `isDisjointFrom` C.

### tcsreltype:rt006

<table style="width:100%;">
	<tbody>
		<tr>
			<td>Identifier</td>
			<td>http://rs.tdwg.org/tcs-taxon-concept-relationship-type/values/rt006</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>http://www.w3.org/2004/02/skos/core#Concept</td>
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
			<td>Controlled value</td>
			<td>intersects</td>
		</tr>
	</tbody>
</table>


**Comments**

`intersects` is the opposite of `isDisjointFrom` and the union of  `isCongruentWith`, `hasProperSubset`, `isProperSubsetOf` and  `partiallyOverlaps`, meaning it can be any of these relationships. This  relationship type can be used when the more precise nature of the  relationship is not known, for example when dealing with statements in  traditional synonymies.

<!-- termlist-footer.md ==>
