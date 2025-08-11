# TaxonConceptMapping includes example 1


**Term:** [tcs:includes](/terms/#tcs_includes)

[TaxonConcept-includes-example-1](./TaxonConcept-includes-example-1.html) | [TaxonConceptMapping-includes-example-2](./TaxonConceptMapping-includes-example-2.html) | TaxonConceptMapping-includes-example-1
```turtle
# Andropogon glomeratus sec. BONAP 2014 includes Andropogon tenuispatheus sec. Weakley 2006
[] a tcs:TaxonConceptMapping ;
    tcs:mappingAccordingTo <https://doi.org/10.3233/SW-160220> ;
    tcs:mappingRelation tcs:includes ;
    tcs:subjectTaxonConcept [ a tcs:TaxonConcept ;
        dcterms:title "Andropogon glomeratus sec. BONAP 2014" ;
        tcs:taxonName <https://ipni.org/n/12850-2> ;
        tcs:accordingTo <http://bonap.net/napa#2014> ] ;
    tcs:objectTaxonConcept [ a tcs:TaxonConcept ;
        dcterms:title "Andropogon tenuispatheus sec. Weakley 2006" ;
        tcs:taxonName <https://ipni.org/n/13093-2> ;
        tcs:accordingTo <http://www.herbarium.unc.edu/FloraArchives/WeakleyFlora_2006-Jan.pdf> ] .

<https://ipni.org/n/12850-2> a tcs:TaxonName ;
    tcs:nameString "Andropogon glomeratus" ;
    dwc:scientificNameAuthorship "Britton, Sterns & Poggenb." .

<https://ipni.org/n/13093-2> a tcs:TaxonName ;
    tcs:nameString "Andropogon tenuispatheus" ;
    dwc:scientificNameAuthorship "Nash" .
```

[&#91;TurTLe&#93;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonConceptMapping-includes-example-1.ttl)&nbsp;[&#91;JSON-LD&#93;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonConceptMapping-includes-example-1.jsonld)

