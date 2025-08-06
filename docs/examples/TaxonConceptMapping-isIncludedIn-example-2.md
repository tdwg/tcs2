# TaxonConceptMapping-isIncludedIn-example-2

```turtle
_:b1 a tcs:TaxonConcept ;
    dcterms:title "Athyriaceae sec. Rothfels & al. 2012" ;
    tcs:accordingTo <https://doi.org/10.1002/tax.613003> ;
    tcs:taxonName <https://ipni.org/n/30000361-2> .

[] a tcs:TaxonConceptMapping ;
    tcs:mappingAccordingTo <https://doi.org/10.1002/tax.613003> ;
    tcs:mappingRelation tcs:isIncludedIn ;
    tcs:subjectTaxonConcept _:b1 ;
    tcs:objectTaxonConcept [ a tcs:TaxonConcept ;
            dcterms:title "Athyriaceae sec. Christenhusz & al. 2011" ;
            tcs:accordingTo <https://doi.org/10.11646/phytotaxa.19.1.2> ;
            tcs:taxonName <https://ipni.org/n/30000361-2> ] .

[] a tcs:TaxonConceptMapping ;
    tcs:mappingAccordingTo <https://doi.org/10.1002/tax.613003> ;
    tcs:mappingRelation tcs:isIncludedIn ;
    tcs:subjectTaxonConcept _:b1 ;
    tcs:objectTaxonConcept [ a tcs:TaxonConcept ;
            dcterms:title "Woodsiaceae sec. Smith & al. 2006" ;
            tcs:accordingTo <https://doi.org/10.2307/25065646> ;
            tcs:taxonName <https://ipni.org/n/30000455-2> ] .

[] a tcs:TaxonConceptMapping ;
    tcs:mappingAccordingTo <https://doi.org/10.1002/tax.613003> ;
    tcs:mappingRelation tcs:isIncludedIn ;
    tcs:subjectTaxonConcept _:b1 ;
    tcs:objectTaxonConcept [ a tcs:TaxonConcept ;
            dcterms:title "Dryopteridaceae sec. Nayar 1970" ;
            tcs:accordingTo <https://doi.org/10.2307/1217958> ;
            tcs:taxonName <https://ipni.org/n/30014148-2> ] .

[] a tcs:TaxonConceptMapping ;
    tcs:mappingAccordingTo <https://doi.org/10.1002/tax.613003> ;
    tcs:mappingRelation tcs:isIncludedIn ;
    tcs:subjectTaxonConcept _:b1 ;
    tcs:objectTaxonConcept [ a tcs:TaxonConcept ;
            dcterms:title "Dennstaedtiaceae sec. Holttum 1947" ;
            tcs:accordingTo [ a dcterms:BibliographicResource ;
                    dcterms:bibliographicCitation """Holttum, R.E. (1947). A 
                            revised classification of leptosporangiate ferns. 
                            Journal of the Linnean Society. Botany 53: 123–155.""" ] ;
            tcs:taxonName <https://ipni.org/n/17434830-1> ] .
```

[&lsqb;TaxonConceptMapping-isIncludedIn-example-2.ttl&rsqb;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonConceptMapping-isIncludedIn-example-2.ttl)&nbsp;[&lsqb;TaxonConceptMapping-isIncludedIn-example-2.jsonld&rsqb;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonConceptMapping-isIncludedIn-example-2.jsonld)

