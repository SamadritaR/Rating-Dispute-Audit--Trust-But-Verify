# Process changes for the next delivery

The rating was right. The delivery still failed, because the customer lost trust in it. These changes target that.

## 1. Every flag ships with its evidence
Each "Contains Inaccuracy" row carries three extra fields: the exact claim quoted from the response, the correction, and a source. `scripts/audit_report.py` blocks the delivery if any of them is missing. A customer QA reviewer should be able to verify a flag in under a minute without redoing the research. `data/dataset_i_audited.csv` shows the format.

## 2. Agree on strictness before rating starts
Before a project begins, walk the customer through the six examples in `qa/calibration_examples.md`, including borderline ones like the evaporation row, and write down their call on each. Raters get those examples in their guidelines. Borderline rows get tagged "strictness call" so the customer can apply their own bar.

## 3. Second review on every flag
A second rater independently checks every row labeled Contains Inaccuracy. If the two disagree, a lead decides and writes one line on why. Flags are the rows customers push back on, so that is where review time goes.

## 4. Track it
Three numbers per delivery: rater agreement on flagged rows, share of flags the customer disputes, and share of disputes we overturn after review. If disputes rise while overturns stay near zero, the problem is communication or calibration, not rating quality.
