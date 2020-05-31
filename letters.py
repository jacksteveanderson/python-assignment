inp = input("Write a sentence: ")
a = inp.lower()
b = {}
sayac = 0
for i in range(len(a)):
  for j in range(len(a)):
    if a [i] == a [j]:
      sayac = sayac + 1
  b.update({a[i]: sayac})
  sayac = 0
print(b)
