# TaxonConceptMapping isCongruentWith example 1

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

