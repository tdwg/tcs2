# TaxonName combinationAscribedAuthor example 1


**Term:** [tcs:combinationAscribedAuthor](../terms/#tcs_combinationascribedauthor)


```turtle
<https://tropicos.org/name/35153928> a tcs:TaxonName ;
    tcs:nameString "Calymperes serratum" ;
    dwc:scientificNameAuthorship "A.Braun ex Müll.Hal." ;
    tcs:combinationAuthor <https://tropicos.org/person/2> ;
    tcs:combinationAuthorLiteral "Müll.Hal." ;
    tcs:combinationAscribedAuthor <https://tropicos.org/person/973> ;
    tcs:combinationAscribedAuthorLiteral "A.Braun" .

<https://tropicos.org/person/2> a foaf:Person ;
    foaf:givenName "Johann Karl (Carl) August (Friedrich Wilhelm)" ;
    foaf:familyName "Müller" .

<https://tropicos.org/person/973> a foaf:Person ;
    foaf:givenName "Alexander Karl (Carl) Heinrich" ;
    foaf:familyName "Braun" .
```

[&#91;TurTLe&#93;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonName-combinationAscribedAuthor-example-1.ttl)&nbsp;[&#91;JSON-LD&#93;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonName-combinationAscribedAuthor-example-1.jsonld)

