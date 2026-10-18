# Week 06 — Lab report

**Name:** Sansyzbayev Sanzhar
**Group:** Monday 16:00-19:00
**Date:** 18 October 2026

Fill in every section. **Do not delete, rename or renumber the headings** — the checker and the
grader find your answers by them. Add rows to any table; never remove its header.

---

## 1. Setup

| | |
| --- | --- |
| Tool | Bolt.new |
| Exact model (as Bolt shows it, or `not displayed`) | not displayed |
| Bolt project link (or `not shared`, and why) | https://bolt.new/~/sb1-5wcw6gha |
| Browser and version | Chrome (exact version not recorded; visible in evidence/v1.png) |
| If you could not use Bolt.new: the tool you used instead, and why | |

---

## 2. Task 1 — define before generating

**Two predictions, written BEFORE you send the first prompt.** Where do you expect v1 to go wrong?
Fill the first three columns now; fill the last one after Task 3.

| # | What I expect to go wrong | AC it concerns | Was I right? (after Task 3) |
| --- | --- | --- | --- |
| 1 | v1 may reject a request whose start touches an existing booking's end, or allow an overlapping request. | AC4 | Partly. The original sample data did not match the required baseline, so the overlap/touching cases were not all reproducible as specified. |
| 2 | v1 may use the real system clock rather than the supplied current time, making T6 hard to reproduce. | AC1 | The v1 interface exposed a current-time value for testing; the available evidence does not establish that the implementation accepted a separately supplied clock in all cases. |

**The initial prompt exactly as I sent it** — the deck's prompt with AC1–AC6 pasted in place of
`[paste AC1–AC6]`, nothing else changed:

```text
Build a small responsive Smart Campus Room Availability Checker. Requirements: AC1: Accept a candidate interval only when 0 ≤ start < end ≤ 1440 and start is after the supplied current time.
AC2: Reject a booking longer than 120 minutes.
AC3: Reject the request when the selected room is blocked.
AC4: Reject any interval that overlaps an existing booking; touching endpoints are allowed.
AC5: Show a clear Available / Unavailable decision without changing the existing booking data.
AC6: The page remains usable at desktop and narrow/mobile width and gives understandable validation feedback. Use fictional sample data only. Keep the implementation simple and within one-page scope. Do not add authentication, backend services, analytics, or unrelated features. After building, briefly list the main files/components you created.
```

---

## 3. Task 2 — prototype v1

v1 export saved in `original/` and screenshot saved as `evidence/v1.png` **before** any cleanup
prompt: yes

**Files/components present in the v1 export** (from the Bolt preview shown in `evidence/v1.png`):

```text
src/lib/data.ts — fictional sample rooms, bookings, and room blocks
src/lib/availability.ts — the validation/decision logic for AC1-AC4
src/App.tsx — the responsive one-page UI with form, decision card, and room info panel
```

**What v1 does — one line per thing that works, or visibly does not:**

- Shows fictional campus rooms and lets the user select a room and request a time interval.
- Displays an Available / Unavailable decision with explanatory validation feedback.
- Uses interval-overlap logic where touching endpoints are allowed.
- The Aurora Hall sample data initially had two bookings (09:00–10:00 and 13:00–14:00), not the required single 10:00–11:00 booking.
- The initial time parser and end-time input did not allow 24:00.

**Repair prompt** (only if the first build did not run — no repair prompt was needed):

```text
```

---

## 4. Task 3 — the nine cases

Base for every case unless the row says otherwise: **current time 09:00**, room **not blocked**,
the room's **only booking 10:00–11:00**. The Expected column comes from AC1–AC6 — do not change it.
Write each result exactly as **Available**, **Unavailable** or **Not testable** (the page gives you
no way to set up the case). Save each final run as `evidence/final-T<n>.png`.

