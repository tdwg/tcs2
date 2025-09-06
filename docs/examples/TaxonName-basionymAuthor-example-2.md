# TaxonName basionymAuthor example 2


**Term:** [tcs:basionymAuthor](../terms/#tcs_basionymauthor)

[TaxonName-basionymAuthor-example-1](./TaxonName-basionymAuthor-example-1.html) | TaxonName-basionymAuthor-example-2
```turtle
[] a tcs:TaxonName ;
    tcs:nameString "Panthera leo" ;
    dwc:scientificNameAuthorship "(Linnaeus, 1758)" ;
    tcs:basionymAuthor <http://www.wikidata.org/entity/Q1043> ;
    tcs:basionym <https://zoobank.org/NomenclaturalActs/db265300-fb04-4dba-b843-8dd236484ee4> .

<https://zoobank.org/NomenclaturalActs/db265300-fb04-4dba-b843-8dd236484ee4> a tcs:TaxonName ;
    tcs:nameString "Felis leo" ;
    dwc:scientificNameAuthorship "Linnaeus, 1758" ;
    tcs:combinationAuthor <http://www.wikidata.org/entity/Q1043> .

<http://www.wikidata.org/entity/Q1043> a foaf:Person ;
    foaf:givenName: "Carl" ;
    foaf:surname "Linnaeus" .
```

[&#91;TurTLe&#93;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonName-basionymAuthor-example-2.ttl)&nbsp;[&#91;JSON-LD&#93;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonName-basionymAuthor-example-2.jsonld)

