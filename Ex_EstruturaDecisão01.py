maior = 0
n = int(input('insira um número'))
n2 = int(input('insira outro número'))
if n > n2 :
    maior = n
elif n == n2:
    print(n,'precisa ser diferente de ' ,n2)
else:
    maior =  n2
print(  'maior número é ',maior)