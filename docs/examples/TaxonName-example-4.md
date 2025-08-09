# TaxonName example 4


**Term:** [tcs:TaxonName](/terms/#tcs_taxonname)

[TaxonName-example-1](./TaxonName-example-1.html) | [TaxonName-example-2](./TaxonName-example-2.html) | [TaxonName-example-3](./TaxonName-example-3.html) | TaxonName-example-4
```turtle
# Example from TCS 1
<https://ipni.org/n/50985479-1> a tcs:TaxonName ;
    tcs:nomenclaturalCode <http://rs.gbif.org/vocabulary/gbif/nomenclatural_code/ICN> ;
    tcs:taxonomicNameString "Rhododendron sect. Sciadorhodion" ;
    dwc:scientificNameAuthorship "Rehder & Wilson" ;
    dwc:namePublishedIn "Monogr. Azaleas 79 (1921)" ;
    tcs:namePublishedIn [ a bibo:Book ;
        dcterms:bibliographicCitation """Wilson, E.H. & Rehder, A. (1921). A 
                monograph of the azaleas. Publication of the Arnold Arboretum 
                No. 9 Harvard University, Cambridge MA.""" ] ;
    tcs:microReference "79" ;
    dwc:namePublishedInYear "1921" ;
    dwc:genericName "Rhododendron" ;
    dwc:infragenericName "Sciadorhodion" .
```

[&#91;TaxonName-example-4.ttl&#93;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonName-example-4.ttl)&nbsp;[&#91;TaxonName-example-4.jsonld&#93;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonName-example-4.jsonld)

