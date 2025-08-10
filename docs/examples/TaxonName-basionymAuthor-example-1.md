# TaxonName basionymAuthor example 1


**Term:** [tcs:basionymAuthor](/terms/#tcs_basionymauthor)


```turtle
<https://tropicos.org/name/35121611> a tcs:taxonName ;
    tcs:nameString "Dicranoloma robustum" ;
    dwc:scientificNameAuthorship "(Hook.f. & Wilson) Paris" ;
    tcs:combinationAuthor <https://tropicos.org/person/2011> ;
    tcs:combinationAuthorLiteral "Paris" 
    tcs:basionymAuthor _:b1 ;
    tcs:basionymAuthorLiteral "Hook.f. & Wilson" ;
    tcs:basionym <https://tropicos.org/name/35124067> .

<https://tropicos.org/name/35124067> a tcs:TaxonName ;
    tcs:nameString "Dicranum robustum" ;
    dwc:scientificNameAuthorship ;
    tcs:combinationAuthor _:b1 ;
    tcs:combinationAuthorLiteral "Hook.f. & Wilson" .

<https://tropicos.org/person/2011> a foaf:Person ;
    foaf:givenName "Jean Édouard Gabriel Narcisse" ;
    foaf:surname "Paris" .

_:b1 a rdf:Seq ;
    rdf:_1 <https://tropicos.org/person/3> ;
    rdf:_2 <https://tropicos.org/person/10481> .

<https://tropicos.org/person/3> a foaf:Person ;
    foaf:givenName "Joseph Dalton" ;
    foaf:surname "Hooker" .

<https://tropicos.org/person/10481> a foaf:Person ;
    foaf:givenName "William" ;
    foaf:surname "Wilson" .
```

[&#91;TurTLe&#93;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonName-basionymAuthor-example-1.ttl)&nbsp;[&#91;JSON-LD&#93;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonName-basionymAuthor-example-1.jsonld)

