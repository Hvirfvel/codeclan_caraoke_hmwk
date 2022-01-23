class Guest:
    def __init__(self, name, wallet, favourite_song):
        self.name = name
        self.wallet = wallet
        self.favourite_song = favourite_song

    def reduce_wallet(self, guest, entry_fee):
        guest.wallet -= entry_fee
