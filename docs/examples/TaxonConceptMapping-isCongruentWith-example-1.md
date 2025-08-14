# TaxonConceptMapping isCongruentWith example 1


**Term:** [tcs:isCongruentWith](../terms/#tcs_iscongruentwith)

[TaxonConcept-isCongruentWith-example-1](./TaxonConcept-isCongruentWith-example-1.html) | [TaxonConceptMapping-isCongruentWith-example-2](./TaxonConceptMapping-isCongruentWith-example-2.html) | [TaxonConcept-isCongruentWith-example-3](./TaxonConcept-isCongruentWith-example-3.html) | TaxonConceptMapping-isCongruentWith-example-1
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

[&#91;TurTLe&#93;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonConceptMapping-isCongruentWith-example-1.ttl)&nbsp;[&#91;JSON-LD&#93;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonConceptMapping-isCongruentWith-example-1.jsonld)

