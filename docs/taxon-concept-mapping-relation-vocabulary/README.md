# TCS Taxon Concept Mapping Relation vocabulary

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

[&lsqb;TaxonConceptMappingRelation-isCongruentWith-1.ttl&rsqb;](../../examples/TaxonConceptMappingRelation-isCongruentWith-1.ttl)&nbsp;[&lsqb;TaxonConceptMappingRelation-isCongruentWith-1.jsonld&rsqb;](../../examples/TaxonConceptMappingRelation-isCongruentWith-1.jsonld)


```turtle
[] a tcs:TaxonConceptMapping ;
    tcs:mappingAccordingTo <https://doi.org/10.1002/tax.613003> ;
    tcs:mappingRelation <http://rs.tdwg.org/tcs-taxon-concept-mapping-relation/values/isCongruentWith> ;
    tcs:subjectTaxonConcept _:b0 ;
    tcs:objectTaxonConcept [ a tcs:TaxonConcept ;
            dcterms:title "Aspleniaceae sec. Christenhusz & al. 2011" ;
            tcs:accordingTo <https://doi.org/10.11646/phytotaxa.19.1.2> ;
            tcs:taxonName <https://ipni.org/n/30001382-2> ] .

[] a tcs:TaxonConceptMapping ;
    tcs:mappingAccordingTo <https://doi.org/10.1002/tax.613003> ;
    tcs:mappingRelation <http://rs.tdwg.org/tcs-taxon-concept-mapping-relation/values/isCongruentWith> ;
    tcs:subjectTaxonConcept _:b0 ;
    tcs:objectTaxonConcept [ a tcs:TaxonConcept ;
            dcterms:title "Aspleniaceae sec. Smith & al. 2006" ;
            tcs:accordingTo <https://doi.org/10.2307/25065646> ;
            tcs:acceptedName <https://ipni.org/n/30001382-2> ] .

[] a tcs:TaxonConceptMapping ;
    tcs:mappingAccordingTo <https://doi.org/10.1002/tax.613003> ;
    tcs:mappingRelation <http://rs.tdwg.org/tcs-taxon-concept-mapping-relation/values/isCongruentWith> ;
    tcs:subjectTaxonConcept _:b0 ;
    tcs:objectTaxonConcept [ a tcs:TaxonConcept ;
            dcterms:title "Aspleniaceae sec. Pichi Sermolli 1977" ;
            tcs:accordingTo <https://doi.org/10.1080/00837792.1977.10670077> ;
            tcs:taxonName <https://ipni.org/n/30001382-2> ] .

[] a tcs:TaxonConceptMapping ;
    tcs:mappingAccordingTo <https://doi.org/10.1002/tax.613003> ;
    tcs:mappingRelation <http://rs.tdwg.org/tcs-taxon-concept-mapping-relation/values/isCongruentWith> ;
    tcs:subjectTaxonConcept _:b0 ;
    tcs:objectTaxonConcept [ a tcs:TaxonConcept ;
            dcterms:title "Aspleniaceae sec. Nayar 1970" ;
            tcs:accordingTo <https://doi.org/10.2307/1217958> ;
            tcs:taxonName <https://ipni.org/n/30001382-2> ] .
```

[&lsqb;TaxonConceptMappingRelation-isCongruentWith-2.ttl&rsqb;](../../examples/TaxonConceptMappingRelation-isCongruentWith-2.ttl)&nbsp;[&lsqb;TaxonConceptMappingRelation-isCongruentWith-2.jsonld&rsqb;](../../examples/TaxonConceptMappingRelation-isCongruentWith-2.jsonld)

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

[&lsqb;TaxonConceptMappingRelation-includes-1.ttl&rsqb;](../../examples/TaxonConceptMappingRelation-includes-1.ttl)&nbsp;[&lsqb;TaxonConceptMappingRelation-includes-1.jsonld&rsqb;](../../examples/TaxonConceptMappingRelation-includes-1.jsonld)


