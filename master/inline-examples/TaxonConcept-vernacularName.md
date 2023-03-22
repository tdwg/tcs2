```turtle
[] a :TaxonConcept ;
    dcterms:title "Graphium macleayanum sec. Orr & Kitching (2010)"
    :taxonName [ a :TaxonName ;
            :taxonNameString "Graphium macleayanum" ] ;
    :vernacularName [ a gbif:VernacularName ;
            dwc:vernacularName "Macleay's Swallowtail" 
            dcterms:language: "en" ] ;
    :accordingTo <urn:isbn:978-1-74175-108-6> .

<urn:isbn:978-1-74175-108-6> a bibo:Book ; 
    dcterms:bibliographicCitation """Orr, A. & Kitching, R. (2010). The 
            butterflies of Australia. Jacana Books, Crows Nest, Australia.""" .
```

```turtle
[] a :TaxonConcept ;
    dcterms:title "Quercus robur sec. Duistermaat (2020)" ;
    :taxonName <https://www.ipni.org/n/304293-2> ;
    :vernacularName [ a gbif:VernacularName ;
            dwc:vernacularName "Zomereik" ;
            dcterms:language "nl" ] ;
    :accordingTo [ <urn:isbn:978-90-01-58956-1> a bibo:Book ;
            dcterms:bibliographicCitation """Duistermaat, H. (2020). Heukels 
                    Flora van Nederland, edn 24. Noordhoff, Groningen.""" ] .

<https://www.ipni.org/n/304293-2> a :TaxonName ;
    :taxonNameString "Quercus robur" .
```

```turtle
<https://vicflora.rbg.vic.gov.au/flora/taxon/93c88fde-ab15-4a9a-a61d-3830a57a0160#2023-03-02> 
    a :TaxonConcept ;
    dcterms:title "Callitris verrucosa sec. VicFlora (2023-03-22)" ;
    :taxonName <https://www.ipni.org/n/134460-3> ;
    :vernacularName [ a gbif:VernacularName ; 
            dwc:vernacularName "Scrub Cypress-pine" ;
            dcterms:language "en" ;
            gbif:isPreferredName: <http://rs.gbif.org/vocab/boolean/true> ] ;
    :vernacularName [ a gbif:VernacularName ; 
            dwc:vernacularName "Mallee Pine" ;
            dcterms:language "en" ;
            gbif:isPreferredName: <http://rs.gbif.org/vocab/boolean/false> ] ;
    :vernacularName [ a gbif:VernacularName ; 
            dwc:vernacularName "Cow Pine" ;
            dcterms:language "en" ;
            gbif:isPreferredName: <http://rs.gbif.org/vocab/boolean/false> ] ;
    :vernacularName [ a gbif:VernacularName ; 
            dwc:vernacularName "Turpentine Pine" ;
            dcterms:language "en" ;
            gbif:isPreferredName: <http://rs.gbif.org/vocab/boolean/false> ] ;
    :accordingTo [ a bibo:Website ;
            dcterms:bibliographicCitation """VicFlora (2023). Flora of Victoria, 
                    Royal Botanic Gardens Victoria. Available online: 
                    https://vicflora.rbg.vic.gov.au (accessed on: 22 Mar. 2023).""" ].

<https://www.ipni.org/n/134460-3> a TaxonName ;
    :taxonNameString "Callitris verrucosa" .
```
