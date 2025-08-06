# TaxonConceptMapping-isIncludedIn-example-1

```turtle
# Andropogon hirsutior sec. BONAP 2014 is included in Andropogon glomeratus sec. Weakley 2006
[] a tcs:TaxonConceptMapping ;
    tcs:mappingAccordingTo <https://doi.org/10.3233/SW-160220> ;
    tcs:mappingRelation tcs:isIncludedIn ;
    tcs:subjectTaxonConcept [ a tcs:TaxonConcept ;
        dcterms:title "Andropogon hirsutior sec. BONAP 2014" ;
        tcs:taxonName <https://ipni.org/n/60458078-2> ;
        tcs:accordingTo <http://bonap.net/napa#2014> ] ;
    tcs:objectTaxonConcept [ a tcs:TaxonConcept ;
        dcterms:title "Andropogon glomeratus sec. Weakley 2006" ;
        tcs:taxonName <https://ipni.org/n/12850-2> ;
        tcs:accordingTo <http://www.herbarium.unc.edu/FloraArchives/WeakleyFlora_2006-Jan.pdf> ] .
```

[&lsqb;TaxonConceptMapping-isIncludedIn-example-1.ttl&rsqb;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonConceptMapping-isIncludedIn-example-1.ttl)&nbsp;[&lsqb;TaxonConceptMapping-isIncludedIn-example-1.jsonld&rsqb;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonConceptMapping-isIncludedIn-example-1.jsonld)

