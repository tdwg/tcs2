# Example 1
## Example of a Taxon Concept from a taxonomic revision: Dicranoloma assimile sec. Klazenga 1999

### JSON-LD

```json
{
  "@context": [
    "https://raw.githubusercontent.com/tdwg/tcs2/examples/docs/examples/context.jsonld",
    {"ex": "https://tdwg.github.io/tcs2/examples/"}
  ],
  "@id": "ex:1",
  "dcterms:title": "Example of a Taxon Concept from a taxonomic revision: Dicranoloma assimile sec. Klazenga 1999",
  "@graph": [
    {
      "@id": "ex:1/taxon-concept/1",
      "@type": [
        "TaxonConcept", 
        "skos:Concept", 
        "openbiodiv-o:TaxonomicConcept", 
        "dwc:Taxon"
      ],
      "skos:prefLabel": "Dicranoloma assimile sec. Klazenga 1999",
      "taxonName": "tropicos:35121458",
      "accordingTo": "https://www.tropicos.org/reference/9020903",
      "dwc:scientificName": "Dicranoloma assimile (Hampe) Renauld",
      "dwc:nameAccordingTo": "Klazenga, 1999",
      "synonyms": [
        "tropicos:35124384",
        "tropicos:35121535",
        {
          "taxonomicNameString": "Dicranoloma assimile f. major",
          "dwc:scientificName": "Dicranoloma assimile f. major M.Fleisch.",
          "dwc:scientificNameAuthorship": "M.Fleisch.",
          "dwc:namePublishedIn": "Musci Fl. Buitenzorg 74 (1904)",
          "dwc:namePublishedInYear": "1904"
        },
        "tropicos:35121587",
        "tropicos:35121523",
        "tropicos:35121524",
        "tropicos:35121480",
        "tropicos:35168349"
      ]
    },
    {
      "@id": "tropicos:35121458",
      "@type": ["TaxonName", "skosxl:Label"],
      "taxonomicNameString": "Dicranoloma assimile",
      "skosxl:literalForm": "Dicranoloma assimile",
      "dwc:scientificNameAuthorship": "(Hampe) Renauld",
      "dwc:namePublishedIn": "Rev. Bryol. 28: 69 (1901)",
      "dwc:namePublishedInYear": "1901",
      "basionym": "tropicos:35121913"
    },
    {
      "@id": "tropicos:35121913",
      "@type": "TaxonName",
      "taxonomicNameString": "Dicranum assimile",
      "dwc:scientificNameAuthorship": "Hampe",
      "dwc:namePublishedIn": "Icon. Musc. 24 (1844)",
      "dwc:namePublishedInYear": "1844"
    },
    {
      "@id": "tropicos:35154841",
      "@type": "TaxonName",
      "taxonomicNameString": "Leucoloma assimile",
      "dwc:scientificNameAuthorship": "(Hampe) Broth.",
      "dwc:namePublishedIn": "Nat. Pflanzenfam. 1,3: 322 (1901)",
      "dwc:namePublishedInYear": "1901",
      "basionym": "tropicos:35121913"
    },
    {
      "@id": "tropicos:35124384",
      "@type": "TaxonName",
      "taxonomicNameString": "Dicranum sumatranum",
      "dwc:scientificNameAuthorship": "Müll.Hal.",
      "dwc:namePublishedIn": "Genera musc. fr.: 285 (1901)",
      "dwc:namePublishedInYear": "1901"
    },
    {
      "@id": "tropicos:35155131",
      "@type": "TaxonName",
      "taxonomicNameString": "Leucoloma sumatranum",
      "dwc:scientificNameAuthorship": "(Müll.Hal.) Broth.",
      "dwc:namePublishedIn": "Nat. Pflanzenfam. 1,3: 322 (1901)",
      "dwc:namePublishedInYear": "1901",
      "basionym": "tropicos:35124384"
    },
    {
      "@id": "tropicos:35121646",
      "@type": "TaxonName",
      "taxonomicNameString": "Dicranoloma sumatranum",
      "dwc:scientificNameAuthorship": "(Müll.Hal.) Renauld",
      "dwc:namePublishedIn": "Essai Leucoloma 14 (1909)",
      "dwc:namePublishedInYear": "1901",
      "basionym": "tropicos:35124384"
    },
    {
      "@id": "tropicos:35121535",
      "@type": "TaxonName",
      "taxonomicNameString": "Dicranoloma gedeanum",
      "dwc:scientificNameAuthorship": "Renauld & Cardot",
      "dwc:namePublishedIn": "Rev. Bryol. 28: 117 (1901)",
      "dwc:namePublishedInYear": "1901"
    },
    {
      "@id": "tropicos:35121587",
      "@type": "TaxonName",
      "taxonomicNameString": "Dicranoloma perarmatum",
      "dwc:scientificNameAuthorship": "Broth.",
      "dwc:namePublishedIn": "Öfvers. Finska Vetensk.-Soc. Förh. 47(14): 1 (1905)",
      "dwc:namePublishedInYear": "1905"
    },
    {
      "@id": "tropicos:35121523",
      "@type": "TaxonName",
      "taxonomicNameString": "Dicranoloma euryloma",
      "dwc:scientificNameAuthorship": "Dixon",
      "dwc:namePublishedIn": "J. Linn. Soc. Bot. 50: 69 (1935)",
      "dwc:namePublishedInYear": "1935"
    },
    {
      "@id": "tropicos:35121524",
      "@type": "TaxonName",
      "taxonomicNameString": "Dicranoloma euryloma var. rugifolium",
      "dwc:scientificNameAuthorship": "E.B.Bartram",
      "dwc:namePublishedIn": "Philipp. J. Sci. 61: 237 (1936)",
      "dwc:namePublishedInYear": "1936"
    },
    {
      "@id": "tropicos:35121480",
      "@type": "TaxonName",
      "taxonomicNameString": "Dicranoloma brachyphyllum",
      "dwc:scientificNameAuthorship": "Nog.",
      "dwc:namePublishedIn": "J. Hattori Bot. Lab. 10: 3 (1953)",
      "dwc:namePublishedInYear": "1953"
    },
    {
      "@id": "tropicos:35168349",
      "@type": "TaxonName",
      "taxonomicNameString": "Dicranoloma havilandii var. latifolium",
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
          "foaf:givenname": "Niels",
          "foaf:surname": "Klazenga"
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

### Turtle

```turtle
@prefix : <http://rs.tdwg.org/tcs/terms/> .
@prefix bibo: <http://purl.org/ontology/bibo/> .
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix dwc: <http://rs.tdwg.org/dwc/terms/> .
@prefix foaf: <http://xmlns.com/foaf/0.1/> .
@prefix openbiodiv-o: <http://openbiodiv.net/> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix skosxl: <http://www.w3.org/2008/05/skos-xl#> .
@prefix tropicos: <https://www.tropicos.org/name/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://tdwg.github.io/tcs2/examples/1> 
    dcterms:title "Example of a Taxon Concept from a taxonomic revision: Dicranoloma assimile sec. Klazenga 1999" .

