# crie uma programa que possui uma lista onde o úsuario escolhe o número de termos e o mesmo peça o indice do elemento que ele escolher

def pesquisa(lista,elemento):
    for i in range(0,lista - 1):
        achou = False
        ini = 0
        fim = len(lista) - 1
        while ini <= fim and not achou:
            meio = (ini + fim) // 2
            if lista[meio] == elemento:
                return meio
            elif elemento < lista[meio]:
                fim = meio - 1
            else:
                ini = meio + 1


pesquisa(int(input('Insira o número de termos do vetor:')) , int(input('Insira o elemento que deseja descobrir o índice:')))

