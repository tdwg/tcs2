# TaxonConcept accordingTo example 2


**Term:** [tcs:accordingTo](/terms/#tcs_accordingto)

[TaxonConcept-accordingTo-example-1](./TaxonConcept-accordingTo-example-1.html) | TaxonConcept-accordingTo-example-2 | [TaxonConcept-accordingTo-example-3](./TaxonConcept-accordingTo-example-3.html)
```turtle
# Field guide (object of property only)
<urn:isbn:978-0-307-95790-0> a bibo:Book ;
    dcterms:title "The Sibley guide to birds" ;
    dcterms:date "2014" ;
    dcterms:language "en" ;
    dcterms:publisher [ 
        a foaf:Organization ;
        address:localityName "New York, NY, USA" ;
        foaf:name "Alfred A. Knopf" 
    ] ;
    bibo:isbn "978-0-307-95790-0" ;
    bibo:edition "2" ;
    bibo:numPages "599" ;
    dcterms:creator "_:b1" ;
    bibo:authorList ( "_:b1" ) .

_:b1 a foaf:Person ;
    foaf:givenName "David Allen" ;
    foaf:surname "Sibley" .
```

[&#91;TurTLe&#93;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonConcept-accordingTo-example-2.ttl)&nbsp;[&#91;JSON-LD&#93;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonConcept-accordingTo-example-2.jsonld)

