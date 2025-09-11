# NomenclaturalType example 1


**Term:** [tcs:NomenclaturalType](../terms/#tcs_nomenclaturaltype)


```turtle
# Examples from TCS 1
[] a tcs:NomenclaturalType ;
    tcs:typifiedName <https://ipni.org/n/50985479-1> ;
    tcs:typeOfType <http://rs.gbif.org/vocabulary/gbif/type_status/lectotype> ;
    tcs:typeName <https://ipni.org/n/333193-1> ;
    tcs:typePublishedIn [ a bibo:Article ;
            dcterms:bibliographicCitation """Copeland, H.F. (1943). A study, anatomical and 
                    taxonomic, of the genera of Rhododendroideae. Am. Midl. Nat. 30: 533-625""" ] .

[] a tcs:NomenclaturalType ;
    tcs:typifiedName <https://ipni.org/n/333193-1> ;
    tcs:typeOfType <http://rs.gbif.org/vocabulary/gbif/type_status/lectotype> ;
    tcs:typeSpecimen [ a dwc:MaterialCitation ;
            dwc:verbatimLocality "Japan, Honshu, Nikko" ;
            dwc:recordedBy "Bisset" ;
            dwc:recordNumber "233" ;
            dwc:eventDate "1876-05-23" ;
            dwc:institutionCode "E" ;
            schema:itemLocation <https://scientific-collections.gbif.org/collection/427c8cd7-4358-4a00-9ef3-2b2676d28d1e> ] ;
    tcs:typePublishedIn [ a bibo:Article ; 
            dcterms:bibliographicCitation """Judd, W.S.; Kron, K.A. (1995). A revision of Rhododendron 
                    VI. Subgenus Pentanthera (sections Sciadorhodon, Rhodora and Viscidula). Edinburgh 
                    Journal of Botany 52: 1-54.""" ] .

# name used in TaxonName examples; more data there
<https://ipni.org/n/50985479-1> a tcs:TaxonName ;
    tcs:nameString "Rhododendron sect. Sciadorhodion" ;
    dwc:scientificNameAuthorship "Rehder & Wilson" .

<https://ipni.org/n/333193-1> a tcs:TaxonName ;
    tcs:nameString "Rhododendron quinquefolium" ;
    dwc:scientificNameAuthorship "Bisset & S.Moore" .
```

[&#91;TurTLe&#93;](https://github.com/tdwg/tcs2/blob/master/examples/NomenclaturalType-example-1.ttl)&nbsp;[&#91;JSON-LD&#93;](https://github.com/tdwg/tcs2/blob/master/examples/NomenclaturalType-example-1.jsonld)

