class Calc:
    def __init__(self):
        self.lastSum = -1

    def get_sum(self, n1, n2):
        self.lastSum = n1 + n2
        return self.lastSum


calc = Calc()
sum1 = calc.get_sum(5, 3)
# sum1 is 8

sum2 = calc.get_sum(2, 3)
# sum2 is 5

print(f"{sum1 = }")
print(f"{sum2 = }")
print(f"{calc.lastSum = }")
