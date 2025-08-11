# TaxonConcept child example 1


**Term:** [tcs:childTaxonConcept](/terms/#tcs_childtaxonconcept)


```turtle
<https://www.catalogueoflife.org/data/taxon/6DBT> a tcs:TaxonConcept ;
    dcterms:title "Panthera sec. Catalogue of Life 2024-01-24" ;
    tcs:accordingTo <https://doi.org/10.48580/dfrdl> ;
    tcs:taxonName: [ a tcs:TaxonName ;
            tcs:nameString: "Panthera" ;
            dwc:scientificNameAuthorship: "Oken, 1816" ]  ;
    tcs:childTaxonConcept <https://www.catalogueoflife.org/data/taxon/4CGXP> ,
            <https://www.catalogueoflife.org/data/taxon/4CGXQ> ,
            <https://www.catalogueoflife.org/data/taxon/4CGXR> ,
            <https://www.catalogueoflife.org/data/taxon/4CGXS> .

<https://www.catalogueoflife.org/data/taxon/4CGXP> a tcs:TaxonConcept ;
    dcterms:title "Panthera leo sec. Catalogue of Life 2024-01-24" ;
    tcs:accordingTo <https://doi.org/10.48580/dfrdl> ;
    tcs:taxonName: [ a tcs:TaxonName ;
            tcs:nameString: "Panthera leo" ;
            dwc:scientificNameAuthorship: "(Linnaeus, 1758)" ] .

<https://www.catalogueoflife.org/data/taxon/4CGXQ> a tcs:TaxonConcept ;
    dcterms:title "Panthera onca sec. Catalogue of Life 2024-01-24" ;
    tcs:accordingTo <https://doi.org/10.48580/dfrdl> ;
    tcs:taxonName: [ a tcs:TaxonName ;
            tcs:nameString: "Panthera onca" ;
            dwc:scientificNameAuthorship: "(Linnaeus, 1758)" ] .

<https://www.catalogueoflife.org/data/taxon/4CGXR> a tcs:TaxonConcept ;
    dcterms:title "Panthera pardus sec. Catalogue of Life 2024-01-24" ;
    tcs:accordingTo <https://doi.org/10.48580/dfrdl> ;
    tcs:taxonName: [ a tcs:TaxonName ;
            tcs:nameString: "Panthera pardus" ;
            dwc:scientificNameAuthorship: "(Linnaeus, 1758)" ] .

<https://www.catalogueoflife.org/data/taxon/4CGXS> a tcs:TaxonConcept ;
    dcterms:title "Panthera tigris sec. Catalogue of Life 2024-01-24" ;
    tcs:accordingTo <https://doi.org/10.48580/dfrdl> ;
    tcs:taxonName: [ a tcs:TaxonName ;
            tcs:nameString: "Panthera tigris" ;
            dwc:scientificNameAuthorship: "(Linnaeus, 1758)" ] .
```

[&#91;TurTLe&#93;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonConcept-child-example-1.ttl)&nbsp;[&#91;JSON-LD&#93;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonConcept-child-example-1.jsonld)

