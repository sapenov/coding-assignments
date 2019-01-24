# flatten list of lists
def flatten(lst):
    for x in lst:
        if type(x) is list:
            for sub_x in flatten(x):
                yield sub_x
        else:
            yield x

print(list(flatten(l)))

def flatten(d, parent_key='', sep='_'):
    items = []
    for k, v in d.items():
        new_key = parent_key + sep + k if parent_key else k
        if type(v) is dict:
            items.extend(flatten(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)

print(flatten({'a': 1, 'c': {'a': 2, 'b': {'x': 5, 'y' : 10}}, 'd': [1, 2, 3]}))
