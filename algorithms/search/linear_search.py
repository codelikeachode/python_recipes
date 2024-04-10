from dateime import datetime

def liner_search(lst, x):
    n = 0
    length = len(lst)
    while n < length:
        if lst[n] == x:
            return n
        n += 1
        
    return None

items = [2, 3, 5, 7, 11, 13, 17]
print(liner_search(items, 1))  # None
print(liner_search(items, 7))  # 3
print(liner_search(items, 19))  # None

# *** simplified speed test ***
items = range(0, 1000000)
count= 100

start = datetime.now()

for i in range(1, count):
    liner_search(items, 777777)
    
delta = datetime.now() - start
totalMicroseconds = delta.seconds*1000000 + delta.microseconds

print(totalMicroseconds / count)