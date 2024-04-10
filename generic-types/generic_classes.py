from typing import TypeVar, Generic
T = TypeVar('T')

class Size(Generic[T]):
    def __init__(self, width: T, height: T):
        self.width = width
        self.height = height
        
    def as_text(self):
        return f"[{self.width};
    {self.height}]"
    
size_int = Size[int](5, 8)
text_int = size_int.as_text()

size_float = Size[float](3.7, 1.58)
text_float = size_float.as_text()

print(f"{text_int}")
print(f"{text_float}")