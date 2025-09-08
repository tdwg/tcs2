# PreservedSpecimen typeStatus examples

In the following examples we link a `tcs:NomenclaturalType` to a
`dwc:PreservedSpecimen` with the `dwciri:typeStatus` property, which we consider
the inverse of the `tcs:typeSpecimen` property of the `tcs:NomenclaturalType`.
Elsewhere, e.g. in the [Rhododendron subg. penthantera example from TCS
1](https://github.com/tdwg/tcs2/blob/master/examples/rhododendron-subg-pentanthera.ttl#L178-L187),
we also use the `dwc:MaterialCitation` class in relation to nomenclatural types,
but only as the object of `tcs:typeSpecimen`, so as part of the typification of
a name, and never with `dcw:typeStatus` as the type status of a specimen.

## Example 1

```turtle
<https://specify.rbg.vic.gov.au/specify/view/collectionobject/273521> a dwc:PreservedSpecimen ;
    dsw:evidenceFor <https://avh.ala.org.au/occurrences/89086162-0bd8-4504-8abd-960d0a97d41a> ;
    dsw:isBasisForId _:b0 ;
    dwciri:typeStatus [ a tcs:NomenclaturalType ;
            tcs:typeOfType <http://rs.gbif.org/vocabulary/gbif/type_status/isolectotype> ;
            tcs:typifiedName <https://ipni.org/n/703183-1> ;
            tcs:typeSpecimen <https://specify.rbg.vic.gov.au/specify/view/collectionobject/273521> ] .

[] a oa:Annotation ;
    oa:motivatedBy oa:commenting ;
    oa:hasBody _:b0 ;
    oa:hasTarget <https://specify.rbg.vic.gov.au/specify/view/collectionobject/273521> ;
    dcterms:creator <http://www.wikidata.org/entity/Q6135471> ;
    dcterms:created "1942-02-25" .

_:b0 a dwc:Identification ;
    dwciri:toTaxon <https://id.biodiversity.org.au/instance/apni/601693> ;
    dwciri:identifiedBy <http://www.wikidata.org/entity/Q6135471> ;
    dwc:dateIdentified "1942-02-25" .

<https://id.biodiversity.org.au/instance/apni/601693> a tcs:TaxonConcept ;
    dcterms:title "Banksia serrata sec. Australian Plant Census 2005" ;
    tcs:taxonName <https://ipni.org/n/703183-1> ;
    tcs:accordingTo <https://id.biodiversity.org.au/reference/apni/42312> .

<https://ipni.org/n/703183-1> a tcs:TaxonName ;
    tcs:nameString "Banksia serrata" ;
    dwc:scientificNameAuthorship "L.f." ;
    dwc:namePublishedIn "Suppl. Pl. 126" ;
    dwc:namePublishedInYear "1782" .

<https://avh.ala.org.au/occurrences/89086162-0bd8-4504-8abd-960d0a97d41a> a dwc:Occurrence ;
    dwciri:recordedBy <http://www.wikidata.org/entity/Q153408> ,
            <http://www.wikidata.org/entity/Q39789> ;
    dsw:atEvent [ a dwc:Event ;
            dwc:eventDate "1770-04" ;
            dwciri:inDescribedPlace [ a dcterms:Location ;
                    dwc:country "Australia" ;
                    dwc:stateOrProvince "New South Wales" ;
                    dwc:verbatimLocality "Botany Bay" ;
                    dwc:verbatimLatitude "33° 58' S" ;
                    dwc:verbatimLongitude "151° 12' E" ;
                    dwc:decimalLatitude -33.96670 ;
                    dwc:decimalLongitude 151.20000 ;
                    dwc:coordinatePrecision 0.016667 ;
                    dwc:coordinateUncertaintyInMeters 10000 ;
                    dwciri:geodeticDatum <https://epsg.io/4326> ] ] ;
    dsw:hasEvidence <https://specify.rbg.vic.gov.au/specify/view/collectionobject/273521> .

<http://www.wikidata.org/entity/Q6135471> a foaf:Person ;
    foaf:givenName "James Hamlyn" ;
    foaf:familyName "Willis" .

<http://www.wikidata.org/entity/Q153408> a foaf:Person ;
    foaf:givenName "Joseph" ;
    foaf:familyName "Banks" .

<http://www.wikidata.org/entity/Q39789> a foaf:Person ;
    foaf:givenName "Daniel Carl" ;
    foaf:familyName "Solander" .
```

[TurTLe](https://github.com/tdwg/tcs2/blob/master/examples/PreservedSpecimen-typeStatus-example-1.ttl) |
[JSON-LD](https://github.com/tdwg/tcs2/blob/master/examples/PreservedSpecimen-typeStatus-example-1.jsonld)


## Example 2

```turtle
<https://specify.rbg.vic.gov.au/specify/view/collectionobject/739393> a dwc:PreservedSpecimen ;
    dwc:catalogNumber "MEL 0227036A" ;
    dsw:evidenceFor <https://avh.ala.org.au/occurrences/78ba3182-76a4-4fcd-a231-d657acf3d347> ;
    dsw:isBasisForId _:b0 ;
    dwciri:typeStatus [ a tcs:NomenclaturalType ;
            tcs:typifiedName <https://ipni.org/n/717216-1> ;
            tcs:typeOfType <http://rs.gbif.org/vocabulary/gbif/type_status/lectotype> ;
            tcs:typePublishedIn <https://id.biodiversity.org.au/reference/apni/39897> ] .

[] a oa:Annotation ;
    oa:motivatedBy oa:commenting ;
    oa:hasBody _:b0 ;
    oa:hasTarget <https://specify.rbg.vic.gov.au/specify/view/collectionobject/739393> ;
    dcterms:creator <https://orcid.org/0000-0001-9124-9802> ;
    dcterms:created "2024-04-12" .

[] a oa:Annotation ;
    oa:motivatedBy oa:commenting ;
    oa:hasBody _:b1 ;
    oa:hasTarget <https://specify.rbg.vic.gov.au/specify/view/collectionobject/739393> ;
    dcterms:creator <https://orcid.org/0000-0001-9124-9802> ;
    dcterms:created "2024-04-12" .

[] a oa:Annotation ;
    oa:motivatedBy oa:commenting ;
    oa:hasBody [ a dwc:Identification ;
            dwciri:toTaxon <https://id.biodiversity.org.au/instance/apni/698961> ;
            dwc:identifiedBy <http://www.wikidata.org/entity/Q5719316> ;
            dwc:dateIdentified "1999-09-28" ] ;
    oa:hasTarget <https://specify.rbg.vic.gov.au/specify/view/collectionobject/739393> ;
    dcterms:creator <http://www.wikidata.org/entity/Q5719316> ;
    dcterms:created "1999-09-28" .

[] a oa:Annotation ;
    oa:motivatedBy oa:commenting ;
    oa:hasBody [ a tcs:NomenclaturalType ;
            tcs:typifiedName <https://ipni.org/n/717216-1> ;
            tcs:typeOfType <http://rs.gbif.org/vocabulary/gbif/type_status/holotype> ;
            tcs:typeSpecimen <https://specify.rbg.vic.gov.au/specify/view/collectionobject/739393> ] ;
    dcterms:creator <http://www.wikidata.org/entity/Q5719316> ;
    dcterms:created "1999-09-28" .

_:b0 a dwc:Identification ;
    dwciri:toTaxon <https://id.biodiversity.org.au/instance/apni/698961> ;
    dwciri:identifiedBy <https://orcid.org/0000-0001-9124-9802> ;
    dwc:dateIdentified "2024-04-12" .

_:b1 a tcs:NomenclaturalType ;
    tcs:typifiedName <https://ipni.org/n/717216-1> ;
    tcs:typeOfType <http://rs.gbif.org/vocabulary/gbif/type_status/lectotype> ;
    tcs:typeSpecimen <https://specify.rbg.vic.gov.au/specify/view/collectionobject/739393> ;
    tcs:typePublishedIn <https://id.biodiversity.org.au/reference/apni/39897> .

<https://id.biodiversity.org.au/instance/apni/698961> a tcs:TaxonConcept ;
    dcterms:title "Stenanthemum coronatum sec. Australian Plant Census 2011" ;
    tcs:taxonName <https://ipni.org/n/718981-1> ;
    tcs:accordingTo <https://id.biodiversity.org.au/reference/apni/49840> .

<https://ipni.org/n/718981-1> a tcs:TaxonName ;
    tcs:nameString "Stenanthemum coronatum" ;
    dwc:scientificNameAuthorship "(Reissek) Reissek" ;
    dwc:namePublishedIn "Linnaea 29: 295" ;
    dwc:namePublishedInYear "1858" ;
    tcs:basionym <https://ipni.org/n/717216-1> .

<https://ipni.org/n/717216-1> a tcs:TaxonName ;
    tcs:nameString "Cryptandra coronata" ;
    dwc:scientificNameAuthorship "Reissek" ;
    dwc:namePublishedIn "Pl. Preiss. [J.G.C.Lehmann] 2(2-3): 288" ;
    dwc:namePublishedInYear "1848" .

<https://avh.ala.org.au/occurrences/78ba3182-76a4-4fcd-a231-d657acf3d347> a dwc:Occurrence ;
    dwciri:recordedBy <http://www.wikidata.org/entity/Q2589989> ;
    dwc:recordNumber "722" ;
    dwciri:atEvent [ a dwc:Event ;
            dwc:eventDate "1829/1863" ;
            dwciri:inDescribedPlace [ a dcterms:Location ;
                    dwc:country "Australia" ;
                    dwc:stateOrProvince "Western Australia" ;
                    dwc:verbatimLocality "Swan River" ] ;
    dsw:hasEvidence <https://specify.rbg.vic.gov.au/specify/view/collectionobject/739393> ,
            <http://specimens.kew.org/herbarium/K001096706> ,
            <http://specimens.kew.org/herbarium/K001096705> ,
            _:BM000050758 ] .

<https://orcid.org/0000-0001-9124-9802> a foaf:Person ;
    foaf:givenName "Jürgen" ;
    foaf:familyName "Kellermann" .

<http://www.wikidata.org/entity/Q5719316> a foaf:Person ;
    foaf:givenName "Barbara Lynette" ;
    foaf:familyName "Rye" .

<http://www.wikidata.org/entity/Q2589989> a foaf:Person ;
    foaf:givenName "James" ;
    foaf:familyName "Drummond" .

<http://specimens.kew.org/herbarium/K001096706> a dwc:PreservedSpecimen ;
    dwc:catalogNumber "K001096706" ;
    dsw:evidenceFor <https://avh.ala.org.au/occurrences/78ba3182-76a4-4fcd-a231-d657acf3d347> ;
    dsw:isBasisForId [ a dwc:Identification ;
            dwciri:toTaxon <https://id.biodiversity.org.au/instance/apni/698961> ;
            dwciri:identifiedBy <https://orcid.org/0000-0001-9124-9802> ] ;
    dwciri:typeStatus [ a tcs:NomenclaturalType ;
            tcs:typifiedName <https://ipni.org/n/717216-1> ;
            tcs:typeOfType <http://rs.gbif.org/vocabulary/gbif/type_status/isolectotype> ;
            tcs:typePublishedIn <https://id.biodiversity.org.au/reference/apni/39897> ] .

<http://specimens.kew.org/herbarium/K001096705> a dwc:PreservedSpecimen ;
    dwc:catalogNumber "K001096705" ;
    dsw:evidenceFor <https://avh.ala.org.au/occurrences/78ba3182-76a4-4fcd-a231-d657acf3d347> ;
    dsw:isBasisForId [ a dwc:Identification ;
            dwciri:toTaxon <https://id.biodiversity.org.au/instance/apni/698961> ;
            dwciri:identifiedBy <https://orcid.org/0000-0001-9124-9802> ] ;
    dwciri:typeStatus [ a tcs:NomenclaturalType ;
            tcs:typifiedName <https://ipni.org/n/717216-1> ;
            tcs:typeOfType <http://rs.gbif.org/vocabulary/gbif/type_status/isolectotype> ;
            tcs:typePublishedIn <https://id.biodiversity.org.au/reference/apni/39897> ] .

_:BM000050758 a dwc:PreservedSpecimen ;
    dwc:catalogNumber "BM000050758" ;
    dsw:evidenceFor <https://avh.ala.org.au/occurrences/78ba3182-76a4-4fcd-a231-d657acf3d347> ;
    dsw:isBasisForId [ a dwc:Identification ;
            dwciri:toTaxon <https://id.biodiversity.org.au/instance/apni/698961> ;
            dwciri:identifiedBy <https://orcid.org/0000-0001-9124-9802> ] ;
    dwciri:typeStatus [ a tcs:NomenclaturalType ;
            tcs:typifiedName <https://ipni.org/n/717216-1> ;
            tcs:typeOfType <http://rs.gbif.org/vocabulary/gbif/type_status/isolectotype> ;
            tcs:typePublishedIn <https://id.biodiversity.org.au/reference/apni/39897> ] .

# From the literature

[] a tcs:NomenclaturalType ;
    tcs:typifiedName <https://ipni.org/n/717216-1> ;
    tcs:typeOfType <http://rs.gbif.org/vocabulary/gbif/type_status/holotype> ;
    tcs:typeSpecimen <https://specify.rbg.vic.gov.au/specify/view/collectionobject/739393> ;
    dcterms:source <https://id.biodiversity.org.au/reference/apni/39897> .

<https://id.biodiversity.org.au/reference/apni/39897> a bibo:JournalArticle ;
    dcterms:bibliographicCitation """Rye, B.L. (1995), New and priority taxa in 
            the genera Cryptandra and Stenanthemum (Rhamnaceae) of Western 
            Australia. Nuytsia 10(2): 255-305""" .

# The incorrect listing of Drummond 722 (MEL 227036) as the holotype ("type") of
# Cryptandra coronata constitutes a lectotypification under the botanical code.
[] a tcs:NomenclaturalType ;
    tcs:typifiedName <https://ipni.org/n/717216-1> ;
    tcs:typeOfType <http://rs.gbif.org/vocabulary/gbif/type_status/holotype> ;
    tcs:typeSpecimen <https://specify.rbg.vic.gov.au/specify/view/collectionobject/739393> ;
    tcs:typePublishedIn <https://id.biodiversity.org.au/reference/apni/39897> ;
    dcterms:source <https://id.biodiversity.org.au/reference/apni/51399981> .

<https://id.biodiversity.org.au/reference/apni/51399981> a bibo:JournalArticle ;
    dcterms:bibliographicReference """Kellermann, J. & Thiele, K.R. (2021), The 
            other ‘propeller plant’ – Notes on Stenanthemum Reissek (Rhamnaceae: 
            Pomaderreae) and a key to the genus in Australia. Swainsona 35: 
            11-22""" .
```

[TurTLe](https://github.com/tdwg/tcs2/blob/master/examples/PreservedSpecimen-typeStatus-example-2.ttl) |
[JSON-LD](https://github.com/tdwg/tcs2/blob/master/examples/PreservedSpecimen-typeStatus-example-2.jsonld)


## Example 3

```turtle
<https://specify.rbg.vic.gov.au/specify/view/collectionobject/51589> a dwc:PreservedSpecimen ;
    dwc:catalogNumber "MEL 0687503A" ;
    dsw:evidenceFor <https://avh.ala.org.au/occurrences/f121f99a-5b02-4f7b-9d57-bb2718c0c7de> ;
    dsw:isBasisForId _:b0 ;
    dwciri:typeStatus [ a tcs:NomenclaturalType ;
            tcs:typeOfType <http://rs.gbif.org/vocabulary/gbif/type_status/isolectotype> ;
            tcs:typifiedName <https://ipni.org/n/933707-1> ;
            tcs:typeSpecimen <https://specify.rbg.vic.gov.au/specify/view/collectionobject/51589> ] .

[] a oa:Annotation ;
    oa:motivatedBy oa:commenting ;
    oa:hasBody _:b0 ;
    oa:hasTarget <https://specify.rbg.vic.gov.au/specify/view/collectionobject/51589> ;
    dcterms:creator <https://orcid.org/0000-0001-6661-7722> ;
    dcterms:created "2015-08-07" .

_:b0 a dwc:Identification ;
    dwciri:toTaxon <https://id.biodiversity.org.au/instance/apni/612750> ;
    dwc:dateIdentified "2015-08-27" ;
    dwciri:identifiedBy [ a foaf:Organization ;
            foaf:name "National Herbarium of Victoria (MEL)" ] .

[] a oa:Annotation ;
    oa:motivatedBy oa:commenting ;
    oa:hasBody [ a dwc:Identification ;
            dwciri:toTaxon <https://id.biodiversity.org.au/instance/apni/455406> ;
            dwciri:identifiedBy <https://www.ipni.org/a/1174-1> ;
            dwciri:dateIdentified "1993-02/1993-03" ] ;
    dcterms:creator <https://www.ipni.org/a/1174-1> ;
    dcterms:created "1993-02/1993-03" .

<https://id.biodiversity.org.au/instance/apni/455406> a tcs:TaxonConcept ;
    dcterms:title "Eucalyptus xanthoclada sec. Brooker & Bean 1987" ;
    tcs:taxonName <https://ipni.org/n/933707-1> ;
    tcs:accordingTo <https://id.biodiversity.org.au/reference/apni/40410> .

<https://id.biodiversity.org.au/instance/apni/612750> a tcs:TaxonConcept ;
    dcterms:title "Eucalyptus crebra sec. Australian Plant Census 2006" ;
    tcs:taxonName <https://ipni.org/n/592841-1> ;
    tcs:accordingTo <https://id.biodiversity.org.au/reference/apni/42942> .

<https://ipni.org/n/592841-1> a tcs:TaxonName ;
    tcs:nameString "Eucalyptus crebra" ;
    dwc:scientificNameAuthorship "F.Muel." ;
    dwc:namePublishedIn "J. Proc. Linn. Soc., Bot. 3: 87" ;
    dwc:namePublishedInYear "1858" .

<https://ipni.org/n/933707-1> a tcs:TaxonName ;
    tcs:nameString "Eucalyptus xanthoclada" ;
    dwc:scientificNameAuthorship "Brooker & A.R.Bean" ;
    dwc:namePublishedIn "Brunonia 10(2): 193" ;
    dwc:namePublishedInYear "1987" .

<https://avh.ala.org.au/occurrences/f121f99a-5b02-4f7b-9d57-bb2718c0c7de> a dwc:Occurrence ;
    dwciri:recordedBy <https://www.ipni.org/a/1174-1> ;
    dwc:recordNumber "8969" ;
    dsw:atEvent [ a dwc:Event ;
            dwc:eventDate "1985-05-01" ;
            dwciri:inDescribedPlace [ a dcterms:Location ;
                    dwc:country "Australia" ;
                    dwc:stateOrProvince "Queensland" ;
                    dwc:verbatimLocality "10 km NE of Pentland" ;
                    dwc:verbatimLatitude "20° 28' S" ;
                    dwc:verbatimLongitude "145° 29' E" ;
                    dwc:decimalLatitude -20.46670 ;
                    dwc:decimalLongitude 145.48330 ;
                    dwc:coordinatePrecision 0.01667 ;
                    dwc:coordinateUncertaintyInMeters 1000 ;
                    dwciri:geodeticDatum <https://epsg.io/4326> ] ] ;
    dsw:hasEvidence <https://specify.rbg.vic.gov.au/specify/view/collectionobject/51589> .

<https://www.ipni.org/a/1174-1> a foaf:Person ;
    foaf:givenName "Brooker" ;
    foaf:familyName "Murray Ian Hill" .

<https://orcid.org/0000-0001-6661-7722> a foaf:Person ;
    foaf:givenName "Wayne" ;
    foaf:familyName "Gebert" .
```

[TurTLe](https://github.com/tdwg/tcs2/blob/master/examples/PreservedSpecimen-typeStatus-example-3.ttl) |
[JSON-LD](https://github.com/tdwg/tcs2/blob/master/examples/PreservedSpecimen-typeStatus-example-3.jsonld)


## Example 4

```turtle
<https://specify.rbg.vic.gov.au/specify/view/collectionobject/313208> a dwc:PreservedSpecimen ;
    dwc:catalogNumber "MEL 1516494A" ;
    dsw:evidenceFor <https://avh.ala.org.au/occurrences/794ef2b7-956e-44e5-9321-cbe9553d6057> ;
    dsw:isBasisForId _:b0 ;
    dwciri:typeStatus _:b1 .

[] a oa:Annotation ;
    oa:motivatedBy oa:commenting ;
    oa:hasBody _:b0 ;
    oa:hasTarget <https://specify.rbg.vic.gov.au/specify/view/collectionobject/313208> ;
    dcterms:creator <http://www.wikidata.org/entity/Q5925767> ;
    dcterms:created "1980-03-24" .

[] a oa:Annotation ;
    oa:motivatedBy oa:commenting ;
    oa:hasBody _:b1 ;
    oa:hasTarget <https://specify.rbg.vic.gov.au/specify/view/collectionobject/313208> ;
    dcterms:creator <http://www.wikidata.org/entity/Q5925767> ;
    dcterms:created "1980-03-24" .

_:b0 a dwc:Identification ;
    dwciri:toTaxon <https://id.biodiversity.org.au/instance/apni/683275> ;
    dwciri:identifiedBy <http://www.wikidata.org/entity/Q5925767> ;
    dwc:dateIdentified "1980-03-24" .

_:b1 a tcs:NomenclaturalType ;
    tcs:typifiedName <https://ipni.org/n/520357-1> ;
    tcs:typeOfType <http://rs.gbif.org/vocabulary/gbif/type_status/syntype> ;
    tcs:typeSpecimen <https://specify.rbg.vic.gov.au/specify/view/collectionobject/313208> .

<https://id.biodiversity.org.au/instance/apni/683275> a tcs:TaxonConcept ;
    dcterms:title "Templetonia stenophylla sec. Ross 1996" ;
    tcs:taxonName <https://ipni.org/n/520361-1> ;
    tcs:accordingTo <https://id.biodiversity.org.au/reference/apni/50798> .

<https://ipni.org/n/520361-1> a tcs:TaxonName ;
    tcs:nameString "Templetonia stenophylla" ;
    dwc:scientificNameAuthorship "(F.Muell.) J.M.Black" ;
    dwc:namePublishedIn "Fl. S. Austral. 304" ;
    dwc:namePublishedInYear "1924" .

<https://ipni.org/n/520357-1> a tcs:TaxonName ;
    tcs:nameString "Templetonia muelleri" ;
    dwc:scientificNameAuthorship "Benth." ;
    dwc:namePublishedIn "Fl. Austral. 2: 169" ;
    dwc:namePublishedInYear "1864" ;
    tcs:nomenclaturalStatus <http://rs.gbif.org/vocabulary/gbif/nomenclatural_status/superfluum> ;
    rdfs:comment "Templestonia muelleri Benth. includes the type of Bossiaea stenophylla F.Muell." .

<https://avh.ala.org.au/occurrences/794ef2b7-956e-44e5-9321-cbe9553d6057> a dwc:Occurrence ;
    dwciri:recordedBy <http://www.wikidata.org/entity/Q16065577> ;
    dwc:recordNumber "88" ;
    dsw:atEvent [ a dwc:Event ;
            dwc:eventDate "1852/1862" ;
            dwciri:inDescribedPlace [ a dcterms:Location ;
                    dwc:country "Australia" ;
                    dwc:stateOrProvince "Victoria" ;
                    dwc:verbatimLocality "Between Mount Arapiles and Lake Hindmarsh" ;
                    dwc:locality "Mount Arapiles" ;
                    dwc:verbatimLatitude "36° 45' S" ;
                    dwc:verbatimLongitude "141° 50' E" ;
                    dwc:decimalLatitude -36.75000 ;
                    dwc:decimalLongitude 141.83330 ;
                    dwc:coordinatePrecision 0.01677 ;
                    dwc:coordinateUncertaintyInMeters 25000 ;
                    dwciri:geodeticDatum <https://epsg.io/4326> ] ] .

<http://www.wikidata.org/entity/Q5925767> a foaf:Person ;
    foaf:givenName "James Henderson" ;
    foaf:familyName "Ross" .

<http://www.wikidata.org/entity/Q16065577> a foaf:Person ;
    foaf:givenName "John" ;
    foaf:familyName "Dallachy" .
```

[TurTLe](https://github.com/tdwg/tcs2/blob/master/examples/PreservedSpecimen-typeStatus-example-4.ttl) |
[JSON-LD](https://github.com/tdwg/tcs2/blob/master/examples/PreservedSpecimen-typeStatus-example-4.jsonld)




