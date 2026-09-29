# RatingDisputeAudit

A customer disputed a truthfulness rating delivery, claiming 40% of it was flawed and asking not to be charged. This repo is how I worked the problem as a product operations case: check the data first, find where trust broke, then write the reply and fix the process.

## What I found
All five labels hold up. Two flags are clear factual errors (asbestos called synthetic, "Imagine" listed as a Beatles song). The third, evaporation needing temperatures above freezing, is wrong but borderline, and that is most likely where the customer's team read things differently.

The real failure was the handoff. Labels went out with no reasons attached, and strictness for simplifications was never agreed with the customer.

## Contents
| Path | What it is |
|---|---|
| `email/customer_response.pdf` | The reply to the customer |
| `audit/row_by_row.md` | Independent check of all five rows, with sources |
| `data/dataset_i_audited.csv` | Full dataset plus the evidence fields every flag should ship with |
| `qa/process_changes.md` | What changes for the next delivery |
| `qa/calibration_examples.md` | Examples to agree on strictness with the customer before rating |
| `scripts/audit_report.py` | Preship check that blocks any flag missing its claim, correction, or source |

## Sources
1. [EPA, Learn About Asbestos](https://www.epa.gov/asbestos/learn-about-asbestos)
2. [USGS Water Science School, Sublimation and the Water Cycle](https://www.usgs.gov/special-topics/water-science-school/science/sublimation-and-water-cycle)
3. [History.com, John Lennon's Imagine released](https://www.history.com/this-day-in-history/october-11/john-lennon-yoko-ono-imagine-released)

## Run it
```
python scripts/audit_report.py data/dataset_i_audited.csv
```
The script exits with an error if any "Contains Inaccuracy" row is missing evidence, or if the quoted claim doesn't appear word for word in the response, or if the source has no link. It turns the promise in the email into a gate that runs before every delivery.

## How I approached it
1. Verify before agreeing. A customer being upset does not make them right, and conceding a correct label teaches raters the wrong lesson.
2. Separate the rating from the delivery. The ratings were fine. The way they were handed over was not.
3. Hold on billing, stay generous on process. Offer a call and a free second rating on anything still disputed, and credit only what turns out wrong.

Samadrita Roy Chowdhury · [github.com/SamadritaR](https://github.com/SamadritaR)
