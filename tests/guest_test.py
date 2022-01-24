import unittest
from src.guest import Guest
# from src.room import Room

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest = Guest("Marie", 35, "Whitney Houston")

    def test_guest_has_name(self):
        self.assertEqual("Marie", self.guest.name)

    def test_guest_has_wallet(self):
        self.assertEqual(35, self.guest.wallet)

    def test_guest_has_favourite_artist(self):
        self.assertEqual("Whitney Houston", self.guest.favourite_artist)

    def test_wallet_is_decreased(self):
        entry_fee = 5
        self.guest.reduce_wallet(self.guest, entry_fee)
        self.assertEqual(30, self.guest.wallet)