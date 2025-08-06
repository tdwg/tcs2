# TaxonConcept-vernacularName-example-3

```turtle
<https://vicflora.rbg.vic.gov.au/flora/taxon/93c88fde-ab15-4a9a-a61d-3830a57a0160#2023-03-02> 
    a tcs:TaxonConcept ;
    dcterms:title "Callitris verrucosa sec. VicFlora 2023-03-22" ;
    tcs:accordingTo [ a bibo:Website ;
            dcterms:bibliographicCitation """VicFlora (2023). Flora of Victoria, 
                    Royal Botanic Gardens Victoria. Available online: 
                    https://vicflora.rbg.vic.gov.au (accessed on: 22 Mar. 2023).""" ] ;
    tcs:taxonName <https://ipni.org/n/134460-3> ;
    tcs:vernacularName [ a gbif:VernacularName ; 
            dwc:vernacularName "Scrub Cypress-pine" ;
            dcterms:language "en" ;
            gbif:isPreferredName <http://rs.gbif.org/vocab/boolean/true> ] ,
        [ a gbif:VernacularName ; 
            dwc:vernacularName "Mallee Pine" ;
            dcterms:language "en" ;
            gbif:isPreferredName <http://rs.gbif.org/vocab/boolean/false> ] ,
        [ a gbif:VernacularName ; 
            dwc:vernacularName "Cow Pine" ;
            dcterms:language "en" ;
            gbif:isPreferredName <http://rs.gbif.org/vocab/boolean/false> ] ,
        [ a gbif:VernacularName ; 
            dwc:vernacularName "Turpentine Pine" ;
            dcterms:language "en" ;
            gbif:isPreferredName <http://rs.gbif.org/vocab/boolean/false> ] .

<https://ipni.org/n/134460-3> a tcs:TaxonName ;
    tcs:nameString "Callitris verrucosa" ;
    dwc:scientificNameAuthorship "(A.Cunn. ex Endl.) F.Muell." .
```

[&lsqb;TaxonConcept-vernacularName-example-3.ttl&rsqb;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonConcept-vernacularName-example-3.ttl)&nbsp;[&lsqb;TaxonConcept-vernacularName-example-3.jsonld&rsqb;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonConcept-vernacularName-example-3.jsonld)

