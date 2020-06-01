mapping = {1000: "M", 900: "CM", 500: "D", 400: "CD", 100: "C",
             90: "XC", 50: "L", 40: "XL", 10: "X", 9: "IX", 5:"V", 4:"IV", 1:"I"}
number = int(input("Enter a number : ")) # 1994 "MCMXCIV"

result = ""

for k,v in mapping.items(): # k = 1000
    value = number // k # 1
    result += v * value # M * 1
    number %= k # 994

print(result)

# "MCMXCIV"

my_input = result
final_result = 0
for k,v in mapping.items():
    while my_input.startswith(v):
        final_result += k
        my_input = my_input[len(v):]
print(final_result)