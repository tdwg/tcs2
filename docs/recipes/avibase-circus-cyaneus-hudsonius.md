# Avibase Circus cyaneus–hudsonius recipe

[Recipes](../recipes)

Avibase is an extensive database information system about all birds of the
world, containing over 53 million records about 10,000 species and 22,000
subspecies of birds, including distribution information for 20,000 regions,
taxonomy, synonyms in several languages and more. Avibase aligns the taxonomy
from 263 sources and assigns Avibase IDs to groups of concepts with the same
circumscription.

This example was presented by Jeff Gerbracht at TCS Maintenance Group meeting 
in 2021. It revolves around _Circus cyaneus_, which was considered a holarctic
species, but has been split into a paleo-arctic species, _Circus cyaneus_, and a
neo-arctic species, _Circus hudsonius_.

Concepts from the sources that the Avibase concepts are based on are linked to
the Avibase concept using the `isCongruentWith` property. Mappings between
Avibase concepts are not made in so many words in Avibase, so they are provided
in the form of annotations, but the information comes from Avibase's taxon
grids.

## Avibase concepts

```turtle
<https://avibase.ca/82745BAA> a tcs:TaxonConcept ;
    dcterms:identifier "avibase-82745BAA" ;
    skosxl:label "Circus [cyaneus or hudsonius]" ;
    tcs:accordingTo <https://avibase.bsc-eoc.org> ;
    tcs:taxonName _:tn1 ;
    tcs:isCongruentWith [ a tcs:TaxonConcept ;
            dcterms:title "Circus cyaneus sec. Howard & Moore 2013" ;
            tcs:accordingTo _:ref4 ;
            tcs:taxonName _:tn1 ] .

<https://avibase.ca/F558C7F9> a tcs:TaxonConcept ;
    dcterms:identifier "avibase-F558C7F9" ;
    skosxl:label "Circus cyaneus" ;
    tcs:accordingTo <https://avibase.bsc-eoc.org> ;
    tcs:taxonName [ a skosxl:Label ;
            skosxl:literalForm "Circus cyaneus" ] ;
    tcs:isCongruentWith [ a tcs:TaxonConcept ;
            dcterms:title "Circus cyaneus sec. Clements 2021" ;
            tcs:accordingTo _:ref1 ;
            tcs:taxonName _:tn1 ] ,
        [ a tcs:TaxonConcept ;
            dcterms:title "Circus cyaneus sec. Gill & al. 2021" ;
            tcs:accordingTo _:ref2 ;
            tcs:taxonName _:tn1 ] ,
        [ a tcs:TaxonConcept ;
            dcterms:title "Circus cyaneus sec. HBW/Birdlife 2020" ;
            tcs:accordingTo _:ref3 ;
            tcs:taxonName _:tn1 ] ,
        [ a tcs:TaxonConcept ;
            dcterms:title "Circus cyaneus cyaneus sec. Howard & Moore 2013" ;
            tcs:accordingTo _:ref4 ;
            tcs:taxonName [ a tcs:TaxonName ;
                    tcs:nameString "Circus cyaneus cyaneus" ] ] .

<https://avibase.ca/A091D50A> a tcs:TaxonConcept ;
    dcterms:identifier "avibase-A091D50A" ;
    skosxl:label "Circus hudsonius" ;
    tcs:accordingTo <https://avibase.bsc-eoc.org> ;
    tcs:taxonName _:tn2 ;
    tcs:isCongruentWith [ a tcs:TaxonConcept ;
            dcterms:title "Circus hudsonius sec. Clements 2021" ;
            tcs:accordingTo _:ref1 ;
            tcs:taxonName _:tn2 ] ,
        [ a tcs:TaxonConcept ;
            dcterms:title "Circus hudsonius sec. Gill & al. 2021" ;
            tcs:accordingTo _:ref2 ;
            tcs:taxonName _:tn2 ] ,
        [ a tcs:TaxonConcept ;
            dcterms:title "Circus hudsonius sec. HBW/Birdlife 2020" ;
            tcs:accordingTo _:ref3 ;
            tcs:taxonName _:tn2 ] ,
        [ a tcs:TaxonConcept ;
            dcterms:title "Circus cyaneus hudsonius sec. Howard & Moore 2013" ;
            tcs:accordingTo _:ref4 ;
            tcs:taxonName [ a tcs:TaxonName ;
                    tcs:nameString "Circus cyaneus hudsonius" ;
                    dwc:scientificNameAuthorship "(Linnaeus 1766)" ] ] .


_:tn1 a tcs:TaxonName ;
    tcs:nameString "Circus cyaneus" ;
    dwc:scientificNameAuthorship "(Linnaeus 1766)" .

_:tn2 a tcs:TaxonName ;
    tcs:nameString "Circus hudsonius" ;
    dwc:scientificNameAuthorship "(Linnaeus 1766)" .


<https://avibase.bsc-eoc.org> a bibo:Website ;
    dcterms:title "Avibase" ;
    dcterms:creator [ a foaf:Person ;
            foaf:givenNames "Denis" ;
            foaf:surname "Lepage" ] ;
    bibo:uri "https://avibase.bsc-eoc.org/avibase.jsp" .

_:ref1 a dcterms:BibliographicResource ;
    dcterms:bibliographicCitation "Clements, 2021" .

_:ref2 a dcterms:BibliographicResource ;
    dcterms:bibliographicCitation "Gill et al., 2021" .

_:ref3 a dcterms:BibliographicResource ;
    dcterms:bibliographicCitation "HBW/Birdlife, 2020" .

_:ref4 a dcterms:BibliographicResource ;
    dcterms:bibliographicCitation "Howard & Moore, 2013" .
```

