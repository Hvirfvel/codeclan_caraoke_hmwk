import unittest
from src.song import Song

class TestSong(unittest.TestCase):
    def setUp(self):
        self.song = Song("Angels", "Robbie Williams")

    def test_song_has_title(self):
        self.assertEqual("Angels", self.song.title)

    def test_song_has_artist(self):
        self.assertEqual("Robbie Williams", self.song.artist)