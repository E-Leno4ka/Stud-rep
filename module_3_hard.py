
def sum_nested_data(nd):
    if isinstance(nd, int) or isinstance(nd, float):
        return nd
    if isinstance(nd,str):
        return len(nd)
    if len(nd) == 0:
        return 0
    if isinstance(nd, list) or isinstance(nd, tuple) or isinstance(nd, set):
        a = sum_nested_data(list(nd)[0]) + sum_nested_data(list(nd)[1:])
        return a
    if isinstance(nd, dict):
        a = sum_nested_data(list(nd.keys())) + sum_nested_data(list(nd.values()))
        return a


data_structure=[[1, 2, 3.7], {'a':4, 'b':5}, (6, {'cube':7, 'drum':8}), "Hello", ((), [{(2, 'Urban', ('Urban2', 35))}])]
print(sum_nested_data(data_structure))
