def min_abs_diff(lst):
    lst.sort()
    return min([abs(lst[cnt + 1] - lst[cnt]) for cnt in range(len(lst) - 1)])

print(min_abs_diff([6,4,2,77,8]))
