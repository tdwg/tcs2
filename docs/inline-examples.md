# Inline examples

## Taxon Concept

Taxonomic treatment:

```turtle
ex:taxon-concept/1 a :TaxonConcept ;
    skos:prefLabel "Dicranoloma blumei sec. Klazenga 1999" ;
    :taxonName [ <https://www.tropicos.org/name/35121475> a :TaxonName ;
            :taxonNameString "Dicranoloma blumei" ;
            dwc:scientificNameAuthorship "(Nees) Renauld" ] ;
    :accordingTo [ <https://www.tropicos.org/reference/9020903> a bibo:AcademicArticle ;
            dcterms:bibliographicCitation "Klazenga, N. (1999). A revision of the Malesian 
                    species of Dicranoloma (Dicranaceae, Musci). Journal of the Hattori
                    Botanical Laboratory 87: 1-130" ] .
```

Field guide:

```turtle
ex:taxon-concept/3 a :TaxonConcept ;
        skos:prefLabel "Orthetrum caledonicum sec. Theischinger and Hawking 2010" ;
        :taxonName [ a :TaxonName ; 
                :taxonNameString "Orthetrum caledonicum" ] ;
        :vernacularName [ a :TaxonName ;
                :taxonNameString "Blue Skimmer" ] ;
        :accordingTo [ <urn:isbn:978-0-643-09073-6> a bibo:Book ;
                dcterms:bibliographicCitation "Theischinger, G.; Hawking, J. (2010). The 
                        complete field guide to dragonflies of Australia. CSIRO Publishing, 
                        Collingwood, Australia" ] .

```

Checklist:

```turtle
ex:taxon-concept/2 a :TaxonConcept ;
    skos:prefLabel "Calymperes moluccense sec. Yong et al. 2013" ;
    :taxonName [ <https://www.tropicos.org/name/35153806> a :TaxonName ;
            :taxonNameString "Calymperes moluccense" ;
            dwc:scientificNameAuthorship "Schwägr." ] ;
    :accordingTo [ <urn:isbn:978-967-5221-99-6> a bibo:Book ;
            dcterms:bibliographicCitation "Yong, K.T.; Tan, B.C.; Ho, B.C.; Ho, Q.Y.; Mohamed, H.
                    A revised Moss Checklist of Peninsular Malaysia and Singapore. Research 
                    Pamphlet no. 133, Forest Research Institute Malaysia, Kepong, Malaysia" ] .
```

### synonym

```turtle
[] a :TaxonConcept ;
    skos:prefLabel "Hebe imbricata sec. Bayly & Kellow 2006" ;
    :taxonName [ <https://www.ipni.org/n/989261-1> a :TaxonName ;
            :taxonNameString "Hebe imbricata" ;
            dwc:scientificNameAuthorship "Cockayne & Allen" ;
            dwc:namePublishedIn "Trans. & Proc. New Zealand Inst. lvii. 42 (1927) (1927)" ] ;
    :synonym [ <https://www.ipni.org/n/812507-1> a :TaxonName ;
            :taxonNameString "Veronica poppelwellii" ;
            dwc:scientificNameAuthorship "Cockayne" ; 
            dwc:namePublishedIn "Trans. & Proc. New Zealand Inst. 1915, xlviii. 200 (1916)"] ;
    :accordingTo [ <urn:isbn:978-0-909010-12-6> a bibo:Book ;
            dcterms:bibliographicCitation "Bayly, M.; Kellow, A. (2006). An illustrated guide to 
                    New Zealand Hebes. Te Papa Press, Wellington, New Zealand" ] .
```

### vernacularName
```turtle
[] a :TaxonConcept ;
    skos:prefLabel "Graphium macleayanum sec. Orr & Kitching 2010"
    :taxonName [ a :TaxonName ;
            :taxonNameString "Graphium macleayanum" ]
    :vernacularName [ a TaxonName ;
            :taxonNameString "Macleay's Swallowtail" ] ;
    :accordingTo [ <978-1-74175-108-6> a bibo:Book ; 
            dcterms:bibliographicCitation "Orr, A. & Kitching, R. The butterflies of Australia. 
                    Jacana Books, Crows Nest, Australia" ].
```

