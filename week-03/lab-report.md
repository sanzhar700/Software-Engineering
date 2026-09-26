# Lab report — Practice #03, Requirements Engineering with AI

Fill in every section. **Do not delete or renumber the headings** — the README points at them and a
missing heading reads as a missing section.

Name:
Student ID:
GitHub username:

---

## 1. Setup

| | |
| --- | --- |
| AI assistant (tool) | |
| Exact model name and version | |
| Date of the session | |
| Diagram renderer used | |

One tool and one model for all three prompts. If you switched, say why here — it changes what your
findings mean.

---

## 2. Original AI output — user stories (Part 1)

Paste the **unedited** response to Prompt 1. Do not tidy it. If it is long, paste all of it anyway;
this is the baseline everything else is measured against.

```
(Ниже — 8 user stories, строго в рамках заданных 2 ролей и 6 функций. Ничего про оплату, QR, уведомления и т. п. не добавляю.

Student goals
Find available rooms and time slots.
Book a free room.
Cancel their own booking.
Receive confirmation of booking/cancellation.
Administrator goals
Block or unblock rooms.
Review room usage.
Receive/use booking and cancellation confirmations as part of the system process.
#	User Story	Priority	Assumption
US-01	As a Student, I want to view room availability, so that I can find a free room for my study session.	High	Availability information reflects the current booking status of rooms.
US-02	As a Student, I want to book a free room for a time slot, so that I can reserve it for individual or group study.	High	The selected room is free and not blocked at the requested time.
US-03	As a Student, I want to cancel a booking I made, so that the room becomes available again.	High	The booking being cancelled was made by the Student.
US-04	As a Student, I want to receive a confirmation when I book a room, so that I know my reservation was recorded.	Medium	The booking satisfies all four business rules.
US-05	As a Student, I want to receive a confirmation when I cancel a booking, so that I know the reservation was released.	Medium	The cancellation is for an existing booking made by the Student.
US-06	As an Administrator, I want to block a room, so that it cannot be booked while it is unavailable.	High	A blocked room cannot be booked.
US-07	As an Administrator, I want to unblock a room, so that it can become available for booking again.	High	The room is currently blocked.
US-08	As an Administrator, I want to review room usage over a period, so that I can see how the study rooms are being used.	Medium	Usage information is available for the selected period.

Проверка соответствия: все 6 use cases покрыты; actors — только Student и Administrator; бизнес-правила R1–R4 не нарушены и не добавлены новые правила.)
```

---

## 3. Story review (Part 2)

One row per change you made. "Kept unchanged" is a valid row and needs a reason too.

| Story (as generated) | What I did | Why | Final ID |
| --- | --- | --- | --- |
| US-01: view room availability | Kept unchanged | It names the Student stakeholder, has one clear outcome, gives a valid reason, and stays within the scenario. | US-01 |
| US-02: book a free room | Kept unchanged | It describes one clear booking outcome and its assumption is consistent with the scenario and R4. | US-02 |
| US-03: cancel a booking | Rewritten slightly | The original reason said the room becomes available again. The scenario explicitly says a cancellation releases the reservation, so the reason was narrowed to the supported outcome. | US-03 |
| US-04: receive confirmation when booking | Merged with the cancellation confirmation story | Booking and cancellation confirmation are the same business outcome represented by UC-06 Send confirmation. Combining them avoids two stories for the same confirmation goal. | US-04 |
| US-05: receive confirmation when cancelling | Merged with the booking confirmation story | It duplicates the confirmation goal already covered by the booking confirmation story. | US-04 |
| US-06: block a room | Kept as a separate story | Blocking is one clear Administrator goal and directly corresponds to part of UC-04. | US-05 |
| US-07: unblock a room | Kept as a separate story | Unblocking is a separate, testable Administrator goal and together with blocking covers UC-04. | US-06 |
| US-08: review room usage | Kept unchanged | It names Administrator, describes one clear outcome, and directly corresponds to UC-05. | US-07 |

