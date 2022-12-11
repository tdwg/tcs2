```turtle
[] a :TaxonConcept ;
    skos:prefLabel "Graphium macleayanum sec. Orr & Kitching 2010"
    :taxonName [ a :TaxonName ;
            :taxonNameString "Graphium macleayanum" ]
    :vernacularName [ a TaxonName ;
            :taxonNameString "Macleay's Swallowtail" ] ;
    :accordingTo [ <urn:isbn:978-1-74175-108-6> a bibo:Book ; 
            dcterms:bibliographicCitation "Orr, A. & Kitching, R. (2010). The butterflies of 
                    Australia. Jacana Books, Crows Nest, Australia." ] .
```

```turtle
[] a :TaxonConcept ;
    skos:prefLabel "Quercus robur sec. Duistermaat 2020" ;
    :taxonName [ <https://www.ipni.org/n/304293-2> a :TaxonName ;
            :taxonNameString "Quercus robur" ] ;
    :vernacularName [ a :TaxonName ;
            :taxonNameString "Zomereik" ] ;
    :accordingTo [ <urn:isbn:978-90-01-58956-1> a bibo:Book ;
            dcterms:bibliographicCitation "Duistermaat, H. (2020). Heukels Flora van Nederland, edn 
            24. Noordhoff, Groningen." ] .
```