```turtle
[] a :TaxonConcept ;
    skos:prefLabel "Quercus robur sec. Duistermaat 2020" ;
    :taxonName [ <https://www.ipni.org/n/304293-2> a :TaxonName ;
            :taxonNameString "Quercus robur" ] ;
    :vernacularName [ a :TaxonName ;
            :taxonNameString "Zomereik" ] ;
    :accordingTo [ <urn:isbn:978-90-01-58956-1> a bibo:Book ;
            dcterms:bibliographicCitation "Duistermaat, H. (2020). Heukels Flora van Nederland. 
            Noordhoff, Groningen" ] .
```
## Taxon Relationship

```turtle
# Athyriaceae sec. Rothfels et al. 2012 is proper subset of Woodsiaceae sec. Smith et al. 2006
[] a :TaxonRelationship ; # isProperSubsetOf
    :relationshipType <http://rs.tdwg.org/tcs-taxon-concept-relationship-type/values/rt003> ; 
    :subjectTaxonConcept [ a :TaxonConcept ; 
            skos:prefLabel "Athyriaceae sec. Rothfels et al. 2012" ;
            :taxonName [ a :TaxonName ;
                    :taxonNameString "Athyriaceae" ] ;
            :accordingTo <https://doi.org/10.1002/tax.613003> ] ;
    :objectTaxonConcept [ a :TaxonConcept ;
            skos:prefLabel "Woodsiaceae sec. Smith et al. 2006" ;
            :taxonName [ a :TaxonName ;
                    :taxonNameString "Woodsiaceae" ] ;
            :accordingTo <https://doi.org/10.2307/25065646> ] ;
    :relationshipAccordingTo <https://doi.org/10.1002/tax.613003> .

<https://doi.org/10.1002/tax.613003> a bibo:AcademicArticle ;
    dcterms:bibliographicCitation "Rothfels, Carl J.; Sundue, Michael A.; Kuo, Li-Yaung; Larsson, 
            Anders; Kato, Masahiro; Schuettpelz, Eric; Pryer, Kathleen M. (2012). A revised 
            family–level classification for eupolypod II ferns (Polypodiidae: Polypodiales). Taxon 
            61(3): 515-533." .

<https://doi.org/10.2307/25065646> a bibo:AcademicArticle ;
    dcterms:bibliographicCitation "Smith, Alan R.; Pryer, Kathleen M.; Schuettpelz, Eric; Korall, 
            Petra; Schneider, Harald; Wolf, Paul G. (2006). A classification for extant ferns. Taxon 
            55(3): 705-731." .
```

```turtle
# Dicranum fuscescens sec. Koperski et al. 2000 is congruent with Dicranum fuscescens sec. Corley 
# et al. 1981
[] a :TaxonRelationship ;
        :relationshipType <http://rs.tdwg.org/tcs-taxon-concept-relationship-type/values/rt001> ; 
        :subjectTaxonConcept [ a :TaxonConcept ;
                skos:prefLabel "Dicranum fuscescens sec. Koperski et al. 2000" ;
                :taxonName <https://www.tropicos.org/name/35122385> ;
                :accordingTo <https://www.tropicos.org/reference/9022656> ] ;
        :objectTaxonConcept [ a :TaxonConcept ;
                skos:prefLabel "Dicranum fuscescens sec. Corley et al. 1981" ;
                :taxonName <https://www.tropicos.org/name/35122385> ;
                :accordingTo <https://www.tropicos.org/reference/9004554> ] ;
        :raletionshipAccordingTo <https://www.tropicos.org/reference/9022656> .

<https://www.tropicos.org/name/35122385> a :TaxonName ;
    :taxonNameString "Dicranum fuscescens" ;
    dwc:scientificNameAuthorship "Turner" .        

<https://www.tropicos.org/reference/9022656> a bibo:Book ;
    dcterms:bibliographicCitation "Koperski, Monika; Sauer, Michael; Braun, Walter; Gradstein, S. 
            Rob (2000). Referenzliste der Moose Deuthschlands. Schriftenreihe für Vegetationskunde 
            34. Bundersamt für Naturschutz, Bonn-Bad Godesberg." .

<https://www.tropicos.org/reference/9004554> a bibo:AcademicArticle ;
    dcterms:bibliographicCitation "Corley, M.F.V.; Crundwell, A.C.; Düll, R.; Hill, M.O.; Smith, 
    A.J.E. (1981). Mosses of Europe and the Azores; an annotated list of species, with synonyms from 
    the recent literature. Journal of Bryology 11(4): 609-689." .
```

