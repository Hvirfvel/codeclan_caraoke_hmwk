class Guest:
    def __init__(self, name, wallet):
        self.name = name
        self.wallet = wallet

    def reduce_wallet(self, guest, entry_fee):
        guest.wallet -= entry_fee
        # return guest.wallet
