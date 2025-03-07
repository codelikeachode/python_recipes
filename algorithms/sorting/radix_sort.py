from datetime import datetime


# Time Complexity O(nk)
# Space Complexity O(n+k)
def radix_sort(data, base=10):
    def list_to_buckets(s_data, s_base, m):
        buckets = [[] for _ in range(s_base)]
        p_base = s_base**m
        for x in s_data:
            # Isolate the base-digit from the number
            digit = (x // p_base) % s_base
            # Drop the number into the correct bucket
            buckets[digit].append(x)
        return buckets

    def buckets_to_list(buckets):
        result = []
        for bucket in buckets:
            # append the numbers in a bucket
            # sequentially to the returned array
            for number in bucket:
                result.append(number)
        return result

    max_val = max(data)

    i = 0
    # Iterate, sorting the array by each base-digit
    array = []
    while base**i <= max_val:
        array = buckets_to_list(list_to_buckets(data, base, i))
        i += 1

    return array


items = [4, 1, 5, 3, 2]

sortItems = radix_sort(items)
# sortItems is [1, 2, 3, 4, 5]

print(items)
print(sortItems)

items = list(range(1, 200))
items[5], items[6] = items[6], items[5]
count = 1000
start = datetime.now()

for n in range(1, count):
    radix_sort(items)

delta = datetime.now() - start
totalMicroseconds = delta.seconds * 1000000 + delta.microseconds

print(totalMicroseconds)
