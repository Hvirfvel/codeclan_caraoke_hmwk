import unittest
from src.room import Room
from src.song import Song
from src.guest import Guest

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room = Room("Unicorn", 2)
        self.guest_1 = Guest("Gördis", 50)
        self.guest_2 = Guest("Hugo", 40)
        self.guest_3 = Guest("Karl", 3)
        self.entry_fee = 5

    def test_room_has_name(self):
        self.assertEqual("Unicorn", self.room.name)

    def test_can_add_song_to_room(self):
        song = Song("I'm a barbie girl", "Aqua")
        self.room.add_song(song)
        self.assertEqual(1, len(self.room.songs))

    def test_check_in_guest(self):
        self.room.check_in_guest(self.guest_2)
        self.assertEqual(1, len(self.room.checked_in_guests))

    def test_can_remove_guest_from_room(self):
        self.room.check_in_guest(self.guest_1)
        self.room.check_out_guest(self.guest_1)
        self.assertEqual(0, len(self.room.checked_in_guests))

    def test_can_increase_total_cash(self):
        self.assertEqual(5, self.room.increase_total_cash(self.entry_fee))

    def test_room_has_capacity__returns_true(self):
        self.assertEqual(True, self.room.room_has_capacity(self.room))

    def test_room_has_capacity__returns_false(self):
        self.room.check_in_guest(self.guest_1)
        self.room.check_in_guest(self.guest_2)
        self.assertEqual(False, self.room.room_has_capacity(self.room))

    def test_guest_can_pay__returns_true(self):
        self.assertEqual(True, self.room.guest_can_pay(self.guest_2, self.entry_fee))

    def test_guest_can_pay__returns_false(self):
        self.assertEqual(False, self.room.guest_can_pay(self.guest_3, self.entry_fee))

    def test_can_check_in__room_has_capacity__returns_true(self):
        self.assertEqual(True, self.room.can_check_in(self.room, self.entry_fee, self.guest_1))

    def test_can_check_in__room_has_capacity__returns_false(self):
        room = Room("Cameleon", 1)
        room.check_in_guest(self.guest_1)
        self.assertEqual(False, self.room.can_check_in(room, self.entry_fee, self.guest_1))

    def test_can_check_in__guest_can_pay__returns_true(self):
        self.assertEqual(True, self.room.can_check_in(self.room, self.entry_fee, self.guest_1))

    def test_can_check_in__guest_can_pay__returns_false(self):
        self.assertEqual(False, self.room.can_check_in(self.room, self.entry_fee, self.guest_3))

    