| # | Case | What you set up and request | Expected | AC | Result on v1 | Result on final | Final screenshot |
| --- | --- | --- | --- | --- | --- | --- | --- |
| T1 | Touching | 11:00–12:00 | Available | AC4 | Available | Available | final-T1.png |
| T2 | Overlap | 10:30–11:30 | Unavailable | AC4 | Available | Unavailable | final-T2.png |
| T3 | Blocked | 11:00–12:00, room blocked | Unavailable | AC3 | Unavailable | Unavailable | final-T3.png |
| T4 | Exactly 2 hours | 12:00–14:00 | Available | AC2 | Unavailable | Available | final-T4.png |
| T5 | Over 2 hours | 12:00–14:01 | Unavailable | AC2 | Unavailable | Unavailable | final-T5.png |
| T6 | Starts now | 09:00–09:30 (current time 09:00) | Unavailable | AC1 | Unavailable | Unavailable | final-T6.png |
| T7 | Reversed times | 12:00–11:00, and the page says why | Unavailable | AC1, AC6 | Unavailable | Unavailable | final-T7.png |
| T8 | Same check twice | T1, then T1 again without reloading | Available | AC5 | Available | Available | final-T8.png |
| T9 | Narrow screen | T1 at about 375 px wide | Available | AC6 | Available | Available | final-T9.png |


---

## 5. Issue log — cleanup targets

One row per issue you chose to act on (or deliberately not act on). At least **two**: one
functional and one usability or code-quality issue when you have them. If v1 passed every case,
log a justified cleanup that preserves behaviour. Save a screenshot of each as
`evidence/issue-<n>.png`.

| # | Issue | Evidence: steps → expected → observed | Priority | Decision |
| --- | --- | --- | --- | --- |
| 1 | Test data differs from the required baseline | Set Aurora Hall, current time 09:00, and request 10:30–11:30 → expected Unavailable for the required 10:00–11:00 booking → the original page showed bookings 09:00–10:00 and 13:00–14:00 and returned Available (`evidence/issue-1.png`) | High | Fix |
| 2 | Time input cannot represent 24:00 | In the original page, set 23:00 and try to enter 24:00 → AC1 permits an end of 1440 → the native time field could not hold 24:00 (it displayed an empty time), and checking returned “Please enter valid times.” (`evidence/issue-2.png`; `original/project/src/lib/availability.ts`) | Medium | Fix |

---

## 6. Task 4 — cleanup with focused prompts

One issue per prompt. The two prompt texts below are reproduced as provided by the student. Bolt's response text below is a concise summary from the available notes, not a verbatim transcript.

**Functional fix prompt, as sent, and Bolt's answer:**

```text
In the current prototype, selecting Aurora Hall and requesting 10:30–11:30 produces Available, but AC4 requires Unavailable. Make the smallest change that fixes this behavior. Preserve the other acceptance criteria. Explain which file/component you changed and why.
```

Bolt's recorded answer (summary from the notes, not a verbatim transcript):

Updated `src/lib/data.ts`. Replaced Aurora Hall's two bookings with one booking from 10:00–11:00. The other fictional sample data and the existing AC1–AC6 logic were preserved.

**Cleanup prompt, as sent, and Bolt's answer:**

```text
Review only src/lib/availability.ts for unnecessary duplication, confusing naming, or UI feedback problems. Suggest one small cleanup. Do not add features or redesign the whole application. Implement it only if it preserves AC1–AC6.
```

Bolt's recorded answer (summary from the notes, not a verbatim transcript):

Updated `src/lib/availability.ts` so `parseTime` accepts 24:00 only as the end-of-day boundary, while preserving the existing validation rules. The end-time input in `src/App.tsx` was also updated so 24:00 can be typed.

**Every change or suggestion Bolt made, judged.** Accepting is a decision; so is rejecting. Cite
the AC (or the scope) that justifies it.

| # | What Bolt changed or suggested | accept / reject | Reason — cite the AC or the scope | Retest: which cases, result |
| --- | --- | --- | --- | --- |
| 1 | Replaced Aurora Hall's two bookings with one booking from 10:00–11:00 in `src/lib/data.ts` | accept | AC4: the overlap test must use the specified baseline data | Final T1–T9 retested in Chrome; all nine matched the expected results and have screenshots |
| 2 | Updated `parseTime` to support the 24:00 end-of-day boundary | accept | AC1 permits an end time of 1440 minutes | 23:00–24:00 was manually tested and returned Available |
| 3 | Updated the end-time input so the user can enter 24:00 | accept | AC1 permits the interval to end at 1440; the UI must let the user express that valid boundary | 23:00–24:00 was manually tested and returned Available |

---

