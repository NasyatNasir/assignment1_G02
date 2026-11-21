# Variant Triage Service (SECB3203 Assignment 1)

> Replace the text in this template. The README must let a stranger install, run and test the
> project with the exact commands below. All data are synthetic teaching data, not clinical data.

## Group

- Group ID: G02
- Members: MUHAMMAD NASYAT BIN MOHAMAD NASIR (A24CS0141), ZARIFF BIN MOHAMMAD AZAM(A24CS0217), MOHAMAD FARHAN BIN MOHAMAD HARIRI (A24CS0114), MOHAMAD ASYIK ILLAHI BIN NASRUDDIN (A24CS0113)

## What this project does

A library sorting service decides which returned books go back on the shelf, which need repair, and which are removed. Each book arrives as a record with a title, a condition score and a damage type. The service also receives settings, such as the minimum condition score for shelving. It returns a decision and a reason for every book, plus counts, a ranked list of the most urgent repairs, and a short report.

## Set up

```
python -m venv .venv
<activate command for your system>
pip install -r requirements.txt
```

## Run

<Write the exact command. The course command is: python src/a1_triage.py data/variants.csv data/params.json results>
<Say which files appear in results/.>

    python -m pytest                 # all tests
    ruff check src                   # style check
    python src/a1_triange.py data/variants.csv data/params.json --out results/cli      # the command-line tool

## Test and lint

```
python -m pytest
ruff check src
```

## Our parameters

Our thresholds, priority genes and top_k are in data/params.json (<write the values here>).
They are read at run time and passed to the functions; they are not typed into the rules.

## Design

<Link to docs/design.md and say in two sentences what it contains.>

## Limitations

<At least two honest limitations, for example: rules use depth, quality and impact only; the data are synthetic.>

## Who did what

| Member | Main contributions | Commits |
|---|---|---|
| <name> | <files or functions> | <number> |

## AI use

<One sentence: see AI_USE_LOG.md. Say whether the group used AI.>
