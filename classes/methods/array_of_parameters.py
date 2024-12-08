class Calc:
    @staticmethod
    def get_avg(*values):
        if len(values) == 0:
            return 0

        sum_v = 0
        for value in values:
            sum_v += value
        return sum_v / len(values)


avg = Calc.get_avg(1, 2, 3, 4)
# avg is 2.5

print(avg)
