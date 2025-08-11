# TaxonConcept example 6


**Term:** [tcs:TaxonConcept](/terms/#tcs_taxonconcept)

[TaxonConcept-example-1](./TaxonConcept-example-1.html) | [TaxonConcept-example-2](./TaxonConcept-example-2.html) | [TaxonConcept-example-3](./TaxonConcept-example-3.html) | [TaxonConcept-example-4](./TaxonConcept-example-4.html) | [TaxonConcept-example-5](./TaxonConcept-example-5.html) | TaxonConcept-example-6 | [TaxonConcept-example-7](./TaxonConcept-example-7.html)
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

[&#91;TurTLe&#93;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonConcept-example-6.ttl)&nbsp;[&#91;JSON-LD&#93;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonConcept-example-6.jsonld)

