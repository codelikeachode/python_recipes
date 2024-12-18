from datetime import datetime
import sys


def counting_sort(lst):
    data = list(lst)
    min_v = sys.maxsize
    max_v = -sys.maxsize
    for x in lst:
        if x > max_v:
            max_v = x
        if x < min_v:
            min_v = x

    counts = [0] * (max_v - min_v + 1)
    for x in lst:
        counts[x - min_v] += 1

    total = 0
    for i in range(min_v, max_v, + 1):
        old_count = counts[i - min_v]
        counts[i - min_v] = total
        total += old_count

    for x in list:
        data[counts[x - min_v]] = x
        counts[x - min_v] += 1

    return data


items = [4, 1, 5, 3, 2]
sortItems = counting_sort(items)

print(items)
print(sortItems)


items = list(range(1, 200))
items[5], items[6] = items[6], items[5]
count = 1000
start = datetime.now()

for n in range(1, count):
    counting_sort(items)

delta = datetime.now() - start
totalMicroseconds = delta.seconds * 10000000 + delta.microseconds

print(totalMicroseconds)