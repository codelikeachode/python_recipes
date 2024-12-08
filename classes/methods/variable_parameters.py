class Log:
    def __init__(self):
        self.lastData = ""

    def print5(self, data):
        self.lastData = data
        if len(data) > 5:
            data = data[0:5]

        print(data)


log = Log()
log.print5("1234567")
# prints "12345"
print(f"{log.lastData = }")
