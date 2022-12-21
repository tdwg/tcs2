# Example 7

## Example from Catalogue of Life with classification

This example shows *Panthera leo*, Lion, and its higher classification. The 
example has been marked up in [JSON-LD](example7.jsonld) as well as 
[TurTLe](example7).

The higher classification can be created by using the `parent` property on the 
Taxon Concept. Because the definition behind a Catalogue of Life URL can change 
between versions – which means the same URI in different versions can stand for 
different taxon concepts – the version has been appended to the ID and the taxon 
concept label.

```turtle
<https://www.catalogueoflife.org/data/taxon/4CGXP#v2022-11-14> a :TaxonConcept ;
    dcterms:title "Panthera leo sec. Catalogue of Life (v2022-11-14)" ;
    :taxonName [ a :TaxonName ;
            dwc:scientificNameAuthorship "(Linnaeus, 1758)"^^xsd:string ;
            :taxonNameString "Panthera leo" ] ;
    :accordingTo <https://www.catalogueoflife.org#v2022-11-14> ;
    :taxonomicRank gbif-rank:species ;
    :parent <https://www.catalogueoflife.org/data/taxon/6DBT#v2022-11-14> .

<https://www.catalogueoflife.org/data/taxon/6DBT#v2022-11-14> a :TaxonConcept ;
    dcterms:title "Panthera sec. Catalogue of Life (v2022-11-14)" ;
    :accordingTo <https://www.catalogueoflife.org#v2022-11-14> ;
    :taxonName [ a :TaxonName ;
            :taxonNameString "Panthera" ] ;
    :taxonomicRank gbif-rank:genus ;
    :parent <https://www.catalogueoflife.org/data/taxon/628LP#v2022-11-14> .

<https://www.catalogueoflife.org/data/taxon/628LP#v2022-11-14> a :TaxonConcept ;
    dcterms:title "Pantherinae sec. Catalogue of Life (v2022-11-14)" ;
    :taxonName [ a :TaxonName ;
            :taxonNameString "Pantherinae" ] ;
    :accordingTo <https://www.catalogueoflife.org#v2022-11-14> ;
    :taxonomicRank gbif-rank:subfamily ;
    :parent <https://www.catalogueoflife.org/data/taxon/623RM> .

<https://www.catalogueoflife.org/data/taxon/623RM#v2022-11-14> a :TaxonConcept ;
    dcterms:title "Felidae sec. Catalogue of Life (v2022-11-14)" ;
    :taxonName [ a :TaxonName ;
            :taxonNameString "Felidae" ] ;
    :accordingTo <https://www.catalogueoflife.org#v2022-11-14> ;
    :taxonomicRank gbif-rank:family ;
    :parent <https://www.catalogueoflife.org/data/taxon/4DL#v2022-11-14> .
...
```