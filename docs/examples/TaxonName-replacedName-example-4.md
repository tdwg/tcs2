# TaxonName replacedName example 4


**Term:** [tcs:replacedName](/terms/#tcs_replacedname)

[TaxonName-replacedName-example-1](./TaxonName-replacedName-example-1.html) | [TaxonName-replacedName-example-2](./TaxonName-replacedName-example-2.html) | [TaxonName-replacedName-example-3](./TaxonName-replacedName-example-3.html) | TaxonName-replacedName-example-4
```turtle
<https://ipni.org/n/471632-1> a tcs:TaxonName ;
    tcs:nameString "Acacia tenuifolia" ;
    dwc:scientificNameAuthorship "F.Muell." ;
    dwc:namePublishedIn "Trans. Philos. Soc. Victoria 1: 37" ;
    dwc:namePublishedInYear "1855" ;
    tcs:nomenclaturalStatus <http://rs.gbif.org/vocabulary/gbif/nomenclatural_status/illegitimum> ;
    rdf:seeAlso <https://ipni.org/n/81578-3> ,
            <https://id.biodiversity.org.au/name/apni/71120> .

<https://ipni.org/n/469641-1> a tcs:TaxonName ;
    tcs:nameString "Acacia aculeatissima" ;
    dwc:scientificNameAuthorship "J.F.Macbr." ;
    dwc:namePublishedIn "Contr. Gray Herb. 59: 6" ;
    dwc:namePublishedInYear "1919" ;
    tcs:replacedName <https://ipni.org/n/471632-1> ;
    rdf:seeAlso <https://ipni.org/n/56412-3> ,
            <https://id.biodiversity.org.au/name/apni/58056> .

<https://ipni.org/n/60428094-2> a tcs:TaxonName ;
    tcs:nameString "Racosperma aculeatissimum" ;
    dwc:scientificNameAuthorship "(J.F.Macbr.) Pedley" ;
    dwc:namePublishedIn "Austrobaileya 6(3): 447" ;
    dwc:namePublishedInYear "2003" ;
    tcs:basionym <https://ipni.org/n/469641-1> ;
    rdf:seeAlso <https://id.biodiversity.org.au/name/apni/190652> .
```

[&#91;TurTLe&#93;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonName-replacedName-example-4.ttl)&nbsp;[&#91;JSON-LD&#93;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonName-replacedName-example-4.jsonld)