```turtle
[] a tcs:TaxonConceptMapping ;
    tcs:mappingAccordingTo <https://doi.org/10.1002/tax.613003> ;
    tcs:mappingRelation <http://rs.tdwg.org/tcs-taxon-concept-mapping-relation/values/includess> ;
    tcs:subjectTaxonConcept [ a tcs:TaxonConcept ;
            dcterms:title "Diplaziopsidaceae sec. Rothfels & al. 2012" ;
            tcs:accordingTo <https://doi.org/10.1002/tax.613003> ;
            tcs:taxonName <https://ipni.org/n/77110538-1> ] ;
    tcs:objectTaxonConcept [ a tcs:TaxonConcept ;
            dcterms:title "Diplaziopsidaceae sec. Christenhusz & al. 2011" ;
            tcs:accordingTo <https://doi.org/10.11646/phytotaxa.19.1.2> ;
            tcs:taxonName <https://ipni.org/n/77110538-1> ] .
```

[&lsqb;TaxonConceptMappingRelation-includes-2.ttl&rsqb;](../../examples/TaxonConceptMappingRelation-includes-2.ttl)&nbsp;[&lsqb;TaxonConceptMappingRelation-includes-2.jsonld&rsqb;](../../examples/TaxonConceptMappingRelation-includes-2.jsonld)

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

[&lsqb;TaxonConceptMappingRelation-isIncludedIn-1.ttl&rsqb;](../../examples/TaxonConceptMappingRelation-isIncludedIn-1.ttl)&nbsp;[&lsqb;TaxonConceptMappingRelation-isIncludedIn-1.jsonld&rsqb;](../../examples/TaxonConceptMappingRelation-isIncludedIn-1.jsonld)


```turtle
[] a tcs:TaxonConceptMapping ;
    tcs:mappingAccordingTo <https://doi.org/10.1002/tax.613003> ;
    tcs:mappingRelation <http://rs.tdwg.org/tcs-taxon-concept-mapping-relation/values/isIncludedIn> ;
    tcs:subjectTaxonConcept _:b1 ;
    tcs:objectTaxonConcept [ a tcs:TaxonConcept ;
            dcterms:title "Athyriaceae sec. Christenhusz & al. 2011" ;
            tcs:accordingTo <https://doi.org/10.11646/phytotaxa.19.1.2> ;
            tcs:taxonName <https://ipni.org/n/30000361-2> ] .

_:b1 a tcs:TaxonConcept ;
    dcterms:title "Athyriaceae sec. Rothfels & al. 2012" ;
    tcs:accordingTo <https://doi.org/10.1002/tax.613003> ;
    tcs:taxonName <https://ipni.org/n/30000361-2> .

[] a tcs:TaxonConceptMapping ;
    tcs:mappingAccordingTo <https://doi.org/10.1002/tax.613003> ;
    tcs:mappingRelation <http://rs.tdwg.org/tcs-taxon-concept-mapping-relation/values/isIncludedIn> ;
    tcs:subjectTaxonConcept _:b1 ;
    tcs:objectTaxonConcept [ a tcs:TaxonConcept ;
            dcterms:title "Woodsiaceae sec. Smith & al. 2006" ;
            tcs:accordingTo <https://doi.org/10.2307/25065646> ;
            tcs:taxonName <https://ipni.org/n/30000455-2> ] .

[] a tcs:TaxonConceptMapping ;
    tcs:mappingAccordingTo <https://doi.org/10.1002/tax.613003> ;
    tcs:mappingRelation <http://rs.tdwg.org/tcs-taxon-concept-mapping-relation/values/isIncludedIn> ;
    tcs:subjectTaxonConcept _:b1 ;
    tcs:objectTaxonConcept [ a tcs:TaxonConcept ;
            dcterms:title "Dryopteridaceae sec. Nayar 1970" ;
            tcs:accordingTo <https://doi.org/10.2307/1217958> ;
            tcs:taxonName <https://www.ipni.org/n/30014148-2> ] .

[] a tcs:TaxonConceptMapping ;
    tcs:mappingAccordingTo <https://doi.org/10.1002/tax.613003> ;
    tcs:mappingRelation <http://rs.tdwg.org/tcs-taxon-concept-mapping-relation/values/isIncludedIn> ;
    tcs:subjectTaxonConcept _:b1 ;
    tcs:objectTaxonConcept [ a tcs:TaxonConcept ;
            dcterms:title "Dennstaedtiaceae sec. Holttum 1947" ;
            tcs:accordingTo [ a dcterms:BibliographicResource ;
                    dcterms:bibliographicCitation """Holttum, R.E. (1947). A 
                            revised classification of leptosporangiate ferns. 
                            Journal of the Linnean Society. Botany 53: 123–155.""" ] ;
            tcs:taxonName <https://ipni.org/n/17434830-1> ] .
```

