# TaxonConceptMapping isDisjointFrom example 1

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

[&lsqb;TaxonConceptMapping-isDisjointFrom-example-1.ttl&rsqb;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonConceptMapping-isDisjointFrom-example-1.ttl)&nbsp;[&lsqb;TaxonConceptMapping-isDisjointFrom-example-1.jsonld&rsqb;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonConceptMapping-isDisjointFrom-example-1.jsonld)

