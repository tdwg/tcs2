Taxonomic treatment:

```turtle
ex:taxon-concept/1 a :TaxonConcept ;
    skos:prefLabel "Dicranoloma blumei sec. Klazenga 1999" ;
    :taxonName [ <https://www.tropicos.org/name/35121475> a :TaxonName ;
            :taxonNameString "Dicranoloma blumei" ;
            dwc:scientificNameAuthorship "(Nees) Renauld" ] ;
    :accordingTo [ <https://www.tropicos.org/reference/9020903> a bibo:AcademicArticle ;
            dcterms:bibliographicCitation "Klazenga, N. (1999). A revision of the Malesian 
                    species of Dicranoloma (Dicranaceae, Musci). Journal of the Hattori
                    Botanical Laboratory 87: 1-130." ] .
```

Field guide:

```turtle
ex:taxon-concept/3 a :TaxonConcept ;
        skos:prefLabel "Orthetrum caledonicum sec. Theischinger and Hawking 2010" ;
        :taxonName [ a :TaxonName ; 
                :taxonNameString "Orthetrum caledonicum" ] ;
        :vernacularName [ a :TaxonName ;
                :taxonNameString "Blue Skimmer" ] ;
        :accordingTo [ <urn:isbn:978-0-643-09073-6> a bibo:Book ;
                dcterms:bibliographicCitation "Theischinger, G.; Hawking, J. (2010). The 
                        complete field guide to dragonflies of Australia. CSIRO Publishing, 
                        Collingwood, Australia." ] .

```

Checklist:

```turtle
ex:taxon-concept/2 a :TaxonConcept ;
    skos:prefLabel "Calymperes moluccense sec. Yong et al. 2013" ;
    :taxonName [ <https://www.tropicos.org/name/35153806> a :TaxonName ;
            :taxonNameString "Calymperes moluccense" ;
            dwc:scientificNameAuthorship "Schwägr." ] ;
    :accordingTo [ <urn:isbn:978-967-5221-99-6> a bibo:Book ;
            dcterms:bibliographicCitation "Yong, K.T.; Tan, B.C.; Ho, B.C.; Ho, Q.Y.; Mohamed, H.
                    A revised Moss Checklist of Peninsular Malaysia and Singapore. Research 
                    Pamphlet no. 133, Forest Research Institute Malaysia, Kepong, Malaysia." ] .
```

Plants of the World Online:

```turtle
<https://powo.science.kew.org/taxon/urn:lsid:ipni.org:names:105644-1> a :TaxonConcept ;
    skos:prefLabel "Begonia salaziensis sec. POWO 2022" ;
    :taxonName [ <https://www.ipni.org/n/105644-1> a :TaxonName ;
            :taxonNameString "Begonia salaziensis" ; 
            dwc:scientificNameAuthorship "Warb." ;
            dwc:namePublishedIn "Nat. Pflanzenfam. [Engler & Prantl] iii. 6 a. (1894) 139." ] ;
    :accordingTo [ <urn:lsid:ipni.org:publications:17755-2> a bibo:Book ;
        dcterms:bibliographicCitation "Govaerts, R. (1996). World Checklist of Seed Plants 2(1, 2): 
                1-492. MIM, Deurne." ] .
```

Catalogue of Life:

```turtle
<https://www.catalogueoflife.org/data/taxon/KF8T> a :TaxonConcept ;
    skos:prefLabel "Balaenoptera musculus sec. CoL 2022-11-14" ;
    :taxonName [ a :TaxonName ;
            :taxonNameString "Balaenoptera musculus" ;
            dwc:scientificNameAuthorship "(Linnaeus, 1758)" ] ;
    :accordingTo [ <https://www.catalogueoflife.org#v2022-11-14> a bibo:Website ;
            dcterms:isVersionOf "https://www.catalogueoflife.org" ;
            dcterms:title "Catalogue of Life, version 2022-11-14" ;
            bibo:uri "https://www.catalogueoflife.org" ] .
```


