# Example 3

## Rhododendron example from TCS 1

This example stays as close as possible in TCS 2 to the example of TCS 1, so 
looks a bit different from other examples.

The example illustrates nicely how the handling of taxon relationships in TCS 2 
differs from TCS 1.

### Horizontal relationships

Horizontal or topological relationships were categorised as 'set relationships' 
in TCS 1. They are handled the same in TCS 2 as they were in TCS 1. In fact, 
they are the only relationship types we've kept in the Taxon Concept 
Relationship (Taxon Relationship Assertion in TCS 1). Only difference is that in 
TCS 1 they could be either in a Taxon Relationship element nested in a Taxon 
Concept element or in a Taxon Relationship Assertion element outside the Taxon 
Concept, while in TCS 2 they can only be in a Taxon Concept Relationship object. 
This makes all Taxon Concept Relationships third-party assertions, even though 
two of the three parties can be the same party.

So, TCS 1:

```xml
<TaxonConcept id="3">
    <Name scientific="true" ref="6">Azalea schlippenbachii (Maxim.) Kuntze</Name>
    <AccordingTo>
        <Simple>Kuntze (1891)</Simple>
    </AccordingTo>
    <TaxonRelationships>
        <TaxonRelationship type="is congruent to">
            <ToTaxonConcept ref="2"/>
        </TaxonRelationship>
    </TaxonRelationships>
</TaxonConcept>
```

in TCS 2 becomes:

```json
[
  {
    "@id": "ex_tc:3.3",
    "@type": "TaxonConcept",
    "skos:prefLabel": "Azalea schlippenbachii sec. Kuntze 1891",
    "taxonName": "ipni:326933-1",
    "accordingTo": "ex_ref:3.4"
  },
  {
    "@id": "ex_tc:3.2",
    "@type": "TaxonConcept",
    "skos:prefLabel": "Rhododendron schlippenbachii sec. Judd & Kron 1995",
    "taxonName": "ipni:333307-1",
    "accordingTo": "ex_ref:3.4",
    "parent": "ex_tc:3.1"
  },
  {
    "@id": "ex_tr:3.1",
    "@type": "TaxonConceptRelationship",
    "relationshipType": "tcs-reltype:rt001",
    "subjectTaxonConcept": "ex_tc:3.3",
    "objectTaxonConcept": "ex_tc:3.2",
    "relationshipAccordingTo": "ex_ref:3.4"
  }
]
```

### Hierarchical relationships

We consider that the 'according to' for hierachical relationships is always the same as that of the (subject) Taxon Concept. Therefore, he hierarchical relationships in TCS 1 have been replaced by a `parent` property on the Taxon Concept.

So, in the example, TCS 1:

```xml
<TaxonConcept id="1">
    <Name scientific="true" linkType="local" ref="2">Rhododendron sect. Sciadorhodion Rehder
        &amp; Wilson</Name>
    <Rank code="sect">Section</Rank>
    <AccordingTo>
        <Simple>Judd &amp; Kron (1995)</Simple>
        <AccordingToDetailed>
            <PublishedIn linkType="local" ref="4">Judd &amp; Kron (1995) A Revision of
                Rhododendron VI </PublishedIn>
            <MicroReference>Page 13-14</MicroReference>
        </AccordingToDetailed>
    </AccordingTo>
    <TaxonRelationships>
        <TaxonRelationship type="is parent taxon of">
            <ToTaxonConcept linkType="local" ref="2"/>
        </TaxonRelationship>
    </TaxonRelationships>
</TaxonConcept>
<TaxonConcept id="2">
    <Name scientific="true" linkType="local" ref="5">Rhododendron schlippenbachii Maxim.</Name>
    <AccordingTo>
        <Simple>Judd &amp; Kron (1995)</Simple>
        <AccordingToDetailed>
            <PublishedIn linkType="local" ref="4"/>
            <MicroReference>Page 15</MicroReference>
        </AccordingToDetailed>
    </AccordingTo>
    <TaxonRelationships>
        <TaxonRelationship type="is child taxon of">
            <ToTaxonConcept ref="1">Rhododendron sect. Sciadorhodion Rehder &amp;
            Wilson</ToTaxonConcept>
        </TaxonRelationship>
    </TaxonRelationships>
</TaxonConcept>
```

