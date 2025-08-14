# TaxonConcept intersects example 2


**Term:** [tcs:intersects](../terms/#tcs_intersects)

[TaxonConcept-intersects-example-1](./TaxonConcept-intersects-example-1.html) | TaxonConcept-intersects-example-2 | [TaxonConceptMapping-intersects-example-1](./TaxonConceptMapping-intersects-example-1.html) | [TaxonConcept-intersects-example-3](./TaxonConcept-intersects-example-3.html)
```turtle
<https://id.biodiversity.org.au/instance/apni/545068> a tcs:TaxonConcept ;
    dcterms:title "Euphrasia gibbsiae sec. Barker 1982" ;
    tcs:accordingTo <https://www.jstor.org/stable/23873848> ;
    tcs:taxonName <https://ipni.org/n/802545-1> ;
    tcs:synonym <https://ipni.org/n/802619-1> ;
    tcs:intersects <https://id.biodiversity.org.au/instance/apni/713514> ,
        [ rdf:value [ a tcs:TaxonConcept ;
                    dcterms:title "Euphrasia gibbsiae sec. Willis 1967" ;
                    tcs:accordingTo <https://www.biodiversitylibrary.org/page/49934392> ;
                    tcs:taxonName <https://ipni.org/n/802545-1> ] ;
            rdfs:comment """p.p. (as to Tasmanian occurrences and f. 
                    subglabrifolia in Victoria)""" ] ,
        [ rdf:value [ a tcs:TaxonConcept ;
                    dcterms:title "Euphrasia gibbsiae sec. Harris 1970" ;
                    tcs:accordingTo [ a dcterms:BibliographicResource ;
                            dcterms:bibliographicCitation "Harris, Alp. Pl. Austral. (1970)" ] ;
                    tcs:taxonName <https://ipni.org/n/802545-1> ] ;
            rdfs:comment """p.p. (excl. "f. comberi" in Victoria)""" ] ,
        [ rdf:value [ a tcs:TaxonConcept ;
                    dcterms:title "Euphrasia striata sec. Bentham 1868" ;
                    tcs:accordingTo [ a dcterms:BibliographicResource ;
                            dcterms:bibliographicCitation "Bentham, Fl. Austral. (1868)" ] ;
                    tcs:taxonName <https://ipni.org/n/802876-1> ] ;
            rdfs:comment """p.p. (as to Stuart 1745, Milligan MEL41451, p.p., 
                    Mueller MEL41539)""" ] .

<https://id.biodiversity.org.au/instance/apni/713514> a tcs:TaxonConcept ;
    dcterms:title "Euphrasia gibbsiae sec. Curtis 1967" ;
    tcs:accordingTo <https://id.biodiversity.org.au/reference/apni/23028> ;
    tcs:taxonName <https://ipni.org/n/802545-1> .

# This treatment can be found in the BHL at
# https://www.biodiversitylibrary.org/page/61979377.

# This is only a small part of the nomenclature section of the treatment of
# Euphrasia gibbsiae sec. Barker 1982. See
# examples/euphrasia_gibbsiae_sec_barker_1982.ttl for the full example.
```

[&#91;TurTLe&#93;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonConcept-intersects-example-2.ttl)&nbsp;[&#91;JSON-LD&#93;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonConcept-intersects-example-2.jsonld)