**Did the assistant invent anything outside the scenario?** Name it No major out-of-scope functionality was invented in the eight stories. I checked the stories against the explicit out-of-scope list, including payments, fees, fines, check-in, QR codes, equipment, maintenance, extra notifications, authentication, waiting lists, screens, databases, and servers.

**How many stories did you end with, and why that number?**

I ended with 7 stories. The original 8 stories were reviewed individually. The two confirmation stories were merged because both describe the same confirmation goal covered by UC-06, while the blocking and unblocking goals were kept separate because they are distinct Administrator actions.

---

## 4. Original AI output — acceptance criteria (Part 3)

```
(US-01 — View room availability

Assumptions:

Availability information is provided for the requested time slot.
The system knows which rooms are currently blocked.

Acceptance Criteria:

Successful availability check
Given a Student selects a future date and time slot
When the Student requests room availability
Then the system displays the rooms available for that time slot.
Future booking validation
Given a Student selects a time slot in the past
When the Student requests room availability
Then the system rejects the request and indicates that the time must be in the future.
Blocked rooms
Given a room is blocked for the selected time slot
When the Student requests room availability
Then the blocked room is not shown as available.
Maximum duration
Given a Student selects a future time slot
When the selected duration is more than two hours
Then the system rejects the request and indicates that the maximum duration is two hours.
US-02 — Book a free room

Assumptions:

The Student is allowed to book study rooms.
The selected room is free and not blocked at the requested time.
Bookings must be made for a future time and can last no more than two hours.

Acceptance Criteria:

Successful booking
Given a room is free and not blocked
When the Student selects a future time slot of up to two hours and confirms the booking
Then the system creates the booking for the selected room and time slot.
Past booking validation
Given the Student selects a time in the past
When the Student attempts to book the room
Then the system rejects the booking and indicates that bookings must be in the future.
Maximum duration validation
Given the Student selects a future time slot
When the requested booking duration is more than two hours
Then the system rejects the booking and indicates that the maximum duration is two hours.
Overlapping booking
Given a room already has a booking during the selected time
When the Student attempts to book the same room for an overlapping time
Then the system rejects the booking because the room is already reserved.
Blocked room
Given a room is blocked during the selected time
When the Student attempts to book the room
Then the system rejects the booking and indicates that the room cannot be booked.
US-04 — Receive booking/cancellation confirmation

Assumptions:

The system sends a confirmation after a successful booking or cancellation.
A confirmation is not sent when the requested action fails.

Acceptance Criteria:

Booking confirmation
Given a Student successfully books a free room for a valid future time slot
When the booking is recorded
Then the system provides a confirmation of the booking.
Cancellation confirmation
Given a Student has an existing booking
When the Student successfully cancels the booking
Then the system provides a confirmation of the cancellation.
Invalid booking
Given a Student attempts to book a blocked room or overlapping time slot
When the booking is rejected
Then the system does not provide a successful booking confirmation and indicates that the booking failed.
Invalid time
Given a Student attempts to book a time in the past or for more than two hours
When the system validates the booking
Then the system rejects the booking and does not send a booking confirmation.)
```

---

## 5. Criteria review (Part 3)

## 5. Acceptance-Criteria Review

| ID | Decision | Reason |
|---|---|---|
| AC-01 | Kept | Defines the successful availability-check behavior and is testable. |
| AC-02 | Kept | Covers invalid past time input. |
| AC-03 | Kept | Ensures blocked rooms are not treated as available. |
| AC-04 | Kept | Covers the maximum two-hour duration rule. |
| AC-05 | Kept | Defines the successful room-booking outcome. |
| AC-06 | Kept | Covers the future-booking rule. |
| AC-07 | Kept | Covers the maximum booking duration rule. |
| AC-08 | Kept | Covers the no-overlap business rule. |
| AC-09 | Kept | Covers the blocked-room business rule. |
| AC-10 | Kept | Covers confirmation after successful booking. |
| AC-11 | Kept | Covers confirmation after successful cancellation. |
| AC-12 | Rewritten | Clarified that failed booking attempts do not produce a successful confirmation. |
| AC-13 | Rewritten | Clarified the invalid-time cases and confirmation behavior. |

