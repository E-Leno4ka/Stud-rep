
mv=('+', '-', '*', '/', '**')

def ress(a, m, b):
    if m == '+':
        res = a + b
    elif m == '-':
        res = a - b
    elif m == '*':
        res = a * b
    elif m == '/':
        res = a / b
    elif m == '**':
        res = a ** b
    print(f"{a} {m} {b} = {res}")

try:
    a = int(input('First num: '))
    m = input('Math operation (+, -, *, /): ')
    b = int(input('Second num: '))
    if m not in mv:
        print(f"Я не умею выполнять арифметическое действие '{m}' ")
    elif m == '/' and b == 0:
        print('Деление на ноль недопустимо. Попробуйте ещё раз.')
    else:
        print('А не посчитать ли нам, благородные кроты?')
        ress(a, m, b)
except ValueError:
    print('Введены некорректные данные. Попробуйте ещё раз.')
except NameError:
     print('Введены некорректные данные. Попробуйте ещё раз.')
