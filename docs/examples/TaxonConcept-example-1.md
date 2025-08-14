# TaxonConcept example 1


**Term:** [tcs:TaxonConcept](../terms/#tcs_taxonconcept)

TaxonConcept-example-1 | [TaxonConcept-example-2](./TaxonConcept-example-2.html) | [TaxonConcept-example-3](./TaxonConcept-example-3.html) | [TaxonConcept-example-4](./TaxonConcept-example-4.html) | [TaxonConcept-example-5](./TaxonConcept-example-5.html) | [TaxonConcept-example-6](./TaxonConcept-example-6.html) | [TaxonConcept-example-7](./TaxonConcept-example-7.html)
```turtle
[] a tcs:TaxonConcept ;
    dcterms:title "Dicranoloma blumei sec. Klazenga 1999" ;
    tcs:accordingTo <https://www.tropicos.org/reference/9020903> 
    tcs:taxonName <https://www.tropicos.org/name/35121475> .

<https://www.tropicos.org/name/35121475> a tcs:TaxonName ;
    tcs:nameString "Dicranoloma blumei" ;
    dwc:scientificNameAuthorship "(Nees) Renauld" .

<https://www.tropicos.org/reference/9020903> a bibo:AcademicArticle ;
    dcterms:bibliographicCitation """Klazenga, N. (1999). A revision of the 
            Malesian species of Dicranoloma (Dicranaceae, Musci). Journal of the 
            Hattori Botanical Laboratory 87: 1-130.""" .
```

[&#91;TurTLe&#93;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonConcept-example-1.ttl)&nbsp;[&#91;JSON-LD&#93;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonConcept-example-1.jsonld)

