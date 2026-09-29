# Row by row audit

The customer said three flagged responses were wrong and only one had an inaccuracy, making "40% of the data flawed." I checked all five rows, including the two marked Accurate, before deciding anything.

| Row | Topic | Rater label | Audit | The claim that matters | Source |
|---|---|---|---|---|---|
| 1 | Seahawks | Accurate | Agree | XLIX (2015) is Seattle's third Super Bowl, after XL and XLVIII. Marshawn Lynch was the starting running back. | |
| 2 | Asbestos | Contains Inaccuracy | Agree | Calls asbestos "synthetic." It is a naturally occurring mineral fiber. | [EPA](https://www.epa.gov/asbestos/learn-about-asbestos) |
| 3 | Rolling Stones | Accurate | Agree | All ten songs are Jagger and Richards originals. | |
| 4 | Evaporation | Contains Inaccuracy | Agree, borderline | Says evaporation needs temperatures above freezing. Ice turns to vapor below 0°C through sublimation. | [USGS](https://www.usgs.gov/special-topics/water-science-school/science/sublimation-and-water-cycle) |
| 5 | Beatles | Contains Inaccuracy | Agree | Lists "Imagine," a 1971 John Lennon solo song. | [History.com](https://www.history.com/this-day-in-history/october-11/john-lennon-yoko-ono-imagine-released) |

## What this means

All five labels hold. Rows 2 and 5 are clear factual errors. Row 4 is where the disagreement most likely lives: the statement is wrong, but a reviewer could fairly read it as a simplification for a general audience.

So the root cause is a handoff problem, in two parts:

1. Labels shipped without the reason attached, so the customer could not see what our raters saw.
2. Nobody agreed upfront on how strict "Contains Inaccuracy" should be for simplifications.

Both are fixable before the next delivery. See `qa/process_changes.md`.