### Open-question decisions

1 A booking that ends exactly when another booking starts is not considered overlapping.
2 A booking lasting exactly two hours is allowed.

| Question | My decision | Why |
| --- | --- | --- |
| A booking ending exactly when another begins — overlap under R3? | allowed / not-allowed | |
| Is exactly two hours allowed under R2? | allowed / not-allowed | |

**Which invalid or boundary case did the assistant leave out?**

---

## 6. Original AI output — use-case diagram (Part 4)

```
(```plantuml
@startuml

left to right direction

actor Student
actor Administrator

rectangle "Smart Campus — KBTU Library Study Room Booking" {

  usecase "UC-01 View availability" as UC01
  usecase "UC-02 Book room" as UC02
  usecase "UC-03 Cancel booking" as UC03
  usecase "UC-04 Block or unblock room" as UC04
  usecase "UC-05 Review usage" as UC05
  usecase "UC-06 Send confirmation" as UC06
}

Student --> UC01
Student --> UC02
Student --> UC03

Administrator --> UC04
Administrator --> UC05

UC02 ..> UC06 : <<include>>

@enduml
```
)
```

Rendered diagram (image, or a link):

---

## 7. Diagram review (Part 4)
## 7. Use-Case Diagram Review

The generated diagram contained the required two actors and six use cases. The system boundary and actor associations were appropriate.

One issue was identified: UC-06 Send confirmation was connected only to UC-02 Book room. Since confirmation is also required after a successful cancellation, the diagram was revised to include UC-03 Cancel booking -> UC-06 Send confirmation.

No additional actors, use cases, databases, screens, or other out-of-scope components were added.

**Associations.** Which actor–use-case links did the assistant draw that a person does not actually
trigger? Name them.

**Did any screen, database or internal component appear as a use case or an actor?**

---

## 8. Traceability (Part 5)

The traceability table shows that all six required use cases have corresponding user stories, and every final user story is traced to a use case.

- Use cases with **no story** behind them: none.
- Stories with **no use case** they belong to: none.
- Criteria that test **no rule** from section 1: AC-01, AC-10, AC-11.

The largest gap is not a missing story but the limited acceptance-criteria coverage for UC-04 and UC-05. The acceptance-criteria generation covered only US-01, US-02 and US-04, so the Administrator use cases for blocking/unblocking rooms and reviewing usage do not have dedicated acceptance criteria in this iteration.

---

## 9. Checker runs

Paste the **real terminal output** of both runs. A table with nothing behind it does not count.

```
$ python tests/check_requirements.py
($ python3 tests/check_requirements.py

PASS   US-1  user-stories.md         no placeholders left
PASS   US-2  user-stories.md         7 stories, IDs US-01…US-07
PASS   US-3  user-stories.md         every story has the required sentence shape
PASS   US-4  user-stories.md         every story has a priority
PASS   US-5  user-stories.md         every story declares an assumption
PASS   US-6  user-stories.md         only Student and Administrator appear as roles
PASS   US-7  user-stories.md         nothing from the out-of-scope list appears
PASS   AC-1  acceptance-criteria.md  no placeholders left
PASS   AC-2  acceptance-criteria.md  three sections, all naming real stories: US-01, US-02, US-04
PASS   AC-3  acceptance-criteria.md  every section has 3 to 5 uniquely numbered criteria
PASS   AC-4  acceptance-criteria.md  all 13 criteria are complete Given/When/Then
PASS   AC-5  acceptance-criteria.md  every section covers an invalid or boundary case
PASS   AC-6  acceptance-criteria.md  2 assumptions listed before the criteria
PASS   AC-7  acceptance-criteria.md  both open questions are settled in the assumptions
PASS   PU-1  use-cases.puml          valid PlantUML block, no placeholders
PASS   PU-2  use-cases.puml          exactly two actors: Student, Administrator
PASS   PU-3  use-cases.puml          all six use cases present
PASS   PU-4  use-cases.puml          system boundary present
PASS   PU-5  use-cases.puml          no screens, databases or internal components
PASS   PU-6  use-cases.puml          no unjustified actor associations found
PASS   TR-1  traceability.md         all six use cases have a row
PASS   TR-2  traceability.md         every ID in the table resolves
PASS   TR-3  traceability.md         every story appears in the table
------------------------------------------------------------------------
23 PASS · 0 FAIL · 0 ERROR   (23 checks)
Shape is clean. This says nothing about whether the requirements are good.)
```

