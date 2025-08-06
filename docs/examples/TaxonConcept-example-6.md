# TaxonConcept-example-6

```turtle
# Species Hypothesis (SH) from UNITE

<https://doi.plutof.ut.ee/doi/10.15156/BIO/SH1109146.09FU> a tcs:TaxonConcept ;
    tcs:taxonName [ a skosxl:Label ;
        skosxl:literalForm "SH1109146.09FU" ] ;
    tcs:accordingTo <https://unite.ut.ee> ;
    tcs:isIncludedIn <https://doi.plutof.ut.ee/doi/10.15156/BIO/TH077737> .

<https://doi.plutof.ut.ee/doi/10.15156/BIO/TH077737> a tcs:TaxonConcept ;
    tcs:accordingTo <https://unite.ut.ee> ;
    tcs:taxonName <https://www.indexfungorum.org/names/NamesRecord.asp?RecordID=17175> .

<https://www.indexfungorum.org/names/NamesRecord.asp?RecordID=17175> a tcs:TaxonNAme ;
    tcs:nameString "Boletus" ;
    dwc:scientificNameAuthorship "L" ;
    dwc:namePublishedIn "Sp. pl. 2: 1176" ;
    dwc:namePublishedInYear "1753" .

<https://unite.ut.ee> a bibo:Website ;
    dcterms:title """UNITE: rDNA ITS based identification of Eukaryotes and 
            their communication via DOIs""" ;
    bibo:uri "https://unite.ut.ee" .
```

[&lsqb;TaxonConcept-example-6.ttl&rsqb;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonConcept-example-6.ttl)&nbsp;[&lsqb;TaxonConcept-example-6.jsonld&rsqb;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonConcept-example-6.jsonld)

