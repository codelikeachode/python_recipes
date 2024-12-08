class ListAssistant:
    def __init__(self, data: list[int]):
        self.data = data

    def get_first_last(self):
        first = -1
        last = -1
        if len(self.data) > 0:
            first = self.data[0]
            last = self.data[len(self.data) - 1]

        return first, last


lst = [2, 3, 5]
assistant = ListAssistant(lst)
result = assistant.get_first_last()
# result[0] is 2
# result[1] is 5

print(result[0])
print(result[1])
