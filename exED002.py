n1=float(input('numero1:'))
n2=float(input('numero2:'))
n3=float(input('numero3:'))
if n1 > n2 and n1 > n3:
    maior = n1
elif n2 > n1 and n3:
    maior = n2
else:
    maior = n3
if maior.is_integer():
    print(f"maior número: {int(maior)}")    
else: print(f"Maior número:{maior}")