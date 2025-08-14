# TaxonConcept example 2


**Term:** [tcs:TaxonConcept](../terms/#tcs_taxonconcept)

[TaxonConcept-example-1](./TaxonConcept-example-1.html) | TaxonConcept-example-2 | [TaxonConcept-example-3](./TaxonConcept-example-3.html) | [TaxonConcept-example-4](./TaxonConcept-example-4.html) | [TaxonConcept-example-5](./TaxonConcept-example-5.html) | [TaxonConcept-example-6](./TaxonConcept-example-6.html) | [TaxonConcept-example-7](./TaxonConcept-example-7.html)
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

[&#91;TurTLe&#93;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonConcept-example-2.ttl)&nbsp;[&#91;JSON-LD&#93;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonConcept-example-2.jsonld)