[&lsqb;TaxonConceptMappingRelation-isIncludedIn-2.ttl&rsqb;](../../examples/TaxonConceptMappingRelation-isIncludedIn-2.ttl)&nbsp;[&lsqb;TaxonConceptMappingRelation-isIncludedIn-2.jsonld&rsqb;](../../examples/TaxonConceptMappingRelation-isIncludedIn-2.jsonld)

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

[&lsqb;TaxonConceptMappingRelation-partiallyOverlaps-1.ttl&rsqb;](../../examples/TaxonConceptMappingRelation-partiallyOverlaps-1.ttl)&nbsp;[&lsqb;TaxonConceptMappingRelation-partiallyOverlaps-1.jsonld&rsqb;](../../examples/TaxonConceptMappingRelation-partiallyOverlaps-1.jsonld)


```turtle
[] a tcs:TaxonConceptMapping ;
    tcs:mappingAccordingTo <https://doi.org/10.1002/tax.613003> ;
    tcs:mappingRelation <http://rs.tdwg.org/tcs-taxon-concept-mapping-relation/values/partiallyOverlaps> ;
    tcs:subjectTaxonConcept [ a tcs:TaxonConcept ;
            dcterms:title "Diplaziopsidaceae sec. Rothfels & al. 2012" ;
            tcs:accordingTo <https://doi.org/10.1002/tax.613003> ;
            tcs:taxonName <https://ipni.org/n/77110538-1> ] ;
    tcs:objectTaxonConcept [ a tcs:TaxonConcept ;
            dcterms:title "Athyriaceae sec. Christenhusz & al. 2011" ;
            tcs:accordingTo <https://doi.org/10.11646/phytotaxa.19.1.2> ;
            tcs:taxonName <https://ipni.org/n/30000361-2> ] .
```

[&lsqb;TaxonConceptMappingRelation-partiallyOverlaps-2.ttl&rsqb;](../../examples/TaxonConceptMappingRelation-partiallyOverlaps-2.ttl)&nbsp;[&lsqb;TaxonConceptMappingRelation-partiallyOverlaps-2.jsonld&rsqb;](../../examples/TaxonConceptMappingRelation-partiallyOverlaps-2.jsonld)

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

[&lsqb;TaxonConceptMappingRelation-isDisjointFrom-1.ttl&rsqb;](../../examples/TaxonConceptMappingRelation-isDisjointFrom-1.ttl)&nbsp;[&lsqb;TaxonConceptMappingRelation-isDisjointFrom-1.jsonld&rsqb;](../../examples/TaxonConceptMappingRelation-isDisjointFrom-1.jsonld)


```turtle
[] a tcs:TaxonConceptMapping ;
    tcs:mappingAccordingTo <https://www.tropicos.org/reference/9022656> ;
    tcs:mappingRelation <http://rs.tdwg.org/tcs-taxon-concept-mapping-relation/values/isDisjointFrom> ;
    tcs:subjectTaxonConcept [ a tcs:TaxonConcept ;
            dcterms:title "Campylopus introflexus sec. Koperski & al. 2000" ; 
            tcs:accordingTo <https://www.tropicos.org/reference/9022656> ;
            tcs:taxonName <https://www.tropicos.org/name/35156181> ] ;
    tcs:objectTaxonConcept [ a tcs:TaxonConcept ;
            dcterms:title "Campylopus introflexus sec. Mönkemeyer 1927" ;
            tcs:accordingTo <https://www.tropicos.org/publication/700> ;
            tcs:taxonName <https://www.tropicos.org/publication/700> ] ;
    rdfs:comment """Mit dem Taxon in Mönkemeyer ist der Beschreibung nach 
            eindeutig *C. pilifer Brid. (C. polytrichoides De Not.), eine 
            ozeanisch-submediterrane Art, gemeint. In älteren Floren wird C. 
            introflexus, bevor diese Art von Störmer (1958) für Europa 
            nachgewiesen wurde, regelmäßig als Synonym von C. polytrichoides 
            aufgeführt oder in diesem Sinne verwendet (vgl. u. a. Demaret & 
            Castagne 1961: 203)""" .
```

[&lsqb;TaxonConceptMappingRelation-isDisjointFrom-2.ttl&rsqb;](../../examples/TaxonConceptMappingRelation-isDisjointFrom-2.ttl)&nbsp;[&lsqb;TaxonConceptMappingRelation-isDisjointFrom-2.jsonld&rsqb;](../../examples/TaxonConceptMappingRelation-isDisjointFrom-2.jsonld)

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