In TCS 2 becomes:

```json
[
  {
    "@id": "ex_tc:3.1",
    "@type": "TaxonConcept",
    "skos:prefLabel": "Rhododendron sect. Sciadorhodion sec. Judd & Kron 1995",
    "taxonName": "ipni:50985479-1",
    "accordingTo": "ex_ref:3.4",
    "taxonomicRank": "gbif-rank:section"
  },
  {
    "@id": "ex_tc:3.2",
    "@type": "TaxonConcept",
    "skos:prefLabel": "Rhododendron schlippenbachii sec. Judd & Kron 1995",
    "taxonName": "ipni:333307-1",
    "accordingTo": "ex_ref:3.4",
    "parent": "ex_tc:3.1"
  }
]
```

### Synonyms

Synonyms are not taxonomic relationships at all, but are about applying labels 
to things. The documentation for the `has synonym` relationship type in the TCS 
XML Schema says as much:

> This is an ambiguous relationship. It can mean: 1) a nomenclatural 
relationship where all that is implied is that the type of the target concept is 
included in the current circumscription. This is more precisely expressed as a 
SpecimenCircumscription (for heterotypic synonyms) or as TaxonName basionym 
relationships (for homotypic synonyms) 2) a concept relationship where some 
part of (or all of) the target concept is included in the current 
circumscription. This is more precisely expressed using the set relationships 
such as 'is congruent to'. This is intended for handling legacy data.

The `has synonym` relationships in the example, as behoves all synonyms, fall in 
the first category.

#### Homotypic synonyms

TCS 2 deals with homotypic synonyms the same way as TCS 1, namely through the 
`basionym` and `replacementNameFor` properties on the Taxon Name object.

TCS 1:

```xml
<TaxonName id="9" nomenclaturalCode="Botanical">
    <Simple>Rhododendron pentaphyllum var. nikoense Komatsu</Simple>
    <Rank code="var">variety</Rank>
    <CanonicalName>
        <Simple>Rhododendron pentaphyllum var. nikoense</Simple>
        <Genus ref="0">Rhododendron</Genus>
        <SpecificEpithet>pentaphyllum</SpecificEpithet>
        <InfraspecificEpithet>nikoense</InfraspecificEpithet>
    </CanonicalName>
    <CanonicalAuthorship>
        <Simple>Konatsu</Simple>
    </CanonicalAuthorship>
    <PublishedIn>Icon. Pl. Koisikav. 3: 45, t 168 (1916)</PublishedIn>
</TaxonName>
<TaxonName id="10" nomenclaturalCode="Botanical">
    <Simple>Rhododendron nikoense (Komatsu) Nakai</Simple>
    <Rank code="sp">Species</Rank>
    <CanonicalName>
        <Simple>Rhododendron nikoense</Simple>
        <Genus ref="0">Rhododendron</Genus>
        <SpecificEpithet>nikoense</SpecificEpithet>
    </CanonicalName>
    <CanonicalAuthorship>
        <Simple>(Komatsu) Nakai</Simple>
        <BasionymAuthorship>
            <Simple>Komatsu</Simple>
        </BasionymAuthorship>
        <CombinationAuthorship>
            <Simple>Nakai</Simple>
        </CombinationAuthorship>
    </CanonicalAuthorship>
    <PublishedIn>Nakai &amp; Koidz. Trees and Shrubs Japan 1: 68 (1922)</PublishedIn>
    <Basionym>
        <RelatedName ref="9">Rhododendron pentaphyllum var. nikoense</RelatedName>
    </Basionym>
</TaxonName>
```

TCS 2:

