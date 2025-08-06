# TaxonConcept vernacularName example 2

```turtle
[] a tcs:TaxonConcept ;
    dcterms:title "Quercus robur sec. Duistermaat 2020" ;
    tcs:accordingTo <urn:isbn:978-90-01-58956-1> ;
    tcs:taxonName <https://ipni.org/n/304293-2> ;
    tcs:vernacularName [ a gbif:VernacularName ;
            dwc:vernacularName "Zomereik" ;
            dcterms:language "nl" ] .

<https://ipni.org/n/304293-2> a tcs:TaxonName ;
    tcs:nameString "Quercus robur" .

<urn:isbn:978-90-01-58956-1> a bibo:Book ;
    dcterms:bibliographicCitation """Duistermaat, H. (2020). Heukels 
            Flora van Nederland, edn 24. Noordhoff, Groningen.""" .
```

[&lsqb;TaxonConcept-vernacularName-example-2.ttl&rsqb;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonConcept-vernacularName-example-2.ttl)&nbsp;[&lsqb;TaxonConcept-vernacularName-example-2.jsonld&rsqb;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonConcept-vernacularName-example-2.jsonld)

