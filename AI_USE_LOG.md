# AI USE LOG: MEMBER 1

- Course: SECB3203
- Assessment: Assignment 1
- Student name: MUHAMMAD NASYAT BIN MOHAMAD NASIR
- Matric no: A24CS0141
- Group ID: G02
- AI level: 1
- Tools cited: Anthropic (2026). Claude (Claude Sonnet 5.5). Retrieved 22 November 2026 from https://claude.ai

## Declaration (tick exactly one)

- [ ] NIL RETURN: I did not use any generative AI tool for this assessment.
- [x] I used AI. Every interaction that influenced my work is logged below. The log is true and complete.

## Entry 1

- Date: 19/11/2026
- Tool: Claude (Claude Sonnet 5.5), claude.ai, retrieved 22 November 2026
- Purpose: explain
- Prompt: "explain task one? and can explain what the case study want?" and "so for task one, i have to design all functions? or certain function only?"
- Output: Explained the case study (triage of variants) and the five parts of design.md. Said only classify_variant needs pseudocode, and the decomposition table covers the whole module.
- Verified by: Compared with assignment instructions
- My change: Used it to understand the task. No text copied.
- Used in: docs/design.md (structure only)

## Entry 2

- Date: 19/11/2026
- Tool: Claude (Claude Sonnet 5.5), claude.ai, retrieved 22 November 2026
- Purpose: explain
- Prompt: "the params.json containing both min and max value, how am i gonna use it in python?", "but before that, we have a helper function for load parameters" and "what is this impact? i don't see any on the params.json"
- Output: Explained that params arrives as a dictionary, that CSV values are text (so int() is needed) while JSON values are already numbers, and that impact comes from variants.csv.
- Verified by: n/a
- My change: Used it to understand where each value comes from.
- Used in: classify_variant pseudocode and code

## Entry 3

- Date: 20/11/2026
- Tool: Claude (Claude Sonnet 5.5), claude.ai, retrieved 22 November 2026
- Purpose: hint, review
- Prompt: "how should we design this in pseudocode?", then I pasted four drafts of my pseudocode for review. I also asked "can you just fix it for me?" (the AI declined, and gave a different example to copy the pattern from).
- Output: Pointed out missing int() conversion, the wrong parameter in rule 1's reason, an undefined priority_gene, the ambiguous "impact is high OR moderate", and that reasons should name the rule and the threshold. Also advised cleaning both sides of the gene comparison in the same way.
- Verified by: Hand trace using 7 rows
- My change: I rewrote the pseudocode myself in each draft. I kept the rule order and boundaries and applied each fix in my own wording.
- Used in: docs/design.md section 2

## Entry 4

- Date: 20/11/2026
- Tool: Claude (Claude Sonnet 5.5), claude.ai, retrieved 22 November 2026
- Purpose: hint, review, tests-plan
- Prompt: "how to fill in the decomposition table?", plus one question per cell (constraints, rule order, out of scope) and several pasted drafts of design.md
- Output: Explained what each cell should contain, with examples from a different domain. Reviewed my drafts (typos, Input and Output wording, the <= instead of < slip in the pseudocode, missing priority genes in the header, thin test plan, missing work-plan order).
- Verified by: Checked against the brief and the data
- My change: Wrote all cells in my own words. Fixed the typos and boundaries, added the priority genes from params.json, and extended the test plan and work plan.
- Used in: docs/design.md sections 1, 3, 4 and 5

## Entry 5

- Date: 20/11/2026
- Tool: Claude (Claude Sonnet 5.5), claude.ai, retrieved 22 November 2026
- Purpose: hint, debug
- Prompt: "can you help me with the decision_counts?" and my pasted versions of decision_counts and impact_counts (several attempts)
- Output: Explained the tally-sheet idea and gave a fruit-counting example. Pointed out the wrong field in the loop, the missing return, the missing skip of excluded variants and the missing cleaning of the impact text. Told me the correct method is lower(), not tolower(), and that result[impact] was the wrong lookup.
- Verified by: ran python -m pytest
- My change: Wrote the code myself and fixed it after each hint.
- Used in: src/a1_triage.py, decision_counts() and impact_counts()

## Entry 6

- Date: 21/11/2026
- Tool: Claude (Claude Sonnet 5.5), claude.ai, retrieved 22 November 2026
- Purpose: tests-plan, review
- Prompt: "so make test based on?", "so how many test should i write?" and my pasted test file
- Output: Explained how to build tests from the brief and my test plan, gave the shape of a test with blanks, and suggested adding assert list(answer.keys()) == [...] to check key order.
- Verified by: ran python -m pytest
- My change: Wrote the four tests myself with my own expected values. I will add the key-order assertion.
- Used in: tests/test_a1_triage.py

# AI USE LOG: MEMBER 2

- Course: SECB3203
- Assessment: Assignment 1
- Student name: ZARIFF BIN MOHAMMAD AZAM
- Matric no: A24CS0217
- Group ID: G02
- AI level: 1
- Tools cited: Anthropic (2026). Claude (3.5 Sonnet). Retrieved 22 November 2026 from https://claude.ai/

## Declaration (tick exactly one)

- [ ] NIL RETURN: I did not use any generative AI tool for this assessment.
- [/] I used AI. Every interaction that influenced my work is logged below. The log is true and complete.

## Entry 1

- Date: 22 November 2026
- Tool: Anthropic (2026). Claude (3.5 Sonnet). Retrieved 22 November 2026 from https://claude.ai/
- Purpose: 
- Prompt: \
    Help me draft some tests for the functions gene_summary() and rank_variants()
