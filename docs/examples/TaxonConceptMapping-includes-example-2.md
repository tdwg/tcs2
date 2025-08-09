# TaxonConceptMapping includes example 2


**Term:** [tcs:includes](/terms/#tcs_includes)

[TaxonConcept-includes-example-1](./TaxonConcept-includes-example-1.html) | TaxonConceptMapping-includes-example-2 | [TaxonConceptMapping-includes-example-1](./TaxonConceptMapping-includes-example-1.html)
```turtle
[] a tcs:TaxonConceptMapping ;
    tcs:mappingAccordingTo <https://doi.org/10.1002/tax.613003> ;
    tcs:mappingRelation tcs:includes ;
    tcs:subjectTaxonConcept [ a tcs:TaxonConcept ;
            dcterms:title "Diplaziopsidaceae sec. Rothfels & al. 2012" ;
            tcs:accordingTo <https://doi.org/10.1002/tax.613003> ;
            tcs:taxonName <https://ipni.org/n/77110538-1> ] ;
    tcs:objectTaxonConcept [ a tcs:TaxonConcept ;
            dcterms:title "Diplaziopsidaceae sec. Christenhusz & al. 2011" ;
            tcs:accordingTo <https://doi.org/10.11646/phytotaxa.19.1.2> ;
            tcs:taxonName <https://ipni.org/n/77110538-1> ] .
```

[&#91;TaxonConceptMapping-includes-example-2.ttl&#93;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonConceptMapping-includes-example-2.ttl)&nbsp;[&#91;TaxonConceptMapping-includes-example-2.jsonld&#93;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonConceptMapping-includes-example-2.jsonld)

