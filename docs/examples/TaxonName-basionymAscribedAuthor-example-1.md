# TaxonName basionymAscribedAuthor example 1


**Term:** [tcs:basionymAscribedAuthor](../terms/#tcs_basionymascribedauthor)


```turtle
<https://ipni.org/n/3007069-1> a tcs:TaxonName ;
    tcs:nameString "Senna artemisioides" ;
    dwc:scientificNameAuthorship "(Gaudich. ex DC.) Isely)" ;
    tcs:combinationAuthor <https://ipni.org/a/4317-1> ;
    tcs:combinationAuthorLiteral "Isely" ;
    tcs:basionymAuthor <https://ipni.org/a/16855-1> ;
    tcs:basionymAuthorLiteral "DC." ;
    tcs:basionymAscribedAuthor <https://ipni.org/a/3050-1> ;
    tcs:basionymAscribedAuthorLiteral "Gaudich." ;
    tcs:basionym <https://ipni.org/n/484142-1> .

<https://ipni.org/n/484142-1> a tcs:TaxonName ;
    tcs:nameString "Cassia artemisioides" ;
    dwc:scientificNameAuthorship "Gaudich. ex DC." ;
    tcs:combinationAuthor <https://ipni.org/a/16855-1> ;
    tcs:combinationAuthorLiteral "DC." ;
    tcs:combinationAscribedAuthor <https://ipni.org/a/3050-1> ;
    tcs:combinationAscribedAuthorLiteral "Gaudich." .

<https://ipni.org/a/4317-1> a foaf:Person ;
    foaf:givenName "Duane" ;
    foaf:surname "Isely" .

<https://ipni.org/a/16855-1> a foaf:Person ;
    foaf:givenName "Augustin Pyramus" ;
    foaf:surname "De Candolle" .

<https://ipni.org/a/3050-1> a foaf:Person ;
    foaf:givenName "Charles" ;
    foaf:surname "Gaudichaud-Beaupré" .
```

[&#91;TurTLe&#93;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonName-basionymAscribedAuthor-example-1.ttl)&nbsp;[&#91;JSON-LD&#93;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonName-basionymAscribedAuthor-example-1.jsonld)

