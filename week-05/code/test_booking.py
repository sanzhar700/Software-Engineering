import unittest
from booking import can_book


class BookingTests(unittest.TestCase):
    def test_touching_end_is_allowed(self):
        self.assertIs(can_book(660, 720, 540, False, [(600, 660)]), True)

    def test_overlap_is_rejected(self):
        self.assertIs(can_book(630, 690, 540, False, [(600, 660)]), False)

    def test_blocked_room_is_rejected(self):
        self.assertIs(can_book(660, 720, 540, True, []), False)

    def test_exactly_two_hours_is_allowed(self):
        self.assertIs(can_book(600, 720, 540, False, []), True)

    def test_more_than_two_hours_is_rejected(self):
        self.assertIs(can_book(600, 721, 540, False, []), False)

    def test_starting_now_is_rejected(self):
        self.assertIs(can_book(540, 600, 540, False, []), False)

    def test_zero_duration_is_rejected(self):
        self.assertIs(can_book(600, 600, 540, False, []), False)

    def test_reversed_interval_is_rejected(self):
        self.assertIs(can_book(660, 600, 540, False, []), False)

    def test_negative_start_is_rejected(self):
        self.assertIs(can_book(-1, 60, 0, False, []), False)

    def test_end_after_1440_is_rejected(self):
        self.assertIs(can_book(1380, 1441, 1000, False, []), False)

    def test_end_at_1440_is_allowed(self):
        self.assertIs(can_book(1380, 1440, 1000, False, []), True)

    def test_empty_existing_bookings(self):
        self.assertIs(can_book(600, 660, 540, False, []), True)

    def test_overlap_with_later_booking_is_rejected(self):
        self.assertIs(
            can_book(700, 750, 600, False, [(600, 650), (740, 800)]),
            False
        )

    def test_proposed_booking_contains_existing(self):
        self.assertIs(can_book(600, 720, 540, False, [(630, 660)]), False)

    def test_existing_booking_contains_proposed(self):
        self.assertIs(can_book(630, 660, 540, False, [(600, 720)]), False)

    def test_existing_list_is_unchanged(self):
        existing = [(600, 660), (720, 780)]
        original = existing.copy()

        can_book(800, 860, 540, False, existing)

        self.assertEqual(existing, original)


    def test_blocked_room_with_overlap_is_rejected(self):
        result = can_book(630, 690, 540, True, [(600, 660)])
        self.assertIs(result, False)

    def test_invalid_booking_is_never_accepted(self):
        invalid_cases = [
            (540, 600, 540, False, []),              # starts now
            (600, 721, 540, False, []),              # over 120 minutes
            (600, 660, 540, True, []),               # blocked room
            (630, 690, 540, False, [(600, 660)]),    # overlaps
        ]

        for start, end, now, blocked, existing in invalid_cases:
            with self.subTest(start=start, end=end, blocked=blocked):
                self.assertIs(
                    can_book(start, end, now, blocked, existing),
                    False
                )

if __name__ == "__main__":
    unittest.main()