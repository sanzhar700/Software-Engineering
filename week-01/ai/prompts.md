# AI Prompt Log — Week 01

## Initial prompt

Build a small program that processes a list of student marks and prints:
average, highest, lowest, and pass rate.

## Rocket's first response

Agent detected prompt score: 80%.

Rocket built a MarksAnalyzer web application using Next.js.

It added:
- average, highest, lowest and pass rate;
- grade distribution chart;
- sortable/searchable results table;
- configurable pass threshold;
- single student entry;
- bulk import;
- 12 pre-loaded mock students.

## Questions Rocket asked

No questions were asked before the application was built.

## Rewritten / enhanced prompt

No separate rewritten prompt was shown in the Rocket interface.

## Case A

Input:
85, 23, 45, 90, 92

Result:
The application already contained 12 mock students, so the test was not isolated.

## Case B

Input:
88, 47, -5, 101, abc, 73, 50, , 100

Initial result:
Rocket reported 4 parsing errors:
- -5
- 101
- abc
- empty value

## Follow-up prompt

Invalid marks such as values below 0, above 100, text, and empty values should be ignored instead of causing parsing errors. Keep valid marks and calculate the statistics only from them.

## Result of the fix

Rocket updated the bulk import parser.

It now skips empty, non-numeric, below-0 and above-100 scores and calculates statistics only from valid marks.