## Third-party taxon concept mappings

```turtle
_:ann1 a oa:Annotation ;
    oa:motivatedBy oa:commenting ;
    oa:hasBody [ a tcs:TaxonConceptMapping ;
            tcs:mappingAccordingTo _:ann1 ;
            tcs:mappingRelation tcs:includes ;
            tcs:subjectTaxonConcept <https://avibase.ca/82745BAA> ;
            tcs:objectTaxonConcept <https://avibase.ca/F558C7F9> ] ;
    oa:hasTarget <https://avibase.ca/82745BAA> ;
    dcterms:creator <https://orcid.org/0000-0003-2224-6821> ;
    dcterms:created "2023-10-21T13:55:00+10" .

_:ann2 a oa:Annotation ;
    oa:motivatedBy oa:commenting ;
    oa:hasBody [ a tcs:TaxonConceptMapping ;
            tcs:mappingAccordingTo _:ann2 ;
            tcs:mappingRelation tcs:includes ;
            tcs:subjectTaxonConcept <https://avibase.ca/82745BAA> ;
            tcs:objectTaxonConcept <https://avibase.ca/A091D50A> ];
    oa:hasTarget <https://avibase.ca/82745BAA> ;
    dcterms:creator <https://orcid.org/0000-0003-2224-6821> ;
    dcterms:created "2023-10-21T13:55:00+10" .

_:ann3 a oa:Annotation ;
    oa:motivatedBy oa:commenting ;
    oa:hasBody [ a tcs:TaxonConceptMapping ;
            tcs:mappingAccordingTo _:ann3 ;
            tcs:mappingRelation tcs:isDisjointFrom ;
            tcs:subjectTaxonConcept <https://avibase.ca/F558C7F9> ;
            tcs:objectTaxonConcept <https://avibase.ca/A091D50A> ] ;
    oa:hasTarget <https://avibase.ca/F558C7F9> ;
    dcterms:creator <https://orcid.org/0000-0003-2224-6821> ;
    dcterms:created "2023-10-21T13:55:00+10" .
```

[TurTLe](https://github.com/tdwg/tcs2/blob/master/recipes/avibase-circus-cyaneus-hudsonius.ttl) |
[JSON-LD](https://github.com/tdwg/tcs2/blob/master/recipes/avibase-circus-cyaneus-hudsonius.jsonld)
