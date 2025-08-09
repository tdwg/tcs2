# TaxonName replacedName example 2


**Term:** [tcs:replacedName](/terms/#tcs_replacedname)

[TaxonName-replacedName-example-1](./TaxonName-replacedName-example-1.html) | TaxonName-replacedName-example-2 | [TaxonName-replacedName-example-3](./TaxonName-replacedName-example-3.html) | [TaxonName-replacedName-example-4](./TaxonName-replacedName-example-4.html)
```turtle
<https://www.tropicos.org/name/35000146> a tcs:TaxonName ;
    tcs:nameString "Braunfelsia" ;
    dwc:scientificNameAuthorship "Paris" ;
    dwc:namePublishedIn "Index Bryol.: 148" ;
    dwc:namePublishedInYear "1894" ;
    tcs:replacedName <https://www.tropicos.org/name/35001206> .

<https://www.tropicos.org/name/35001206> a tcs:TaxonName ;
    tcs:nameString "Solmsia" ;
    dwc:scientificNameAuthorship "Hampe" ;
    dwc:namePublishedIn "Nuovo Giorn. Bot. Ital. 4(4): 273, 281" ;
    dwc:namePublishedInYear "1872" ;
    tcs:nomenclaturalStatus <http://rs.gbif.org/vocabulary/gbif/nomenclatural_status/illegitimum> .

# prior homonym
<https://ipni.org/n/39527-1> a tcs:TaxonName ;
    tcs:nameString "Solmsia" ;
    dwc:scientificNameAuthorship "Baill." ;
    dwc:namePublishedIn "Adansonia 10: 37" ;
    dwc:namePublishedInYear "1871" .
```

[&#91;TaxonName-replacedName-example-2.ttl&#93;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonName-replacedName-example-2.ttl)&nbsp;[&#91;TaxonName-replacedName-example-2.jsonld&#93;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonName-replacedName-example-2.jsonld)

