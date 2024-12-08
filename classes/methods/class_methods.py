class Calc:
    @staticmethod
    def get_min(*values):
        if len(values) == 0:
            return 0
        min_v = values[0]
        for i in range(1, len(values)):
            if values[i] < min_v:
                min_v = values[i]

        return min_v


result = Calc.get_min(3, 2, 5, 1, 4)
# result is 1

print(result)
