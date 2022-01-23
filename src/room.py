import pdb
class Room:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.songs = []
        self.checked_in_guests = []
        self.total_cash = 0
        self.entry_fee = 5

    def add_song(self, song):
        self.songs.append(song)


    def check_in_guest(self, guest):
        self.checked_in_guests.append(guest)

    def check_out_guest(self, guest):
        self.checked_in_guests.remove(guest)

    def can_check_in(self, room, entry_fee, guest):
        if not self.room_has_capacity(room):
            return False
        if not self.guest_can_pay(guest, entry_fee):
            return False
        return True

    def guest_can_pay(self, guest, entry_fee):
        return guest.wallet >= entry_fee

    def increase_total_cash(self, amount):
        self.total_cash += amount
        return self.total_cash

    def room_has_capacity(self, room):
        return room.capacity > len(room.checked_in_guests)

  


        
