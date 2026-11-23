# Variant Triage Service (SECB3203 Assignment 1)

All data are synthetic teaching data, not clinical data. Nothing here is clinical advice.

## Group

- Group ID: G02
- Members: MUHAMMAD NASYAT BIN MOHAMAD NASIR (A24CS0141), ZARIFF BIN MOHAMMAD AZAM (A24CS0217), MOHAMAD FARHAN BIN MOHAMAD HARIRI (A24CS0114), MOHAMAD ASYIK ILLAHI BIN NASRUDDIN (A24CS0113)

## What this project does

A variant triage service decides which genetic variant calls deserve attention, which need a second look, and which are set aside. Each variant arrives as a record with a gene, depth, quality score and impact label, and the service also receives settings such as the minimum depth and minimum quality. It returns a decision (prioritize, review or exclude) and a reason for every variant, plus decision counts, a ranked top-k list of the most important variants, a CSV file of all results and a short text report.

## Set up

```
python -m venv .venv
```

Activate the virtual environment:

- Windows (PowerShell): `.venv\Scripts\activate`
- macOS / Linux: `source .venv/bin/activate`

Then install the requirements:

```
pip install -r requirements.txt
```

## Run

```
python src/a1_triage.py data/variants.csv data/params.json results
```

The three arguments are the input variants, the parameters file and the output folder (created if it does not exist). Two files appear in `results/`:

- `triage.csv` - one line per variant with its decision and reason
- `report.txt` - the short text report (it is also printed in the terminal)

## Test and lint

```
python -m pytest
ruff check src
```

## Our parameters

Our thresholds, priority genes and top_k are in `data/params.json`:

- `min_depth` = 12
- `min_quality` = 70
- `priority_genes` = APC, MLH1, PTEN, RB1, TP53
- `top_k` = 5

They are read at run time and passed to the functions; they are not typed into the rules.

## Design

See [docs/design.md](docs/design.md). It describes how we broke the problem down (input, output, constraints and rule order), the pseudocode of `classify_variant`, a hand trace of our data, our test plan and our work plan.

## Limitations

- The rules use only gene, depth, quality and impact. Other evidence, such as allele frequency or variant type, is not considered.
- The data and thresholds are synthetic teaching values and have not been validated clinically, so the decisions must not be used for real patients.
- The report lists only the top k variants. It does not show the impact counts or the per-gene summary.

## Who did what

| Member | Main contributions | Commits |
|---|---|---|
| MUHAMMAD NASYAT BIN MOHAMAD NASIR | `decision_counts`, `impactCounts` | <number> |
| ZARIFF BIN MOHAMMAD AZAM | <files or functions> | <number> |
| MOHAMAD FARHAN BIN MOHAMAD HARIRI | <files or functions> | <number> |
| MOHAMAD ASYIK ILLAHI BIN NASRUDDIN | `results_to_csv`, `build_report`, and their test cases in `tests/test_visible.py` | <number> |

## AI use

Yes, the group used AI (Claude) to help write and test `results_to_csv` and `build_report`; all AI-assisted code was run against the tests and is recorded in `AI_USE_LOG.md`.
