def pesquisa_binaria(lista, elemento):
   achou = False
   ini = 0
   fim = len(lista) - 1

   while ini <= fim and not achou:
       meio = (ini + fim) // 2

       if lista[meio] == elemento:
           achou = True
           print(f'Número {elemento}, está no índice {meio}')
       elif elemento < lista[meio]:
           fim = meio - 1
       else:
           ini = meio + 1
   if not achou:
       print(-1)
pesquisa_binaria([1,2,3,4,5,6,7,8,9],int(input('insira um número')))

