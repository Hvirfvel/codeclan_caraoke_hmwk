import pdb
class Room:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.songs = []
        self.checked_in_guests = []
        self.total_cash = 100.00
        self.entry_fee = 5

    def add_song(self, song):
        self.songs.append(song)

    def can_check_in(self, room, entry_fee, guest):
        if not self.room_has_capacity(room):
            return False
        if not self.guest_can_pay(guest, entry_fee):
            return False
        return True

    def check_in_guest(self, room, entry_fee, guest):
        if self.can_check_in(room, entry_fee, guest):
            self.checked_in_guests.append(guest)
            guest.reduce_wallet(guest, entry_fee)
            self.increase_total_cash(entry_fee)
    
    def increase_total_cash(self, amount):
        self.total_cash += amount

    def check_out_guest(self, guest):
        self.checked_in_guests.remove(guest)

    def guest_can_pay(self, guest, entry_fee):
        return guest.wallet >= entry_fee

    def room_has_capacity(self, room):
        return room.capacity > len(room.checked_in_guests)
  
    def room_has_favourite_artist(self, guest):
        for song in self.songs:
            if not song.artist == guest.favourite_artist:
                return False
        return True

    def list_songs_by_favourite_artist(self, guest):
        if self.room_has_favourite_artist(guest):
            titles_by_favourite_artist = [song.title for song in self.songs if song.artist == guest.favourite_artist]
        return titles_by_favourite_artist
    
