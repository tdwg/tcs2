# TaxonConcept partiallyOverlaps example 1


**Term:** [tcs:partiallyOverlaps](/terms/#tcs_partiallyoverlaps)

TaxonConcept-partiallyOverlaps-example-1 | [TaxonConceptMapping-partiallyOverlaps-example-2](./TaxonConceptMapping-partiallyOverlaps-example-2.html) | [TaxonConceptMapping-partiallyOverlaps-example-1](./TaxonConceptMapping-partiallyOverlaps-example-1.html)
```turtle
[] a tcs:TaxonConcept ;
    dcterms:title "Diplaziopsidaceae sec. Rothfels & al. 2012" ;
    tcs:accordingTo <https://doi.org/10.1002/tax.613003> ;
    tcs:taxonName <https://ipni.org/n/77110538-1> ;
    tcs:partiallyOverlaps [ a tcs:TaxonConcept ;
            dcterms:title "Athyriaceae sec. Christenhusz & al. 2011" ;
            tcs:accordingTo <https://doi.org/10.11646/phytotaxa.19.1.2> ;
            tcs:taxonName <https://ipni.org/n/30000361-2> ] .
```

[&#91;TaxonConcept-partiallyOverlaps-example-1.ttl&#93;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonConcept-partiallyOverlaps-example-1.ttl)&nbsp;[&#91;TaxonConcept-partiallyOverlaps-example-1.jsonld&#93;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonConcept-partiallyOverlaps-example-1.jsonld)

