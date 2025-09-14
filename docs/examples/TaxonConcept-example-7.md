# TaxonConcept example 7


**Term:** [tcs:TaxonConcept](../terms/#tcs_taxonconcept)

[TaxonConcept-example-1](./TaxonConcept-example-1.html) | [TaxonConcept-example-2](./TaxonConcept-example-2.html) | [TaxonConcept-example-3](./TaxonConcept-example-3.html) | [TaxonConcept-example-4](./TaxonConcept-example-4.html) | [TaxonConcept-example-5](./TaxonConcept-example-5.html) | [TaxonConcept-example-6](./TaxonConcept-example-6.html) | TaxonConcept-example-7
```turtle
<https://avibase.ca/E0E4DFB8> a tcs:TaxonConcept ;
    dcterms:identifier "E0E4DFB8DA0FBD09" , "avibase-E0E4DFB8" ;
    rdfs:label "Acrocephalus seychellensis" ;
    tcs:accordingTo <https://avibase.bsc-eoc.org> ;
    tcs:taxonName: [ a tcs:TaxonName ;
            tcs:nameString "Acrocephalus sechellensis" ;
            dwc:scientificNameAuthorship "(Oustalet, J-FÉ 1877)" ;
            tcs:basionym [ a tcs:TaxonName ;
                    tcs:nameString "Ellisia sechellensis" ;
                    dwc:scientificNameAuthorship "Oustalet, J-FÉ 1877" ;
                    dwc:namePublishedIn "Bull. (Sci.) Soc. Philomath. [Paris] (7), 1 p.103" ;
                    dwc:namePublishedInYear "1877" ]] ;
    tcs:vernacularName [ a <http://rs.gbif.org/terms/1.0/VernacularName> ;
            dwc:vernacularName "Seychelles Warbler" ;
            dcterms:language "en" ] .
```

[&#91;TurTLe&#93;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonConcept-example-7.ttl)&nbsp;[&#91;JSON-LD&#93;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonConcept-example-7.jsonld)

