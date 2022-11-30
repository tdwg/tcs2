# Example of a Taxon Concept from a taxonomic revision: Dicranoloma assimile sec. Klazenga 1999

```json
{
  "@context": [
    {
      "xsd": "http://www.w3.org/2001/XMLSchema#",

      "@vocab": "http://rs.tdwg.org/tcs/terms/",
      "taxonName": { "@type": "@id" },
      "accordingTo": { "@type": "@id" },
      "verbatimNameString": { "@type": "xsd:String" },
      "taxonomicRank": { "@type": "@id" },
      "parent": { "@type": "@id" },
      "children": { "@reverse": "parent" },
      "synonyms": { "@id": "http://rs.tdwg.org/tcs/terms/synonym", "@type": "@id" },
      "vernacularName": { "@type": "@id" },
      "relationshipType": { "@type": "@id" },
      "subjectTaxonConcept": { "@type": "@id" },
      "objectTaxonConcept": { "@type": "@id" },
      "relationshipAccordingTo": { "@type": "@id" },
      "taxonomicNameString": { "@type": "xsd:String" },
      "namePublishedIn": { "@type": "@id" },
      "microReference": { "@type": "xsd:String" },
      "nomenclaturalCode": { "@type": "@id" },
      "nomenclaturalStatus": { "@type": "@id" },
      "basionym": { "@type": "@id" },
      "replacementNameFor": { "@type": "@id" },
      "basedOn": { "@type": "@id" },
      "conservedAgainst": { "@type": "@id" },
      "typifiedName": { "@type": "@id" },
      "typeOfType": { "@type": "@id" },
      "typeName": { "@type": "@id" },
      "typeSpecimen": { "@type": "@id" },
      "typePublishedIn": { "@type": "@id" },

      "dwc": "http://rs.tdwg.org/dwc/terms/",
      "dwc:scientificName": { "@type": "xsd:string"},
      "dwc:scientificNameAuthorship": { "@type": "xsd:string" },
      "dwc:namePublishedIn": { "@type": "xsd:string" },
      "dwc:genericName": { "@type": "xsd:string" },
      "dwc:infragenericEpithet": { "@type": "xsd:string" },
      "dwc:specificEpithet": { "@type": "xsd:string" },
      "dwc:infraspecificEpithet": { "@type": "xsd:string" },
      "dwc:cultivarEpithet": { "@type": "xsd:string" }     
    },
    {
      "dcterms": "http://purl.org/dc/terms/",
      "skos": "http://www.w3.org/2004/02/skos/core#",
      "skosxl": "http://www.w3.org/2008/05/skos-xl#",
      "ex": "https://tdwg.github.io/tcs2/examples/"
    }
  ],
  "@id": "ex:1",
  "dcterms:title": "Example of a Taxon Concept from a taxonomic revision: Dicranoloma assimile sec. Klazenga 1999",
  "@graph": [
    {
      "@id": "ex:1/taxon-concept/1",
      "@type": ["TaxonConcept", "skos:Concept"],
      "skos:prefLabel": "Dicranoloma assimile sec. Klazenga 1999",
      "taxonName": "https://www.tropicos.org/name/35121458",
      "accordingTo": "https://www.tropicos.org/reference/9020903",
      "synonyms": [
        "https://www.tropicos.org/name/35124384",
        "https://www.tropicos.org/name/35121535",
        {
          "taxonomicNameString": "Dicranoloma assimile f. major",
          "dwc:scientificName": "Dicranoloma assimile f. major M.Fleisch.",
          "dwc:scientificNameAuthorship": "M.Fleisch.",
          "dwc:namePublishedIn": "Musci Fl. Buitenzorg 74 (1904)",
          "dwc:namePublishedInYear": "1904"
        },
        "https://www.tropicos.org/name/35121587",
        "https://www.tropicos.org/name/35121523",
        "https://www.tropicos.org/name/35121524",
        "https://www.tropicos.org/name/35121480",
        "https://www.tropicos.org/name/35168349"
      ]
    },
    {
      "@id": "https://www.tropicos.org/name/35121458",
      "@type": ["TaxonName", "skosxl:Label"],
      "taxonomicNameString": "Dicranoloma assimile",
      "dwc:scientificName": "Dicranoloma assimile (Hampe) Renauld",
      "dwc:scientificNameAuthorship": "(Hampe) Renauld",
      "dwc:namePublishedIn": "Rev. Bryol. 28: 69 (1901)",
      "dwc:namePublishedInYear": "1901",
      "basionym": "https://www.tropicos.org/name/35121913"
    },
    {
      "@id": "https://www.tropicos.org/name/35121913",
      "@type": "TaxonName",
      "taxonomicNameString": "Dicranolum assimile",
      "dwc:scientificName": "Dicranum assimile Hampe",
      "dwc:scientificNameAuthorship": "Hampe",
      "dwc:namePublishedIn": "Icon. Musc. 24 (1844)",
      "dwc:namePublishedInYear": "1844"
    },
    {
      "@id": "https://www.tropicos.org/name/35154841",
      "@type": "TaxonName",
      "taxonomicNameString": "Leucoloma assimile",
      "dwc:scientificName": "Leucoloma assimile (Hampe) Broth.",
      "dwc:scientificNameAuthorship": "(Hampe) Broth.",
      "dwc:namePublishedIn": "Nat. Pflanzenfam. 1,3: 322 (1901)",
      "dwc:namePublishedInYear": "1901",
      "basionym": "https://www.tropicos.org/name/35121913"
    },
    {
      "@id": "https://www.tropicos.org/name/35124384",
      "@type": "TaxonName",
      "taxonomicNameString": "Dicranum sumatranum",
      "dwc:scientificName": "Dicranum sumatranum Müll.Hal.",
      "dwc:scientificNameAuthorship": "Müll.Hal.",
      "dwc:namePublishedIn": "Genera musc. fr.: 285 (1901)",
      "dwc:namePublishedInYear": "1901"
    },
    {
      "@id": "https://www.tropicos.org/name/35155131",
      "@type": "TaxonName",
      "taxonomicNameString": "Leucoloma sumatranum",
      "dwc:scientificName": "Leucoloma sumatranum (Müll.Hal.) Broth.",
      "dwc:scientificNameAuthorship": "(Müll.Hal.) Broth.",
      "dwc:namePublishedIn": "Nat. Pflanzenfam. 1,3: 322 (1901)",
      "dwc:namePublishedInYear": "1901",
      "basionym": "https://www.tropicos.org/name/35124384"
    },
    {
      "@id": "https://www.tropicos.org/name/35121646",
      "@type": "TaxonName",
      "taxonomicNameString": "Dicranoloma sumatranum",
      "dwc:scientificName": "Dicranoloma sumatranum (Müll.Hal.) Renauld",
      "dwc:scientificNameAuthorship": "(Müll.Hal.) Renauld",
      "dwc:namePublishedIn": "Essai Leucoloma 14 (1909)",
      "dwc:namePublishedInYear": "1901",
      "basionym": "https://www.tropicos.org/name/35124384"
    },
    {
      "@id": "https://www.tropicos.org/name/35121535",
      "@type": "TaxonName",
      "taxonomicNameString": "Dicranoloma gedeanum",
      "dwc:scientificName": "Dicranoloma gedeanum Renauld & Cardot",
      "dwc:scientificNameAuthorship": "Renauld & Cardot",
      "dwc:namePublishedIn": "Rev. Bryol. 28: 117 (1901)",
      "dwc:namePublishedInYear": "1901"
    },
    {
      "@id": "https://www.tropicos.org/name/35121587",
      "@type": "TaxonName",
      "taxonomicNameString": "Dicranoloma perarmatum",
      "dwc:scientificName": "Dicranoloma gedeanum Broth.",
      "dwc:scientificNameAuthorship": "Broth.",
      "dwc:namePublishedIn": "Öfvers. Finska Vetensk.-Soc. Förh. 47(14): 1 (1905)",
      "dwc:namePublishedInYear": "1905"
    },
    {
      "@id": "https://www.tropicos.org/name/35121523",
      "@type": "TaxonName",
      "taxonomicNameString": "Dicranoloma euryloma",
      "dwc:scientificName": "Dicranoloma euryloma Dixon",
      "dwc:scientificNameAuthorship": "Dixon",
      "dwc:namePublishedIn": "J. Linn. Soc. Bot. 50: 69 (1935)",
      "dwc:namePublishedInYear": "1935"
    },
    {
      "@id": "https://www.tropicos.org/name/35121524",
      "@type": "TaxonName",
      "taxonomicNameString": "Dicranoloma euryloma var. rugifolium",
      "dwc:scientificName": "Dicranoloma euryloma var. rugifolium E.B.Bartram",
      "dwc:scientificNameAuthorship": "E.B.Bartram",
      "dwc:namePublishedIn": "Philipp. J. Sci. 61: 237 (1936)",
      "dwc:namePublishedInYear": "1936"
    },
    {
      "@id": "https://www.tropicos.org/name/35121480",
      "@type": "TaxonName",
      "taxonomicNameString": "Dicranoloma brachyphyllum",
      "dwc:scientificName": "Dicranoloma brachyphyllum Nog.",
      "dwc:scientificNameAuthorship": "Nog.",
      "dwc:namePublishedIn": "J. Hattori Bot. Lab. 10: 3 (1953)",
      "dwc:namePublishedInYear": "1953"
    },
    {
      "@id": "https://www.tropicos.org/name/35168349",
      "@type": "TaxonName",
      "taxonomicNameString": "Dicranoloma havilandii var. latifolium",
      "dwc:scientificName": "Dicranoloma havilandii var. latifolium Zanten",
      "dwc:scientificNameAuthorship": "Zanten",
      "dwc:namePublishedIn": "Nova Guinea, Bot. 10(16): 272 (1964)",
      "dwc:namePublishedInYear": "1964"
    },
    {
      "@id": "https://www.tropicos.org/reference/9020903",
      "@type": "bibo:AcademicArticle",
      "dcterms:title": "A revision of the Malesian species of Dicranoloma (Dicranaceae, Musci)",
      "bibo:pages": "1-130",
      "bibo:authorList": [
        {
          "@type": "foaf:Person",
          "foaf:givenName": "Niels",
          "foaf:familyName": "Klazenga"
        }
      ],
      "dcterms:isPartOf": {
        "@type": "bibo:Issue",
        "dcterms:date": "1999",
        "bibo:volume": "87",
        "dcterms:isPartOf": {
          "@type": "bibo:Journal",
          "dcterms:title": "Journal of the Hattori Botanical Laboratory",
          "dcterms:shortTitle": "J. Hattori Bot. Lab."
        }
      }
    }
  ]
}
```

