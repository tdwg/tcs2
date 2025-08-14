# TaxonName basionym example 2


**Term:** [tcs:basionym](../terms/#tcs_basionym)

[TaxonName-basionym-example-1](./TaxonName-basionym-example-1.html) | TaxonName-basionym-example-2
```turtle
[] a tcs:TaxonName ;
    tcs:nameString "Osphranter rufus" ;
    dwc:scientificNameAuthorship "(Desmaret, 1882)" ;
    tcs:basionym _:b1 .

[] a tcs:TaxonName ;
    tcs:nameString "Macropus rufus" ;
    dwc:scientificNameAuthorship "(Desmaret, 1882)" ;
    tcs:basionym: _:b1 .

_:b1 a tcs:TaxonName ;
    tcs:nameString "Kangurus rufus" ;
    dwc:scientificNameAuthorship "Desmaret, 1882" .
```

[&#91;TurTLe&#93;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonName-basionym-example-2.ttl)&nbsp;[&#91;JSON-LD&#93;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonName-basionym-example-2.jsonld)

