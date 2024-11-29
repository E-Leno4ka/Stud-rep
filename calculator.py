mv=('+', '-', '*', '/', '**')

try:
    a=int(input('First num: '))
    if not isinstance(a,int):
        print('Введены некорректные данные. Попробуйте ещё раз.')
    else:
        m=str(input('Math operation (+, -, *, /): '))
        if m not in mv:
            print(f"Я не умею выполнять арифметическое действие '{m}' ")
        else:
            b=int(input('Second num: '))
            if not isinstance(b,int):
                print('Введены некорректные данные. Попробуйте ещё раз.')
            else:
                if m == '/' and b == 0:
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
except:
    print('Введены некорректные данные. Попробуйте ещё раз.')