## 7. Change log — v1 to final

Two to four concrete changes, each one retested.

| # | Issue | Decision | Change (file or component) | Result after retest |
| --- | --- | --- | --- | --- |
| 1 | Aurora Hall test data did not match the specified baseline. | Fix | `src/lib/data.ts`: changed Aurora Hall to one booking, 10:00–11:00. | Final T1–T9 all matched expected results in Chrome; screenshots are saved in evidence/. |
| 2 | The time parser rejected the valid 24:00 end boundary. | Fix | `src/lib/availability.ts`: accept `24:00` only as an end-of-day value. | 23:00–24:00 was manually tested and returned Available. |
| 3 | The end-time field itself did not allow typing 24:00. | Fix | Updated the end-time input in `src/App.tsx` while keeping start-time validation restricted. | 23:00–24:00 was manually tested and returned Available. |

---

## 8. One generated component, in my own words

Pick one file or component Bolt generated that matters for AC1–AC5 — the one that decides
availability is the best choice. Name its path in backticks, then explain in your own words, without
the assistant, what it does and how it decides. 60 words or more.

**File:** `src/lib/availability.ts`

<!-- Write your explanation below this line -->

The availability logic converts the requested start and end times into minutes so that comparisons are consistent. It first checks that the interval is valid and that the start is strictly later than the supplied current time. It then rejects intervals longer than 120 minutes, requests for blocked rooms, and intervals that overlap an existing booking. The overlap check uses the condition that the requested start is before an existing booking's end and the requested end is after its start. Because the comparisons are strict, a request that starts exactly when another booking ends is allowed. The function reports reasons for an unavailable result rather than silently changing bookings. Checking availability should be read-only, which is required by AC5.

---

## 9. What still fails, and what the criteria do not say

### 9.1 Checks I am keeping as FAIL or ERROR

The same IDs as `known_fails` in `submission.yml`. The latest checker run at commit `902a90a` is clean.

| Check | Why it stays |
| --- | --- |
| None | The checker reports 27 PASS, 0 FAIL and 0 ERROR. |

### 9.2 The end of the day

AC1 allows `end ≤ 1440` — a booking may end at 24:00. Can a user of your final page ask for
23:00–24:00? How — and if not, why is that acceptable or not? (This is the value you declare in
`submission.yml` under `assumptions.end_of_day`.)

The final page accepts 24:00 as an end time. I tested 23:00–24:00 and received Available. This supports AC1 because the interval ends at 1440 minutes, which is the allowed upper boundary.

### 9.3 Which "now"?

AC1 says "after the supplied current time". What did **v1** use as the current time, and what did
that mean for testing case T6?

v1 exposed a current-time value in the interface, but the recorded evidence does not establish that every test used a supplied current-time parameter independent of the real clock. Therefore T6's v1 observation is reported from the actual run at 09:00, not as proof of a general clock-injection mechanism.

---

## 10. Conclusion (120–180 words)

<!-- Answer all three, in your own words, without the assistant:
     (a) Which of your two predictions in section 2 was right, and what did v1 actually get wrong?
     (b) Which AI suggestion did you reject, or would have been wrong to accept, and why?
     (c) What is the difference between "the prototype looks finished" and "the prototype meets
         AC1-AC6" - shown with one case from section 4?
     Worthless: "Bolt made some mistakes and I fixed them."
     Worth everything: "T8 failed on v1: the Check button also added the booking to the list, so
     checking 11:00-12:00 a second time said Unavailable. AC5 says the check must not change the
     booking data." -->

My first prediction about overlap was partly right: the original page returned Available for 10:30–11:30, but its Aurora Hall bookings were 09:00–10:00 and 13:00–14:00 rather than the required 10:00–11:00 baseline. My second prediction about the supplied clock was inconclusive; the request starting at 09:00 returned Unavailable, but the saved evidence does not show how the clock was controlled. I accepted the baseline correction and the 24:00 boundary change. I would reject keeping the Supabase dependency present in v1 because this practice excludes backend services. A finished-looking page does not prove that it meets the criteria: T2 must reject 10:30–11:30 when 10:00–11:00 is the only booking. I ran T1–T9 on the final page; all matched the expected results, including the second T8 check and T9 at 375 px. The separate final screenshots show those runs.