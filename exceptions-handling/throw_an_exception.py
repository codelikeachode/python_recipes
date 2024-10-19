class Seller:
    def __init__(self):
        self.cars = []

    def sell(self):
        if len(self.cars) == 0:
            raise Exception("No cars for sale")


seller = Seller()
try:
    seller.sell()
except Exception as e:
    print(e.args[0])
    # e.args[0] is "No cars for sale"
