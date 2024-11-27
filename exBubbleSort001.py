lista = [5,3,8,6,7,2]
n = len(lista)
lista.insert(5,2)
print(lista)
troca = 0
for i in range(n):
    for j in range(0,n-i-1):
        if lista[j] > lista[j+1]:
            lista[j], lista[j + 1] = lista[j + 1], lista[j]
            troca += 1

print('lista ordenada:', lista, 'número de trocas:', troca)
print