# TaxonConcept vernacularName example 4


**Term:** [tcs:vernacularName](../terms/#tcs_vernacularname)

[TaxonConcept-vernacularName-example-1](./TaxonConcept-vernacularName-example-1.html) | [TaxonConcept-vernacularName-example-2](./TaxonConcept-vernacularName-example-2.html) | [TaxonConcept-vernacularName-example-3](./TaxonConcept-vernacularName-example-3.html) | TaxonConcept-vernacularName-example-4
```turtle
<https://www.catalogueoflife.org/data/taxon/4CGXT> a tcs:TaxonConcept ;
    dcterms:title "Panthera uncia sec. Catalogue of Life 2025-09-04" ;
    tcs:accordingTo <https://doi.org/10.48580/dfrdl> ;
    tcs:taxonName [ a tcs:TaxonName ;
            tcs:nameString "Panthera uncia" ;
            tcs:basionym [ a tcs:TaxonName ;
                    tcs:nameString: "Felis uncia" ;
                    dwc:scientificNameAuthorship "Schreber" ;
                        dwc:namePublishedInYear "1775" ]] ;
    tcs:vernacularName [ a gbif:VernacularName ;
            dwc:vernacularName "Snow leopard" ;
            dcterms:language "en" ] ,
        [  a gbif:VernacularName ;
            dwc:vernacularName "Panthère de neige" ;
            dcterms:language "fr" ] ,
        [  a gbif:VernacularName ;
            dwc:vernacularName "Once" ;
            dcterms:language "fr" ] ,
        [  a gbif:VernacularName ;
            dwc:vernacularName "Pantera de las nieves" ;
            dcterms:language "es" ] .
```

[&#91;TurTLe&#93;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonConcept-vernacularName-example-4.ttl)&nbsp;[&#91;JSON-LD&#93;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonConcept-vernacularName-example-4.jsonld)

