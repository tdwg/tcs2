# TCS Taxon Concept Relationship Type Vocabulary

**Note:** The content below is created dynamically from the
[tcsTaxonConceptRelationshipType.yaml](./tcsTaxonConceptRelationshipType.yaml) file. Please
do not edit the markdown directly, but make any changes in the YAML file.

## Index of terms

[Taxon Concept Relationship Type Concept Scheme](#tcsreltype_rt) | [Is Congruent With](#tcsreltype_rt001) | [Has proper subset](#tcsreltype_rt002) | [Is proper subset of](#tcsreltype_rt003) | [partiallyOverlaps](#tcsreltype_rt004) | [Is disjoint from](#tcsreltype_rt005) | [Intersects](#tcsreltype_rt006)

## Vocabulary

<table style="width:100%;">
	<thead>
		<tr>
			<th colspan="2">
            <a id="tcsreltype_rt"></a><span style="display:block;float:left;">tcsreltype:rt</span> 
            <span style="color:#ffffff;background-color:#617694;display:block;float:right;padding:0 5px;">[conceptscheme]</span>
            </th>
		</tr>
	</thead>
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

<table style="width:100%;">
	<thead>
		<tr>
			<th colspan="2">
            <a id="tcsreltype_rt001"></a><span style="display:block;float:left;">tcsreltype:rt001 (Is Congruent With)</span> 
            <span style="color:#ffffff;background-color:#617694;display:block;float:right;padding:0 5px;">[concept]</span>
            </th>
		</tr>
	</thead>
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
			<td>Comments</td>
			<td><p>The <code>isCongruentWith</code> relationship is symmetrical, so if A <code>isCongruentWith</code>  B then B <code>isCongruentWith</code> A, as well as transitive, so if A  <code>isCongruentWith</code> B and B <code>isCongruentWith</code> C it follows that A  <code>isCongruentWith</code> C.</p></td>
		</tr>
		<tr>
			<td>Controlled value</td>
			<td>isCongruentWith</td>
		</tr>
	</tbody>
</table>

<table style="width:100%;">
	<thead>
		<tr>
			<th colspan="2">
            <a id="tcsreltype_rt002"></a><span style="display:block;float:left;">tcsreltype:rt002 (Has proper subset)</span> 
            <span style="color:#ffffff;background-color:#617694;display:block;float:right;padding:0 5px;">[concept]</span>
            </th>
		</tr>
	</thead>
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
			<td>Comments</td>
			<td><p>The <code>hasProperSubset</code> relationship is not symmetric, its inverse  relationship being  <code>isProperSubsetOf</code>, so if A <code>hasProperSubset</code> B then B  <code>isProperSubsetOf</code> A. The <code>hasProperSubset</code> relationship  is transitive, so  if A <code>hasProperSubset</code> B and B <code>hasProperSubset</code> C it follows that A  <code>hasProperSubset</code> C.</p></td>
		</tr>
		<tr>
			<td>Controlled value</td>
			<td>hasProperSubset</td>
		</tr>
	</tbody>
</table>

<table style="width:100%;">
	<thead>
		<tr>
			<th colspan="2">
            <a id="tcsreltype_rt003"></a><span style="display:block;float:left;">tcsreltype:rt003 (Is proper subset of)</span> 
            <span style="color:#ffffff;background-color:#617694;display:block;float:right;padding:0 5px;">[concept]</span>
            </th>
		</tr>
	</thead>
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
			<td>Comments</td>
			<td><p>The <code>isProperSubsetOf</code> relationship is not symmetric, its inverse  relationship being  <code>hasProperSubset</code>, so if A <code>isProperSubsetOf</code> B then B  <code>hasProperSubset</code> A. The <code>isProperSubsetOf</code> relationship  is transitive, so  if A <code>isProperSubsetOf</code> B and B <code>isProperSubsetOf</code> C it follows that A  <code>isProperSubsetOf</code> C.</p></td>
		</tr>
		<tr>
			<td>Controlled value</td>
			<td>isProperSubsetOf</td>
		</tr>
	</tbody>
</table>

<table style="width:100%;">
	<thead>
		<tr>
			<th colspan="2">
            <a id="tcsreltype_rt004"></a><span style="display:block;float:left;">tcsreltype:rt004 (partiallyOverlaps)</span> 
            <span style="color:#ffffff;background-color:#617694;display:block;float:right;padding:0 5px;">[concept]</span>
            </th>
		</tr>
	</thead>
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
			<td>Comments</td>
			<td><p>The <code>partiallyOverlaps</code>  relationship is symmetrical, so if A  <code>partiallyOverlaps</code> B then B <code>partiallyOverlaps</code> A, but not transitive, so,  if A <code>partiallyOverlaps</code> B and B <code>partiallyOverlaps</code> C, it does not follow  that A <code>partiallyOverlaps</code> C.</p></td>
		</tr>
		<tr>
			<td>Controlled value</td>
			<td>partiallyOverlaps</td>
		</tr>
	</tbody>
</table>

<table style="width:100%;">
	<thead>
		<tr>
			<th colspan="2">
            <a id="tcsreltype_rt005"></a><span style="display:block;float:left;">tcsreltype:rt005 (Is disjoint from)</span> 
            <span style="color:#ffffff;background-color:#617694;display:block;float:right;padding:0 5px;">[concept]</span>
            </th>
		</tr>
	</thead>
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
			<td>Comments</td>
			<td><p>The <code>isDisjointFrom</code>  relationship is symmetrical, so if A <code>isDisjointFrom</code>  B then B <code>isDisjointFrom</code> A, but not transitive, so, if A <code>isDisjointFrom</code>  B and B <code>isDisjointFrom</code> C, it does not follow that A <code>isDisjointFrom</code> C.</p></td>
		</tr>
		<tr>
			<td>Controlled value</td>
			<td>isDisjointFrom</td>
		</tr>
	</tbody>
</table>

<table style="width:100%;">
	<thead>
		<tr>
			<th colspan="2">
            <a id="tcsreltype_rt006"></a><span style="display:block;float:left;">tcsreltype:rt006 (Intersects)</span> 
            <span style="color:#ffffff;background-color:#617694;display:block;float:right;padding:0 5px;">[concept]</span>
            </th>
		</tr>
	</thead>
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
			<td>Comments</td>
			<td><p><code>intersects</code> is the opposite of <code>isDisjointFrom</code> and the union of  <code>isCongruentWith</code>, <code>hasProperSubset</code>, <code>isProperSubsetOf</code> and  <code>partiallyOverlaps</code>, meaning it can be any of these relationships. This  relationship type can be used when the more precise nature of the  relationship is not known, for example when dealing with statements in  traditional synonymies.</p></td>
		</tr>
		<tr>
			<td>Controlled value</td>
			<td>intersects</td>
		</tr>
	</tbody>
</table>

<!-- termlist-footer.md ==>
