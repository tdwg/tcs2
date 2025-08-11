# TaxonName typification example 1


**Term:** [tcs:typification](/terms/#tcs_typification)

TaxonName-typification-example-1 | [TaxonName-typification-example-2](./TaxonName-typification-example-2.html)
```turtle
<https://ipni.org/n/105731-1> a tcs:TaxonName ;
    tcs:nameString "Begonia seychellensis" ;
    dwc:scientificNameAuthorship "Hemsl." ;
    dwc:namePublishedIn "J. Bot. 54(Suppl. 2): 15 (1916)" ;
    tcs:typification [ a tcs:NomenclaturalType ;
            tcs:typifiedName <https://ipni.org/n/105731-1> ;
            tcs:typeSpecimen [ a dwc:MaterialCitation ;
                    dwc:country "Seychelles" ;
                    dwc:island "Mahé" ;
                    dwc:recordedBy "Horne" ;
                    dwc:recordNumber "s.n." ;
                    dwc:institutionCode "G" ] ;
            tcs:typeOfType <http://rs.gbif.org/vocabulary/gbif/type_status/isolectotype> ] ,
        [ a tcs:NomenclaturalType ;
            tcs:typifiedName <https://ipni.org/n/105731-1> ;
            tcs:typeSpecimen [ a dwc:MaterialCitation ;
                    dwc:country "Seychelles" ;
                    dwc:island "Mahé" ;
                    dwc:recordedBy "Horne" ;
                    dwc:recordNumber "245" ;
                    dwc:institutionCode "K" ] ;
            tcs:typeOfType <http://rs.gbif.org/vocabulary/gbif/type_status/lectotype> ]  ,
        [ a tcs:NomenclaturalType ;
            tcs:typifiedName <https://ipni.org/n/105731-1> ;
            tcs:typeSpecimen [ a dwc:MaterialCitation ;
                    dwc:country "Seychelles" ;
                    dwc:island "Mahé" ;
                    dwc:recordedBy "Gardiner" ;
                    dwc:recordNumber "s.n." ;
                    dwc:institutionCode "K" ] ;
            tcs:typeOfType <http://rs.gbif.org/vocabulary/gbif/type_status/syntype> ]  ,
        [ a tcs:NomenclaturalType ;
            tcs:typifiedName <https://ipni.org/n/105731-1> ;
            tcs:typeSpecimen [ a dwc:MaterialCitation ;
                    dwc:country "Seychelles" ;
                    dwc:island "Silhouette" ;
                    dwc:recordedBy "Gardiner" ;
                    dwc:recordNumber "111" ;
                    dwc:institutionCode "K" ] ;
            tcs:typeOfType <http://rs.gbif.org/vocabulary/gbif/type_status/syntype> ]  ,
        [ a tcs:NomenclaturalType ;
            tcs:typifiedName <https://ipni.org/n/105731-1> ;
            tcs:typeSpecimen [ a dwc:MaterialCitation ;
                    dwc:country "Seychelles" ;
                    dwc:island "Mahé and Silhouette" ;
                    dwc:recordedBy "Neville" ;
                    dwc:recordNumber "s.n." ;
                    dwc:institutionCode "K" ] ;
            tcs:typeOfType <http://rs.gbif.org/vocabulary/gbif/type_status/syntype> ]  .
```

[&#91;TurTLe&#93;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonName-typification-example-1.ttl)&nbsp;[&#91;JSON-LD&#93;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonName-typification-example-1.jsonld)

