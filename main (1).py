"""
Usando do algoritmo da bolha, ordene a lista de nomes do vetor nomes.
"""
V = []

arquivo = open('nomes.txt')
for linha in arquivo:
    V.append(linha.strip())
arquivo.close()

print(V)
