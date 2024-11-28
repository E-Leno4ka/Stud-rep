def res():
    a=int(input('Type first number: '))
    b=int(input('Type second number: '))
    c=int(input('Type third number: '))
    if a==b==c:
        res=3
    elif a==b or a==c or b==c:
        res=2
    else:
        res=0
    print(res)
res()