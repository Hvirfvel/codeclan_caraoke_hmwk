class Guest:
    def __init__(self, name, wallet, favourite_artist):
        self.name = name
        self.wallet = wallet
        self.favourite_artist = favourite_artist

    def reduce_wallet(self, guest, entry_fee):
        guest.wallet -= entry_fee