```
$ python tests/validate_submission.py
(sanche@MacBook-Air-Sanzhar week-03 % python3 tests/check_requirements.py
PASS   US-1  user-stories.md         no placeholders left
PASS   US-2  user-stories.md         7 stories, IDs US-01…US-07
PASS   US-3  user-stories.md         every story has the required sentence shape
PASS   US-4  user-stories.md         every story has a priority
PASS   US-5  user-stories.md         every story declares an assumption
PASS   US-6  user-stories.md         only Student and Administrator appear as roles
PASS   US-7  user-stories.md         nothing from the out-of-scope list appears
PASS   AC-1  acceptance-criteria.md  no placeholders left
PASS   AC-2  acceptance-criteria.md  three sections, all naming real stories: US-01, US-02, US-04
PASS   AC-3  acceptance-criteria.md  every section has 3 to 5 uniquely numbered criteria
PASS   AC-4  acceptance-criteria.md  all 13 criteria are complete Given/When/Then
PASS   AC-5  acceptance-criteria.md  every section covers an invalid or boundary case
PASS   AC-6  acceptance-criteria.md  2 assumptions listed before the criteria
PASS   AC-7  acceptance-criteria.md  both open questions are settled in the assumptions
PASS   PU-1  use-cases.puml          valid PlantUML block, no placeholders
PASS   PU-2  use-cases.puml          exactly two actors: Student, Administrator
PASS   PU-3  use-cases.puml          all six use cases present
PASS   PU-4  use-cases.puml          system boundary present
PASS   PU-5  use-cases.puml          no screens, databases or internal components
PASS   PU-6  use-cases.puml          no unjustified actor associations found
PASS   TR-1  traceability.md         all six use cases have a row
PASS   TR-2  traceability.md         every ID in the table resolves
PASS   TR-3  traceability.md         every story appears in the table
------------------------------------------------------------------------
23 PASS · 0 FAIL · 0 ERROR   (23 checks)
Shape is clean. This says nothing about whether the requirements are good.)
```

| | PASS | FAIL | ERROR |
| --- | --- | --- | --- |
| `check_requirements.py` | | | |

Commit these numbers were produced at (`git rev-parse --short HEAD`):

**Every FAIL, one line each: what it is and what you decided to do about it.** A FAIL you report and
explain costs you nothing.

**Did you run the checks by hand instead of with Python?** Say so here — it costs nothing, but it
has to be said.

---

## 10. Conclusion (150–200 words)

Answer all three:

## 10. Conclusion

The most important problem in the generated requirements was the confirmation functionality. The first AI output created two separate confirmation stories, one for booking and one for cancellation, even though both represent the same confirmation goal covered by UC-06. I caught this by manually comparing the generated stories with the six fixed use cases and checking whether each story represented a distinct stakeholder goal. The UML output also connected UC-06 only to booking, so I revised it to include cancellation confirmation.

The assistant did several things correctly that would have taken longer to create manually. It produced seven structured user stories with priorities and assumptions, generated 13 Given/When/Then acceptance criteria covering the main business rules, and created a complete PlantUML diagram with the required actors and six use cases. The automated checker confirmed that all 23 structural checks passed.

If I could rewrite one requirement first, I would rewrite US-04, the confirmation story. It should explicitly state that confirmation is provided after both successful booking and successful cancellation. This would make the requirement clearer for an implementer and keep the relationship with UC-06 unambiguous..
