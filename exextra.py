V = [10, 20, 30, 40, 50, 60, 70, 80, 90]
N = int(input('digite o numero que procura:'))
achou = False
ini = 0
fim = len(V) - 1
while ini <= fim and not achou:
    meio = (ini + fim // 2)
    
    if V[meio] == N:
        achou = True
        print(f'Número{N}, está na posição:{meio}')
    elif V[meio] > N:
        fim = meio - 1
    else:
        ini = meio + 1
if not achou:
    print(f'{N} não está na lista')
V = [10, 20, 30, 40, 50, 60, 70, 80, 90]
N = int(input('Digite o número que deseja buscar: '))
achou = False
ini = 0
fim = len(V) - 1

while ini <= fim and not achou:
    meio = (ini + fim) // 2  # Corrigido o cálculo da posição do meio

    if V[meio] == N:
        achou = True
        print(f'Número {N} encontrado no índice {meio}')
    elif V[meio] < N:
        ini = meio + 1  # Busca no lado direito
    else:
        fim = meio - 1  # Busca no lado esquerdo

if not achou:
    print(f'Número {N} não encontrado no array.')





