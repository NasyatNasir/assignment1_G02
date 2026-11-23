# Design - Variant Triage Service

Group ID: G02      Thresholds from data/params.json: min_depth = 12, min_quality = 70, top_k = 5
Priority genes from data/params.json: APC, MLH1, PTEN, RB1, TP53


## 1. Decomposition

| Question | Our answer |
|---|---|
| Input | variants.csv (variant, gene, chromosome (chrom), position (pos), reference (ref), alternative (alt), depth, quality, impact). Settings from params (min_depth, min_quality, priority_genes, top_k) |
| Output | A decision (prioritize, review or exclude) with a reason for every variant, the number of variants per decision, the number of non-excluded variants per impact label, a per-gene summary, a ranked top-k list of variants, CSV text and a text report (saved as results/triage.csv and results/report.txt)|
| Constraints (named thresholds, what happens at exactly the threshold) | thresholds and genes are read from params. min_depth, depth equal to min_depth passes. min_quality, quality equal to min_quality passes. Only value below min_depth and min_quality are excluded. Input never modified. Gene and impact must be compared after strip and case folding. Reasons must contain no commas |
| Rule order and why the order matters | Rule order: 1) Depth below min_depth should be excluded. 2) Quality below min_quality should be excluded. 3) Priority gene and impact high or moderate should be prioritized. 4) Priority gene and impact low or modifier should be reviewed. 5) Not a priority gene and impact high or moderate should be reviewed. 6) Not a priority gene and impact low or modifier should be excluded. Rule order matters: depth and quality are checked first so that unreliable calls are excluded before gene and impact are considered. The first rule that fires decides.|
| Out of scope | Real clinical variant classification, real patient data, classes, and checking the CSV for missing or invalid values. We assume impact is always one of high, moderate, low or modifier |

## 2. Pseudocode or flowchart of classify_variant

    FUNCTION classify_variant(row: dict, params: dict)

        depth = integer of row.depth
        quality = integer of row.quality
        gene = row.gene, remove surrounding spaces, to upper case
        impact = row.impact, remove surrounding spaces, to lower case
        priority_genes = each gene in params.priority_genes, remove surrounding spaces, to upper case

        IF depth < params.min_depth
            RETURN "exclude", "Rule 1: Depth {depth} is below min_depth ({params.min_depth})"

        IF quality < params.min_quality
            RETURN "exclude", "Rule 2: Quality ({quality}) is below min_quality ({params.min_quality})"

        IF (gene in priority_genes) AND (impact is "high" OR impact is "moderate")
            RETURN "prioritize", "Rule 3: Priority gene ({gene}) and {impact} impact"

        IF gene in priority_genes AND (impact is "low" OR impact is "modifier")
            RETURN "review", "Rule 4: Priority gene ({gene}) and {impact} impact"

        IF (gene NOT in priority_genes) AND (impact IS "high" OR impact is "moderate")
            RETURN "review", "Rule 5: Not a priority gene ({gene}) and {impact} impact"

        IF (gene NOT in priority_genes) AND (impact is "low" OR impact is "modifier")
            RETURN "exclude", "Rule 6: Not a priority gene ({gene}) and {impact} impact"

## 3. Hand trace

| Variant | Gene | Depth | Quality | Impact | Rule that fires | Decision | Reason |
|---|---|---|---|---|---|---|---|
| v1 | APC | 9 | 90 | modifier | 1 | exclude | Rule 1: Depth 9 is below min_depth (12) |
| v2 | BRCA2 | 10 | 90 | low | 1 | exclude | Rule 1: Depth 10 is below min_depth (12) |
| v3 | BRCA1 | 11 | 90 | modifier | 1 | exclude | Rule 1: Depth 11 is below min_depth (12) |
| v4 | RB1 | 30 | 79 | modifier | 4 | review | Rule 4: Priority gene (RB1) and modifier impact |
| v5 | BRCA1 | 30 | 80 | modifier | 6 | exclude | Rule 6: Not a priority gene (BRCA1) and modifier impact |
| v6 | BRCA1 | 30 | 81 | moderate | 5 | review | Rule 5: Not a priority gene (BRCA1) and moderate impact |
| v9 | APC | 13 | 85 | high | 3 | prioritize | Rule 3: Priority gene (APC) and high impact |
| v27 | PTEN | 27 | 66 | modifier | 2 | exclude | Rule 2: Quality (66) is below min_quality (70) |


## 4. Test plan

1. Normal: one case for each of rules 1 to 6.
2. Boundary: depth 11, 12, 13 and quality 69, 70, 71, for both thresholds.
3. Awkward: ' brca1 ', 'HIGH', an empty list, k = 0, and k larger than the data.
4. Invalid: a negative k raises ValueError, tested with pytest.raises.

## 5. Work plan

- Member 1: design.md, GROUP_CONTRACT.md, decision_counts(), impact_counts(), test for both functions
- Member 2: gene_summary(), rank_variants(), tests for both functions
- Member 3: classify_variant(), triage(), tests for both functions
- Member 4: results_to_csv(), build_report(), README.md, ruff check, and final pytest, tests for both functions

Order: design first, then functions, then tests, then README. Each member reads another member's function before it is merged.
