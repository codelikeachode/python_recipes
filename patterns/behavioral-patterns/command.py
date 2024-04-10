# Invoker
class BankClient:
    def __init__(self, c_put, c_get):
        self.__putCommand = c_put
        self.__getCommand = c_get
        
    def put_money(self):
        self.__putCommand.execute()
        
    def get_money(self):
        self.__getCommand.execute()
        

# Receiver
class Bank:
    @staticmethod
    def give_money():
        print("money is given")
        
    @staticmethod
    def receive_money():
        print("money is received")
        
class Command:
    def execute(self):
        pass

# ConcreteCommand
class PutCommand(Command):
    def __init__(self, p_bank):
        self.__bank = p_bank
        
    def execute(self):
        self.__bank.receive_money()
        
# ConcreteCommand
class GetCommand(Command):
    def __init__(self, p_bank):
        self.__bank = p_bank
        
    def execute(self):
        self.__bank.give_money()
        

# Client
bank = Bank()
cPut = PutCommand(bank)
cGet = GetCommand(bank)
client = BankClient(cPut, cGet)
client.get_money()
# printed: money is given
client.put_money()
# printed: money is received


"""
Encapsulate a request as an object, thereby letting you parameterize clients
with different requests, queue or log requests, and support undoable operations.
"""