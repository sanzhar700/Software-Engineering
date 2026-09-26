# Acceptance Criteria

## Assumptions

- A booking that ends exactly when another booking starts is not considered overlapping.
- A booking lasting exactly two hours is allowed.

## US-01 — View room availability

### AC-01 — Successful availability check
**Given** a Student selects a future date and time slot  
**When** the Student requests room availability  
**Then** the system displays the rooms available for that time slot.

### AC-02 — Future booking validation
**Given** a Student selects a time slot in the past  
**When** the Student requests room availability  
**Then** the system rejects the request and indicates that the time must be in the future.

### AC-03 — Blocked rooms
**Given** a room is blocked for the selected time slot  
**When** the Student requests room availability  
**Then** the blocked room is not shown as available.

### AC-04 — Maximum duration
**Given** a Student selects a future time slot  
**When** the selected duration is more than two hours  
**Then** the system rejects the request and indicates that the maximum duration is two hours.

---

## US-02 — Book a free room

### AC-05 — Successful booking
**Given** a room is free and not blocked  
**When** the Student selects a future time slot of up to two hours and confirms the booking  
**Then** the system creates the booking for the selected room and time slot.

### AC-06 — Past booking validation
**Given** the Student selects a time in the past  
**When** the Student attempts to book the room  
**Then** the system rejects the booking and indicates that bookings must be in the future.

### AC-07 — Maximum duration validation
**Given** the Student selects a future time slot  
**When** the requested booking duration is more than two hours  
**Then** the system rejects the booking and indicates that the maximum duration is two hours.

### AC-08 — Overlapping booking
**Given** a room already has a booking during the selected time  
**When** the Student attempts to book the same room for an overlapping time  
**Then** the system rejects the booking because the room is already reserved.

### AC-09 — Blocked room
**Given** a room is blocked during the selected time  
**When** the Student attempts to book the room  
**Then** the system rejects the booking and indicates that the room cannot be booked.

---

## US-04 — Receive booking/cancellation confirmation

### AC-10 — Booking confirmation
**Given** a Student successfully books a free room for a valid future time slot  
**When** the booking is recorded  
**Then** the system provides a confirmation of the booking.

### AC-11 — Cancellation confirmation
**Given** a Student has an existing booking  
**When** the Student successfully cancels the booking  
**Then** the system provides a confirmation of the cancellation.

### AC-12 — Invalid booking
**Given** a Student attempts to book a blocked room or overlapping time slot  
**When** the booking is rejected  
**Then** the system does not provide a successful booking confirmation and indicates that the booking failed.

### AC-13 — Invalid time
**Given** a Student attempts to book a time in the past or for more than two hours  
**When** the system validates the booking  
**Then** the system rejects the booking and does not send a booking confirmation.