# TaxonConcept vernacularName example 1


**Term:** [tcs:vernacularName](../terms/#tcs_vernacularname)

TaxonConcept-vernacularName-example-1 | [TaxonConcept-vernacularName-example-2](./TaxonConcept-vernacularName-example-2.html) | [TaxonConcept-vernacularName-example-3](./TaxonConcept-vernacularName-example-3.html) | [TaxonConcept-vernacularName-example-4](./TaxonConcept-vernacularName-example-4.html)
```turtle
[] a tcs:TaxonConcept ;
    dcterms:title "Graphium macleayanum sec. Orr & Kitching 2010" ;
    tcs:accordingTo <urn:isbn:978-1-74175-108-6> ;
    tcs:taxonName [ a tcs:TaxonName ;
            tcs:nameString "Graphium macleayanum" ] ;
    tcs:vernacularName [ a gbif:VernacularName ;
            dwc:vernacularName "Macleay's Swallowtail" ;
            dcterms:language: "en" ] .

<urn:isbn:978-1-74175-108-6> a bibo:Book ; 
    dcterms:bibliographicCitation """Orr, A. & Kitching, R. (2010). The 
            butterflies of Australia. Jacana Books, Crows Nest, Australia.""" .
```

[&#91;TurTLe&#93;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonConcept-vernacularName-example-1.ttl)&nbsp;[&#91;JSON-LD&#93;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonConcept-vernacularName-example-1.jsonld)

