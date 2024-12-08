class Greeting:
    @staticmethod
    def say_goodbye(message="Goodbye"):
        print(message)

    @staticmethod
    def say_hello(message="Hello"):
        print(message)


Greeting.say_goodbye()
# print "Goodbye"

Greeting.say_hello("Hi")
# prints "Hi"
