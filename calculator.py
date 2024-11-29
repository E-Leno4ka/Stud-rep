mv=('+', '-', '*', '/', '**')
try:
    a=int(input('First num: '))
    m=str(input('Math operation (+, -, *, /): '))
    b=int(input('Second num: '))
except ValueError:
    print('Введены некорректные данные. Попробуйте ещё раз.')
if m not in mv:
    print(f"Я не умею выполнять арифметическое действие '{m}' ")
elif m == '/' and b == 0:
    print('Деление на ноль недопустимо. Попробуйте ещё раз.')
else:
    if m == '+':
        res = a + b
    elif m == '-':
        res = a - b
    elif m == '*':
        res = a * b
    elif m == '/':
        res = a / b
    elif m == '**':
        res = a**b
    print(f"{a} {m} {b} = {res}")
