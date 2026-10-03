# Week 04 — Lab report: Modeling the System with UML

## 1. Setup

| Field | Value |
| --- | --- |
| Name | Sanzhar Sansyzbayev |
| Group | KBTU |
| AI assistant | ChatGPT |
| Exact model | GPT-5.6 Luna |
| Renderer | PlantUML web editor |
| Behaviour diagram | sequence |
| Stories used | my week-03 stories, revised |

---

## 2. Prompts as sent

### 2.1 Task 1 — use-case prompt

```text
Using the supplied scenario and approved stories, generate PlantUML for a use-case diagram. Include Student and Administrator outside a named system boundary. Model their goals, show justified associations, and list assumptions. Use include or extend only with a clear reason.

2.2 Task 2 — class prompt
Create a UML domain class diagram in PlantUML for Smart Campus. Start with Student, Room, and Booking. Add attributes, appropriate operations, and association multiplicities. Add other classes only when requirements justify them. Explain each relationship and list assumptions. Avoid unjustified inheritance or composition.

2.3 Task 3 — behaviour prompt (3A sequence)
Generate PlantUML for Book room. Use Student, BookingService, and BookingRepository lifelines. Validate the supplied rules, then attempt the reservation. Show a successful confirmation and an unavailable-room alternative using alt. Label messages and replies. Explain new design components and all assumptions.

2.4 Focused correction prompts (if you sent any)
none

2.5 Critique prompt
Compare my diagrams with the requirements. Identify missing rules, inconsistent names, and unjustified elements. Cite each issue and propose a specific correction.

| # | Element | Problem | Rule or story | Fix |
| --- | --- | --- | --- | --- |
| 1 | Student → UC-04 Receive confirmation | The original model directly associated Student with the confirmation use case, although confirmation is an outcome of booking/cancellation rather than a separate actor goal. | R4 and US-04 | Removed the direct Student → UC-04 association and modeled confirmation through `<<include>>`. |
| 2 | Business rules note | The original AI response used incorrect rule numbers: duration was labeled R2 and blocked-room booking was labeled R4. | R1-R4 | Corrected the rule numbering and definitions. |
| 3 | UC-02 → UC-04 | The original include lacked a clear reason comment. | PlantUML review convention | Added a `why:` comment explaining that successful booking produces confirmation. |

4. Task 2 — class diagram review
4.1 Relationships, read both ways
Association	Read left → right	Read right → left	Multiplicities
Student — Booking	One Student makes zero or more bookings.	Each Booking belongs to exactly one Student.	1 / 0..*
Room — Booking	One Room has zero or more bookings over time.	Each Booking reserves exactly one Room.	1 / 0..*

4.2 Constraints the multiplicities cannot show
- R2: A note on Booking states that active bookings for the same room cannot overlap.
- R1: The Booking note states that the booking starts in the future and has a duration greater than 0 and at most 2 hours.
- R3: The Booking note states that a blocked room cannot accept a new booking.
- R4: The Booking note states that a successful booking produces a confirmation.
4.3 Assumptions
- A1: Each Booking belongs to exactly one Student.
- A2: Each Booking reserves exactly one Room.
- A3: Touching bookings such as 10:00–12:00 and 12:00–13:00 do not overlap.
- A4: Blocking a room does not cancel or modify existing bookings.
- A5: Administrator remains an actor and is not modeled as a domain class.
- A6: Confirmation is system behavior and is not modeled as a separate domain class.
4.4 Findings
#	Element	Problem	Rule or story	Fix
1	Booking constraints	The original AI assigned the wrong rule numbers and described R2 as a duration constraint.	R1-R4	Replaced the original constraints with the correct R1-R4 definitions.
2	Administrator	The original AI added Administrator as a domain class even though it is primarily an actor in the scenario.	Task 2 requirement	Removed Administrator from the revised domain class diagram.
3	Booking → Room / Student	The original AI duplicated relationships already represented by the two associations with multiplicities.	UML association structure	Removed the duplicate directional relationships.
4	Booking isValid()	The original AI added an operation that was not explicitly required by the scenario.	Task 2 requirement to add classes/operations only when justified	Removed isValid().


5. Task 3 — behaviour diagram review
Option chosen and why: 3A sequence, because it shows the booking interaction between the Student and the design components used to validate and save a booking.
Design components added beyond the domain model: BookingService validates the booking request and coordinates the reservation; BookingRepository checks availability and saves a successful booking.

| # | Element | Problem | Rule or story | Fix |
| --- | --- | --- | --- | --- |
| 1 | Booking flow | The behaviour model must not save a booking before validation and availability checks. | R1, R2, R3 | The revised sequence validates the time first, checks availability, and saves only on the successful branch. |
| 2 | Failure branches | A failed booking must not be saved. | Booking requirements | The unavailable and invalid branches return to Student without a save operation. |

| # | Issue the AI raised | Element it cited | Verdict | Why |
| --- | --- | --- | --- | --- |
| 1 | The class model should keep the domain model focused on Student, Room and Booking. | Class diagram | accept | These are the core domain concepts required by the scenario. |
| 2 | Administrator should not automatically be treated as a domain entity merely because it is an actor. | Administrator | accept | Administrator is an actor with responsibilities; the revised domain model does not require an Administrator class. |
| 3 | The behaviour components are design components rather than domain entities. | BookingService, BookingRepository | accept | They are used to model the interaction flow and are explicitly explained in §5. |

| Requirement / story | Use case | Classes | Behaviour element |
| --- | --- | --- | --- |
| R1 | UC-02 Book room | Student, Booking, Booking.startTime, Booking.endTime | `validate future start and duration` |
| R2 | UC-02 Book room | Booking, Room | `check availability(room, start, end)` |
| R3 | UC-02 Book room | Room.blocked, Booking | `check availability(room, start, end)` and unavailable branch |
| R4 | UC-02 Book room | Booking | `confirmation` reply after booking is created |
| US-01 | UC-01 View availability | Student, Room, Booking | Availability information |
| US-02 | UC-02 Book room | Student, Room, Booking | `bookRoom(room, start, end)` |
| US-03 | UC-03 Cancel booking | Student, Booking | Cancel booking behavior |
| US-04 | UC-04 Receive confirmation | Student, Booking | Confirmation after booking/cancellation |
| US-05 | UC-05 Block room | Administrator, Room | Block room behavior |
| US-06 | UC-06 Unblock room | Administrator, Room | Unblock room behavior |
| US-07 | UC-07 Review room usage | Administrator, Room, Booking | Review usage behavior |

| # | Diagram | Before (AI's original) | After (your revision) | Reason |
| --- | --- | --- | --- | --- |
| 1 | use case | Direct Student association with confirmation and incorrect rule numbering. | Confirmation is included from booking/cancellation and R1-R4 are corrected. | R4 and approved stories; UML use-case semantics. |
| 2 | class | Administrator class, duplicated relationships, and incorrect R2/R4 definitions. | Domain model contains Student, Room and Booking with two clean associations and corrected constraints. | Domain-model scope and R1-R4. |
| 3 | sequence | Initial booking flow generated by AI. | Validation and availability checks occur before save; failure branches do not save. | R1-R3 and booking behavior. |


9. Checker output
Week 04 structural check - shape only, never quality

UC1  PASS  Student and Administrator declared
UC2  PASS  named system boundary: "Smart Campus Study Room Booking System"
UC3  PASS  all actors declared outside the boundary
UC4  PASS  all scenario goals present (7 use cases)
UC5  PASS  no actor is associated with a confirmation use case
UC6  PASS  actor responsibilities match the scenario
UC7  PASS  use cases are goals, not screens or components
UC8  PASS  every include / extend / generalization carries a ' why: comment (or there are none)
UC9  PASS  revised diagram differs from the AI's original
CL1  PASS  Student, Room and Booking present
CL2  PASS  Booking is associated with Student and with Room
CL3  PASS  every association has multiplicities at both ends
CL4  PASS  1 student / 1 room per booking, 0..* bookings per student and per room
CL5  PASS  every inheritance / composition / aggregation carries a ' why: comment (or there are none)
CL6  PASS  only domain concepts in the class diagram
CL7  PASS  attributes needed by R1-R3 are present
CL8  PASS  a note states R2 (no overlapping active bookings)
SQ1  PASS  Student, BookingService and BookingRepository lifelines present
SQ2  PASS  alt block with a guard on every branch (4 branches)
SQ3  PASS  validation happens before creation
SQ4  PASS  nothing is saved on a failure branch
SQ5  PASS  every message is labelled
SQ6  PASS  R1 (time range) is visible - checked or stated as a precondition
SQ7  PASS  R3 (blocked room) is visible
FI1  FAIL  missing: original/sequence.puml
FI2  FAIL  missing rendered image: img/class.png|svg, img/sequence.png|svg
LR1  FAIL  §1 not filled: name, ai assistant, exact model, behaviour diagram
LR2  FAIL  §2 needs the task 1, 2, 3 and critique prompts pasted (found 0)
LR3  FAIL  §3 needs at least 2 filled findings (found 0)
LR4  FAIL  §4.1 needs every association read both ways (found 0 rows); §4.3 declares no assumption
LR5  FAIL  §5 needs at least 1 filled finding
LR6  FAIL  §6 needs at least 3 critique rows with accept / reject (found 0)
LR7  FAIL  §8 needs >= 3 rows and one per diagram (rows: 0, missing: use case, class, behaviour)
CS1  PASS  7 approved stories
CS2  FAIL  §7 has no filled row for: R1, R2, R3, R4
CS3  FAIL  use case(s) with no §7 row tracing to an approved story: UC-01\nView availability, UC-02\nBook room, UC-03\nCancel booking, UC-04\nReceive confirmation, UC-05\nBlock room, UC-06\nUnblock room, UC-07\nReview room usage
CS4  FAIL  lifeline(s) neither in the class diagram nor explained in §5: BookingRepository

SUMMARY pass=25 fail=12 error=0
A FAIL you report and explain costs you nothing. One you hide costs the criterion.

FAILs I am keeping, and why:
- FI1 — the original sequence file existed when reviewed, so this was a stale checker result before the file was saved.
- FI2 — the rendered class and sequence images were created after this checker run.
- LR1 — fixed by filling §1.
- LR2 — fixed by filling all required prompts in §2.
- LR3 — fixed by adding findings in §3.
- LR4 — fixed by completing relationship readings and assumptions in §4.
- LR5 — fixed by adding behaviour-diagram findings in §5.
- LR6 — fixed by adding three critique rows in §6.
- LR7 — fixed by adding three change-log rows in §8.
- CS2 — fixed by adding R1-R4 traceability in §7.
- CS3 — fixed by adding all seven approved stories in §7.
- CS4 — BookingRepository is a design component rather than a domain class and is explained in §5.

10. Conclusion (120–180 words)
The class diagram was the part where the AI introduced the most important modeling errors. The original response mixed the business-rule numbering: it treated the two-hour duration as R2 even though the supplied requirements place the duration constraint in R1, and it treated the blocked-room rule as R4 instead of R3. It also added Administrator as a domain class and duplicated the Student/Booking and Room/Booking relationships with additional directional links. These issues could have propagated into an implementation by giving developers the wrong interpretation of booking validation and by encouraging unnecessary domain objects and relationships.
The review corrected the rule definitions, kept Student, Room and Booking as the core domain concepts, and removed the duplicate relationships. The sequence diagram was also checked so validation and availability happen before a booking is saved and failure branches do not save anything. The review process showed why the AI-generated diagrams cannot simply be accepted without checking them against the supplied rules and user stories.
