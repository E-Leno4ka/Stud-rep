def get_matrix(n=2,m=3,val=8):
    matrix=[]
    for i in range(n):
        raw=[]
        matrix.append(raw)
        for j in range(m):
            raw.append(val)
    print(matrix)
#get_matrix()
get_matrix(int(input('Строк ')),int(input('Столбцов ')),int(input('Значение ')))
