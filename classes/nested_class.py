class SomeClass:
    @staticmethod
    def create():
        return SomeClass.NestedClass()
    
    class NestedClass:
        pass

someClass = SomeClass()
nested1 = someClass.create()
nested2 = someClass.NestedClass()
nested3 = SomeClass.NestedClass()

print(nested1)
print(nested2)
print(nested3)