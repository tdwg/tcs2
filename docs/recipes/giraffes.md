# IUCN Taxonomic Status of Giraffes Report Recipe

The following recipe is based on a recently published IUCN report on the
taxonomic status of Giraffes (IUCN SSC Giraffe and Okapi Specialist Group
Taxonomic Task Force, 2025
[\[iucn_ssc_giraffe_and_okapi_specialist_group_taxonomic_task_force_evaluation_2025\]](../bibliography#iucn_ssc_giraffe_and_okapi_specialist_group_taxonomic_task_force_evaluation_2025)).
The report recognises four species and eight subspecies of Giraffe, while at the
time the last assessment for the IUCN Red List of Threatened Species (Muller et
al., 2018 [\[muller_giraffa_2018\]](../bibliography#muller_giraffa_2018)) was
made only a single species with nine subspecies was recognised.

This recipe compares the four-species classification of the present IUCN report
with the single-species classification (Dagg, 1971
[\[dagg_giraffa_1971\]](../bibliography#dagg_giraffa_1971)) that underpinned the
Red List assessment. In the full code in GitHub an eight-species classification
(Groves & Grubb, 2011
[\[groves_ungulate_2011\]](../bibliography#groves_ungulate_2011)) is also
included, as well as a much older classification that recognises two species and
11 subspecies (Lydekker, 1904
[\[lydekker_subspecies_1904\]](../bibliography#lydekker_subspecies_1904)).

## Taxon Concepts

### IUCN 2025

>
> - Giraffa
>   - Giraffa camelopardalis (Northern giraffe)
>     - Giraffa camelopardalis peralta (West African giraffe)
>     - Giraffa camelopardalis antiquorum (Kordofan giraffe)
>     - Giraffa camelopardalis camelopardalis (Nubian giraffe)
>   - Giraffa reticulata (Reticulated giraffe)
>   - Giraffa tippelskirchi (Masai giraffe)
>     - Giraffa tippelskirchi tippelskirchi (Masai giraffe)
>     - Giraffa tippelskirchi thornicrofti (Luangwa giraffe)
>   - Giraffa giraffa (Southern giraffe)
>     - Giraffa giraffa giraffa (South African giraffe)
>     - Giraffa giraffa angolensis (Angolan giraffe)
>

<br>

```turtle
_:tc33 a tcs:TaxonConcept ;
    dcterms:title "Giraffa sec. IUCN 2025" ;
    tcs:taxonName <zoobank:29a6803b-c1d8-4460-96c7-cc006095413f> ;
    tcs:accordingTo _:ref0 ;
    tcs:taxonRank <http://rs.gbif.org/vocabulary/gbif/rank/genus> ;
    tcs:vernacularName [ a gbif:VernacularName ;
            dwc:vernacularName "Giraffe" ] .

_:tc20 a tcs:TaxonConcept ;
    dcterms:title "Giraffa camelopardalis sec. IUCN 2025" ;
    tcs:taxonName _:tn1 ;
    tcs:accordingTo _:ref0 ;
    tcs:taxonRank <http://rs.gbif.org/vocabulary/gbif/rank/species> ;
    tcs:parentTaxonConcept _:tc33 ;
    tcs:vernacularName [ a gbif:VernacularName ;
            dwc:vernacularName "Northern giraffe" ] .

_:tc21 a tcs:TaxonConcept ;
    dcterms:title "Giraffa camelopardalis peralta sec. IUCN 2025" ;
    tcs:taxonName <zoobank:a1d014fd-cdbf-4eaf-a979-100186fc2f41> ;
    tcs:accordingTo _:ref0 ;
    tcs:taxonRank <http://rs.gbif.org/vocabulary/gbif/rank/subspecies> ;
    tcs:parentTaxonConcept _:tc20 ;
    tcs:vernacularName [ a gbif:VernacularName ;
            dwc:vernacularName "West African giraffe" ] .

_:tc22 a tcs:TaxonConcept ;
    dcterms:title "Giraffa camelopardalis antiquorum sec. IUCN 2025" ;
    tcs:taxonName _:tn3 ;
    tcs:accordingTo _:ref0 ;
    tcs:taxonRank <http://rs.gbif.org/vocabulary/gbif/rank/subspecies> ;
    tcs:parentTaxonConcept _:tc20 ;
    tcs:vernacularName [ a gbif:VernacularName ;
            dwc:vernacularName "Kordofan giraffe" ] .

_:tc23 a tcs:TaxonConcept ;
    dcterms:title "Giraffa camelopardalis camelopardalis sec. IUCN 2025" ;
    tcs:taxonName _:tn2 ;
    tcs:accordingTo _:ref0 ;
    tcs:taxonRank <http://rs.gbif.org/vocabulary/gbif/rank/subspecies> ;
    tcs:parentTaxonConcept _:tc20 ;
    tcs:vernacularName [ a gbif:VernacularName ;
            dwc:vernacularName "Nubian giraffe" ] .

_:tc24 a tcs:TaxonConcept ;
    dcterms:title "Giraffa reticulata sec. IUCN 2025" ;
    tcs:taxonName _:tn0 ;
    tcs:accordingTo _:ref0 ;
    tcs:taxonRank <http://rs.gbif.org/vocabulary/gbif/rank/species> ;
    tcs:parentTaxonConcept _:tc33 ;
    tcs:vernacularName [ a gbif:VernacularName ;
            dwc:vernacularName "Reticulated giraffe" ] .

_:tc25 a tcs:TaxonConcept ;
    dcterms:title "Giraffa tippelskirchi sec. IUCN 2025" ;
    tcs:taxonName <zoobank:fc4e3aca-4e59-4fae-a052-f220b4a5c70b> ;
    tcs:accordingTo _:ref0 ;
    tcs:taxonRank <http://rs.gbif.org/vocabulary/gbif/rank/species> ;
    tcs:parentTaxonConcept _:tc33 ;
    tcs:vernacularName [ a gbif:VernacularName ;
            dwc:vernacularName "Masai giraffe" ] .

_:tc26 a tcs:TaxonConcept ;
    dcterms:title "Giraffa tippelskirchi tippelskirchi sec. IUCN 2025" ;
    tcs:taxonName _:tn26 ;
    tcs:accordingTo _:ref0 ;
    tcs:taxonRank <http://rs.gbif.org/vocabulary/gbif/rank/subspecies> ;
    tcs:parentTaxonConcept _:tc25 ;
    tcs:vernacularName [ a gbif:VernacularName ;
            dwc:vernacularName "Masai giraffe" ] .

_:tc27 a tcs:TaxonConcept ;
    dcterms:title "Giraffa tippelskirchi thornicrofti sec. IUCN 2025" ;
    tcs:taxonName _:tn28 ;
    tcs:accordingTo _:ref0 ;
    tcs:taxonRank <http://rs.gbif.org/vocabulary/gbif/rank/subspecies> ;
    tcs:parentTaxonConcept _:tc25 ;
    tcs:vernacularName [ a gbif:VernacularName ;
            dwc:vernacularName "Luangwa giraffe" ] ,
        [ a gbif:VernacularName ;
            dwc:vernacularName "Thornicroft's giraffe" ] .

_:tc28 a tcs:TaxonConcept ;
    dcterms:title "Giraffa giraffa sec. IUCN 2025" ;
    tcs:taxonName _:tn22 ;
    tcs:accordingTo _:ref0 ;
    tcs:taxonRank <http://rs.gbif.org/vocabulary/gbif/rank/species> ;
    tcs:parentTaxonConcept _:tc33 ;
    tcs:vernacularName [ a gbif:VernacularName ;
            dwc:vernacularName "Southern giraffe" ] .

_:tc29 a tcs:TaxonConcept ;
    dcterms:title "Giraffa giraffa giraffa sec. IUCN 2025" ;
    tcs:taxonName _:tn27 ;
    tcs:accordingTo _:ref0 ;
    tcs:taxonRank <http://rs.gbif.org/vocabulary/gbif/rank/subspecies> ;
    tcs:parentTaxonConcept _:tc25 ;
    tcs:vernacularName [ a gbif:VernacularName ;
            dwc:vernacularName "South African giraffe" ] .

_:tc30 a tcs:TaxonConcept ;
    dcterms:title "Giraffa giraffa angolensis sec. IUCN 2025" ;
    tcs:taxonName _:tn27 ;
    tcs:accordingTo _:ref0 ;
    tcs:taxonRank <http://rs.gbif.org/vocabulary/gbif/rank/subspecies> ;
    tcs:parentTaxonConcept _:tc25 ;
    tcs:vernacularName [ a gbif:VernacularName ;
            dwc:vernacularName "Angolan giraffe" ] .
```

<br>

### Dagg 1971

> - Giraffa
>   - Giraffa camelopardalis
>     - Giraffa camelopardalis camelopardalis
>     - Giraffa camelopardalis antiquorum
>     - Giraffa camelopardalis peralta
>     - Giraffa camelopardalis reticulata
>     - Giraffa camelopardalis rothschildi
>     - Giraffa camelopardalis tippelskirchi
>     - Giraffa camelopardalis thornicrofti
>     - Giraffa camelopardalis angolensis
>     - Giraffa camelopardalis giraffa

```turtle
_:tc34 a tcs:TaxonConcept ;
    dcterms:title "Giraffa sec. Dagg 1971" ;
    tcs:taxonName <zoobank:29a6803b-c1d8-4460-96c7-cc006095413f> ;
    tcs:accordingTo <https://doi.org/10.2307/3503830> ;
    tcs:taxonRank <http://rs.gbif.org/vocabulary/gbif/rank/genus> ;
    tcs:synonym <https://zoobank.org/NomenclaturalActs/092ff21a-bd6b-4eb3-a27b-c74943868b9e> .

_:tc35 a tcs:TaxonConcept ;
    dcterms:title "Giraffa camelopardalis sec. Dagg 1971" ;
    tcs:taxonName "_:tn1" ;
    tcs:accordingTo <https://doi.org/10.2307/3503830> ;
    tcs:taxonRank <http://rs.gbif.org/vocabulary/gbif/rank/species> ;
    tcs:parentTaxonConcept _:tc34 ;
    tcs:synonym <zoobank:d877e595-ff30-4d86-b4bd-39d06e5e2cf3> ,
        <zoobank:6b9469dc-6f06-4fba-911b-c08c2667278f> ,
        <zoobank:e6851c80-2e77-4a51-bbbc-7179249e9d5c> ,
        _:tn14 ,
        <zoobank:507a1a9e-dcf8-4c92-a94d-2ad984ad8f46> ,
        <zoobank:fc4e3aca-4e59-4fae-a052-f220b4a5c70b> ,
        <zoobank:aed6605c-7811-4260-9c4c-21b26b946e5d> ,
        <zoobank:f4bc8451-d2f8-41be-a900-e61af09734b6> .

_:tc36 a tcs:TaxonConcept ;
    dcterms:title "Giraffa camelopardalis camelopardalis sec. Dagg 1971" ;
    tcs:taxonName _:tn2 ;
    tcs:accordingTo <https://doi.org/10.2307/3503830> ;
    tcs:taxonRank <http://rs.gbif.org/vocabulary/gbif/rank/subspecies> ;
    tcs:parentTaxonConcept _:tc35 ;
    tcs:synonym <zoobank:e6851c80-2e77-4a51-bbbc-7179249e9d5c> .

_:tc37 a tcs:TaxonConcept ;
    dcterms:title "Giraffa camelopardalis antiquorum sec. Dagg 1971" ;
    tcs:taxonName _:tn3 ;
    tcs:accordingTo <https://doi.org/10.2307/3503830> ;
    tcs:taxonRank <http://rs.gbif.org/vocabulary/gbif/rank/subspecies> ;
    tcs:parentTaxonConcept _:tc35 ;
    tcs:synonym <zoobank:507a1a9e-dcf8-4c92-a94d-2ad984ad8f46> .

_:tc38 a tcs:TaxonConcept ;
    dcterms:title "Giraffa camelopardalis peralta sec. Dagg 1971" ;
    tcs:taxonName <zoobank:a1d014fd-cdbf-4eaf-a979-100186fc2f41> ;
    tcs:accordingTo <https://doi.org/10.2307/3503830> ;
    tcs:taxonRank <http://rs.gbif.org/vocabulary/gbif/rank/subspecies> ;
    tcs:parentTaxonConcept _:tc35 .

_:tc39 a tcs:TaxonConcept ;
    dcterms:title "Giraffa camelopardalis reticulata sec. Dagg 1971" ;
    tcs:taxonName <zoobank:3ac03875-1c25-49a5-96c5-981b87cfa73a> ;
    tcs:accordingTo <https://doi.org/10.2307/3503830> ;
    tcs:taxonRank <http://rs.gbif.org/vocabulary/gbif/rank/subspecies> ;
    tcs:parentTaxonConcept _:tc35 ;
    tcs:synonym <zoobank:f4bc8451-d2f8-41be-a900-e61af09734b6> ,
        <zoobank:5bdb022d-954d-42d4-b6ca-a273af39789f> .

_:tc40 a tcs:TaxonConcept ;
    dcterms:title "Giraffa camelopardalis rothschildi sec. Dagg 1971" ;
    tcs:taxonName <zoobank:a3492a30-8739-4b4e-8e6f-5c09e2c34315> ;
    tcs:accordingTo <https://doi.org/10.2307/3503830> ;
    tcs:taxonRank <http://rs.gbif.org/vocabulary/gbif/rank/subspecies> ;
    tcs:parentTaxonConcept _:tc35 ;
    tcs:synonym <zoobank:9cba7e21-4f14-4354-b559-36b7db538c08> .

_:tc41 a tcs:TaxonConcept ;
    dcterms:title "Giraffa camelopardalis tippelskirchi sec. Dagg 1971" ;
    tcs:taxonName _:tn6 ;
    tcs:accordingTo <https://doi.org/10.2307/3503830> ;
    tcs:taxonRank <http://rs.gbif.org/vocabulary/gbif/rank/subspecies> ;
    tcs:parentTaxonConcept _:tc35 ;
    tcs:synonym <zoobank:aed6605c-7811-4260-9c4c-21b26b946e5d> .

_:tc42 a tcs:TaxonConcept ;
    dcterms:title "Giraffa camelopardalis thornicrofti sec. Dagg 1971" ;
    tcs:taxonName _:tn30 ;
    tcs:accordingTo <https://doi.org/10.2307/3503830> ;
    tcs:taxonRank <http://rs.gbif.org/vocabulary/gbif/rank/subspecies> ;
    tcs:parentTaxonConcept _:tc35 .

_:tc43 a tcs:TaxonConcept ;
    dcterms:title "Giraffa camelopardalis angolensis sec. Dagg 1971" ;
    tcs:taxonName <zoobank:c8aeee34-3551-4227-871c-13f2a52bcf02> ;
    tcs:accordingTo <https://doi.org/10.2307/3503830> ;
    tcs:taxonRank <http://rs.gbif.org/vocabulary/gbif/rank/subspecies> ;
    tcs:parentTaxonConcept _:tc35 ;
    tcs:synonym <zoobank:be7a0080-ff1c-4857-a536-6d0016ccc1e8> .

_:tc44 a tcs:TaxonConcept ;
    dcterms:title "Giraffa camelopardalis giraffa sec. Dagg 1971" ;
    tcs:taxonName _:tn31 ;
    tcs:accordingTo <https://doi.org/10.2307/3503830> ;
    tcs:taxonRank <http://rs.gbif.org/vocabulary/gbif/rank/subspecies> ;
    tcs:parentTaxonConcept _:tc35 ;
    tcs:synonym _:tn14 , 
        _:tn15 , 
        <zoobank:0477d1d3-3602-4bec-b4a3-11d108886065> .
```

<br>

## Taxon Concept Mappings

The following mappings can be made between the concepts in the IUCN report and 
the classifications by Groves and Grubb (2011) and Lydekker (1904).

### Giraffa sec. IUCN 2025

> **Giraffa sec. IUCN 2025**<br>
> &cong; Giraffa sec. Dagg 1971

<br>

```turtle
# Giraffa sec. IUCN 2025 == Giraffa sec. Dagg 1971
[] a tcs:TaxonConceptMapping ;
    tcs:subjectTaxonConcept _:tc33 ;
    tcs:mappingRelation tcs:isCongruentWith ;
    tcs:objectTaxonConcept _:tc34 ;
    dcterms:creator <https://orcid.org/0000-0003-2224-6821> ;
    dcterms:created "2025-09-01" .
```

<br>

### Giraffa camelopardalis sec. IUCN 2025

> **Giraffa camelopardalis sec. IUCN 2025**<br>
> &lt; Giraffa camelopardalis sec. Dagg 1971<br>
> &gt; Giraffa camelopardalis camelopardalis sec. Dagg 1971<br>
> &gt; Giraffa camelopardalis antiquorum sec. Dagg 1971<br>
> &gt; Giraffa camelopardalis peralta sec. Dagg 1971<br>
> &gt; Giraffa camelopardalis rothschildi sec. Dagg 1971

<br>

```turtle
# Giraffa camelopardalis sec. IUCN 2025 < Giraffa camelopardalis sec. Dagg 1971
[] a tcs:TaxonConceptMapping ;
    tcs:subjectTaxonConcept _:tc20 ;
    tcs:mappingRelation tcs:isIncludedIn ;
    tcs:objectTaxonConcept _:tc35 ;
    dcterms:creator <https://orcid.org/0000-0003-2224-6821> ;
    dcterms:created "2025-09-01" .

# Giraffa camelopardalis sec. IUCN 2025 > Giraffa camelopardalis camelopardalis sec. Dagg 1971
[] a tcs:TaxonConceptMapping ;
    tcs:subjectTaxonConcept _:tc20 ;
    tcs:mappingRelation tcs:includes ;
    tcs:objectTaxonConcept _:tc36 ;
    dcterms:creator <https://orcid.org/0000-0003-2224-6821> ;
    dcterms:created "2025-09-01" .

# Giraffa camelopardalis sec. IUCN 2025 > Giraffa camelopardalis antiquorum sec. Dagg 1971
[] a tcs:TaxonConceptMapping ;
    tcs:subjectTaxonConcept _:tc20 ;
    tcs:mappingRelation tcs:includes ;
    tcs:objectTaxonConcept _:tc37 ;
    dcterms:creator <https://orcid.org/0000-0003-2224-6821> ;
    dcterms:created "2025-09-01" .

# Giraffa camelopardalis sec. IUCN 2025 > Giraffa camelopardalis peralta sec. Dagg 1971
[] a tcs:TaxonConceptMapping ;
    tcs:subjectTaxonConcept _:tc20 ;
    tcs:mappingRelation tcs:includes ;
    tcs:objectTaxonConcept _:tc38 ;
    dcterms:creator <https://orcid.org/0000-0003-2224-6821> ;
    dcterms:created "2025-09-01" .

# Giraffa camelopardalis sec. IUCN 2025 > Giraffa camelopardalis rothschildi sec. Dagg 1971
[] a tcs:TaxonConceptMapping ;
    tcs:subjectTaxonConcept _:tc20 ;
    tcs:mappingRelation tcs:includes ;
    tcs:objectTaxonConcept _:tc40 ;
    dcterms:creator <https://orcid.org/0000-0003-2224-6821> ;
    dcterms:created "2025-09-01" .
```

<br>

### Giraffa camelopardalis peralta sec. IUCN 2025

> **Giraffa camelopardalis peralta sec. IUCN 2025**<br>
> &lt; Giraffa camelopardalis sec. Dagg 1971<br>
> &cong; Giraffa camelopardalis peralta sec. Dagg 1971

<br>

```turtle
# Giraffa camelopardalis peralta sec. IUCN 2025 < Giraffa camelopardalis sec. Dagg 1971
[] a tcs:TaxonConceptMapping ;
    tcs:subjectTaxonConcept _:tc21 ;
    tcs:mappingRelation tcs:isIncludedIn ;
    tcs:objectTaxonConcept _:tc35 ;
    dcterms:creator <https://orcid.org/0000-0003-2224-6821> ;
    dcterms:created "2025-09-01" .

# Giraffa camelopardalis peralta sec. IUCN 2025 == Giraffa camelopardalis peralta sec. Dagg 1971
[] a tcs:TaxonConceptMapping ;
    tcs:subjectTaxonConcept _:tc21 ;
    tcs:mappingRelation tcs:isCongruentWith ;
    tcs:objectTaxonConcept _:tc38 ;
    dcterms:creator <https://orcid.org/0000-0003-2224-6821> ;
    dcterms:created "2025-09-01" .
```

<br>

### Giraffa camelopardalis antiquorum sec. IUCN 2025

> **Giraffa camelopardalis antiquorum sec. IUCN 2025**<br>
> &lt; Giraffa camelopardalis sec. Dagg 1971<br>
> &cong; Giraffa camelopardalis antiquorum sec. Dagg 1971

<br>

```turtle
# Giraffa camelopardalis peralta sec. IUCN 2025 < Giraffa camelopardalis sec. Dagg 1971
[] a tcs:TaxonConceptMapping ;
    tcs:subjectTaxonConcept _:tc22 ;
    tcs:mappingRelation tcs:isIncludedIn ;
    tcs:objectTaxonConcept _:tc35 ;
    dcterms:creator <https://orcid.org/0000-0003-2224-6821> ;
    dcterms:created "2025-09-01" .

# Giraffa camelopardalis peralta sec. IUCN 2025 == Giraffa camelopardalis antiquorum sec. Dagg 1971
[] a tcs:TaxonConceptMapping ;
    tcs:subjectTaxonConcept _:tc22 ;
    tcs:mappingRelation tcs:isCongruentWith ;
    tcs:objectTaxonConcept _:tc37 ;
    dcterms:creator <https://orcid.org/0000-0003-2224-6821> ;
    dcterms:created "2025-09-01" .
```

<br>

### Giraffa camelopardalis camelopardalis sec. IUCN 2025

> **Giraffa camelopardalis camelopardalis sec. IUCN 2025**<br>
> &lt; Giraffa camelopardalis sec. Dagg 1971<br>
> &gt; Giraffa camelopardalis camelopardalis sec. Dagg 1971<br>
> &gt; Giraffa camelopardalis rothschildi sec. Dagg 1971

<br>

```turtle
# Giraffa camelopardalis camelopardais sec. IUCN 2025 < Giraffa camelopardalis sec. Dagg 1971
[] a tcs:TaxonConceptMapping ;
    tcs:subjectTaxonConcept _:tc23 ;
    tcs:mappingRelation tcs:isIncludedIn ;
    tcs:objectTaxonConcept _:tc35 ;
    dcterms:creator <https://orcid.org/0000-0003-2224-6821> ;
    dcterms:created "2025-09-01" .

# Giraffa camelopardalis camelopardalis sec. IUCN 2025 > Giraffa camelopardalis camelopardalis sec. Dagg 1971
[] a tcs:TaxonConceptMapping ;
    tcs:subjectTaxonConcept _:tc23 ;
    tcs:mappingRelation tcs:includes ;
    tcs:objectTaxonConcept _:tc36 ;
    dcterms:creator <https://orcid.org/0000-0003-2224-6821> ;
    dcterms:created "2025-09-01" .

# Giraffa camelopardalis camelopardalis sec. IUCN 2025 > Giraffa camelopardalis rothschildi sec. Dagg 1971
[] a tcs:TaxonConceptMapping ;
    tcs:subjectTaxonConcept _:tc23 ;
    tcs:mappingRelation tcs:includes ;
    tcs:objectTaxonConcept _:tc40 ;
    dcterms:creator <https://orcid.org/0000-0003-2224-6821> ;
    dcterms:created "2025-09-01" .
```

<br>

### Giraffa reticulata sec. IUCN 2025

> **Giraffa reticulata sec. IUCN 2025**<br>
> &lt; Giraffa camelopardalis sec. Dagg 1971<br>
> &cong; Giraffa camelopardalis reticulata sec. Dagg 1971

<br>

```turtle
# Giraffa reticulata sec. IUCN 2025 < Giraffa camelopardalis sec. Dagg 1971
[] a tcs:TaxonConceptMapping ;
    tcs:subjectTaxonConcept _:tc24 ;
    tcs:mappingRelation tcs:isIncludedIn ;
    tcs:objectTaxonConcept _:tc35 ;
    dcterms:creator <https://orcid.org/0000-0003-2224-6821> ;
    dcterms:created "2025-09-01" .

# Giraffa reticulata sec. IUCN 2025 == Giraffa camelopardalis reticulata sec. Dagg 1971
[] a tcs:TaxonConceptMapping ;
    tcs:subjectTaxonConcept _:tc24 ;
    tcs:mappingRelation tcs:isCongruentWith ;
    tcs:objectTaxonConcept _:tc39 ;
    dcterms:creator <https://orcid.org/0000-0003-2224-6821> ;
    dcterms:created "2025-09-01" .
```

<br>

### Giraffa tippelskirchi sec. IUCN 2025

> **Giraffa tippelskirchi sec. IUCN 2025**<br>
> &lt; Giraffa camelopardalis sec. Dagg 1971<br>
> &gt; Giraffa camelopardalis tippelskirchi sec. Dagg 1971<br>
> &gt; Giraffa camelopardalis thornicrofti sec. Dagg 1971

<br>

```turtle
# Giraffa tippelskirchi sec. IUCN 2025 < Giraffa camelopardalis sec. Dagg 1971
[] a tcs:TaxonConceptMapping ;
    tcs:subjectTaxonConcept _:tc25 ;
    tcs:mappingRelation tcs:isIncludedIn ;
    tcs:objectTaxonConcept _:tc35 ;
    dcterms:creator <https://orcid.org/0000-0003-2224-6821> ;
    dcterms:created "2025-09-01" .

# Giraffa tippelskirchi sec. IUCN 2025 > Giraffa camelopardalis tippelskirchi sec. Dagg 1971
[] a tcs:TaxonConceptMapping ;
    tcs:subjectTaxonConcept _:tc25 ;
    tcs:mappingRelation tcs:includes ;
    tcs:objectTaxonConcept _:tc41 ;
    dcterms:creator <https://orcid.org/0000-0003-2224-6821> ;
    dcterms:created "2025-09-01" .

# Giraffa tippelskirchi sec. IUCN 2025 > Giraffa camelopardalis thornicrofti sec. Dagg 1971
[] a tcs:TaxonConceptMapping ;
    tcs:subjectTaxonConcept _:tc21 ;
    tcs:mappingRelation tcs:includes ;
    tcs:objectTaxonConcept _:tc42 ;
    dcterms:creator <https://orcid.org/0000-0003-2224-6821> ;
    dcterms:created "2025-09-01" .
```

<br>

### Giraffa tippelskirchi tippelskirchi sec. IUCN 2025

> **Giraffa tippelskirchi tippelskirchi sec. IUCN 2025**<br>
> &lt; Giraffa camelopardalis sec. Dagg 1971<br>
> &cong; Giraffa camelopardalis tippelskirchi

<br>

```turtle
# Giraffa tippelskirchi tippelskirchi sec. IUCN 2025 < Giraffa camelopardalis sec. Dagg 1971
[] a tcs:TaxonConceptMapping ;
    tcs:subjectTaxonConcept _:tc26 ;
    tcs:mappingRelation tcs:includes ;
    tcs:objectTaxonConcept _:tc35 ;
    dcterms:creator <https://orcid.org/0000-0003-2224-6821> ;
    dcterms:created "2025-09-01" .

# Giraffa tippelskirchi tippelskirchi sec. IUCN 2025 == Giraffa camelopardalis tippelskirchi sec. Dagg 1971
[] a tcs:TaxonConceptMapping ;
    tcs:subjectTaxonConcept _:tc26 ;
    tcs:mappingRelation tcs:isCongruentWith ;
    tcs:objectTaxonConcept _:tc41 ;
    dcterms:creator <https://orcid.org/0000-0003-2224-6821> ;
    dcterms:created "2025-09-01" .
```

<br>

### Giraffa tippelskirchi thornicrofti sec. IUCN 2025

> **Giraffa tippelskirchi thornicrofti sec. IUCN 2025**<br>
> &lt; Giraffa camelopardalis sec. Dagg 1971<br>
> &cong; Giraffa camelopardalis thornicrofti sec. Dagg 1971

<br>

```turtle
# Giraffa tippelskirchi thornicrofti sec. IUCN 2025 < Giraffa camelopardalis sec. Dagg 1971
[] a tcs:TaxonConceptMapping ;
    tcs:subjectTaxonConcept _:tc27 ;
    tcs:mappingRelation tcs:includes ;
    tcs:objectTaxonConcept _:tc35 ;
    dcterms:creator <https://orcid.org/0000-0003-2224-6821> ;
    dcterms:created "2025-09-01" .

# Giraffa tippelskirchi thornicrofti sec. IUCN 2025 == Giraffa camelopardalis thornicrofti sec. Dagg 1971
[] a tcs:TaxonConceptMapping ;
    tcs:subjectTaxonConcept _:tc27 ;
    tcs:mappingRelation tcs:isCongruentWith ;
    tcs:objectTaxonConcept _:tc42 ;
    dcterms:creator <https://orcid.org/0000-0003-2224-6821> ;
    dcterms:created "2025-09-01" .
```

<br>

### Giraffa giraffa sec. IUCN 2025

> **Giraffa giraffa sec. IUCN 2025**<br>
> &lt; Giraffa camelopardalis sec. Dagg 1971<br>
> &gt; Giraffa camelopardalis angolensis sec. Dagg 1971<br>
> &gt; Giraffa camelopardalis giraffa sec. Dagg 1971<br>

<br>

```turtle
# Giraffa giraffa sec. IUCN 2025 < Giraffa camelopardalis sec. Dagg 1971
[] a tcs:TaxonConceptMapping ;
    tcs:subjectTaxonConcept _:tc28 ;
    tcs:mappingRelation tcs:includes ;
    tcs:objectTaxonConcept _:tc35 ;
    dcterms:creator <https://orcid.org/0000-0003-2224-6821> ;
    dcterms:created "2025-09-01" .

# Giraffa giraffa sec. IUCN 2025 > Giraffa camelopardalis angolensis sec. Dagg 1971
[] a tcs:TaxonConceptMapping ;
    tcs:subjectTaxonConcept _:tc26 ;
    tcs:mappingRelation tcs:includes ;
    tcs:objectTaxonConcept _:tc43 ;
    dcterms:creator <https://orcid.org/0000-0003-2224-6821> ;
    dcterms:created "2025-09-01" .

# Giraffa giraffa sec. IUCN 2025 > Giraffa camelopardalis giraffa sec. Dagg 1971
[] a tcs:TaxonConceptMapping ;
    tcs:subjectTaxonConcept _:tc26 ;
    tcs:mappingRelation tcs:includes ;
    tcs:objectTaxonConcept _:tc44 ;
    dcterms:creator <https://orcid.org/0000-0003-2224-6821> ;
    dcterms:created "2025-09-01" .
```

<br>

### Giraffa giraffa giraffa sec. IUCN 2025

> **Giraffa giraffa giraffa sec. IUCN 2025**<br>
> &gt; Giraffa camelopardalis sec. Dagg 1971<br>
> &cong; Giraffa camelopardalis giraffa sec. Dagg 1971

<br>

```turtle
# Giraffa giraffa giraffa sec. IUCN 2025 < Giraffa camelopardalis sec. Dagg 1971
[] a tcs:TaxonConceptMapping ;
    tcs:subjectTaxonConcept _:tc29 ;
    tcs:mappingRelation tcs:includes ;
    tcs:objectTaxonConcept _:tc35 ;
    dcterms:creator <https://orcid.org/0000-0003-2224-6821> ;
    dcterms:created "2025-09-01" .

# Giraffa giraffa sec. IUCN 2025 == Giraffa camelopardalis giraffa sec. Dagg 1971
[] a tcs:TaxonConceptMapping ;
    tcs:subjectTaxonConcept _:tc29 ;
    tcs:mappingRelation tcs:isCongruentWith ;
    tcs:objectTaxonConcept _:tc44 ;
    dcterms:creator <https://orcid.org/0000-0003-2224-6821> ;
    dcterms:created "2025-09-01" .
```

<br>

### Giraffa giraffa angolensis sec. IUCN 2025

> **Giraffa giraffa angolensis sec. IUCN 2025**<br>
> &gt; Giraffa camelopardalis sec. Dagg 1971<br>
> &cong; Giraffa camelopardalis angolensis sec. Dagg 1971

<br>

```turtle
# Giraffa giraffa angolensis sec. IUCN 2025 < Giraffa camelopardalis sec. Dagg 1971
[] a tcs:TaxonConceptMapping ;
    tcs:subjectTaxonConcept _:tc30 ;
    tcs:mappingRelation tcs:includes ;
    tcs:objectTaxonConcept _:tc35 ;
    dcterms:creator <https://orcid.org/0000-0003-2224-6821> ;
    dcterms:created "2025-09-01" .

# Giraffa giraffa angolensis sec. IUCN 2025 == Giraffa camelopardalis angolensis sec. Dagg 1971
[] a tcs:TaxonConceptMapping ;
    tcs:subjectTaxonConcept _:tc26 ;
    tcs:mappingRelation tcs:isCongruentWith ;
    tcs:objectTaxonConcept _:tc43 ;
    dcterms:creator <https://orcid.org/0000-0003-2224-6821> ;
    dcterms:created "2025-09-01" .
```

<br>

## Full code in GitHub

[TurTLe](https://github.com/tdwg/tcs2/blob/master/recipes/giraffes.ttl) |
[JSON-LD](https://github.com/tdwg/tcs2/blob/master/recipes/giraffes.jsonld) |
[Data Package](https://github.com/tdwg/tcs2/blob/master/recipes/giraffes/datapackage/)
