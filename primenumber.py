# Prime Number Check (Finds 5 Prime Number)
times = 0
while times < 5 :
    enterprime = True
    while enterprime:
        number = input("Enter a positive integer number : ")
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
    if int(number) == 0 or int(number) == 1:
        print(number, "is NOT a prime number.")
    elif int(number) == 2:
        print(number, " is the smallest Prime Number.")
        times += 1
        enterprime = False
    else:
        for i in range(2,int(number)):
            if int(number) % i == 0:
                print(number, "is NOT a prime number.")
                break
            if i == int(number)-1:
                print(number, " is a Prime Number.")
                times += 1
                enterprime = False
                break