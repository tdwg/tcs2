# TaxonConceptMapping isDisjointFrom example 2


**Term:** [tcs:isDisjointFrom](/terms/#tcs_isdisjointfrom)

[TaxonConcept-isDisjointFrom-example-1](./TaxonConcept-isDisjointFrom-example-1.html) | TaxonConceptMapping-isDisjointFrom-example-2 | [TaxonConceptMapping-isDisjointFrom-example-1](./TaxonConceptMapping-isDisjointFrom-example-1.html)
```turtle
[] a tcs:TaxonConceptMapping ;
    tcs:mappingAccordingTo <https://www.tropicos.org/reference/9022656> ;
    tcs:mappingRelation tcs:isDisjointFrom ;
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

[&#91;TurTLe&#93;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonConceptMapping-isDisjointFrom-example-2.ttl)&nbsp;[&#91;JSON-LD&#93;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonConceptMapping-isDisjointFrom-example-2.jsonld)