```turtle
@prefix : <http://rs.tdwg.org/tcs/terms/> .
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix dwc: <http://rs.tdwg.org/dwc/terms/> .
@prefix ns1: <bibo:> .
@prefix ns2: <foaf:> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix skosxl: <http://www.w3.org/2008/05/skos-xl#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://tdwg.github.io/tcs2/examples/1> dcterms:title "Example of a Taxon Concept from a taxonomic revision: Dicranoloma assimile sec. Klazenga 1999" .

<https://tdwg.github.io/tcs2/examples/1/taxon-concept/1> a :TaxonConcept, skos:Concept ;
    skos:prefLabel "Dicranoloma assimile sec. Klazenga 1999" ;
    :taxonName <https://www.tropicos.org/name/35121458> ;
    :accordingTo <https://www.tropicos.org/reference/9020903> ;
    :synonym (  
        <https://www.tropicos.org/name/35124384> 
        <https://www.tropicos.org/name/35121535> 
        [ 
            dwc:namePublishedIn "Musci Fl. Buitenzorg 74 (1904)"^^xsd:string ;
            dwc:namePublishedInYear "1904" ;
            dwc:scientificName "Dicranoloma assimile f. major M.Fleisch."^^xsd:string ;
            dwc:scientificNameAuthorship "M.Fleisch."^^xsd:string ;
            :taxonomicNameString "Dicranoloma assimile f. major"^^xsd:String 
        ] 
        <https://www.tropicos.org/name/35121587> 
        <https://www.tropicos.org/name/35121523> 
        <https://www.tropicos.org/name/35121524> 
        <https://www.tropicos.org/name/35121480> 
        <https://www.tropicos.org/name/35168349> 
    ) .

<https://www.tropicos.org/name/35121646> a :TaxonName ;
    dwc:namePublishedIn "Essai Leucoloma 14 (1909)"^^xsd:string ;
    dwc:namePublishedInYear "1901" ;
    dwc:scientificName "Dicranoloma sumatranum (Müll.Hal.) Renauld"^^xsd:string ;
    dwc:scientificNameAuthorship "(Müll.Hal.) Renauld"^^xsd:string ;
    :basionym <https://www.tropicos.org/name/35124384> ;
    :taxonomicNameString "Dicranoloma sumatranum"^^xsd:String .

<https://www.tropicos.org/name/35154841> a :TaxonName ;
    dwc:namePublishedIn "Nat. Pflanzenfam. 1,3: 322 (1901)"^^xsd:string ;
    dwc:namePublishedInYear "1901" ;
    dwc:scientificName "Leucoloma assimile (Hampe) Broth."^^xsd:string ;
    dwc:scientificNameAuthorship "(Hampe) Broth."^^xsd:string ;
    :basionym <https://www.tropicos.org/name/35121913> ;
    :taxonomicNameString "Leucoloma assimile"^^xsd:String .

<https://www.tropicos.org/name/35155131> a :TaxonName ;
    dwc:namePublishedIn "Nat. Pflanzenfam. 1,3: 322 (1901)"^^xsd:string ;
    dwc:namePublishedInYear "1901" ;
    dwc:scientificName "Leucoloma sumatranum (Müll.Hal.) Broth."^^xsd:string ;
    dwc:scientificNameAuthorship "(Müll.Hal.) Broth."^^xsd:string ;
    :basionym <https://www.tropicos.org/name/35124384> ;
    :taxonomicNameString "Leucoloma sumatranum"^^xsd:String .

<https://www.tropicos.org/name/35121458> a :TaxonName,
        skosxl:Label ;
    dwc:namePublishedIn "Rev. Bryol. 28: 69 (1901)"^^xsd:string ;
    dwc:namePublishedInYear "1901" ;
    dwc:scientificName "Dicranoloma assimile (Hampe) Renauld"^^xsd:string ;
    dwc:scientificNameAuthorship "(Hampe) Renauld"^^xsd:string ;
    :basionym <https://www.tropicos.org/name/35121913> ;
    :taxonomicNameString "Dicranoloma assimile"^^xsd:String .

<https://www.tropicos.org/name/35121480> a :TaxonName ;
    dwc:namePublishedIn "J. Hattori Bot. Lab. 10: 3 (1953)"^^xsd:string ;
    dwc:namePublishedInYear "1953" ;
    dwc:scientificName "Dicranoloma brachyphyllum Nog."^^xsd:string ;
    dwc:scientificNameAuthorship "Nog."^^xsd:string ;
    :taxonomicNameString "Dicranoloma brachyphyllum"^^xsd:String .

<https://www.tropicos.org/name/35121523> a :TaxonName ;
    dwc:namePublishedIn "J. Linn. Soc. Bot. 50: 69 (1935)"^^xsd:string ;
    dwc:namePublishedInYear "1935" ;
    dwc:scientificName "Dicranoloma euryloma Dixon"^^xsd:string ;
    dwc:scientificNameAuthorship "Dixon"^^xsd:string ;
    :taxonomicNameString "Dicranoloma euryloma"^^xsd:String .

<https://www.tropicos.org/name/35121524> a :TaxonName ;
    dwc:namePublishedIn "Philipp. J. Sci. 61: 237 (1936)"^^xsd:string ;
    dwc:namePublishedInYear "1936" ;
    dwc:scientificName "Dicranoloma euryloma var. rugifolium E.B.Bartram"^^xsd:string ;
    dwc:scientificNameAuthorship "E.B.Bartram"^^xsd:string ;
    :taxonomicNameString "Dicranoloma euryloma var. rugifolium"^^xsd:String .

<https://www.tropicos.org/name/35121535> a :TaxonName ;
    dwc:namePublishedIn "Rev. Bryol. 28: 117 (1901)"^^xsd:string ;
    dwc:namePublishedInYear "1901" ;
    dwc:scientificName "Dicranoloma gedeanum Renauld & Cardot"^^xsd:string ;
    dwc:scientificNameAuthorship "Renauld & Cardot"^^xsd:string ;
    :taxonomicNameString "Dicranoloma gedeanum"^^xsd:String .

<https://www.tropicos.org/name/35121587> a :TaxonName ;
    dwc:namePublishedIn "Öfvers. Finska Vetensk.-Soc. Förh. 47(14): 1 (1905)"^^xsd:string ;
    dwc:namePublishedInYear "1905" ;
    dwc:scientificName "Dicranoloma gedeanum Broth."^^xsd:string ;
    dwc:scientificNameAuthorship "Broth."^^xsd:string ;
    :taxonomicNameString "Dicranoloma perarmatum"^^xsd:String .

<https://www.tropicos.org/name/35168349> a :TaxonName ;
    dwc:namePublishedIn "Nova Guinea, Bot. 10(16): 272 (1964)"^^xsd:string ;
    dwc:namePublishedInYear "1964" ;
    dwc:scientificName "Dicranoloma havilandii var. latifolium Zanten"^^xsd:string ;
    dwc:scientificNameAuthorship "Zanten"^^xsd:string ;
    :taxonomicNameString "Dicranoloma havilandii var. latifolium"^^xsd:String .

<https://www.tropicos.org/reference/9020903> a ns1:AcademicArticle ;
    ns1:authorList [ a ns2:Person ;
            ns2:familyName "Klazenga" ;
            ns2:givenName "Niels" ] ;
    ns1:pages "1-130" ;
    dcterms:isPartOf [ a ns1:Issue ;
            ns1:volume "87" ;
            dcterms:date "1999" ;
            dcterms:isPartOf [ a ns1:Journal ;
                    dcterms:shortTitle "J. Hattori Bot. Lab." ;
                    dcterms:title "Journal of the Hattori Botanical Laboratory" ] ] ;
    dcterms:title "A revision of the Malesian species of Dicranoloma (Dicranaceae, Musci)" .

<https://www.tropicos.org/name/35121913> a :TaxonName ;
    dwc:namePublishedIn "Icon. Musc. 24 (1844)"^^xsd:string ;
    dwc:namePublishedInYear "1844" ;
    dwc:scientificName "Dicranum assimile Hampe"^^xsd:string ;
    dwc:scientificNameAuthorship "Hampe"^^xsd:string ;
    :taxonomicNameString "Dicranolum assimile"^^xsd:String .

<https://www.tropicos.org/name/35124384> a :TaxonName ;
    dwc:namePublishedIn "Genera musc. fr.: 285 (1901)"^^xsd:string ;
    dwc:namePublishedInYear "1901" ;
    dwc:scientificName "Dicranum sumatranum Müll.Hal."^^xsd:string ;
    dwc:scientificNameAuthorship "Müll.Hal."^^xsd:string ;
    :taxonomicNameString "Dicranum sumatranum"^^xsd:String .
```