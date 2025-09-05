# TaxonConcept parent example 1


**Term:** [tcs:parentTaxonConcept](../terms/#tcs_parenttaxonconcept)


```turtle
<https://www.catalogueoflife.org/data/taxon/6DBT> a tcs:TaxonConcept ;
    dcterms:title "Panthera sec. Catalogue of Life 2024-01-24" ;
    tcs:accordingTo <https://doi.org/10.48580/dfrdl> ;
    tcs:taxonName: [ a tcs:TaxonName ;
            tcs:nameString "Panthera" ;
            dwc:scientificNameAuthorship "Oken, 1816" ] ;
    tcs:vernacularName [ a gbif:VernacularName ;
            dwc:vernacularName "Roaring cats"] ;
    tcs:taxonRank <http://rs.gbif.org/vocabulary/gbif/rank/genus> .

<https://www.catalogueoflife.org/data/taxon/4CGXP> a tcs:TaxonConcept ;
    dcterms:title "Panthera leo sec. Catalogue of Life 2024-01-24" ;
    tcs:accordingTo <https://doi.org/10.48580/dfrdl> ;
    tcs:taxonName: [ a tcs:TaxonName ;
            tcs:nameString: "Panthera leo" ;
            dwc:scientificNameAuthorship "(Linnaeus, 1758)" ] ;
    tcs:vernacularName: [ a gbif:VernacularName ;
            dwc:vernacularName "Lion"] ;
    tcs:taxonRank <http://rs.gbif.org/vocabulary/gbif/rank/species> ;
    tcs:parentTaxonConcept <https://www.catalogueoflife.org/data/taxon/6DBT> .

<https://www.catalogueoflife.org/data/taxon/4CGXQ> a tcs:TaxonConcept ;
    dcterms:title "Panthera onca sec. Catalogue of Life 2024-01-24" ;
    tcs:accordingTo <https://doi.org/10.48580/dfrdl> ;
    tcs:taxonName: [ a tcs:TaxonName ;
            tcs:nameString "Panthera onca" ;
            dwc:scientificNameAuthorship "(Linnaeus, 1758)" ] ;
    tcs:vernacularName: [ a gbif:VernacularName ;
            dwc:vernacularName "Jaguar"] ;
    tcs:taxonRank <http://rs.gbif.org/vocabulary/gbif/rank/species> ;
    tcs:parentTaxonConcept <https://www.catalogueoflife.org/data/taxon/6DBT> .

<https://www.catalogueoflife.org/data/taxon/4CGXR> a tcs:TaxonConcept ;
    dcterms:title "Panthera pardus sec. Catalogue of Life 2024-01-24" ;
    tcs:accordingTo <https://doi.org/10.48580/dfrdl> ;
    tcs:taxonName: [ a tcs:TaxonName ;
            tcs:nameString "Panthera pardus" ;
            dwc:scientificNameAuthorship "(Linnaeus, 1758)" ] ;
    tcs:vernacularName: [ a gbif:VernacularName ;
            dwc:vernacularName "Panther"] ,
        [ a gbif:VernacularName ;
            dwc:vernacularName "Leopard" ] ;
    tcs:taxonRank <http://rs.gbif.org/vocabulary/gbif/rank/species> ;
    tcs:parentTaxonConcept <https://www.catalogueoflife.org/data/taxon/6DBT> .

<https://www.catalogueoflife.org/data/taxon/4CGXS> a tcs:TaxonConcept ;
    dcterms:title "Panthera tigris sec. Catalogue of Life 2024-01-24" ;
    tcs:accordingTo <https://doi.org/10.48580/dfrdl> ;
    tcs:taxonName: [ a tcs:TaxonName ;
            tcs:nameString "Panthera tigris" ;
            dwc:scientificNameAuthorship "(Linnaeus, 1758)" ] ;
    tcs:vernacularName: [ a gbif:VernacularName ;
            dwc:vernacularName "Tiger"] ;
    tcs:taxonRank <http://rs.gbif.org/vocabulary/gbif/rank/species> ;
    tcs:parentTaxonConcept <https://www.catalogueoflife.org/data/taxon/6DBT> .

<https://www.catalogueoflife.org/data/taxon/4CGXT> a tcs:TaxonConcept ;
    dcterms:title "Panthera uncia sec. Catalogue of Life 2025-09-04" ;
    tcs:accordingTo <https://doi.org/10.48580/dfrdl> ;
    tcs:taxonName: [ a tcs:TaxonName ;
            tcs:nameString "Panthera uncia" ;
            dwc:scientificNameAuthorship "(Schreber, 1775)" ] ;
    tcs:vernacularName: [ a gbif:VernacularName ;
            dwc:vernacularName "Snow leopard"] ;
    tcs:taxonRank <http://rs.gbif.org/vocabulary/gbif/rank/species> ;
    tcs:parentTaxonConcept <https://www.catalogueoflife.org/data/taxon/6DBT> .
```

[&#91;TurTLe&#93;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonConcept-parent-example-1.ttl)&nbsp;[&#91;JSON-LD&#93;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonConcept-parent-example-1.jsonld)

