inp = input("Write a sentence: ")
a = inp.lower()
b = {}
counter = 0
for i in range(len(a)):
  for j in range(len(a)):
    if a [i] == a [j]:
      counter = counter + 1
  b.update({a[i]: counter})
  counter = 0
print(b)
