# TaxonConcept example 3


**Term:** [tcs:TaxonConcept](../terms/#tcs_taxonconcept)

[TaxonConcept-example-1](./TaxonConcept-example-1.html) | [TaxonConcept-example-2](./TaxonConcept-example-2.html) | TaxonConcept-example-3 | [TaxonConcept-example-4](./TaxonConcept-example-4.html) | [TaxonConcept-example-5](./TaxonConcept-example-5.html) | [TaxonConcept-example-6](./TaxonConcept-example-6.html) | [TaxonConcept-example-7](./TaxonConcept-example-7.html)
```turtle
[] a tcs:TaxonConcept ;
    dcterms:title "Calymperes moluccense sec. Yong et al. 2013" ;
    tcs:accordingTo <urn:isbn:978-967-5221-99-6> ;
    tcs:taxonName <https://www.tropicos.org/name/35153806> .

<https://www.tropicos.org/name/35153806> a tcs:TaxonName ;
    tcs:nameString "Calymperes moluccense" ;
    dwc:scientificNameAuthorship "Schwägr." .

<urn:isbn:978-967-5221-99-6> a bibo:Book ;
    dcterms:bibliographicCitation """Yong, K.T.; Tan, B.C.; Ho, B.C.; Ho, Q.Y.; 
            Mohamed, H. (2013). A revised Moss Checklist of Peninsular Malaysia 
            and Singapore. Research Pamphlet no. 133, Forest Research Institute 
            Malaysia, Kepong, Malaysia.""" .
```

[&#91;TurTLe&#93;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonConcept-example-3.ttl)&nbsp;[&#91;JSON-LD&#93;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonConcept-example-3.jsonld)

