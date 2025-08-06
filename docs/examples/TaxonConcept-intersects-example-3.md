# TaxonConcept intersects example 3

```turtle
<https://www.catalogueoflife.org/data/taxon/BRKHX> a tcs:TaxonConcept ;
    dcterms:title "Megalorhipida leucodactylus sec. Gielis & Hobern 2023-01-05" ;
    tcs:accordingTo <https://doi.org/10.48580/dfry-3gd#1.1.23.5> ;
    tcs:taxonName [ a tcs:TaxonName ;
            tcs:nameString "Megalorhipida leucodactylus" ;
            dwc:scientificNameAuthorship "(Fabricius, 1794)" ;
            tcs:basionym <https://zoobank.org/NomenclaturalActs/39b2f236-3914-4962-9dcc-f594671654bd> ] ;
    tcs:intersects [ a tcs:TaxonConcept ;
            dcterms:title "Pterophorus congrualis sec. Walker 1864" ;
            tcs:accordingTo <https://www.biodiversitylibrary.org/page/38948425> ;
            tcs:taxonName [ a tcs:TaxonName ;
                    tcs:nameString "Pterophorus congrualis" ;
                    dwc:scientificNameAuthorship "Walker, 1864" ] ] ,
        [ a tcs:TaxonConcept ;
            dcterms:title "Pterophorus leucodactylus sec. Gielis & al. 2022" ;
            tcs:accordingTo [ a bibo:Book ;
                    dcterms:bibliographicCitation """Gielis, C., Franssen, M., Groenen, 
                            F., & Wangdi, K. (2022). Moths of Bhutan. 1–420.""" ] ;
            tcs:taxonName <https://zoobank.org/NomenclaturalActs/39b2f236-3914-4962-9dcc-f594671654bd> ] ,
        [ a tcs:TaxonConcept ;
            dcterms:title "Pterophorus leucodactylus sec. Ustjuzhanin, Kovtunovich & Streltzov 2022" ;
            tcs:accordingTo [ a bibo:AcademicArticle ;
                    dcterms:bibliographicCitation """Ustjuzhanin, P., Kovtunovich V. & 
                            Streltzov, A. (2022). Review on the fauna of Pterophoridae 
                            of the Republic of Guinea (Lepidoptera: Pterophoridae). 
                            SHILAP Revista De Lepidopterología, 50(199), 435–439.""" ] ;
            tcs:taxonName <https://zoobank.org/NomenclaturalActs/39b2f236-3914-4962-9dcc-f594671654bd> ] .

# This example shows only a fraction of the references that are cited in the
# treatment and lacks some properties of the Taxon Concept. For the full
# treatment, see examples/megalorhipida-leucodactylus-sec-gielis-et-hobern-2020.ttl.
```

[&lsqb;TaxonConcept-intersects-example-3.ttl&rsqb;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonConcept-intersects-example-3.ttl)&nbsp;[&lsqb;TaxonConcept-intersects-example-3.jsonld&rsqb;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonConcept-intersects-example-3.jsonld)

