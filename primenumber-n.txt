# Prime Numbers between 1 - N
enterprime = True
primelist = list()
while enterprime:
    number = input("Enter a positive integer number. I\'ll find the prime numbers between 0 to given number: ")
    digits = len(number)
    if not number.isdigit():
        if number.count(",") == 1 and number.replace(",", "1").isnumeric() and digits >= 2 or number.count(".") == 1 and number.replace(".", "1").isnumeric() and digits >= 2:
            print("Please enter only integer number not float.")
        elif number.count("-") == 1 and number.index("-") == 0 and number.replace("-","1").isnumeric():
            print("Please enter a positive number.")   
        else:
            print("Please Do not use any entries other than numeric values.")
    else:
        enterprime = False
for i in range(2,(int(number)+1)):
    if i == 2:
        primelist.append(i)
    else:
        for ii in range(2,(i+1)):
            if i % ii == 0:
                if ii == i:
                    primelist.append(i)
                break
print(primelist)