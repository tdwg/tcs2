```turtle
# Athyriaceae sec. Rothfels et al. 2012 is proper subset of Woodsiaceae sec. Smith et al. 2006
[] a :TaxonRelationship ; 
    :relationshipType tcreltype:isProperSubsetOf ; 
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
        :relationshipType tcreltype:isCongruentWith ; 
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
# Phyllotrox sec. Franz & O'Brien 2001 partially overlaps Phyllotrox sec. Franz 2006
[] a :TaxonRelationship ;
    :relationshipType tcreltype:partiallyOverlaps ;
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
            phylogeny of Perelleschus (Coleoptera: Curculionidae) with notes on its Association with 
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