- Output: \
    I recommend creating three tests in tests/test_a1_triage_own.py: \
    - Test 1: gene_summary() — checks counting, mean depth and alphabetical ordering. \
    - Test 2: rank_variants() — checks the sorting order and exclusion of variants. \
    - Test 3: rank_variants() — checks that negative k raises ValueError.

- Verified by: \
    verified by implementing tests and ran pytest
- My change: \
    accepted, the tests cover both functions in detail
- Used in: \
    test_gene_summary(), test_rank_variants in test_a1_triage.py

## Entry 2

- Date: 22 November 2026
- Tool: Anthropic (2026). Claude (3.5 Sonnet). Retrieved 22 November 2026 from https://claude.ai/
- Purpose: debug
- Prompt: \
    Why am I getting the error "pytest not defined" when using with pytest.raises(ValueError)?  
- Output: \
    Explained that the pytest module was not imported and suggested adding import pytest at the beginning of the test file.

- Verified by: \
    verified by added the import statement and ran pytest
- My change: \
    accepted, adding import pytest resolved the issue
- Used in: \
    test_a1_triage.py

## Entry 3

- Date: 22 November 2026
- Tool: Anthropic (2026). Claude (3.5 Sonnet). Retrieved 22 November 2026 from https://claude.ai/
- Purpose: explain  
- Prompt: \
    What is the difference between raising a ValueError and checking for a ValueError using pytest?
- Output: \
    Explained that raise ValueError is used in the actual function to signal invalid input, while pytest.raises(ValueError) is used in a test to verify that the exception occurs.

- Verified by: \
    verified by compared the implementation of rank_variants() with the corresponding test
- My change: \
    n/a
- Used in: \
    test_a1_triage.py

## Entry 4

- Date: 22 November 2026
- Tool: Anthropic (2026). Claude (3.5 Sonnet). Retrieved 22 November 2026 from https://claude.ai/
- Purpose: hint
- Prompt: \
    Give me a hint on how to test that rank_variants(results, k) raises a ValueError when k is negative.
- Output: \
    Suggested testing the function with a negative value of k and using pytest.raises(ValueError) to check the expected exception.

- Verified by: \
    verified by ran pytest
- My change: \
    accepted, wrote my own test using -1 as the input for k
- Used in: \
    test_rank_variants_negative_k() in test_a1_triage.py


# AI USE LOG: MEMBER 3

- Course: SECB3203
- Assessment: <e.g. Lab 4>
- Student name: <full name>
- Matric no: <matric>
- Group ID: <group work only, else n/a>
- AI level: <0, 1 or 2 - see the assessment brief>
- Tools cited: <UTM format, e.g. OpenAI (2026). ChatGPT (GPT-5). Retrieved 12 October 2026 from https://chat.openai.com>

## Declaration (tick exactly one)

- [ ] NIL RETURN: I did not use any generative AI tool for this assessment.
- [ ] I used AI. Every interaction that influenced my work is logged below. The log is true and complete.

## Entry 1

- Date: <Date and time of the interaction>
- Tool: <Tool name, version, access date and URL (UTM citation format)>
- Purpose: <One of: explain, hint, review, debug, generate-code, generate-text, tests-plan, other>
- Prompt: <The exact prompt you typed (paste it)>
- Output: <What the AI gave back, in 1 to 3 lines (attach the full text if you used it)>
- Verified by: <How you checked it: ran pytest, read the docs, compared with data, asked lecturer>
- My change: <What you accepted, rejected or rewrote, and why>
- Used in: <File and function, or report section, where it ended up (or 'not used')>

<!-- Copy the whole 'Entry' block for each extra interaction: ## Entry 2, ## Entry 3 ... -->

# AI USE LOG: MEMBER 4

- Course: SECB3203
- Assessment: <e.g. Lab 4>
- Student name: <full name>
- Matric no: <matric>
- Group ID: <group work only, else n/a>
- AI level: <0, 1 or 2 - see the assessment brief>
- Tools cited: <UTM format, e.g. OpenAI (2026). ChatGPT (GPT-5). Retrieved 12 October 2026 from https://chat.openai.com>

## Declaration (tick exactly one)

- [ ] NIL RETURN: I did not use any generative AI tool for this assessment.
- [ ] I used AI. Every interaction that influenced my work is logged below. The log is true and complete.

## Entry 1

- Date: <Date and time of the interaction>
- Tool: <Tool name, version, access date and URL (UTM citation format)>
- Purpose: <One of: explain, hint, review, debug, generate-code, generate-text, tests-plan, other>
- Prompt: <The exact prompt you typed (paste it)>
- Output: <What the AI gave back, in 1 to 3 lines (attach the full text if you used it)>
- Verified by: <How you checked it: ran pytest, read the docs, compared with data, asked lecturer>
- My change: <What you accepted, rejected or rewrote, and why>
- Used in: <File and function, or report section, where it ended up (or 'not used')>

<!-- Copy the whole 'Entry' block for each extra interaction: ## Entry 2, ## Entry 3 ... -->


## Group signatures

- Signed: MUHAMMAD NASYAT BIN MOHAMAD NASIR, A24CS0141, 22/11/2026
- Signed: ZARIFF BIN MOHAMMAD AZAM, A24CS0217, 22/11/2026
- Signed: <full name, matric, date>
- Signed: <full name, matric, date>
