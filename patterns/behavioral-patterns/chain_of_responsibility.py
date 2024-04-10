from abc import ABC, abstractmethod

# Handler
class Rescuer(ABC):
    # HandleRequest()
    def __init__(self, code, rescuer):
        self._code = code
        self._next = rescuer
        
    def help(self, code):
        if self._code == code:
            self.to_help()
        elif isinstance(self._next,
Rescuer):
            self._next.help(code)
            
    @abstractmethod
    def to_help(self):
        pass
    
    
# ConcreteHandler
class Firefighter(Rescuer):
    def __init__(self, rescuer):
        super().__init__(1, rescuer)
        
    def to_help(self):
        print("call firefighters")
        
# ConcreteHandler
class Police(Rescuer):
    def __init__(self, rescuer):
        super().__init__(2, rescuer)
        
    def to_help(self):
        print("call the police")
        
# ConcreteHandler
class Ambulance(Rescuer):
    def __init__(self, rescuer):
        super().__init__(3, rescuer)
        
    def to_help(self):
        print("call an ambulance")
        
ambulance = Ambulance(0)
police = Police(ambulance)
firefighter = Firefighter(police)
firefighter.help(1)
# printed: call firefighters
firefighter.help(2)
# printed: call the police
firefighter.help(3)
# printed: call an ambulance


"""
Avoid coupling the sender of a request to its receiver by giving more than one object a chance to handle the request. 
Chain the receiving objects and pass the request along the chain until an object handles it.
"""