<https://tdwg.github.io/tcs2/examples/1/taxon-concept/1> a :TaxonConcept, 
        skos:Concept, openbiodiv-o:TaxonomicConcept, dwc:Taxon ;
    skos:prefLabel "Dicranoloma assimile sec. Klazenga 1999" ;
    :taxonName tropicos::35121458 ;
    :accordingTo <https://www.tropicos.org/reference/9020903> ;
    dwc:scientificName "Dicranoloma assimile (Hampe) Renauld" ;
    dwc:nameAccordingTo "Klazenga, 1990",
    :synonym (  
        tropicos::35124384 
        tropicos::35121535 
        [ 
            dwc:namePublishedIn "Musci Fl. Buitenzorg 74 (1904)"^^xsd:string ;
            dwc:namePublishedInYear "1904" ;
            dwc:scientificName "Dicranoloma assimile f. major M.Fleisch."^^xsd:string ;
            dwc:scientificNameAuthorship "M.Fleisch."^^xsd:string ;
            :taxonomicNameString "Dicranoloma assimile f. major"^^xsd:String 
        ] 
        tropicos::35121587 
        tropicos::35121523 
        tropicos::35121524 
        tropicos::35121480 
        tropicos::35168349 
    ) .

tropicos::35121458 a :TaxonName, skosxl:Label ;
    :taxonomicNameString "Dicranoloma assimile"^^xsd:String ;
    skosxl:literalForm "Dicranoloma assimile"^^xsd:string ;
    dwc:namePublishedIn "Rev. Bryol. 28: 69 (1901)"^^xsd:string ;
    dwc:namePublishedInYear "1901" ;
    dwc:scientificNameAuthorship "(Hampe) Renauld"^^xsd:string ;
    :basionym tropicos::35121913 .

tropicos::35121913 a :TaxonName ;
    :taxonomicNameString "Dicranum assimile"^^xsd:String ;
    dwc:scientificNameAuthorship "Hampe"^^xsd:string ;
    dwc:namePublishedIn "Icon. Musc. 24 (1844)"^^xsd:string ;
    dwc:namePublishedInYear "1844" .