```turtle
# Phyllotrox sec. Franz & O'Brien 2001 overlaps Phyllotrox sec. Franz 2006
[] a :TaxonRelationship ;
    :relationshipType <http://rs.tdwg.org/tcs-taxon-concept-relationship-type/values/rt001> ;
    :subjectTaxonConcept [ a :TaxonConcept ;
            skos:prefLabel "Phyllotrox sec. Franz & O'Brien 2001" ;
            :taxonName _:n1 ;
            :accordingTo <https://www.jstor.org/stable/25078744> ] ;
    :objectTaxonConcept [ a :TaxonConcept ; 
            skos:prefLabel "Phyllotrox sec. Franz 2006" ;
            :taxonName _:n1 ;
            :accordingTo <https://doi.org/10.1111/j.1365-3113.2005.00308.x> ] ;
    :relationshipAccordingTo <https://doi.org/10.1111/cla.12042> .

_:n1 a :TaxonName ;
    :taxonNameString "Phyllotrox" ;
    dwc:scientificNameAuthorship "Schoenherr" .

<https://www.jstor.org/stable/25078744> a bibo:AcademicArticle ;
    dcterms:bibliographicCitation "Franz, Nico M.; O`Brien, Charles W. (2001). Revision and 
            Phylogeny of Perelleschus (Coleoptera: Curculionidae) with Notes on Its Association with 
            Carludovica (Cyclanthaceae). Transactions of the American Entomological Society 127(2): 
            255-287" .

<https://doi.org/10.1111/j.1365-3113.2005.00308.x> a bibo: AcademicArticle ;
    dcterms:bibliographicReference "Franz, Nico M. (2006). Towards a phylogenetic system of 
            derelomine flower weevils (Coleoptera: Curculionidae). Systematic Entomology 31(2): 
            220-287." .

<https://doi.org/10.1111/cla.12042> a bibo:AcademicArticle ;
    dcterms:bibliographicCitation "Franz, Nico M. (2014). Anatomy of a cladistic analysis. 
            Cladistics 30(3): 294-321." .
```

## Taxon Name

```turtle
<urn:lsid:zoobank.org:act:355AAA50-D89F-466E-A216-96B7A17D5AD4> a :TaxonName ;
    :taxonNameString "Carabus nitens"
    dwc:scientificNameAuthorship "Linnaeus, 1758" .
```

```turtle
<https://www.ipni.org/n/316069-1> a :TaxonName ;
    :taxonNameString "Rafflesia arnoldii" ;
    dwc:scientificNameAuthorship "R.Br." ;
    dwc:namePublishedIn "Account Rafflesia 7, tt. 15-22 (1821)" .
```

```turtle
<http://www.indexfungorum.org/names/NamesRecord.asp?RecordID=178962> a :TaxonName ;
    :taxonNameString "Amanita phalloides" ;
    dwc:scientificNameAuthorship "(Vaill. ex Fr.) Link" ;
    dwc:namePublishedIn "Handb. Erk. Gew. 3: 272 (1833)" .
```

### basionym

```turtle
<https://id.biodiversity.org.au/name/apni/166271> a TaxonName ;
    rdf:seeAlso <https://www.ipni.org/n/17571690-1> ;
    :taxonNameString "Doodia australis" ;
    dwc:scientificNameAuthorship "(Parris) Parris" ;
    dwc:namePublishedIn "Fl. Australia 48: 710 (1998)" ;
    :basionym [ <https://id.biodiversity.org.au/name/apni/117170> a :TaxonName ;
            rdf:seeAlso <https://www.ipni.org/n/17567870-1> ;
            :taxonNameString "Doodia media subsp. australis" ;
            dwc:scientificNameAuthorship "Parris" ;
            dwc:namePublishedIn "New Zealand J. Bot. 10(4): 593 (1972)" ] .
```
