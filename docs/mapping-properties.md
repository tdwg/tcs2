| TCS mapping property | [RCC-5](https://qsrlib.readthedocs.io/en/latest/rsts/handwritten/qsrs/rcc5.html) | [DE-9IM](https://en.wikipedia.org/wiki/DE-9IM) | [schema.org](https://schema.org) | [SKOS](https://www.w3.org/2009/08/skos-reference/skos.html)
|-|-|-|-|-|
| isCongruentWith | is equal to (EQ) | Equals | [geoEquals](https://schema.org/geoEquals) | [closeMatch](https://www.w3.org/2009/08/skos-reference/skos.html#closeMatch)
| includes | is a proper part inverse of (PPi) | Covers | [geoCovers](https://schema.org/geoCovers) | [narrowMatch](https://www.w3.org/2009/08/skos-reference/skos.html#narrowMatch)
| isIncludedIn | is a proper part of (PP) | CoveredBy | [geoCoveredBy](https://schema.org/geoCoveredBy) | [broadMatch](https://www.w3.org/2009/08/skos-reference/skos.html#broadMatch)
| partiallyOverlaps | is partially overlapping (PO) | Overlaps | [geoOverlaps](https://schema.org/geoOverlaps) | ([relatedMatch](https://www.w3.org/2009/08/skos-reference/skos.html#relatedMatch))
| isDisjointFrom | is discrete from (DR) | Disjoint | [geoDisjoint](https://schema.org/geoDisjoint) | ([relatedMatch](https://www.w3.org/2009/08/skos-reference/skos.html#relatedMatch))
| intersects | — | Intersects | [geoIntersects](https://schema.org/geoIntersects) | ([relatedMatch](https://www.w3.org/2009/08/skos-reference/skos.html#relatedMatch))