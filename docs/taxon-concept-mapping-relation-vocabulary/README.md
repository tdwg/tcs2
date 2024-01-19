# TCS Taxon Comcept Mapping Relation Vocabulary

**Note:** The content below is created dynamically from the
[tcsTaxonConceptMappingRelation.yaml](./tcsTaxonConceptMappingRelation.yaml) file. Please
do not edit the markdown directly, but make any changes in the YAML file.

## Index of terms

[Taxon Relationship Type Concept Scheme](#tcreltype) | [Is Congruent With](#tcreltypeiscongruentwith) | [Has proper subset](#tcreltypeincludes) | [Is proper subset of](#tcreltypeisincludedin) | [partiallyOverlaps](#tcreltypepartiallyoverlaps) | [Is disjoint from](#tcreltypeisdisjointfrom) | [Intersects](#tcreltypeintersects)

### tcreltype:

<table style="width:100%;">
	<tbody>
		<tr>
			<td>Identifier</td>
			<td>http://rs.tdwg.org/tcs-taxon-concept-mapping-relation/values/</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>http://www.w3.org/2004/02/skos/core#ConceptScheme</td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Taxon Relationship Type Concept Scheme</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td><p>A SKOS Concept Scheme for controlled values for  <code>tcs:TaxonConceptMappingType</code></p></td>
		</tr>
		<tr>
			<td>Controlled value</td>
			<td>None</td>
		</tr>
	</tbody>
</table>


**Comments**

Publications used in examples:

```turtle
<http://www.herbarium.unc.edu/FloraArchives/WeakleyFlora_2006-Jan.pdf> 
    a bibo:Document ;
    dcterms:bibliographicCitation """A.S. Weakley, Flora of the Carolinas, 
            Virginia, Georgia, and Surrounding Areas, Working Draft of 6 
            January, 2006, University of North Carolina Herbarium, Chapel 
            Hill, 2006, http://www.herbarium.unc.edu/FloraArchives/WeakleyFlora_
            2006-Jan.pdf.""" .

<http://bonap.net/napa#2014> a bibo:Website ;
    dcterms:bibliographicCitation """J.T. Kartesz, The Biota of North America 
            Program (BONAP), 2014, North American Plant Atlas, Chapel Hill, NC, 
            2014, http://bonap.net/napa.""" .

<https://doi.org/10.3233/SW-160220> a bibo:AcademicArticle ;
    dcterms:bibliographicCitation """Franz NM, Chen M, Kianmajd P, Yu S, Bowers 
            S, Weakley AS, Ludäscher B (2016) Names are not good enough: 
            Reasoning over taxonomic change in the Andropogon complex 1. 
            Semantic Web 7, 645–667. doi:10.3233/SW-160220.""" .
```
[&lsqb;TaxonConceptMappingRelation-publications.ttl&rsqb;](examples/TaxonConceptMappingRelation-publications.ttl)

### tcreltype:isCongruentWith

<table style="width:100%;">
	<tbody>
		<tr>
			<td>Identifier</td>
			<td>http://rs.tdwg.org/tcs-taxon-concept-mapping-relation/values/isCongruentWith</td>
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
		<tr>
			<td>GitHub issue</td>
			<td>https://github.com/tdwg/tcs2/issues/52</td>
		</tr>
	</tbody>
</table>


**Comments**

The `isCongruentWith` relationship is symmetrical, so if A `isCongruentWith`  B then B `isCongruentWith` A, as well as transitive, so if A  `isCongruentWith` B and B `isCongruentWith` C it follows that A  `isCongruentWith` C.

![](../media/taxon-relationship-type-is-congruent-with.jpg)

This relationship can also be written as the formula **A &cong; B** or **A == B**.


**Examples**


```turtle
# Andropogon capillipes sec. BONAP 2014 is congruent with Andropogon capillipes sec. Weakley 2006
[] a :TaxonConceptMapping ;
    :mappingRelation <http://rs.tdwg.org/tcs-taxon-concept-mapping-relation/values/isCongruentWith> ;
    :subjectTaxonConcept [ a :TaxonConcept ;
        dcterms:title "Andropogon capillipes sec. BONAP 2014" ;
        :taxonName <https://www.ipni.org/n/12781-2> ;
        :accordingTo <http://bonap.net/napa#2014> ] ;
    :objectTaxonConcept [ a :TaxonConcept ;
        dcterms:title "Andropogon capillipes sec. Weakley 2006" ;
        :taxonName <https://www.ipni.org/n/12781-2> ;
        :accordingTo <http://www.herbarium.unc.edu/FloraArchives/WeakleyFlora_2006-Jan.pdf> ] ;
    :mappingAccordingTo <https://doi.org/10.3233/SW-160220> .

<https://www.ipni.org/n/12781-2> a :TaxonName ;
    :taxonNameString "Andropogon capillipes" ;
    dwc:scientificNameAuthorship "Nash" .
```

[&lsqb;TaxonConceptMappingRelation-isCongruentWith.ttl&rsqb;](../../examples/TaxonConceptMappingRelation-isCongruentWith.ttl)&nbsp;[&lsqb;TaxonConceptMappingRelation-isCongruentWith.jsonld&rsqb;](../../examples/TaxonConceptMappingRelation-isCongruentWith.jsonld)

### tcreltype:includes

<table style="width:100%;">
	<tbody>
		<tr>
			<td>Identifier</td>
			<td>http://rs.tdwg.org/tcs-taxon-concept-mapping-relation/values/includes</td>
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
			<td>includes</td>
		</tr>
		<tr>
			<td>GitHub issue</td>
			<td>https://github.com/tdwg/tcs2/issues/53</td>
		</tr>
	</tbody>
</table>


**Comments**

The `includes` relationship is not symmetric, its inverse  relationship being  `isIncludedIn`, so if A `includes` B then B  `isIncludedIn` A. The `includes` relationship  is transitive, so  if A `includes` B and B `includes` C it follows that A  `includes` C.

![](../media/taxon-relationship-type-includes.jpg)

This relation type can also be written as the formula **A > B**.


**Examples**


```turtle
# Andropogon glomeratus sec. BONAP 2014 has a proper subset Andropogon tenuispatheus sec. Weakley 2006
[] a :TaxonConceptMapping ;
    :mappingRelation <http://rs.tdwg.org/tcs-taxon-concept-mapping-relation/values/includes> ;
    :subjectTaxonConcept [ a :TaxonConcept ;
        dcterms:title "Andropogon glomeratus sec. BONAP 2014" ;
        :taxonName <https://www.ipni.org/n/12850-2> ;
        :accordingTo <http://bonap.net/napa#2014> ] ;
    :objectTaxonConcept [ a :TaxonConcept ;
        dcterms:title "Andropogon tenuispatheus sec. Weakley 2006" ;
        :taxonName <https://www.ipni.org/n/13093-2> ;
        :accordingTo <http://www.herbarium.unc.edu/FloraArchives/WeakleyFlora_2006-Jan.pdf> ] ;
    :mappingAccordingTo <https://doi.org/10.3233/SW-160220> .

<https://www.ipni.org/n/12850-2> a :TaxonName ;
    :taxonNameString "Andropogon glomeratus" ;
    dwc:scientificNameAuthorship "Britton, Sterns & Poggenb." .

<https://www.ipni.org/n/13093-2> a :TaxonName ;
    :taxonNameString "Andropogon tenuispatheus" ;
    dwc:scientificNameAuthorship "Nash" .
```

[&lsqb;TaxonConceptMappingRelation-includes.ttl&rsqb;](../../examples/TaxonConceptMappingRelation-includes.ttl)&nbsp;[&lsqb;TaxonConceptMappingRelation-includes.jsonld&rsqb;](../../examples/TaxonConceptMappingRelation-includes.jsonld)

### tcreltype:isIncludedIn

<table style="width:100%;">
	<tbody>
		<tr>
			<td>Identifier</td>
			<td>http://rs.tdwg.org/tcs-taxon-concept-mapping-relation/values/isIncludedIn</td>
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
			<td>isIncludedIn</td>
		</tr>
		<tr>
			<td>GitHub issue</td>
			<td>https://github.com/tdwg/tcs2/issues/54</td>
		</tr>
	</tbody>
</table>


**Comments**

The `isIncludedIn` relationship is not symmetric, its inverse  relationship being  `includes`, so if A `isIncludedIn` B then B  `includes` A. The `isIncludedIn` relationship  is transitive, so  if A `isIncludedIn` B and B `isIncludedIn` C it follows that A  `isIncludedIn` C.

![](../media/taxon-relationship-type-is-included-in.jpg)

This relation type can also be written as the formula **A < B**.


**Examples**


```turtle
# Andropogon hirsutior sec. BONAP 2014 is a proper subset of Andropogon glomeratus sec. Weakley 2006
[] a :TaxonConceptMapping ;
    :mappingRelation <http://rs.tdwg.org/tcs-taxon-concept-mapping-relation/values/isIncludedIn> ;
    :subjectTaxonConcept [ a :TaxonConcept ;
        dcterms:title "Andropogon hirsutior sec. BONAP 2014" ;
        :taxonName <https://www.ipni.org/n/60458078-2> ;
        :accordingTo <http://bonap.net/napa#2014> ] ;
    :objectTaxonConcept [ a :TaxonConcept ;
        dcterms:title "Andropogon glomeratus sec. Weakley 2006" ;
        :taxonName <https://www.ipni.org/n/12850-2> ;
        :accordingTo <http://www.herbarium.unc.edu/FloraArchives/WeakleyFlora_2006-Jan.pdf> ] ;
    :mappingAccordingTo <https://doi.org/10.3233/SW-160220> .

<https://www.ipni.org/n/60458078-2> a :TaxonName ;
    :taxonNameString "Andropogon hirsutior" ;
    dwc:scientificNameAuthorship "(Hack.) Weakley & LeBlond" .

<https://www.ipni.org/n/12850-2> a :TaxonName ;
    :taxonNameString "Andropogon glomeratus" ;
    dwc:scientificNameAuthorship "Britton, Sterns & Poggenb." .
```

[&lsqb;TaxonConceptMappingRelation-isIncludedIn.ttl&rsqb;](../../examples/TaxonConceptMappingRelation-isIncludedIn.ttl)&nbsp;[&lsqb;TaxonConceptMappingRelation-isIncludedIn.jsonld&rsqb;](../../examples/TaxonConceptMappingRelation-isIncludedIn.jsonld)

### tcreltype:partiallyOverlaps

<table style="width:100%;">
	<tbody>
		<tr>
			<td>Identifier</td>
			<td>http://rs.tdwg.org/tcs-taxon-concept-mapping-relation/values/partiallyOverlaps</td>
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
		<tr>
			<td>GitHub issue</td>
			<td>https://github.com/tdwg/tcs2/issues/55</td>
		</tr>
	</tbody>
</table>


**Comments**

The `partiallyOverlaps`  relationship is symmetrical, so if A  `partiallyOverlaps` B then B `partiallyOverlaps` A, but not transitive, so,  if A `partiallyOverlaps` B and B `partiallyOverlaps` C, it does not follow  that A `partiallyOverlaps` C.

![](../media/taxon-relationship-type-partially-overlaps.jpg)

This relationship can also be written as the formula **A >< B**.


**Examples**


```turtle
# Andropogon glomeratus sec. BONAP 2014 partially overlaps Andropogon glomeratus
# sec. Weakley 2006
[] a :TaxonConceptMapping ;
    :mappingRelation <http://rs.tdwg.org/tcs-taxon-concept-mapping-relation/values/partiallyOverlaps> ;
    :subjectTaxonConcept [ a :TaxonConcept ;
        dcterms:title "Andropogon glomeratus sec. BONAP 2014" ;
        :taxonName <https://www.ipni.org/n/12850-2> ;
        :accordingTo <http://bonap.net/napa#2014> ] ;
    :objectTaxonConcept [ a :TaxonConcept ;
        dcterms:title "Andropogon glomeratus sec. Weakley 2006" ;
        :taxonName <https://www.ipni.org/n/12850-2> ;
        :accordingTo <http://www.herbarium.unc.edu/FloraArchives/WeakleyFlora_2006-Jan.pdf> ] ;
    :mappingAccordingTo <https://doi.org/10.3233/SW-160220> .

<https://www.ipni.org/n/12850-2> a :TaxonName ;
    :taxonNameString "Andropogon glomeratus" ;
    dwc:scientificNameAuthorship "Britton, Sterns & Poggenb." .
```

[&lsqb;TaxonConceptMappingRelation-partiallyOverlaps.ttl&rsqb;](../../examples/TaxonConceptMappingRelation-partiallyOverlaps.ttl)&nbsp;[&lsqb;TaxonConceptMappingRelation-partiallyOverlaps.jsonld&rsqb;](../../examples/TaxonConceptMappingRelation-partiallyOverlaps.jsonld)

### tcreltype:isDisjointFrom

<table style="width:100%;">
	<tbody>
		<tr>
			<td>Identifier</td>
			<td>http://rs.tdwg.org/tcs-taxon-concept-mapping-relation/values/isDisjointFrom</td>
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
		<tr>
			<td>GitHub issue</td>
			<td>https://github.com/tdwg/tcs2/issues/56</td>
		</tr>
	</tbody>
</table>


**Comments**

The `isDisjointFrom`  relationship is symmetrical, so if A `isDisjointFrom`  B then B `isDisjointFrom` A, but not transitive, so, if A `isDisjointFrom`  B and B `isDisjointFrom` C, it does not follow that A `isDisjointFrom` C.

![](../media/taxon-relationship-type-is-disjoint-from.jpg)

This relationship can also be written as the formula **A | B**.


**Examples**


```turtle
# Andropogon glaucopsis sec. BONAP 2014 is disjoint from Andropogon virginicus sec. Weakley 2006
[] a :TaxonConceptMapping ;
    :mappingRelation <http://rs.tdwg.org/tcs-taxon-concept-mapping-relation/values/isDisjointFrom> ;
    :subjectTaxonConcept [ a :TaxonConcept ;
        dcterms:title "Andropogon glaucopsis sec. BONAP 2014" ;
        :taxonName <https://www.ipni.org/n/387942-1> ;
        :accordingTo <http://bonap.net/napa#2014> ] ;
    :objectTaxonConcept [ a :TaxonConcept ;
        dcterms:title "Andropogon virginicus sec. Weakley 2006" ;
        :taxonName <https://www.ipni.org/n/388740-1> ;
        :accordingTo <http://www.herbarium.unc.edu/FloraArchives/WeakleyFlora_2006-Jan.pdf> ] ;
    :mappingAccordingTo <https://doi.org/10.3233/SW-160220> .

<https://www.ipni.org/n/387942-1> a :TaxonName ;
    :taxonNameString "Andropogon glaucopsis" ;
    dwc:scientificNameAuthorship "Steud." .

<https://www.ipni.org/n/388740-1> a :TaxonName ;
    :taxonNameString "Andropogon virginicus" ;
    dwc:scientificNameAuthorship "L." .
```

[&lsqb;TaxonConceptMappingRelation-isDisjointFrom.ttl&rsqb;](../../examples/TaxonConceptMappingRelation-isDisjointFrom.ttl)&nbsp;[&lsqb;TaxonConceptMappingRelation-isDisjointFrom.jsonld&rsqb;](../../examples/TaxonConceptMappingRelation-isDisjointFrom.jsonld)

### tcreltype:intersects

<table style="width:100%;">
	<tbody>
		<tr>
			<td>Identifier</td>
			<td>http://rs.tdwg.org/tcs-taxon-concept-mapping-relation/values/intersects</td>
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
		<tr>
			<td>GitHub issue</td>
			<td>https://github.com/tdwg/tcs2/issues/57</td>
		</tr>
	</tbody>
</table>


**Comments**

`intersects` is the opposite of `isDisjointFrom` and the union of  `isCongruentWith`, `includes`, `isIncludedIn` and  `partiallyOverlaps`, meaning it can be any of these relationships. This  relationship type can be used when the more precise nature of the  relationship is not known, for example when dealing with statements in  traditional synonymies.

<!-- footer -->