tropicos::35154841 a :TaxonName ;
    :taxonomicNameString "Leucoloma assimile"^^xsd:String ;
    dwc:scientificNameAuthorship "(Hampe) Broth."^^xsd:string ;
    dwc:namePublishedIn "Nat. Pflanzenfam. 1,3: 322 (1901)"^^xsd:string ;
    dwc:namePublishedInYear "1901" ;
    :basionym tropicos::35121913 .

tropicos::35124384 a :TaxonName ;
    :taxonomicNameString "Dicranum sumatranum"^^xsd:String ;
    dwc:scientificNameAuthorship "Müll.Hal."^^xsd:string ;
    dwc:namePublishedIn "Genera musc. fr.: 285 (1901)"^^xsd:string ;
    dwc:namePublishedInYear "1901" .

tropicos::35155131 a :TaxonName ;
    :taxonomicNameString "Leucoloma sumatranum"^^xsd:String ;
    dwc:scientificNameAuthorship "(Müll.Hal.) Broth."^^xsd:string ;
    dwc:namePublishedIn "Nat. Pflanzenfam. 1,3: 322 (1901)"^^xsd:string ;
    dwc:namePublishedInYear "1901" ;
    :basionym tropicos::35124384 .

tropicos::35121646 a :TaxonName ;
    :taxonomicNameString "Dicranoloma sumatranum"^^xsd:String ;
    dwc:scientificNameAuthorship "(Müll.Hal.) Renauld"^^xsd:string ;
    dwc:namePublishedIn "Essai Leucoloma 14 (1909)"^^xsd:string ;
    dwc:namePublishedInYear "1901" ;
    :basionym tropicos::35124384 .

tropicos::35121535 a :TaxonName ;
    :taxonomicNameString "Dicranoloma gedeanum"^^xsd:String ;
    dwc:namePublishedIn "Rev. Bryol. 28: 117 (1901)"^^xsd:string ;
    dwc:namePublishedInYear "1901" ;
    dwc:scientificNameAuthorship "Renauld & Cardot"^^xsd:string .

tropicos::35121587 a :TaxonName ;
    :taxonomicNameString "Dicranoloma perarmatum"^^xsd:String ;
    dwc:scientificNameAuthorship "Broth."^^xsd:string ;
    dwc:namePublishedIn "Öfvers. Finska Vetensk.-Soc. Förh. 47(14): 1 (1905)"^^xsd:string ;
    dwc:namePublishedInYear "1905" .

tropicos::35121523 a :TaxonName ;
    :taxonomicNameString "Dicranoloma euryloma"^^xsd:String ;
    dwc:scientificNameAuthorship "Dixon"^^xsd:string ;
    dwc:namePublishedIn "J. Linn. Soc. Bot. 50: 69 (1935)"^^xsd:string ;
    dwc:namePublishedInYear "1935" .

tropicos::35121524 a :TaxonName ;
    :taxonomicNameString "Dicranoloma euryloma var. rugifolium"^^xsd:String .
    dwc:scientificNameAuthorship "E.B.Bartram"^^xsd:string ;
    dwc:namePublishedIn "Philipp. J. Sci. 61: 237 (1936)"^^xsd:string ;
    dwc:namePublishedInYear "1936" .

tropicos::35121480 a :TaxonName ;
    :taxonomicNameString "Dicranoloma brachyphyllum"^^xsd:String ;
    dwc:scientificNameAuthorship "Nog."^^xsd:string ;
    dwc:namePublishedIn "J. Hattori Bot. Lab. 10: 3 (1953)"^^xsd:string ;
    dwc:namePublishedInYear "1953" .

tropicos::35168349 a :TaxonName ;
    :taxonomicNameString "Dicranoloma havilandii var. latifolium"^^xsd:String ;
    dwc:scientificNameAuthorship "Zanten"^^xsd:string ;
    dwc:namePublishedIn "Nova Guinea, Bot. 10(16): 272 (1964)"^^xsd:string ;
    dwc:namePublishedInYear "1964" .

<https://www.tropicos.org/reference/9020903> a bibo:AcademicArticle ;
    dcterms:title "A revision of the Malesian species of Dicranoloma (Dicranaceae, Musci)" ;
    bibo:authorList [ a foaf:Person ; foaf:givenname "Niels" ; foaf:surname "Klazenga" ] ;
    bibo:pages "1-130" ;
    dcterms:isPartOf [ 
        a bibo:Issue ;
        bibo:volume "87" ;
        dcterms:date "1999" ;
        dcterms:isPartOf [ 
            a ns1:Journal ;
            dcterms:shortTitle "J. Hattori Bot. Lab." ;
            dcterms:title "Journal of the Hattori Botanical Laboratory" 
        ] 
    ] .
```