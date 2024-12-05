
def sum_nested_data(arg):
    if isinstance(arg, int) or isinstance(arg, float):
        return arg
    if isinstance(arg,str):
        return len(arg)
    if len(arg) == 0:
        return 0
    if isinstance(arg, list) or isinstance(arg, tuple) or isinstance(arg, set):
        a = sum_nested_data(list(arg)[0]) + sum_nested_data(list(arg)[1:])
        return a
    if isinstance(arg, dict):
        a = sum_nested_data(list(arg.keys())) + sum_nested_data(list(arg.values()))
        return a


data_structure=[[1, 2, 3], {'a':4, 'b':5}, (6, {'cube':7, 'drum':8}), "Hello", ((), [{(2, 'Urban', ('Urban2', 35))}])]
print(sum_nested_data(data_structure))
