# TaxonConcept synonym example 1


**Term:** [tcs:synonym](/terms/#tcs_synonym)

TaxonConcept-synonym-example-1 | [TaxonConcept-synonym-example-2](./TaxonConcept-synonym-example-2.html) | [TaxonConcept-synonym-example-3](./TaxonConcept-synonym-example-3.html)
```turtle
[]  a tcs:TaxonConcept ;
    dcterms:title "Dicranoloma blumei sec. Klazenga 1999" ;
    tcs:accordingTo <https://www.tropicos.org/reference/9020903> ;
    tcs:taxonName <https://www.tropicos.org/name/35121475> ;
    tcs:synonym <https://www.tropicos.org/name/35121973> , 
            <https://www.tropicos.org/name/35121477> ,
            <https://www.tropicos.org/name/35121484> ,
            <https://www.tropicos.org/name/35188177> .

<https://www.tropicos.org/name/35121475> a tcs:TaxonName ;
    tcs:nameString "Dicranoloma blumei" ;
    dwc:scientificNameAuthorship "(Nees) Renauld" ;
    dwc:namePublishedIn "Rev. Bryol. 28(4): 69 (1901)" ;
    tcs:basionym <https://www.tropicos.org/name/35121972> .

<https://www.tropicos.org/name/35121972> a tcs:TaxonName ;
    tcs:nameString "Dicranum blumei" ;
    dwc:scientificNameAuthorship "Nees" ; 
    dwc:namePublishedIn """Nova Acta Phys.-Med. Acad. Caes. Leop.-Carol. Nat. 
            Cur. 11(1): 131 (1823)""" .

<https://www.tropicos.org/name/35154856> a tcs:TaxonName ;
    tcs:nameString "Leucoloma blumei" ;
    dwc:scientificNameAuthorship "(Nees) Broth." ; 
    dwc:namePublishedIn "Nat. Pflanzenfam. I(3): 322 (1901)" ;
    tcs:basionym <https://www.tropicos.org/name/35121972> .

<https://www.tropicos.org/name/35121973> a tcs:TaxonName ;
    tcs:nameString "Dicranum blumei var. laxifolium" ;
    dwc:scientificNameAuthorship "Broth. & Geh." ;
    dwc:namePublishedIn "Biblioth. Bot. 44: 4 (1898)" .

<https://www.tropicos.org/name/35121477> a tcs:TaxonName ;
    tcs:nameString "Dicranoloma blumei var. papillisetum" ;
    dwc:scientificNameAuthorship "M. Fleisch." ;
    dwc:namePublishedIn "Nova Guinea 12(2): 112 (1914)" .

<https://www.tropicos.org/name/35188177> a tcs:TaxonName ;
    tcs:nameString "Dicranoloma blumei f. subintegrum" ;
    dwc:scientificNameAuthorship "Dixon" ;
    dwc:namePublishedIn "J. Bot. 80: 4 (1942)" .

<https://www.tropicos.org/name/35121484> a tcs:TaxonName ;
    tcs:nameString "Dicranoloma braunfelsioides" ;
    dwc:scientificNameAuthorship "Herzog" ;
    dwc:namePublishedIn "Hedwigia 61: 288 (1919)" . 

<https://www.tropicos.org/reference/9020903> a bibo:AcademicArticle ;
    dcterms:bibliographicCitation """Klazenga, N. (1999). A revision of the 
            Malesian species of Dicranoloma (Dicranaceae, Musci). Journal of the 
            Hattori Botanical Laboratory 87: 1-130.""" .

# Example shows both homotypic and heterotypic synonyms:
# 
# Dicranoloma blumei, Dicranum blumei and Leucoloma blumei are homotypic 
# synonyms and are linked through the basionym (Dicranum blumei is the basionym 
# of Dicranoloma blumei and Leucoloma blumei).
# 
# Dicranum blumei var. laxifolium, Dicranoloma blumei var. papillisetum, 
# Dicranoloma braunfelsioides and Dicranoloma blumei f. subintegrum are 
# heterotypic synonyms of Dicranoloma blumei (according to this publication) and 
# are provided using the `synonym` property.
```

[&#91;TaxonConcept-synonym-example-1.ttl&#93;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonConcept-synonym-example-1.ttl)&nbsp;[&#91;TaxonConcept-synonym-example-1.jsonld&#93;](https://github.com/tdwg/tcs2/blob/master/examples/TaxonConcept-synonym-example-1.jsonld)