`intersects` is the opposite of `isDisjointFrom` and the union of  `isCongruentWith`, `includes`, `isIncludedIn` and  `partiallyOverlaps`, meaning it can be any of these relationships. This  relationship type can be used when the more precise nature of the  relationship is not known.

Quasi-nomenclatural statements like 'pro parte synonym' and 'misapplication', are Taxon Concept Mappings, no matter how imperfect, and, in TCS, are best dealt with using the `intersects` relation. In fact, all 'traditional synonymy' relationships, cf. Berendsohn & al. (2000 [\[berendsohn_berlin_2003\]](../bibliography/#berendsohn_berlin_2003)), can be dealt with using `intersects`. Also, citations of references in treatments are, in the context of TCS, best dealt with using the `intersects` relation.


**Examples**


```turtle
[] a tcs:TaxonConceptMapping ;
    tcs:mappingAccordingTo <https://www.jstor.org/stable/23873848> ;
    tcs:mappingRelation <http://rs.tdwg.org/tcs-taxon-concept-mapping-relation/values/intersects> ;
    tcs:subjectTaxonConcept <https://id.biodiversity.org.au/instance/apni/545068> ;
    tcs:objectTaxonConcept <https://id.biodiversity.org.au/instance/apni/713514> .

[] a tcs:TaxonConceptMapping ;
    tcs:mappingAccordingTo <https://www.jstor.org/stable/23873848> ;
    tcs:mappingRelation <http://rs.tdwg.org/tcs-taxon-concept-mapping-relation/values/intersects> ;
    tcs:subjectTaxonConcept <https://id.biodiversity.org.au/instance/apni/545068> ;
    tcs:objectTaxonConcept [ a tcs:TaxonConcept ;
            dcterms:title "Euphrasia gibbsiae sec. Harris 1970" ;
            tcs:accordingTo [ a dcterms:BibliographicResource ;
                    dcterms:bibliographicCitation "Harris, Alp. Pl. Austral. (1970)" ] ;
            tcs:taxonName <https://www.ipni.org/n/802545-1> ] ;
    rdfs:comment """p.p. (excl. "f. comberi" in Victoria)""" .

[] a tcs:TaxonConceptMapping ;
    tcs:mappingAccordingTo <https://www.jstor.org/stable/23873848> ;
    tcs:mappingRelation <http://rs.tdwg.org/tcs-taxon-concept-mapping-relation/values/intersects> ;
    tcs:subjectTaxonConcept <https://id.biodiversity.org.au/instance/apni/545068> ;
    tcs:objectTaxonConcept [ a tcs:TaxonConcept ;
            dcterms:title "Euphrasia striata sec. Bentham 1868" ;
            tcs:accordingTo [ a dcterms:BibliographicResource ;
                    dcterms:bibliographicCitation "Bentham, Fl. Austral. (1868)" ] ;
            tcs:taxonName <https://www.ipni.org/n/802876-1> ] ;
    rdfs:comment """p.p. (as to Stuart 1745, Milligan MEL41451, p.p., Mueller 
            MEL41539)""" .

<https://id.biodiversity.org.au/instance/apni/545068> a tcs:TaxonConcept ;
    dcterms:title "Euphrasia gibbsiae sec. Barker 1982" ;
    tcs:accordingTo <https://www.jstor.org/stable/23873848> ;
    tcs:taxonName <https://www.ipni.org/n/802545-1> ;
    tcs:synonym <https://www.ipni.org/n/802619-1> .

<https://id.biodiversity.org.au/instance/apni/713514> a tcs:TaxonConcept ;
    dcterms:title "Euphrasia gibbsiae sec. Curtis 1967" ;
    tcs:accordingTo <https://id.biodiversity.org.au/reference/apni/23028> ;
    tcs:taxonName <https://www.ipni.org/n/802545-1> .
```

[&lsqb;TaxonConceptMappingRelation-intersects-1.ttl&rsqb;](../../examples/TaxonConceptMappingRelation-intersects-1.ttl)&nbsp;[&lsqb;TaxonConceptMappingRelation-intersects-1.jsonld&rsqb;](../../examples/TaxonConceptMappingRelation-intersects-1.jsonld)

<!-- footer -->