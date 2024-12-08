class Counter:
    def __init__(self):
        self.count = 0

    def inc_by(self, value):
        self.count += value

    def inc_by_amount(self, value, amount):
        self.count += value * amount


counter = Counter()
counter.inc_by(1)
# counter.count is 1

counter.inc_by_amount(2, 5)
# counter.count is 11

print(counter.count)
