import pytest
from a1_triage import (
    load_variants,
    load_params,
    classify_variant,
    triage,
    decision_counts,
    impact_counts,
    gene_summary,
    rank_variants,
    results_to_csv,
    build_report,
    main
)

def test_decision_counts_mixed():
    results = [{"decision": "exclude"}, {"decision": "review"}, {"decision": "exclude"}]
    assert decision_counts(results) == {"prioritize": 0, "review": 1, "exclude": 2}


def test_decision_counts_empty():
    results = []
    assert decision_counts(results) == {"prioritize": 0, "review": 0, "exclude": 0}


def test_impact_counts_skips_excluded_and_cleans():
    results = [
        {"decision": "exclude", "impact": "high"},
        {"decision": "review", "impact": " HIGH "},
        {"decision": "prioritize", "impact": "moderate"},
    ]
    assert impact_counts(results) == {"high": 1, "moderate": 1, "low": 0, "modifier": 0}

def test_impact_counts_empty():
    results = []
    assert impact_counts(results) == {"high": 0, "moderate": 0, "low": 0, "modifier": 0}

def test_gene_summary():
    results = [
        {
            "gene": "TP53",
            "depth": "20",
            "decision": "prioritize"
        },
        {
            "gene": "BRCA1",
            "depth": "10",
            "decision": "review"
        },
        {
            "gene": "TP53",
            "depth": "40",
            "decision": "exclude"
        },
        {
            "gene": "BRCA1",
            "depth": "21",
            "decision": "prioritize"
        }
    ]

    summary = gene_summary(results)

    assert list(summary.keys()) == ["BRCA1", "TP53"]

    assert summary["BRCA1"] == {
        "total": 2,
        "prioritize": 1,
        "review": 1,
        "exclude": 0,
        "mean_depth": 15.5
    }

    assert summary["TP53"] == {
        "total": 2,
        "prioritize": 1,
        "review": 0,
        "exclude": 1,
        "mean_depth": 30.0
    }

def test_rank_variants():
    results = [
        {
            "variant": "var1",
            "gene": "TP53",
            "impact": "high",
            "decision": "prioritize",
            "quality": "90",
            "depth": "30",
            "pos": "50"
        },
        {
            "variant": "var2",
            "gene": "BRCA1",
            "impact": "high",
            "decision": "prioritize",
            "quality": "95",
            "depth": "20",
            "pos": "40"
        },
        {
            "variant": "var3",
            "gene": "BRCA2",
            "impact": "moderate",
            "decision": "prioritize",
            "quality": "99",
            "depth": "50",
            "pos": "10"
        },
        {
            "variant": "var4",
            "gene": "EGFR",
            "impact": "high",
            "decision": "review",
            "quality": "99",
            "depth": "50",
            "pos": "5"
        },
        {
            "variant": "var5",
            "gene": "MYC",
            "impact": "high",
            "decision": "exclude",
            "quality": "100",
            "depth": "100",
            "pos": "1"
        },
        {
            "variant": "var6",
            "gene": "BRCA1",
            "impact": "high",
            "decision": "prioritize",
            "quality": "95",
            "depth": "20",
            "pos": "10"
        }
    ]

    ranked = rank_variants(results, 4)

    assert [row["variant"] for row in ranked] == [
        "var6",
        "var2",
        "var1",
        "var3"
    ]

    assert len(ranked) == 4
    assert all(row["decision"] != "exclude" for row in ranked)

def test_rank_variants_negative_k():
    results = [
        {
            "variant": "var1",
            "gene": "TP53",
            "impact": "high",
            "decision": "prioritize",
            "quality": "90",
            "depth": "30",
            "pos": "50"
        }
    ]

    with pytest.raises(ValueError):
        rank_variants(results, -1)