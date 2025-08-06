# TaxonName replacedName example 2

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

[&lsqb;TaxonName-replacedName-example-2.ttl&rsqb;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonName-replacedName-example-2.ttl)&nbsp;[&lsqb;TaxonName-replacedName-example-2.jsonld&rsqb;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonName-replacedName-example-2.jsonld)

