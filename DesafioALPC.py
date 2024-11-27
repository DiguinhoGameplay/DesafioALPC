import re

def calcular_pontuacao(senha):
    soma = 0
    regras_atendidas = 0

    num_caracteres = len(senha)
    soma += num_caracteres * 4

    maiusculas = len([c for c in senha if c.isupper()])
    minusculas = len([c for c in senha if c.islower()])
    digitos = len([c for c in senha if c.isdigit()])
    simbolos = len([c for c in senha if not c.isalnum()])

    soma += (num_caracteres - maiusculas) * 2
    soma += (num_caracteres - minusculas) * 2
    soma += digitos * 4
    soma += simbolos * 6

    numeros_simbolos_meio = len([c for c in senha[1:-1] if c.isdigit() or not c.isalnum()])
    soma += numeros_simbolos_meio * 2

    if num_caracteres >= 8:
        regras_atendidas += 1
    if sum(1 for x in [maiusculas, minusculas, digitos, simbolos] if x > 0) >= 3:
        regras_atendidas += 1

    soma += regras_atendidas * 2

    if senha.isalpha():
        soma -= num_caracteres
    if senha.isdigit():
        soma -= digitos
    caracteres_unicos = len(set(senha.lower()))
    repetidos = num_caracteres - caracteres_unicos
    soma -= repetidos

    maiusculas_consecutivas = len(re.findall(r'[A-Z]{2,}', senha))
    minusculas_consecutivas = len(re.findall(r'[a-z]{2,}', senha))
    digitos_consecutivos = len(re.findall(r'\d{2,}', senha))

    soma -= (maiusculas_consecutivas * 2)
    soma -= (minusculas_consecutivas * 2)
    soma -= (digitos_consecutivos * 2)

    letras_sequenciais = sum(1 for i in range(len(senha) - 2) 
                             if senha[i:i+3].isalpha() and ''.join(sorted(senha[i:i+3])) == senha[i:i+3])
    numeros_sequenciais = sum(1 for i in range(len(senha) - 2) 
                              if senha[i:i+3].isdigit() and ''.join(sorted(senha[i:i+3])) == senha[i:i+3])
    simbolos_sequenciais = sum(1 for i in range(len(senha) - 2) 
                               if not senha[i].isalnum() and senha[i+1] != senha[i] and senha[i+2] != senha[i+1])

    soma -= (letras_sequenciais * 3)
    soma -= (numeros_sequenciais * 3)
    soma -= (simbolos_sequenciais * 3)

    return max(soma, 0)

def avaliar_senha(senha):
    pontuacao = calcular_pontuacao(senha)
    if pontuacao < 20:
        return "Muito fraca"
    elif 20 <= pontuacao < 40:
        return "Fraca"
    elif 40 <= pontuacao < 60:
        return "Boa"
    elif 60 <= pontuacao < 80:
        return "Forte"
    else:
        return "Muito forte"
senha = input("Digite a senha para avaliar: ")
pontuacao = calcular_pontuacao(senha)
avaliacao = avaliar_senha(senha)
print(f"{avaliacao}")
print(f"{pontuacao}")
