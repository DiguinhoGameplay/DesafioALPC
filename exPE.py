n = [1, 2, 3, 4, 5]
i = 0
j = len(n) - 1
while i < j:
    temp = n[i]
    n[i] = n[j]
    n[j] = temp
    i += 1
    j -= 1
print(n)
