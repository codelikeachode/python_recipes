from abc import ABC, abstractmethod
from typing import TypeVar, Generic

class Vehicle(ABC):
    @abstractmethod
    def test(self):
        pass
    
class Car(Vehicle):
    def test(self):
        print(f"test {self}")
        
T = TypeVar('T', bound=Vehicle)

class Service(Generic[T]):
    def __init__(self):
        self.v_list = list[T]()
        
    def add(self, item: T):
        self.v_list.append(item)
        
    def test(self):
        for item in self.v_list:
            item.test()
            
service = Service[Car]()
service.add(Car())
service.test()