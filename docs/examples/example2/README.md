# Example 2

## Example of a Taxon Concept from a field guide: Mimus polyglottos sec. Sibley 2014

### JSON-LD

```json
{
  "@context": [
    "https://raw.githubusercontent.com/tdwg/tcs2/examples/docs/examples/context.jsonld",
    {"ex": "https://tdwg.github.io/tcs2/examples/"}
  ],
  "@id": "ex:2",
  "dcterms:title": "Example of a Taxon Concept from a field guide: Mimus polyglottos sec. Sibley 2014",
  "@graph": [
    {
      "@id": "ex:2/taxon-concept/1",
      "@type": [
        "TaxonConcept", 
        "skos:Concept", 
        "openbiodiv-o:TaxonomicConcept", 
        "dwc:Taxon"
      ],
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
@prefix openbiodiv-o: <http://openbiodiv.net/> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix skosxl: <http://www.w3.org/2008/05/skos-xl#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://tdwg.github.io/tcs2/examples/1> 
    dcterms:title "Example of a Taxon Concept from a field guide: Mimus polyglottos sec. Sibley 2014" .

<https://tdwg.github.io/tcs2/examples/2/taxon-concept/1> a :TaxonConcept, 
        skos:Concept, openbiodiv-o:TaxonomicConcept, dwc:Taxon ;
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