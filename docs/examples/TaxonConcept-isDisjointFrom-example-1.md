# TaxonConcept-isDisjointFrom-example-1

```turtle
[] a tcs:TaxonConcept 
    dcterms:title "Campylopus introflexus sec. Koperski & al. 2000" ; 
    tcs:accordingTo <https://www.tropicos.org/reference/9022656> ;
    tcs:taxonName <https://www.tropicos.org/name/35156181> ;
    tcs:isDisjointFrom [ rdf:value [ a tcs:TaxonConcept ;
                    dcterms:title "Campylopus introflexus sec. Mönkemeyer 1927" ;
                    tcs:accordingTo <https://www.tropicos.org/publication/700> ;
                    tcs:taxonName <https://www.tropicos.org/name/35156181> ] ;
            rdfs:comment """Mit dem Taxon in Mönkemeyer ist der Beschreibung 
                    nach eindeutig *C. pilifer Brid. (C. polytrichoides De 
                    Not.), eine ozeanisch-submediterrane Art, gemeint. In 
                    älteren Floren wird C. introflexus, bevor diese Art von 
                    Störmer (1958) für Europa nachgewiesen wurde, regelmäßig als 
                    Synonym von C. polytrichoides aufgeführt oder in diesem 
                    Sinne verwendet (vgl. u. a. Demaret & Castagne 1961: 
                    203)""" ] .

# Because of the comment it is better to use a Taxon Concept Mapping object
# here.
```

[&lsqb;TaxonConcept-isDisjointFrom-example-1.ttl&rsqb;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonConcept-isDisjointFrom-example-1.ttl)&nbsp;[&lsqb;TaxonConcept-isDisjointFrom-example-1.jsonld&rsqb;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonConcept-isDisjointFrom-example-1.jsonld)

