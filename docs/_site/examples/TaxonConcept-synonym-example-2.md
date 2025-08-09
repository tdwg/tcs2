# TaxonConcept synonym example 2

```turtle
[] a tcs:TaxonConcept ;
    dcterms:title "Hebe colensoi sec. Bayly & Kellow 2006" ;
    tcs:accordingTo <urn:isbn:978-0-909010-12-6> ;
    tcs:taxonName <https://ipni.org/n/803678-1> ;
    tcs:synonym <https://ipni.org/n/812087-1> .

<https://ipni.org/n/803678-1> a tcs:TaxonName ;
    tcs:nameString "Hebe colensoi" ;
    dwc:scientificNameAuthorship "(Hook.f.) Cockayne" ;
    dwc:namePublishedIn "Trans. & Proc. New Zealand Inst. 60: 384 (1929)" ;
    tcs:basionym <https://ipni.org/n/811835-1> .

<https://ipni.org/n/811835-1> a tcs:TaxonName ;
    tcs:nameString "Veronica colensoi" ;
    dwc:scientificNameAuthorship "Hook.f." ;
    dwc:namePublishedIn "Handb. N. Zeal. Fl. 209. (1864)" .

<https://ipni.org/n/812087-1> a tcs:TaxonName ;
    tcs:nameString "Veronica hillii" ;
    dwc:scientificNameAuthorship "Colenso" ;
    dwc:namePublishedIn "Trans. & Proc. New Zealand Inst. 28: 606 (1896)" .
```

[&lsqb;TaxonConcept-synonym-example-2.ttl&rsqb;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonConcept-synonym-example-2.ttl)&nbsp;[&lsqb;TaxonConcept-synonym-example-2.jsonld&rsqb;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonConcept-synonym-example-2.jsonld)

