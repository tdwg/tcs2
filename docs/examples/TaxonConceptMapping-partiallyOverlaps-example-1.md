# TaxonConceptMapping partiallyOverlaps example 1


**Term:** [tcs:partiallyOverlaps](/terms/#tcs_partiallyoverlaps)

[TaxonConcept-partiallyOverlaps-example-1](./TaxonConcept-partiallyOverlaps-example-1.html) | [TaxonConceptMapping-partiallyOverlaps-example-2](./TaxonConceptMapping-partiallyOverlaps-example-2.html) | TaxonConceptMapping-partiallyOverlaps-example-1
```turtle
# Andropogon glomeratus sec. BONAP 2014 partially overlaps Andropogon glomeratus
# sec. Weakley 2006
[] a tcs:TaxonConceptMapping ;
    tcs:mappingAccordingTo <https://doi.org/10.3233/SW-160220> ;
    tcs:mappingRelation tcs:partiallyOverlaps ;
    tcs:subjectTaxonConcept [ a tcs:TaxonConcept ;
            dcterms:title "Andropogon glomeratus sec. BONAP 2014" ;
            tcs:taxonName <https://ipni.org/n/12850-2> ;
            tcs:accordingTo <http://bonap.net/napa#2014> ] ;
    tcs:objectTaxonConcept [ a tcs:TaxonConcept ;
            dcterms:title "Andropogon glomeratus sec. Weakley 2006" ;
            tcs:taxonName <https://ipni.org/n/12850-2> ;
            tcs:accordingTo <http://www.herbarium.unc.edu/FloraArchives/WeakleyFlora_2006-Jan.pdf> ] .
```

[&#91;TurTLe&#93;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonConceptMapping-partiallyOverlaps-example-1.ttl)&nbsp;[&#91;JSON-LD&#93;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonConceptMapping-partiallyOverlaps-example-1.jsonld)

