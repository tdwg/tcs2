# TaxonConcept accordingTo example 1

```turtle
# Taxonomic article (object of property only)
<https://doi.org/10.1080/14772000.2013.806371> a bibo:AcademicArticle ;
    dcterms:creator <https://orcid.org/0000-0001-7089-7018>,
            <https://orcid.org/0000-0002-2469-8162> ;
    bibo:authorList ( <https://orcid.org/0000-0001-7089-7018> 
        	<https://orcid.org/0000-0002-2469-8162> ) ;
    dcterms:title """Description of two new species and phylogenetic reassessment of 
            Perelleschus O’Brien & Wibmer, 1986 (Coleoptera: Curculionidae), with 
            a complete taxonomic concept history of Perelleschus sec. Franz & 
            Cardona-Duque, 2013""" ;
    bibo:shortTitle """Description of two new species and phylogenetic reassessment 
            of Perelleschus O’Brien & Wibmer, 1986 (Coleoptera""" ;
    dcterms:isPartOf [ a bibo:Issue ;
        dcterms:date "June 1, 2013" ;
        dcterms:isPartOf [ a bibo:Journal ;
                dcterms:title "Systematics and Biodiversity" ;
                bibo:issn "1477-2000" ] ;
                dcterms:publisher [ a foaf:Organization ;
                    foaf:name "Taylor & Francis" ] ;
            bibo:volume "11" ;
            bibo:issue "2" ] ;
    bibo:pages "209-236" ;
    bibo:doi "10.1080/14772000.2013.806371" ;
    bibo:uri "https://doi.org/10.1080/14772000.2013.806371" .

<https://orcid.org/0000-0001-7089-7018> a foaf:Person ;
    foaf:givenName "Nico M." ;
    foaf:surname "Franz" .

<https://orcid.org/0000-0002-2469-8162> a foaf:Person ;
    foaf:givenName "Juliana" ;
    foaf:surname "Cardona-Duque*" .
```

[&lsqb;TaxonConcept-accordingTo-example-1.ttl&rsqb;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonConcept-accordingTo-example-1.ttl)&nbsp;[&lsqb;TaxonConcept-accordingTo-example-1.jsonld&rsqb;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonConcept-accordingTo-example-1.jsonld)

