lst = [1,2,3,4,5,6,7,8,9,4,5]

# return first found
def find_duplicate(collection):
    length = len(collection)
    for i in range(0, length):
            current = collection[i]
            for j in range(0, length):
                if j != i and current == collection[j]:
                    return current
    return False


print(find_duplicate(lst))

# return all duplicates

def get_duplicates(arr):
    counts = {n: arr.count(n) for n in set(arr)}
    d = [k for k, v in counts.items() if v > 1]
    return d


print(get_duplicates(lst))
