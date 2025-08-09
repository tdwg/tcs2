# TaxonConcept example 2

```turtle
[] a tcs:TaxonConcept ;
    dcterms:title "Orthetrum caledonicum sec. Theischinger and Hawking 2010" ;
    tcs:accordingTo <urn:isbn:978-0-643-09073-6> ;
    tcs:taxonName [ a tcs:TaxonName ; 
            tcs:nameString "Orthetrum caledonicum" ] ;
    tcs:vernacularName [ a tcs:TaxonName ;
            tcs:nameString "Blue Skimmer" ] .

<urn:isbn:978-0-643-09073-6> a bibo:Book ;
    dcterms:bibliographicCitation """Theischinger, G.; Hawking, J. (2010). 
            The complete field guide to dragonflies of Australia. CSIRO 
            Publishing, Collingwood, Australia.""" .
```

[&lsqb;TaxonConcept-example-2.ttl&rsqb;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonConcept-example-2.ttl)&nbsp;[&lsqb;TaxonConcept-example-2.jsonld&rsqb;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonConcept-example-2.jsonld)

