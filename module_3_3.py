result = True
div = [2, 3, 5, 7]

file=open('num.txt',"w")
file.write(input('type a number: '))
file.close()

with open('num.txt', 'r') as file:
    n = int(file.read())

def is_prime(m=3):
    for d in div:
        if d>m:
            result='Neutral'
            continue
        if d==m:
            result=True
            break
        else:
            c=m/d
            if int(c)==c:
                result=False
                break
            else:
                result=True
    return result

with open('primes.txt', 'w'):
    pass
with open('not_primes.txt', 'w'):
    pass

for i in range(n+1):
    if is_prime(i)==True:
        p=str(i)+(', ')
        with open("primes.txt", "a") as file:
            file.write(p)
    elif is_prime(i)==False:
        pn=str(i)+(', ')
        with open("not_primes.txt", "a") as file:
            file.write(pn)
    else: continue
