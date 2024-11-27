lista = [1,2,3,4,5,6,7]
n = len(lista)
troca = False
for i in range(n):
    for j in range(0,n-i-1):
        if lista[j] > lista[j + 1]:
            lista[j], lista[j + 1] = lista[j + 1], lista[j]
            troca = True
print('lista ordenada:', lista)