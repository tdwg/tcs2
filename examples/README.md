# Examples

### Revision of Rhododendron subg. Pentanthera

This is the example that shipped with TCS 1. It is based on a revision of 
_Rhododendron_ subg. _Pentanthera_ by Judd & Kron [\[judd_revision_1995\]](../docs/bibliography/#judd_revision_1995).

[TurTLe](https://github.com/tdwg/tcs2/blob/master/examples/rhododendron-subg-pentanthera.ttl) |
[JSON-LD](https://github.com/tdwg/tcs2/blob/master/examples/rhododendron-subg-pentanthera.jsonld)

### Begonia sect. Mezierea in Klazenga & al. (1994)

[TurTLe](https://github.com/tdwg/tcs2/blob/master/examples/begonia-sect-mezierea-sec-klazenga-1993.ttl) |
[JSON-LD](https://github.com/tdwg/tcs2/blob/master/examples/begonia-sect-mezierea-sec-klazenga-1993.jsonld)

### Treatments of Malesian Dicranoloma in Tropicos

This example compares five treatments of Malesian Dicranoloma (Bryophyta, 
Dicranaceae) based on data obtained from [Tropicos](https://tropicos.org). 
Tropicos has taxon concepts (in the References tab on the Name pages) but does 
not expose IDs for them. Therefore Taxon Concept IDs have been made up by adding 
a hash with the Name ID to the URLs of the references.

Tropicos does not generally have nomenclatural types. Therefore type information 
is taken from the latest treatment by Klazenga \[[klazenga_revision_1999](../docs/bibliography/#klazenga_revision_1999)\]. 
In the JSON-LD, types are nested within the Taxon Name objects by reversing the 
`typifiedName` property.

[TurTLe](https://github.com/tdwg/tcs2/blob/master/examples/tropicos-malesian-dicranoloma.ttl) |
[JSON-LD](https://github.com/tdwg/tcs2/blob/master/examples/tropicos-malesian-dicranoloma.jsonld)

Based on the data from Tropicos (and some knowledge of the group), third-party 
taxon concept mappings can be created. The following example maps the concepts 
from the treatment by Klazenga to the concepts in the other four treatments:

[TurTLe](https://github.com/tdwg/tcs2/blob/master/examples/tropicos-malesian-dicranoloma-annotations.ttl) |
[JSON-LD](https://github.com/tdwg/tcs2/blob/master/examples/tropicos-malesian-dicranoloma-annotations.jsonld)

### Euphrasia gibbsiae sec. Barker 1982

[TurTLe](https://github.com/tdwg/tcs2/blob/master/examples/euphrasia_gibbsiae_sec_barker_1982.ttl) |
[JSON-LD](https://github.com/tdwg/tcs2/blob/master/examples/euphrasia_gibbsiae_sec_barker_1982.jsonld)

### Amblystegiaceae in Koperski & al. (2000)

[TurTLe](https://github.com/tdwg/tcs2/blob/master/examples/amblystegium-sec-koperski-et-al.ttl) |
[JSON-LD](https://github.com/tdwg/tcs2/blob/master/examples/amblystegium-sec-koperski-et-al.jsonld)

With embedded Taxon Concept Mappings:

[TurTLe](https://github.com/tdwg/tcs2/blob/master/examples/amblystegium-sec-koperski-et-al-embedded.ttl) |
[JSON-LD](https://github.com/tdwg/tcs2/blob/master/examples/amblystegium-sec-koperski-et-al-embedded.jsonld)

### Circus cyaneus and Circus hudsonianus in Avibase

[TurTLe](https://github.com/tdwg/tcs2/blob/master/examples/avibase-circus-cyaneus-hudsonius.ttl) |
[JSON-LD](https://github.com/tdwg/tcs2/blob/master/examples/avibase-circus-cyaneus-hudsonius.jsonld)

### Eupolypods in Rothfels & al. (2012)

[TurTLe](https://github.com/tdwg/tcs2/blob/master/examples/eupolypods-rothfels-2012.ttl) |
[JSON-LD](https://github.com/tdwg/tcs2/blob/master/examples/eupolypods-rothfels-2012.jsonld)

### Megalorhipida leucodactylus in Catalogue of Life

[TurTLe](https://github.com/tdwg/tcs2/blob/master/examples/megalorhipida-leucodactylus-sec-gielis-et-hobern-2020.ttl) |
[JSON-LD](https://github.com/tdwg/tcs2/blob/master/examples/megalorhipida-leucodactylus-sec-gielis-et-hobern-2020.jsonld)


## Interface with occurrence/specimen data 

TCS interfaces with Darwin Core occurrence data through identifications and nomenclatural type designations.

### Identifications

Taxon concepts are related to identifications through the `dwciri:toTaxon`
property on the `dwc:Identification`. 

Identification-toTaxon-example-1: [TurTLe](https://github.com/tdwg/tcs2/blob/master/examples/Identification-toTaxon-example-1.ttl) |
[JSON-LD](https://github.com/tdwg/tcs2/blob/master/examples/Identification-toTaxon-example-1.jsonld)

### Nomenclatural types

In the following examples we link a `tcs:NomenclaturalType` to a
`dwc:PreservedSpecimen` with the `dwciri:typeStatus` property, which we consider
the inverse of the `tcs:typeSpecimen` property of the `tcs:NomenclaturalType`.
Elsewhere, e.g. in the [Rhododendron subg. penthantera example from TCS
1](https://github.com/tdwg/tcs2/blob/master/examples/rhododendron-subg-pentanthera.ttl#L178-L187),
we also use the `dwc:MaterialCitation` class in relation to nomenclatural types,
but only as the object of `tcs:typeSpecimen`, so as part of the typification of
a name, and never with `dcw:typeStatus` as the type status of a specimen.

PreservedSpecimen-typeStatus-example-1:
[TurTLe](https://github.com/tdwg/tcs2/blob/master/examples/PreservedSpecimen-typeStatus-example-1.ttl)
|
[JSON-LD](https://github.com/tdwg/tcs2/blob/master/examples/PreservedSpecimen-typeStatus-example-1.jsonld)

PreservedSpecimen-typeStatus-example-2:
[TurTLe](https://github.com/tdwg/tcs2/blob/master/examples/PreservedSpecimen-typeStatus-example-2.ttl)
|
[JSON-LD](https://github.com/tdwg/tcs2/blob/master/examples/PreservedSpecimen-typeStatus-example-2.jsonld)

PreservedSpecimen-typeStatus-example-3:
[TurTLe](https://github.com/tdwg/tcs2/blob/master/examples/PreservedSpecimen-typeStatus-example-3.ttl)
|
[JSON-LD](https://github.com/tdwg/tcs2/blob/master/examples/PreservedSpecimen-typeStatus-example-3.jsonld)

PreservedSpecimen-typeStatus-example-4:
[TurTLe](https://github.com/tdwg/tcs2/blob/master/examples/PreservedSpecimen-typeStatus-example-4.ttl)
|
[JSON-LD](https://github.com/tdwg/tcs2/blob/master/examples/PreservedSpecimen-typeStatus-example-4.jsonld)








