
def find_max(lst):
    tmp_max = float('-inf')
    for i in lst:
        if i > tmp_max:
            tmp_max = i
    return tmp_max, float('-inf')

def find_max2(lst):
    lst.sort()
    return lst[-1]

print(find_max2([0,-1,2,3,70,5,-20]))
