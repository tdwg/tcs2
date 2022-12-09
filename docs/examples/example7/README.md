# Example 7

## Example from Catalogue of Life with classification

This example shows *Panthera leo*, Lion, and its higher classification. The 
example has been marked up in [JSON-LD](example7.jsonld) as well as 
[TurTLe](example7).

The higher classification can be created by using the `parent` property on the 
Taxon Concept:

```turtle
<https://www.catalogueoflife.org/data/taxon/4CGXP> a :TaxonConcept ;
    skos:prefLabel "Panthera leo sec. CoL 2022-11-14" ;
    :taxonName [ a :TaxonName ;
            dwc:scientificNameAuthorship "(Linnaeus, 1758)"^^xsd:string ;
            :taxonNameString "Panthera leo" ] ;
    :accordingTo <https://www.catalogueoflife.org#v2022-11-14> ;
    :taxonomicRank gbif-rank:species ;
    :parent <https://www.catalogueoflife.org/data/taxon/6DBT> .

<https://www.catalogueoflife.org/data/taxon/6DBT> a :TaxonConcept ;
    skos:prefLabel "Panthera sec. CoL 2022-11-14" ;
    :accordingTo <https://www.catalogueoflife.org#v2022-11-14> ;
    :taxonName [ a :TaxonName ;
            :taxonNameString "Panthera" ] ;
    :taxonomicRank gbif-rank:genus ;
    :parent <https://www.catalogueoflife.org/data/taxon/628LP> .

<https://www.catalogueoflife.org/data/taxon/628LP> a :TaxonConcept ;
    skos:prefLabel "Pantherinae sec. CoL 2022-11-14" ;
    :taxonName [ a :TaxonName ;
            :taxonNameString "Pantherinae" ] ;
    :accordingTo <https://www.catalogueoflife.org#v2022-11-14> ;
    :taxonomicRank gbif-rank:subfamily ;
    :parent <https://www.catalogueoflife.org/data/taxon/623RM> .

<https://www.catalogueoflife.org/data/taxon/623RM> a :TaxonConcept ;
    skos:prefLabel "Felidae sec. CoL 2022-11-14" ;
    :taxonName [ a :TaxonName ;
            :taxonNameString "Felidae" ] ;
    :accordingTo <https://www.catalogueoflife.org#v2022-11-14> ;
    :taxonomicRank gbif-rank:family ;
    :parent <https://www.catalogueoflife.org/data/taxon/4DL> .
...
```

Alternatively, one can do higher classification with Taxon Concept 
Relationships, using the `isProperSubsetOf` relationship type. This has the 
advantage that you can skip ranks. The following shows the higher classification 
of *Panthera leo* including only the major ranks.

```turtle
<https://tdwg.github.io/tcs2/examples/relationships/7-1> a :TaxonConceptRelationship ;
    :relationshipType <http://rs.tdwg.org/tcs-taxon-concept-relationship-type/values/rt003> ;
    :subjectTaxonConcept <https://www.catalogueoflife.org/data/taxon/4CGXP> ; # species: Panthera leo
    :objectTaxonConcept <https://www.catalogueoflife.org/data/taxon/6DBT> ; # genus: Panthera
    :relationshipAccordingTo <https://www.catalogueoflife.org#v2022-11-14> .

<https://tdwg.github.io/tcs2/examples/relationships/7-2> a :TaxonConceptRelationship ;
    :relationshipType <http://rs.tdwg.org/tcs-taxon-concept-relationship-type/values/rt003> ;
    :subjectTaxonConcept <https://www.catalogueoflife.org/data/taxon/6DBT> ; # genus: Panthera
    :objectTaxonConcept <https://www.catalogueoflife.org/data/taxon/623RM> ; # family: Felidae
    :relationshipAccordingTo <https://www.catalogueoflife.org#v2022-11-14> .

<https://tdwg.github.io/tcs2/examples/relationships/7-3> a :TaxonConceptRelationship ;
    :relationshipType <http://rs.tdwg.org/tcs-taxon-concept-relationship-type/values/rt003> ;
    :subjectTaxonConcept <https://www.catalogueoflife.org/data/taxon/623RM> ; # family: Felidae
    :objectTaxonConcept <https://www.catalogueoflife.org/data/taxon/VS> ; # order: Carnivora
    :relationshipAccordingTo <https://www.catalogueoflife.org#v2022-11-14> .

<https://tdwg.github.io/tcs2/examples/relationships/7-4> a :TaxonConceptRelationship ;
    :relationshipType <http://rs.tdwg.org/tcs-taxon-concept-relationship-type/values/rt003> ;
    :subjectTaxonConcept <https://www.catalogueoflife.org/data/taxon/VS> ; # order: Carnivora
    :objectTaxonConcept <https://www.catalogueoflife.org/data/taxon/924GT> ; # class: Mammalia
    :relationshipAccordingTo <https://www.catalogueoflife.org#v2022-11-14> .

<https://tdwg.github.io/tcs2/examples/relationships/7-5> a :TaxonConceptRelationship ;
    :relationshipType <http://rs.tdwg.org/tcs-taxon-concept-relationship-type/values/rt003> ;
    :subjectTaxonConcept <https://www.catalogueoflife.org/data/taxon/924GT> ; # class: Mammalia
    :objectTaxonConcept <https://www.catalogueoflife.org/data/taxon/CH2> ; # phylum: Chordata
    :relationshipAccordingTo <https://www.catalogueoflife.org#v2022-11-14> .

<https://tdwg.github.io/tcs2/examples/relationships/7-6> a :TaxonConceptRelationship ;
    :relationshipType <http://rs.tdwg.org/tcs-taxon-concept-relationship-type/values/rt003> ;
    :subjectTaxonConcept <https://www.catalogueoflife.org/data/taxon/CH2> ; # phylum: Chordata
    :objectTaxonConcept <https://www.catalogueoflife.org/data/taxon/N> ; # kingdom: Animalia
    :relationshipAccordingTo <https://www.catalogueoflife.org#v2022-11-14> .
```