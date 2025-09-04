# TaxonConcept child example 1


**Term:** [tcs:childTaxonConcept](../terms/#tcs_childtaxonconcept)


```turtle
<https://www.catalogueoflife.org/data/taxon/6DBT> a tcs:TaxonConcept ;
    dcterms:title "Panthera sec. Catalogue of Life 2024-01-24" ;
    tcs:accordingTo <https://doi.org/10.48580/dfrdl> ;
    tcs:taxonName: [ a tcs:TaxonName ;
            tcs:nameString: "Panthera" ;
            dwc:scientificNameAuthorship: "Oken" ;
            dwc:namePublishedInYear "1816" ]  ;
    tcs:vernacularName [ a gbif:VernacularName ;
            dwc:vernacularName "Roaring cats"] ;
    tcs:taxonRank <http://rs.gbif.org/vocabulary/gbif/rank/genus> ;
    tcs:childTaxonConcept <https://www.catalogueoflife.org/data/taxon/4CGXP> ,
            <https://www.catalogueoflife.org/data/taxon/4CGXQ> ,
            <https://www.catalogueoflife.org/data/taxon/4CGXR> ,
            <https://www.catalogueoflife.org/data/taxon/4CGXS> ,
            <https://www.catalogueoflife.org/data/taxon/4CGXT> .

<https://www.catalogueoflife.org/data/taxon/4CGXP> a tcs:TaxonConcept ;
    dcterms:title "Panthera leo sec. Catalogue of Life 2024-01-24" ;
    tcs:accordingTo <https://doi.org/10.48580/dfrdl> ;
    tcs:taxonName: [ a tcs:TaxonName ;
            tcs:nameString: "Panthera leo" ;
            tcs:basionym [ a tcs:TaxonName ;
                    tcs:nameString: "Felis leo" ;
                    dwc:scientificNameAuthorship "Linnaeus" ;
                        dwc:namePublishedInYear "1758" ]] ;
    tcs:vernacularName [ a gbif:VernacularName ;
            dwc:vernacularName "Lion" ] ;
    tcs:taxonRank <http://rs.gbif.org/vocabulary/gbif/rank/species> .

<https://www.catalogueoflife.org/data/taxon/4CGXQ> a tcs:TaxonConcept ;
    dcterms:title "Panthera onca sec. Catalogue of Life 2024-01-24" ;
    tcs:accordingTo <https://doi.org/10.48580/dfrdl> ;
    tcs:taxonName: [ a tcs:TaxonName ;
            tcs:nameString: "Panthera onca" ;
            tcs:basionym [ a tcs:TaxonName ;
                    tcs:nameString: "Felis onca" ;
                    dwc:scientificNameAuthorship "Linnaeus" ;
                        dwc:namePublishedInYear "1758" ]] ;
    tcs:vernacularName [ a gbif:VernacularName ;
            dwc:vernacularName "Jaguar" ] ;
    tcs:taxonRank <http://rs.gbif.org/vocabulary/gbif/rank/species> .

<https://www.catalogueoflife.org/data/taxon/4CGXR> a tcs:TaxonConcept ;
    dcterms:title "Panthera pardus sec. Catalogue of Life 2024-01-24" ;
    tcs:accordingTo <https://doi.org/10.48580/dfrdl> ;
    tcs:taxonName: [ a tcs:TaxonName ;
            tcs:nameString: "Panthera pardus" ;
            tcs:basionym [ a tcs:TaxonName ;
                    tcs:nameString: "Felis pardus" ;
                    dwc:scientificNameAuthorship "Linnaeus" ;
                        dwc:namePublishedInYear "1758" ]] ;
    tcs:vernacularName [ a gbif:VernacularName ;
            dwc:vernacularName "Panther" ] ;
    tcs:taxonRank <http://rs.gbif.org/vocabulary/gbif/rank/species> .

<https://www.catalogueoflife.org/data/taxon/4CGXS> a tcs:TaxonConcept ;
    dcterms:title "Panthera tigris sec. Catalogue of Life 2024-01-24" ;
    tcs:accordingTo <https://doi.org/10.48580/dfrdl> ;
    tcs:taxonName: [ a tcs:TaxonName ;
            tcs:nameString: "Panthera tigris" ;
            tcs:basionym [ a tcs:TaxonName ;
                    tcs:nameString: "Felis tigris" ;
                    dwc:scientificNameAuthorship "Linnaeus" ;
                        dwc:namePublishedInYear "1758" ]] ;
    tcs:vernacularName [ a gbif:VernacularName ;
            dwc:vernacularName "Tiger" ] ;
    tcs:taxonRank <http://rs.gbif.org/vocabulary/gbif/rank/species> .

<https://www.catalogueoflife.org/data/taxon/4CGXT> a tcs:TaxonConcept ;
    dcterms:title "Panthera uncia sec. Catalogue of Life 2025-09-04" ;
    tcs:accordingTo <https://doi.org/10.48580/dfrdl> ;
    tcs:taxonName: [ a tcs:TaxonName ;
            tcs:nameString: "Panthera uncia" ;
            tcs:basionym [ a tcs:TaxonName ;
                    tcs:nameString: "Felis uncia" ;
                    dwc:scientificNameAuthorship "Schreber" ;
                        dwc:namePublishedInYear "1775" ]] ;
    tcs:vernacularName [ a gbif:VernacularName ;
            dwc:vernacularName "Snow leopard" ] ;
    tcs:taxonRank <http://rs.gbif.org/vocabulary/gbif/rank/species> .
```

[&#91;TurTLe&#93;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonConcept-child-example-1.ttl)&nbsp;[&#91;JSON-LD&#93;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonConcept-child-example-1.jsonld)

