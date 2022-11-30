# Example 2

## Example of a Taxon Concept from a field guide: Mimus polyglottos sec. Sibley 2014

### JSON-LD

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
      "ex": "https://tdwg.github.io/tcs2/examples/",
      "bibo": "http://purl.org/ontology/bibo/",
      "foaf": "http://xmlns.com/foaf/0.1/",
      "address": "http://schemas.talis.com/2005/address/schema#"
    }
  ],
  "@id": "ex:2",
  "dcterms:title": "Example of a Taxon Concept from a field guide: Mimus polyglottos sec. Sibley 2014",
  "@graph": [
    {
      "@id": "ex:2/taxon-concept/1",
      "@type": ["TaxonConcept", "skos:Concept"],
      "skos:prefLabel": "Mimus polyglottos sec. Sibley 2014",
      "taxonName": {
        "@type": ["TaxonName", "skosxl:Label"],
        "taxonomicNameString": "Mimus polyglottos"
      },
      "accordingTo": "urn:isbn:978-0-307-95790-0",
      "vernacularName": {
        "@type": "skosxl:Label",
        "skosxl:literalForm": {
          "@value": "Northern Mockingbird",
          "@language": "en"
        }
      },
      "dwc:scientificName": "Mimus polyglottos",
      "dwc:nameAccordingTo": "Sibley, 2014",
      "dwc:vernacularName": {
        "@value": "Northern Mockingbird",
        "@language": "en"
      }
    },
    {
      "@id": "urn:isbn:978-0-307-95790-0",
      "@type": "bibo:Book",
      "dcterms:title": "The Sibley guide to birds",
      "dcterms:date": "2014",
      "dcterms:language": "en",
      "dcterms:publisher": {
        "@type": "foaf:Organization",
        "address:localityName": "New York, NY, USA",
        "foaf:name": "Alfred A. Knopf"
      },
      "bibo:isbn": "978-0-307-95790-0",
      "bibo:edition": "2",
      "bibo:numPages": "599",
      "dcterms:creator": "_:n19",
      "bibo:authorList": {
        "@list": [
          "_:n19"
        ]
      }
    },
    {
      "@id": "_:n19",
      "@type": "foaf:Person",
      "foaf:givenname": "David Allen",
      "foaf:surname": "Sibley"
    }
  ]
}
```

### Turtle

```turtle
@prefix : <http://rs.tdwg.org/tcs/terms/> .
@prefix address: <http://schemas.talis.com/2005/address/schema#> .
@prefix bibo: <http://purl.org/ontology/bibo/> .
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix dwc: <http://rs.tdwg.org/dwc/terms/> .
@prefix foaf: <http://xmlns.com/foaf/0.1/> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix skosxl: <http://www.w3.org/2008/05/skos-xl#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://tdwg.github.io/tcs2/examples/1> 
    dcterms:title "Example of a Taxon Concept from a field guide: Mimus polyglottos sec. Sibley 2014" .

<https://tdwg.github.io/tcs2/examples/2/taxon-concept/1> a :TaxonConcept, skos:Concept ;
    skos:prefLabel "Mimus polyglottos sec. Sibley 2014" ;
    :taxonName [ 
        a :TaxonName, skosxl:Label ;
        :taxonomicNameString "Mimus polyglottos"^^xsd:String 
    ] ;
    :accordingTo <urn:isbn:978-0-307-95790-0> ;
    :vernacularName [ 
        a skosxl:Label ;
        skosxl:literalForm "Northern Mockingbird"@en 
    ] ;
    dwc:scientificName "Mimus polyglottos"^^xsd:string ;
    dwc:nameAccordingTo "Sibley, 2014" ;
    dwc:vernacularName "Northern Mockingbird"@en .

<urn:isbn:978-0-307-95790-0> a bibo:Book ;
    dcterms:title "The Sibley guide to birds" ;
    dcterms:date "2014" ;
    dcterms:language "en" ;
    dcterms:publisher [ 
        a foaf:Organization ;
        address:localityName "New York, NY, USA" ;
        foaf:name "Alfred A. Knopf" 
    ] ;
    bibo:isbn "978-0-307-95790-0" ;
    bibo:edition "2" ;
    bibo:numPages "599" 
    dcterms:creator "_:n19" ;
    bibo:authorList ( "_:n19" ) .

_:n19 a foaf:Person ;
    foaf:givenName "David Allen" ;
    foaf:surname "Sibley" .
```