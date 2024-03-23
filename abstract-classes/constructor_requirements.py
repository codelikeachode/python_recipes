from abc import *

class List(ABC):
    @abstractmethod
    def __init__(self, item_count):
        self.itemCount = item_count

class SortedList(List):
    def __init__(self, item_count):
        super().__init__(item_count)
        # implementation
        print(item_count)

lst = SortedList(10)
print(lst.itemCount)