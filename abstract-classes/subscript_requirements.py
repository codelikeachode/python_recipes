from abc import *


class AIterable(ABC):
    @abstractmethod
    def __getitem__(self, i):
        pass


class PowerOfTwo(AIterable):
    pass

    def __getitem__(self, i):
        return pow(2, i)


power = PowerOfTwo()
p8 = power[8]
# p8 = 256

p16 = power[16]
# p16 = 65536

print(p8)
print(p16)
