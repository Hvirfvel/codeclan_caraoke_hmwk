import unittest
from src.guest import Guest
# from src.room import Room

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest = Guest("Marie", 35, "A Thousand Miles")

    def test_guest_has_name(self):
        self.assertEqual("Marie", self.guest.name)

    def test_guest_has_wallet(self):
        self.assertEqual(35, self.guest.wallet)

    def test_guest_has_favourite_song(self):
        self.assertEqual("A Thousand Miles", self.guest.favourite_song)

    def test_wallet_is_decreased(self):
        entry_fee = 5
        self.guest.reduce_wallet(self.guest, entry_fee)
        self.assertEqual(30, self.guest.wallet)