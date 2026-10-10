# Week 05 — Lab report

**Name:** [Sansyzbayev Sanzhar]  
**Group:** [Monday 16:00-19:00]  
**Date:** 2026-10-10

---

## 1. Setup

| Field | Value |
| --- | --- |
| Assistant (tool) | ChatGPT |
| Exact model name | GPT-6 |
| Language and version | Python 3.14.6 |
| Path | A |
| My Week 04 declaration for touching bookings | [SELECT: allowed / not-allowed / did not submit] |

If my Week 04 model said touching bookings were not allowed, AC4 changes that assumption: bookings may be consecutive when one interval ends exactly as the next begins.

---

## 2. Task 1 — the plan

**The assistant's plan, pasted unedited:**

```text
## 1. Implementation plan for `can_book`

Implement the function as a sequence of validation checks. Return `False` as soon as any rule fails. Return `True` only if all four acceptance criteria pass.

### Checks in order

1. Validate the time interval (AC1).
- Check that `0 <= start < end <= 1440`.
- Check that `start > now`.
- If any condition fails, return `False`.

2. Validate the duration (AC2).
- Calculate `end - start`.
- If the duration exceeds 120 minutes, return `False`.
- A duration of exactly 120 minutes is allowed.

3. Check whether the room is blocked (AC3).
- If `blocked` is `True`, return `False`.
- Otherwise, continue.

4. Check for overlapping bookings (AC4).
- Examine every `(existing_start, existing_end)` tuple in `existing`.
- An overlap exists if `start < existing_end` and `existing_start < end`.
- If any overlap exists, return `False`.
- If the intervals only touch at an endpoint, they are allowed.

5. Return the final decision (AC5).
- Return `True` if all checks pass.
- Never modify `existing` or any other input.

## 2. Assumptions

- Python 3: Use standard comparison and arithmetic operations; no external libraries are required.
- Valid existing bookings: Every tuple in `existing` already represents a valid, active booking for the selected room. No additional validation is necessary.
- Input types: `start` and `end` are integer minute values, `now` is valid, and `blocked` is Boolean. The contract does not specify behavior for incorrect input types.
- One date only: All times belong to the same date. Overnight bookings are not supported by this contract.
- Interval semantics: Intervals include their start and exclude their end: [start, end).
- Function responsibility: The function decides whether a booking is valid. Saving the booking and confirming it belong to the complete system, not this function.

## 3. Boundary cases to test

| Case | Example inputs or condition | Expected |
| --- | --- | --- |
| Start at midnight | start=0, end=60, now=1439 | False |
| Start equals current time | start=600, end=660, now=600 | False |
| Start one minute in the future | start=601, end=660, now=600 | True, if other rules pass |
| End at midnight boundary | start=1380, end=1440, now=1000 | True, if other rules pass |
| End exceeds 1440 | start=1380, end=1441 | False |
| Zero duration | start=600, end=600 | False |
| Reversed interval | start=660, end=600 | False |
| Exact maximum duration | start=600, end=720 | True, if other rules pass |
| Duration exceeds maximum by one minute | start=600, end=721 | False |
| Room blocked | Valid interval, blocked=True | False |
| Booking ends when existing booking starts | Proposed (600,660), existing (660,720) | True, if other rules pass |
| Booking starts when existing booking ends | Proposed (660,720), existing (600,660) | True, if other rules pass |
| Partial overlap | Proposed (600,660), existing (650,710) | False |
| Proposed booking contains existing booking | Proposed (600,720), existing (630,660) | False |
| Existing booking contains proposed booking | Proposed (630,660), existing (600,720) | False |
| Multiple existing bookings | No overlap with first booking, overlap with a later one | False |
| Empty existing list | Valid interval, existing=[] | True, if other rules pass |

## 2.1 What the plan invented or changed

| # | What the plan said | What the contract or the AC says | What I did |
| --- | --- | --- | --- |
| 1 | The plan assumes `existing` contains valid active bookings for the selected room and that all times belong to one date. | The contract explicitly says existing bookings are valid and active for the selected room, and times are for one date. | I kept these assumptions because they match the contract. |
| 2 | The plan says incorrect input types are not specified. | The contract says times are integers but does not define behavior for invalid types. | I did not add extra type validation. |

**Boundary cases the assistant suggested that I kept as tests:**

- Start equals the current time.
- End at 1440 and end beyond 1440.
- Zero duration and reversed interval.
- Exactly 120 minutes and 121 minutes.
- Blocked room.
- Touching endpoints and overlapping bookings.
- Multiple existing bookings and an empty list.
- Unchanged input list.

---

## 3. Task 2 — the first version (v1), read before it was run

v1 is saved as `code/original/booking_v1.py`, exactly as the assistant returned it: **yes**.

**AC map**

| # | Line in v1 | AC it implements | Correct as written? If not, why |
| --- | --- | --- | --- |
| 1 | `if not (0 <= start < end <= 1440 and start > now): return False` | AC1 | Yes. It checks the interval bounds, positive duration, and future start. |
| 2 | `if end - start > 120: return False` | AC2 | Yes. A duration of exactly 120 minutes is allowed. |
| 3 | `if blocked: return False` | AC3 | Yes. A blocked room is rejected. |
| 4 | `if start < existing_end and existing_start < end: return False` | AC4 | Yes. It rejects overlap and allows touching endpoints. |
| 5 | `return True` after all checks | AC5 | Yes. It returns true only after the earlier checks pass. |

**Anything in v1 that no AC asks for:**

No extra functionality was added. The function keeps the required signature, returns a Boolean decision, and does not save bookings or modify the input list.

---

## 4. Task 3 — my tests

Base input unless stated otherwise: `now=540, blocked=False, existing=[(600, 660)]`.

| # | Test name | Request (start, end) | What differs from the base input | Expected | AC | Result on v1 | Result on final |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | `test_touching_end_is_allowed` | (660, 720) | Touches existing end | True | AC4 | PASS | PASS |
| 2 | `test_overlap_is_rejected` | (630, 690) | Partial overlap | False | AC4 | PASS | PASS |
| 3 | `test_blocked_room_is_rejected` | (660, 720) | `blocked=True` | False | AC3 | PASS | PASS |
| 4 | `test_exactly_two_hours_is_allowed` | (600, 720) | Duration is 120 minutes | True | AC2 | PASS | PASS |
| 5 | `test_more_than_two_hours_is_rejected` | (600, 721) | Duration is 121 minutes | False | AC2 | PASS | PASS |
| 6 | `test_starting_now_is_rejected` | (540, 600) | Start equals now | False | AC1 | PASS | PASS |
| 7 | `test_zero_duration_is_rejected` | (600, 600) | Zero duration | False | AC1 | PASS | PASS |
| 8 | `test_reversed_interval_is_rejected` | (660, 600) | End before start | False | AC1 | PASS | PASS |
| 9 | `test_negative_start_is_rejected` | (-1, 60) | Negative start | False | AC1 | PASS | PASS |
| 10 | `test_end_after_1440_is_rejected` | (1380, 1441) | End exceeds day bound | False | AC1 | PASS | PASS |
| 11 | `test_end_at_1440_is_allowed` | (1380, 1440) | End equals 1440 | True | AC1 | PASS | PASS |
| 12 | `test_empty_existing_bookings` | (600, 660) | `existing=[]` | True | AC4 | PASS | PASS |
| 13 | `test_overlap_with_later_booking_is_rejected` | (700, 750) | Overlaps second booking in `[(600,650),(740,800)]` | False | AC4 | PASS | PASS |
| 14 | `test_proposed_booking_contains_existing` | (600, 720) | Proposed interval contains existing | False | AC4 | PASS | PASS |
| 15 | `test_existing_booking_contains_proposed` | (630, 660) | Existing interval contains proposed | False | AC4 | PASS | PASS |
| 16 | `test_existing_list_is_unchanged` | (800, 860) | Check input preservation | True | AC5 | PASS | PASS |
| 17 | `test_blocked_room_with_overlap_is_rejected` | (630, 690) | `blocked=True` and overlap | False | AC3, AC4 | PASS | PASS |

The 17 tests passed in the reported final suite run.

---

## 5. Task 4 — debugging with evidence

The first implementation passed all F1–F10 functional checks. The checker also reported that v1 was identical to the final implementation. Therefore, no functional fix was made based on a failing F check. The following extra edge case was run as an additional check.

| # | Input (the full call) | Expected | Actual | Cause (quote the line) | Fix | Who proposed the fix |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | `can_book(800, 860, 540, False, [])` | True | [RUN THIS CALL AND ENTER THE ACTUAL RESULT] | The interval is in the future, lasts 60 minutes, the room is not blocked, and there are no existing bookings. | No change if actual is True. | Student, based on AC1–AC5 |

**The debug prompt I sent, and the assistant's answer** (leave empty if not used):

```text
Not used. The initial implementation passed the functional checks, so I did not use the debugging prompt for a failing F check.
```

---

## 6. Task 5 — the critique

**The assistant's critique:**

```text
1. The function checks the time interval and future start condition in one compound condition. This still implements AC1 correctly.
2. The duration check uses `end - start > 120`, so exactly 120 minutes is allowed as required by AC2.
3. The overlap check uses `start < existing_end and existing_start < end`, which rejects partial and contained overlaps while allowing touching endpoints under AC4.
4. The function does not explicitly validate input types. The contract does not define behavior for invalid types, so additional type validation is not required.
5. The function does not modify `existing` and returns a Boolean result, as required by AC5.
```

| # | Suggestion | accept / reject | Reason — cite the AC or contract line | Suite after the change |
| --- | --- | --- | --- | --- |
| 1 | Keep the compound AC1 condition | Accept | It checks `0 <= start < end <= 1440` and `start > now`, exactly as required by AC1. | 17 tests, OK |
| 2 | Keep the duration comparison `> 120` | Accept | AC2 allows durations of at most 120 minutes, so exactly 120 must pass. | 17 tests, OK |
| 3 | Keep the overlap condition | Accept | AC4 requires overlap rejection while allowing touching endpoints. | 17 tests, OK |
| 4 | Do not add input-type validation | Accept | The contract does not define behavior for invalid input types; extra validation is not required. | 17 tests, OK |
| 5 | Keep the Boolean result and avoid modifying inputs | Accept | AC5 explicitly requires a Boolean decision and unchanged inputs. | 17 tests, OK |

---

## 7. Change log — v1 to final

| # | What changed (the line, before → after) | Why | Evidence: the test or check that moved |
| --- | --- | --- | --- |
| 1 | `test_booking.py`: one starter test → 16 tests | Added tests for AC1–AC5, boundaries, overlaps, and input preservation. | The suite reported 16 tests, OK. |
| 2 | Added `test_blocked_room_with_overlap_is_rejected` | Added a case where the request is blocked and overlaps an existing booking. | The suite reported 17 tests, OK. M10 remained FAIL. |
| 3 | `booking.py`: no functional change from v1 | v1 passed F1–F10, and the checker reported that v1 and final are identical. | F1–F10 passed. |

---

## 8. Evidence — real output

### 8.1 My suite, final run

Paste the complete output from the actual terminal run of `python3 -m unittest -v` here. The latest reported run contained 17 tests and ended with `Ran 17 tests in 0.000s` and `OK`.

```text
[sanche@MacBook-Air-Sanzhar week-05 % cd ~/se-practice/week-05/code
python3 -m unittest -v
test_blocked_room_is_rejected (test_booking.BookingTests.test_blocked_room_is_rejected) ... ok
test_blocked_room_with_overlap_is_rejected (test_booking.BookingTests.test_blocked_room_with_overlap_is_rejected) ... ok
test_empty_existing_bookings (test_booking.BookingTests.test_empty_existing_bookings) ... ok
test_end_after_1440_is_rejected (test_booking.BookingTests.test_end_after_1440_is_rejected) ... ok
test_end_at_1440_is_allowed (test_booking.BookingTests.test_end_at_1440_is_allowed) ... ok
test_exactly_two_hours_is_allowed (test_booking.BookingTests.test_exactly_two_hours_is_allowed) ... ok
test_existing_booking_contains_proposed (test_booking.BookingTests.test_existing_booking_contains_proposed) ... ok
test_existing_list_is_unchanged (test_booking.BookingTests.test_existing_list_is_unchanged) ... ok
test_invalid_booking_is_never_accepted (test_booking.BookingTests.test_invalid_booking_is_never_accepted) ... ok
test_more_than_two_hours_is_rejected (test_booking.BookingTests.test_more_than_two_hours_is_rejected) ... ok
test_negative_start_is_rejected (test_booking.BookingTests.test_negative_start_is_rejected) ... ok
test_overlap_is_rejected (test_booking.BookingTests.test_overlap_is_rejected) ... ok
test_overlap_with_later_booking_is_rejected (test_booking.BookingTests.test_overlap_with_later_booking_is_rejected) ... ok
test_proposed_booking_contains_existing (test_booking.BookingTests.test_proposed_booking_contains_existing) ... ok
test_reversed_interval_is_rejected (test_booking.BookingTests.test_reversed_interval_is_rejected) ... ok
test_starting_now_is_rejected (test_booking.BookingTests.test_starting_now_is_rejected) ... ok
test_touching_end_is_allowed (test_booking.BookingTests.test_touching_end_is_allowed) ... ok
test_zero_duration_is_rejected (test_booking.BookingTests.test_zero_duration_is_rejected) ... ok

----------------------------------------------------------------------
Ran 18 tests in 0.000s

OK
sanche@MacBook-Air-Sanzhar code % ]
```

### 8.2 The checker, final run

Paste the complete output from the latest checker run here. The latest reported run was before completing this report and showed `SUMMARY pass=22 fail=10 error=0 (32 checks)`. Run the checker again after saving this report and replace this block with that new complete output.

```text
[PASTE THE COMPLETE LATEST CHECKER OUTPUT HERE]
```

### 8.3 Path B only — three faults I planted myself

Not applicable. I used Path A (Python).

---

## 9. What still fails, and what the contract does not say

### 9.1 Checks I am keeping as FAIL or ERROR

| Check | Why it stays |
| --- | --- |
| M10 | The current 17-test suite does not detect one deliberately faulty implementation violating AC5. This remains unresolved and needs another test that follows the contract. |
| L1–L9 | These report checks failed on the previous run because the report was incomplete. They must be checked again after this report is completed. |

### 9.2 Outside the contract

The contract specifies integer minute values but does not define behavior for other input types such as `600.5` or the string `"600"`. The function uses ordinary Python comparisons and arithmetic without explicit type validation. I did not add extra validation because it is outside the stated requirements. The required behavior for valid inputs is defined by AC1–AC5.

### 9.3 A bound that never decides

The lower bound `start >= 0` cannot be the only reason for rejecting a request. Since `now` is valid and non-negative, any negative `start` also fails `start > now`. Therefore, the future-start condition rejects that request as well.

---

## 10. Conclusion (120–180 words)

[

In this practice, I used AI assistance to implement and test the Smart Campus room booking function. The function checks whether a booking starts in the future, has a valid time interval, lasts no more than two hours, is not blocked, and does not overlap with existing bookings. I also checked that the original version was preserved and created a test suite to verify the required behavior.

The test suite currently contains 18 tests, and all of them pass. The booking checker passes the main functional checks, but it also reports that one deliberately faulty version, M10, is not detected by my tests. I will document this limitation honestly rather than claim that every defect has been caught. The submission report and validation results must also be checked before submitting the work.

This practice helped me understand that passing tests does not necessarily prove that a function is completely correct. Tests must cover the acceptance criteria and possible edge cases. AI assistance can speed up implementation, but I still need to review the generated code, verify the results, and explain the decisions made during development.]
