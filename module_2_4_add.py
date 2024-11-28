numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes=[]
not_primes=[]
result=True
div=[2, 3, 5, 7]

def is_prime(n=3):
    for d in div:
        #print('d=',d)
        if d>n:
            result='Neutral'
            continue
        if d==n:
            result=True
            break
        else:
            c=n/d
            #print('c=',c)
            if int(c)==c:
                result=False
                break
            else:
                result=True
    return result

#print(is_prime(int(input('type '))))

for i in numbers:
    if is_prime(i)==True:
        primes.append(i)
    elif is_prime(i)==False:
        not_primes.append(i)
    else: continue

print('numbers: ',numbers)
print('primes: ',primes)
print('not_primes: ',not_primes)