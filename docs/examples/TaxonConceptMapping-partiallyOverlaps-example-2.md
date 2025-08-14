# TaxonConceptMapping partiallyOverlaps example 2


**Term:** [tcs:partiallyOverlaps](../terms/#tcs_partiallyoverlaps)

[TaxonConcept-partiallyOverlaps-example-1](./TaxonConcept-partiallyOverlaps-example-1.html) | TaxonConceptMapping-partiallyOverlaps-example-2 | [TaxonConceptMapping-partiallyOverlaps-example-1](./TaxonConceptMapping-partiallyOverlaps-example-1.html)
```turtle
[] a tcs:TaxonConceptMapping ;
    tcs:mappingAccordingTo <https://doi.org/10.1002/tax.613003> ;
    tcs:mappingRelation tcs:partiallyOverlaps ;
    tcs:subjectTaxonConcept [ a tcs:TaxonConcept ;
            dcterms:title "Diplaziopsidaceae sec. Rothfels & al. 2012" ;
            tcs:accordingTo <https://doi.org/10.1002/tax.613003> ;
            tcs:taxonName <https://ipni.org/n/77110538-1> ] ;
    tcs:objectTaxonConcept [ a tcs:TaxonConcept ;
            dcterms:title "Athyriaceae sec. Christenhusz & al. 2011" ;
            tcs:accordingTo <https://doi.org/10.11646/phytotaxa.19.1.2> ;
            tcs:taxonName <https://ipni.org/n/30000361-2> ] .
```

[&#91;TurTLe&#93;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonConceptMapping-partiallyOverlaps-example-2.ttl)&nbsp;[&#91;JSON-LD&#93;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonConceptMapping-partiallyOverlaps-example-2.jsonld)

