# TaxonName typification example 2


**Term:** [tcs:typification](/terms/#tcs_typification)

[TaxonName-typification-example-1](./TaxonName-typification-example-1.html) | TaxonName-typification-example-2
```turtle
<https://tropicos.org/name/35121972> a tcs:TaxonName ;
    tcs:nameString "Dicranum blumei" ;
    dwc:scientificNameAuthorship "Nees" ;
    dwc:namePublishedIn """Nova Acta Physico-medica Academiae Caesareae Leopoldino-Carolinae Naturae Curiosorum 
            Exhibentia Ephemerides sive Observationes Historias et Experimenta 11(1) tcs: 131. 15 f. 1. 1823. 
            (Nova Acta Phys.-Med. Acad. Caes. Leop.-Carol. Nat. Cur.)""" ;
    tcs:nomenclaturalStatus <http://rs.gbif.org/vocabulary/gbif/nomenclatural_status/legitimate> ;
    tcs:typification [ a tcs:NomenclaturalType ;
            tcs:typifiedName <https://tropicos.org/name/35121972> ;
            tcs:typeSpecimen [ a dwc:MaterialCitation ;
                    dwc:country "Indonesia" ;
                    dwc:island "Java" ;
                    dwc:verbatimLocality "Java in montibus excelsis partim ignivomis Salak et Gédé" ;
                    dwc:recordedBy "C. Blume" ;
                    dwc:recordNumber "s.n." ;
                    dwc:institutionCode "LE" ;
                    dwc:disposition "not located" ] ;
            tcs:typeOfType <http://rs.gbif.org/vocabulary/gbif/type_status/holotype> ] ,
        [ a tcs:NomenclaturalType ;
            tcs:typifiedName <https://tropicos.org/name/35121972> ;
            tcs:typeSpecimen [ a dwc:MaterialCitation ;
                    dwc:country "Indonesia" ;
                    dwc:island "Java" ;
                    dwc:verbatimLocality "Java in montibus excelsis partim ignivomis Salak et Gédé" ;
                    dwc:recordedBy "C. Blume" ;
                    dwc:recordNumber "s.n." ;
                    dwc:institutionCode "JE" ] ;
            tcs:typeOfType <http://rs.gbif.org/vocabulary/gbif/type_status/lectotype> ;
            tcs:typePublishedIn <https://www.tropicos.org/reference/9020903> ] ,
        [ a tcs:NomenclaturalType ;
            tcs:typifiedName <https://tropicos.org/name/35121972> ;
            tcs:typeSpecimen [ a dwc:MaterialCitation ;
                    dwc:country "Indonesia" ;
                    dwc:island "Java" ;
                    dwc:verbatimLocality "Java in montibus excelsis partim ignivomis Salak et Gédé" ;
                    dwc:recordedBy "C. Blume" ;
                    dwc:recordNumber "s.n." ;
                    dwc:institutionCode "L" ] ;
            tcs:typeOfType <http://rs.gbif.org/vocabulary/gbif/type_status/isotype> ] ,
        [ a tcs:NomenclaturalType ;
            tcs:typifiedName <https://tropicos.org/name/35121972> ;
            tcs:typeSpecimen [ a dwc:MaterialCitation ;
                    dwc:country "Indonesia" ;
                    dwc:island "Java" ;
                    dwc:verbatimLocality "Java in montibus excelsis partim ignivomis Salak et Gédé" ;
                    dwc:recordedBy "C. Blume" ;
                    dwc:recordNumber "s.n." ;
                    dwc:institutionCode "NY" ] ;
            tcs:typeOfType <http://rs.gbif.org/vocabulary/gbif/type_status/isotype> ] .
```

[&#91;TurTLe&#93;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonName-typification-example-2.ttl)&nbsp;[&#91;JSON-LD&#93;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonName-typification-example-2.jsonld)

