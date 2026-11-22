from a1_triage import decision_counts, impact_counts


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