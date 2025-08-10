# TaxonName replacedName example 1


**Term:** [tcs:replacedName](/terms/#tcs_replacedname)

TaxonName-replacedName-example-1 | [TaxonName-replacedName-example-2](./TaxonName-replacedName-example-2.html) | [TaxonName-replacedName-example-3](./TaxonName-replacedName-example-3.html) | [TaxonName-replacedName-example-4](./TaxonName-replacedName-example-4.html)
```turtle
<https://www.tropicos.org/name/35183593> a tcs:TaxonName ;
    tcs:nameString "Dicranum bartramianum" ;
    dwc:scientificNameAuthorship "B.H.Allen" ;
    dwc:namePublishedIn "Cryptog. Bryol. Lichénol. 8: 323" ;
    dwc:namePublishedInYear "1987" ;
    tcs:replacedName <https://www.tropicos.org/name/35120798> .

<https://www.tropicos.org/name/35120798> a tcs:TaxonName ;
    tcs:nameString "Dicnemon robustum" ;
    dwc:scientificNameAuthorship "E.B.Bartram" ;
    dwc:namePublishedIn "Bryologist 48: 112" ;
    dwc:namePublishedInYear "1945" .

# blocking name
<https://www.tropicos.org/name/35124067> a tcs:TaxonName ;
    tcs:nameString "Dicranum robustum" ;
    dwc:scientificNameAuthorship "Hook.f. & Wilson" ;
    dwc:namePublishedIn "London J. Bot. 3: 542" ;
    dwc:namePublishedInYear "1844" .

# combination of Dicnemon robustum
<https://www.tropicos.org/name/35162373> a tcs:TaxonName ;
    tcs:nameString "Eucamptodon robustum" ;
    dwc:scientificNameAuthorship "(E.B.Bartram) E.B.Bartram" ;
    dwc:namePublishedIn "Brittonia 11: 88" ;
    dwc:namePublishedInYear "1959" ;
    tcs:basionym <https://www.tropicos.org/name/35120798> .

# combination of Dicranum bartramianum
<https://www.tropicos.org/name/35204723> a tcs:TaxonName ;
    tcs:nameString "Dicranoloma bartramianum" ;
    dwc:scientificNameAuthorship "(B.H.Allen) Klazenga" ;
    dwc:namePublishedIn "J. Hattory Bot. Lab. 87: 57" ;
    dwc:namePublishedInYear "1999" ;
    tcs:basionym <https://www.tropicos.org/name/35183593> .
```

[&#91;TurTLe&#93;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonName-replacedName-example-1.ttl)&nbsp;[&#91;JSON-LD&#93;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonName-replacedName-example-1.jsonld)

