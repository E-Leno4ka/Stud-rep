numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes=[]
not_primes=[]
is_prime=True
div=[]
print('numbers: ',numbers)

for el in numbers:
    div.append(el)
    #print('el=',el)
    #print('div',div)
    if len(div)>1:
        q=[]
        for d in div:
            c=el/d
            if int(c)<c:
                q=q
            else:
                q.append(c)
        #print('qs are',q)
        if len(q)>2:
            is_prime=False
        else:
            is_prime=True
    else: continue
    if is_prime==True:
        primes.append(el)
    else:
        not_primes.append(el)
print('primes: ',primes)
print('not_primes: ',not_primes)