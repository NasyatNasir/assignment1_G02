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
- Output: Quick update: the two functions are written and the end-to-end run works in a scratch copy. I'm now installing pytest and ruff to run the visible tests and lint check before handing the file over.
I've implemented results_to_csv and build_report in a1_triage.py. ruff check src passes on it. I couldn't run it for real, because the other functions in your file are still NotImplementedError. I tested both in a scratch copy with my own temporary versions of those functions. Your 6 visible tests passed there, and the run on your variants.csv and params.json wrote triage.csv (51 lines) and report.txt
- Verified by: <How you checked it: ran pytest, read the docs, compared with data, asked lecturer>
- My change: <What you accepted, rejected or rewrote, and why>
- Used in: <File and function, or report section, where it ended up (or 'not used')>

<!-- Copy the whole 'Entry' block for each extra interaction: ## Entry 2, ## Entry 3 ... -->

# AI USE LOG: MEMBER 3

- Course: SECB3203
- Assessment: Assignment 1
- Student name: Mohamad Asyik Illahi bin Nasruddim
- Matric no: A24CS0113
- Group ID: 2
- AI level: 1
- Tools cited: Anthropic (2026). Claude (Claude Sonnet 5.5). Retrieved 21 November 2026 from https://claude.ai

## Declaration (tick exactly one)

- [ ] NIL RETURN: I did not use any generative AI tool for this assessment.
- [/] I used AI. Every interaction that influenced my work is logged below. The log is true and complete.

## Entry 1

- Date: <21/11/2026 2:00 pm>
- Tools cited: Anthropic (2026). Claude (Claude Sonnet 5.5). Retrieved 22 November 2026 from https://claude.ai
- - Purpose:  generate-code
- Prompt: help me to code report to csv and build report in triage.py
- Output: Quick update: the two functions are written and the end-to-end run works in a scratch copy. I'm now installing pytest and ruff to run the visible tests and lint check before handing the file over.
I've implemented results_to_csv and build_report in a1_triage.py. ruff check src passes on it. I couldn't run it for real, because the other functions in your file are still NotImplementedError. I tested both in a scratch copy with my own temporary versions of those functions. Your 6 visible tests passed there, and the run on your variants.csv and params.json wrote triage.csv (51 lines) and report.txt
- Verified by: <How you checked it: ran pytest
- My change: get content of the code
- Used in: src/ file
-  
## Entry 2

- Date: <21/11/2026 2:00 pm>
- Tools cited: Anthropic (2026). Claude (Claude Sonnet 5.5). Retrieved 22 November 2026 from https://claude.ai
- - Purpose:  generate-code
- Prompt: give me explaination about these two functions and expected output
- Output: 1. results_to_csv(results)
Purpose: turns the list of classified variants into one CSV text string. main() writes that string to results/triage.csv.
How it works, line by line:
code	What it does
io.StringIO()	Creates an in-memory "file" so the CSV is built as text, not written to disk.
csv.writer(buffer, lineterminator="\n")	Writes CSV rows into that buffer. lineterminator="\n" makes every line end with a newline, as the docstring requires.
writer.writerow(CSV_COLUMNS)	Writes the header line first.
for result in results:	Loops through the results in their given order, with no sorting.
[result.get(column, "") for column in CSV_COLUMNS]	Picks the values in the fixed column order. Columns like ref and alt are not in CSV_COLUMNS, so they are dropped. A missing key gives an empty string instead of a crash.
- Verified by: <How you checked it: ran pytest
- My change: get content of the code
- Used in: src/ file
- 
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
- Signed: <full name, matric, date>
- Signed: <full name, matric, date>
- Signed: <full name, matric, date>
