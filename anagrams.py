a ="aaaaaa"
b ="bbbbbb"
pre_total = len(a) + len(b)
for i in a:
    if i in b:
        b = b.replace(i,"",1)
        a = a.replace(i,"",1)

post_total = len(a) + len(b)

print(f"a value is {a}")
print(f"b value is {b}")

if ( post_total == pre_total):
    print("Those two words cant have anagrams")
else:
    print(len(a) + len(b))