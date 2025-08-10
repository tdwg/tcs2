# TaxonConceptMapping isCongruentWith example 2


**Term:** [tcs:isCongruentWith](/terms/#tcs_iscongruentwith)

[TaxonConcept-isCongruentWith-example-1](./TaxonConcept-isCongruentWith-example-1.html) | TaxonConceptMapping-isCongruentWith-example-2 | [TaxonConcept-isCongruentWith-example-3](./TaxonConcept-isCongruentWith-example-3.html) | [TaxonConceptMapping-isCongruentWith-example-1](./TaxonConceptMapping-isCongruentWith-example-1.html)
```turtle
_:b0  a tcs:TaxonConcept ;
    dcterms:title "Aspleniaceae sec. Rothfels & al. 2012" ;
    tcs:accordingTo <https://doi.org/10.1002/tax.613003> ;
    tcs:taxonName <https://ipni.org/n/30001382-2> .

[] a tcs:TaxonConceptMapping ;
    tcs:mappingAccordingTo <https://doi.org/10.1002/tax.613003> ;
    tcs:mappingRelation tcs:isCongruentWith ;
    tcs:subjectTaxonConcept _:b0 ;
    tcs:objectTaxonConcept [ a tcs:TaxonConcept ;
            dcterms:title "Aspleniaceae sec. Christenhusz & al. 2011" ;
            tcs:accordingTo <https://doi.org/10.11646/phytotaxa.19.1.2> ;
            tcs:taxonName <https://ipni.org/n/30001382-2> ] .

[] a tcs:TaxonConceptMapping ;
    tcs:mappingAccordingTo <https://doi.org/10.1002/tax.613003> ;
    tcs:mappingRelation tcs:isCongruentWith ;
    tcs:subjectTaxonConcept _:b0 ;
    tcs:objectTaxonConcept [ a tcs:TaxonConcept ;
            dcterms:title "Aspleniaceae sec. Smith & al. 2006" ;
            tcs:accordingTo <https://doi.org/10.2307/25065646> ;
            tcs:acceptedName <https://ipni.org/n/30001382-2> ] .

[] a tcs:TaxonConceptMapping ;
    tcs:mappingAccordingTo <https://doi.org/10.1002/tax.613003> ;
    tcs:mappingRelation tcs:isCongruentWith ;
    tcs:subjectTaxonConcept _:b0 ;
    tcs:objectTaxonConcept [ a tcs:TaxonConcept ;
            dcterms:title "Aspleniaceae sec. Pichi Sermolli 1977" ;
            tcs:accordingTo <https://doi.org/10.1080/00837792.1977.10670077> ;
            tcs:taxonName <https://ipni.org/n/30001382-2> ] .

[] a tcs:TaxonConceptMapping ;
    tcs:mappingAccordingTo <https://doi.org/10.1002/tax.613003> ;
    tcs:mappingRelation tcs:isCongruentWith ;
    tcs:subjectTaxonConcept _:b0 ;
    tcs:objectTaxonConcept [ a tcs:TaxonConcept ;
            dcterms:title "Aspleniaceae sec. Nayar 1970" ;
            tcs:accordingTo <https://doi.org/10.2307/1217958> ;
            tcs:taxonName <https://ipni.org/n/30001382-2> ] .
```

[&#91;TurTLe&#93;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonConceptMapping-isCongruentWith-example-2.ttl)&nbsp;[&#91;JSON-LD&#93;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonConceptMapping-isCongruentWith-example-2.jsonld)

