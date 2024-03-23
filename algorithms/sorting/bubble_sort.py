from datetime import datetime

def bubble_sort(data):
    lst = list(data)
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if lst[j] < lst[i]:
                lst[j], lst[i] = lst[i], lst[j]
    return lst


items = [4, 1, 5, 3, 2]
sortItems = bubble_sort(items)

print(items)
print(sortItems)


# Simplified speed test
items = list(range(1, 200))
items[5], items[6] = items[6], items[5]
count = 1000
start = datetime.now()

for n in range(1, count):
    bubble_sort(items)

delta = datetime.now() - start
totalMicroseconds = delta.seconds*1000000 + delta.microseconds

print(totalMicroseconds)