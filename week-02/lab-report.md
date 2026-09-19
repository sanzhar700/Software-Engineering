# Lab report — Practice #02: The Prompt Is an Engineering Input

**Name:**
**Group:**
**Date:**

> Fill in every section. **Do not delete or renumber the headings** — the grading pass reads them
> by number. If something did not happen, write "did not happen" and why; an empty section and a
> fabricated one are graded the same way.

---

## 1. The frozen experiment

| | |
| --- | --- |
| AI assistant: ChatGPT| |
| Exact model name: GPT-5.6 Luna | |
| Implementation language: Python | |
| Date of the runs: 19 September 2026 | |

**Non-Python students only** — paste your substituted Prompt B text here, so the substitution can
be checked:

```
(paste here, or write "n/a — used Python")
```

**Confirmations:**

- Each prompt was sent in a **fresh chat**: yes 
- No follow-up questions were asked before Part 7: yes 
- Every output was saved **before** any editing: yes 

---

## 2. Prompt A — minimal

**Prompt sent** (should be exactly one sentence):

```

```

**Assumptions the AI made that I never gave it** — list them, one per line. A data format, a pass
threshold, a rounding rule, an input method, an invented feature all count.

1.Student marks would be stored in a dictionary with student names.
2.The input would contain a fixed set of students: Alice, Bob, Charlie, David and Emma.

3.The task required printing a report rather than implementing a reusable function.

**Questions it should have asked and did not:**

1.What input format should be used?
2.What should the function be called and what should it return?

**Is the function named `analyze_marks` with the required signature?** yes / no — there is no analyze_marks function.

**First impression before testing** (one sentence — you will compare this with section 6 later):The output does not implement the requested function and instead invents a student dictionary and a printed report.

---

## 3. Prompt B — structured context

**Prompt sent** (paste it in full, including any substitutions):

```1 It implemented the required analyze_marks function with the correct signature.
2 It returned a dictionary containing average, highest, lowest and pass_rate.
3 It added validation for empty lists, non-numeric values and marks outside 0–100

4. It used no external libraries.
```

**What B fixed compared to A:**

1.
2.

**What B still leaves open:**

1.
2.

---

## 4. Prompt C — examples and tests

**What I appended to Prompt B:**
Example: analyze_marks([40, 60, 80], 50) -> average 60, highest 80, lowest 40,
pass_rate 66.67. Include tests for: one mark, decimals, custom pass_mark, empty list,
text value, and marks below 0 or above 100. State any remaining assumptions before
the code.

```

```

**Tests the AI wrote for itself** — how many, and which situations do they cover?

| Situation | Covered by the AI's tests? |
| --- | --- |
| one mark | |
| decimals | |
| custom pass_mark | |
| empty list | |
| text value | |
| below 0 / above 100 | |

**Do the AI's own tests pass against the AI's own code?** yes / no

**Do they agree with the harness in section 6?** yes / no — if no, where do they disagree:

**Assumptions C stated explicitly before the code:**

---

## 5. Prompt D — my combined prompt

**The complete prompt I wrote** (one message, sent to a fresh chat):
Prompt used:

You are a Python developer. Implement exactly one function:

analyze_marks(marks, pass_mark=50)

The function must return a dictionary with exactly these keys:
average, highest, lowest, and pass_rate.

Marks are numeric values from 0 to 100 inclusive. A mark passes when it is
greater than or equal to pass_mark. Raise ValueError for an empty marks list,
a non-numeric mark, or a mark outside the range 0–100. Do not use external
libraries.

Calculate average, highest, and lowest normally. Calculate pass_rate as the
percentage of marks that pass and round it to two decimal places. For example,
analyze_marks([40, 60, 80], 50) must return average=60, highest=80, lowest=40,
and pass_rate=66.67.

Use the exact function signature and exact dictionary key names above.

Before the code, briefly state any remaining assumptions. Then provide the
Python code and include tests covering: one mark, decimal marks, a custom
pass_mark, an empty list, a text value, and marks below 0 or above 100.

```

```

**What I deliberately added that A, B and C did not have:**

1.The exact function signature;
2.Explicit rounding of pass_rate to two decimal places;
3.Requirement to state remaining assumptions.

**The ambiguity I found in the specification, and how I resolved it inside Prompt D:**
The handout/test cases use 66.67% for the first example, while the exact
mathematical result before rounding is 66.666666...%. Prompt D explicitly
requires rounding pass_rate to two decimal places, resolving this ambiguity.



---

## 6. Test results — the evidence

| # | Call | Required | A | B | C | D |
|---|---|---|---|---|---|---|
| 1 | analyze_marks([40, 60, 80], 50) | avg 60 · high 80 · low 40 · rate 66.67 | ERROR | PASS | PASS | PASS |
| 2 | analyze_marks([100], 50) | avg 100 · high 100 · low 100 · rate 100 | ERROR | PASS | PASS | PASS |
| 3 | analyze_marks([49.5, 50], 50) | avg 49.75 · high 50 · low 49.5 · rate 50 | ERROR | PASS | PASS | PASS |
| 4 | analyze_marks([], 50) | raises ValueError | ERROR | PASS | PASS | PASS |
| 5 | analyze_marks([40, "60"], 50) | raises ValueError | ERROR | PASS | PASS | PASS |
| 6 | analyze_marks([-1, 50, 101], 50) | raises ValueError | ERROR | PASS | PASS | PASS |
| | Totals | | 0/6 | 6/6 | 6/6 | 6/6 |


