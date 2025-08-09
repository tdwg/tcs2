# TaxonName basionym example 2

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

[&lsqb;TaxonName-basionym-example-2.ttl&rsqb;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonName-basionym-example-2.ttl)&nbsp;[&lsqb;TaxonName-basionym-example-2.jsonld&rsqb;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonName-basionym-example-2.jsonld)