```json
[
  {
    "@id": "ex_tn:3.9",
    "@type": "TaxonName",
    "nomenclaturalCode": "gbif-code:ICN",
    "taxonomicNameString": "Rhododendron pentaphyllum var. nikoense",
    "dwc:scientificNameAuthorship": "Komatsu",
    "taxonomicRank": "gbif-rank:variety",
    "dwc:genericName": "Rhododendron",
    "dwc:specificEpithet": "pentaphyllum",
    "dwc:infraspecificEpithet": "nikoense",
    "dwc:namePublishedIn": "Icon. Pl. Koisikav. 3: 45, t 168 (1916)"
  },
  {
    "@id": "ipni:332955-1",
    "@type": "TaxonName",
    "nomenclaturalCode": "gbif-code:ICN",
    "taxonomicNameString": "Rhododendron nikoense",
    "dwc:scientificNameAuthorship": "(Komatsu) Nakai",
    "taxonomicRank": "gbif-rank:species",
    "dwc:genericName": "Rhododendron",
    "dwc:specificEpithet": "nikoense",
    "dwc:namePublishedIn": "Nakai &amp; Koidz. Trees and Shrubs Japan 1: 68 (1922)",
    "basionym": "ex_tn:3.0"
  }
]
```

#### Heterotypic synonyms

Of heterotypic synonyms TCS says that they are better expessed as a 
`SpecimenCircumscription`. We do not disagree, but if this is the case for 
synonyms, it is the case for the accepted name as well. When types of more than 
one name fall within the circumscription of a Taxon Concept, it is only 
nomenclatural business rules that decide which name is the accepted name and 
which names are synonyms. Therefore synonyms should be treated the same way as 
the accepted name (`taxonName`), i.e. as a property (`synonym`) of a Taxon Name.

So, what in TCS 1 looks like this:

```xml
<TaxonConcept id="4">
    <Name scientific="true" ref="7">Rhododendron pentaphyllum Maxim.</Name>
    <AccordingTo>
        <Simple>Judd &amp; Kron (1995)</Simple>
    </AccordingTo>
    <TaxonRelationships>
        <!-- relationships linking to taxonconcept without any descriptive string -->
        <TaxonRelationship type="has synonym">
            <ToTaxonConcept ref="6"/>
        </TaxonRelationship>
        <TaxonRelationship type="has synonym">
            <ToTaxonConcept ref="7"/>
        </TaxonRelationship>
        <!-- relationship with linking reference to another taxon concept and string description of concept -->
        <TaxonRelationship type="has synonym">
            <ToTaxonConcept ref="8">Rhododendron pentaphyllum var. nikoense
            Komatsu</ToTaxonConcept>
        </TaxonRelationship>
        <!-- relationships without linking -->
        <TaxonRelationship type="has synonym">
            <ToTaxonConcept>Rhododendron pentaphyllum Maxim. var. shikokianum T.
            Yamazaki</ToTaxonConcept>
        </TaxonRelationship>
        <TaxonRelationship type="has synonym">
            <ToTaxonConcept>Rhododendron quinquefolium Bisset &amp; S. Moore var. roseum
                Rehder</ToTaxonConcept>
        </TaxonRelationship>
    </TaxonRelationships>
</TaxonConcept>
<TaxonConcept id="6">
    <Name scientific="true">Rhododendron nikoense (Komatsu) Nakai</Name>
</TaxonConcept>
<TaxonConcept id="7">
    <Name scientific="true" ref="10">Rhododendron nikoense (Komatsu) Nakai</Name>
</TaxonConcept>
<TaxonConcept id="8">
    <Name scientific="true" ref="9">Rhododendron pentaphyllum var. nikoense Komatsu</Name>
</TaxonConcept>
```

in TCS 2 becomes:

```json
{
  "@id": "ex_tc:3.4",
  "@type": "TaxonConcept",
  "skos:prefLabel": "Rhododendron pentaphyllum sec. Judd & Kron 1995",
  "taxonName": "ipni:333062-1",
  "accordingTo": "ex_ref:3.4",
  "synonyms": {
    "@list": [
      "ipni:332955-1",
      "ex_tn:3.9",
      "ipni:950666-1",
      "ex_tn:3.11"
    ]
  }
}
```

Note also that, even though TCS does not prescribe it, synonyms here are names, 
not taxon concepts, again as behoves synonyms. This saves one from having to 
create spurious nominal concept records – like the Taxon Concepts with ids 6 to 
8 in the TCS 1 code snippet. Also, it makes that accepted names (`taxonName`) 
and synonyms (`synonym`) have the same realtionship to the Taxon Concept.

### Full examples

[TCS 1](https://github.com/tdwg/tcs/blob/master/TCS101/example_v101.xml) • [TCS 2 JSON-LD](example3.jsonld) • [TCS 2 Turtle](example3.ttl)