The official harness confirmed that prompts B, C, and D passed all six cases. Prompt A failed all six cases because it did not define a callable analyze_marks function, so the harness recorded all six cases as ERROR.

**For every FAIL and ERROR above, one line: what was returned or raised instead.**

| Prompt | Case | What actually happened |
| --- | --- | --- |
| | | |
| | | |
| | | |

### Pasted terminal output — all four runs

> This is the part that makes the table above count. Paste the **whole** output, unedited,
> including the header lines. A table with nothing behind it is not accepted.

**Prompt A**
1. It assumed that student marks would be stored in a dictionary with student names.
2. It assumed a fixed list of five students: Alice, Bob, Charlie, David and Emma.
3. It assumed that the task required printing a report instead of implementing a reusable function.
4. It assumed the pass threshold was 50.
5. It assumed a command-line style output was required.
```

```

**Prompt B**
1. It implemented the required analyze_marks function with the correct signature.
2. It returned a dictionary containing average, highest, lowest and pass_rate.
3. It added validation for an empty list, non-numeric marks and marks outside 0–100.
4. It used no external libraries.



what b still leaves open - 
1. It does not explicitly state a rounding rule for pass_rate.
2. It does not provide its own tests or examples.
3. It does not explicitly explain the boundary rule for a mark equal to pass_mark.
4. It does not validate pass_mark itself.
```

```

**Prompt C**
Example: analyze_marks([40, 60, 80], 50) -> average 60, highest 80, lowest 40,
pass_rate 66.67. Include tests for: one mark, decimals, custom pass_mark, empty list,
text value, and marks below 0 or above 100. State any remaining assumptions before
the code.
```

```

**Prompt D**

```

```

---

## 7. Scoring

0| Prompt | Correctness | Requirement coverage | Verifiability | Assumptions stated | Noise | Total |
|---|---:|---:|---:|---:|---:|---:|
| A | 0 | 0 | 0 | 0 | 0 | 0/10 |
| B | 2 | 2 | 0 | 0 | 2 | 6/10 |
| C | 2 | 2 | 2 | 0 | 2 | 8/10 |
| D | 2 | 2 | 2 | 0 | 2 | 8/10 |

### Scoring notes

 A: The response did not define analyze_marks, so all six official cases were ERROR. It also invented a fixed student dataset and printed a report instead of implementing the requested reusable function.
 B: The function met the core functional requirements and passed all six official cases, but it contained no tests and did not explicitly state assumptions.
 C:The function passed all six official cases and included its own tests covering valid and invalid inputs. It did not explicitly state assumptions.
 D:The function passed all six official cases and included tests. It explicitly resolved the pass_rate rounding ambiguity, but the generated response did not actually state remaining assumptions before the code as requested.

**Prompt length, in words:** A ____ · B ____ · C ____ · D ____

**Words added per point gained** — B over A, C over B, D over C. One line on what that ratio says:

---

## 8. Conclusion — 150–200 words
## 8. Conclusion

The experiment showed that prompt structure has a significant effect on the usefulness and verifiability of AI-generated code. Prompt A scored 0/10 because the response misunderstood the task: it created a fixed student dataset and printed a report instead of implementing the required `analyze_marks` function. Prompt B scored 6/10. It correctly implemented the required function and validation, but it did not include tests or explicitly state assumptions. Prompt C scored 8/10 because it kept the correct implementation and added tests covering valid and invalid inputs. Prompt D also scored 8/10 and passed all six official cases. Its main additional value was resolving the ambiguity about `pass_rate` by explicitly requiring rounding to two decimal places.

The most useful addition was the explicit specification of the function signature, return keys, validation rules, and expected rounding behavior. The main weakness that remained was that the generated D response did not actually state its remaining assumptions before the code, even though the prompt requested this.

For software engineering work, I would use a structured prompt similar to D because it makes requirements and expected behavior explicit and makes the generated result easier to verify with tests. The official harness was important because it provided objective evidence rather than relying only on the AI's own tests.

Answer in this order: (1) which prompt scored best, and whether it is the one you would actually
use at work; (2) which single addition bought the most correctness, naming the exact case that
changed verdict; (3) what was pure noise; (4) the ambiguity and your resolution.

Name test cases and real returned values. "More detailed prompts work better" scores zero.

```
(150–200 words)

8. Conclusion

C and D scored the best with 8/10 each. I would actually use D at work because it explicitly defines the function signature, required keys, validation rules, and rounding behavior. However, C and D received the same score in this experiment.

The single addition that bought the most correctness was specifying the required function interface: `analyze_marks(marks, pass_mark=50)` with the exact return keys. This directly prevented the failure seen in Prompt A. In A, the AI created a fixed student dictionary and did not define `analyze_marks`, so all six cases were ERROR. For example, case 1 could not be evaluated at all. After the interface was explicitly specified, B, C, and D all passed case 1 with `average=60.0`, `highest=80`, `lowest=40`, and `pass_rate=66.67`.

The pure noise was the fixed student dataset and printed report in Prompt A, including names such as Alice, Bob, and Charlie. These were not required by the task and did not help satisfy the harness.

The main ambiguity was `pass_rate`: the mathematical result for case 1 is 66.666..., while the expected value is 66.67. I resolved this in D by explicitly requiring `pass_rate` to be rounded to two decimal places.


```

**Word count:**

---

## 9. Two questions for the debrief

Written before class, answered in class.

1.
2.
