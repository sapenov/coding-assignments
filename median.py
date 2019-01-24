def find_median(lst):
    lst.sort()
    i = int(len(lst)/2)
    return lst[i]

lst = [1,7,3,9,12,4,1,15,20,22,23]
print(find_median(lst))

import statistics
items = [6, 1, 8, 2, 3]
print(statistics.median(items))
