fibonacci = [1, 1]
for i in range(1,9):
    fibonacci.append(fibonacci[i-1]+fibonacci[i])
print(fibonacci)