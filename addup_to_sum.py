def add_to_sum(lst, summa):
    s = set()
    al = len(lst)
    ret = False
    for i in range(0, al):
        complement = summa - lst[i]
        if complement >= 0 and complement in s:
            return lst[i], complement
        s.add(lst[i])
    return ret

l = [33, 8, 15, 32, 11, 90]
s = 123
print(add_to_sum(l, s))
