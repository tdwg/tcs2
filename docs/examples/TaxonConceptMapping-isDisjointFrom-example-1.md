# TaxonConceptMapping isDisjointFrom example 1


**Term:** [tcs:isDisjointFrom](/terms/#tcs_isdisjointfrom)

[TaxonConcept-isDisjointFrom-example-1](./TaxonConcept-isDisjointFrom-example-1.html) | [TaxonConceptMapping-isDisjointFrom-example-2](./TaxonConceptMapping-isDisjointFrom-example-2.html) | TaxonConceptMapping-isDisjointFrom-example-1
```turtle
# Andropogon glaucopsis sec. BONAP 2014 is disjoint from Andropogon virginicus sec. Weakley 2006
[] a tcs:TaxonConceptMapping ;
    tcs:mappingAccordingTo <https://doi.org/10.3233/SW-160220> ;
    tcs:mappingRelation tcs:isDisjointFrom ;
    tcs:subjectTaxonConcept [ a tcs:TaxonConcept ;
        dcterms:title "Andropogon glaucopsis sec. BONAP 2014" ;
        tcs:taxonName <https://ipni.org/n/387942-1> ;
        tcs:accordingTo <http://bonap.net/napa#2014> ] ;
    tcs:objectTaxonConcept [ a tcs:TaxonConcept ;
        dcterms:title "Andropogon virginicus sec. Weakley 2006" ;
        tcs:taxonName <https://ipni.org/n/388740-1> ;
        tcs:accordingTo <http://www.herbarium.unc.edu/FloraArchives/WeakleyFlora_2006-Jan.pdf> ] .
```

[&#91;TaxonConceptMapping-isDisjointFrom-example-1.ttl&#93;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonConceptMapping-isDisjointFrom-example-1.ttl)&nbsp;[&#91;TaxonConceptMapping-isDisjointFrom-example-1.jsonld&#93;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonConceptMapping-isDisjointFrom-example-1.jsonld)

