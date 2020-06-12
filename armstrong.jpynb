# 5 times armstrong number check
times = 0
while times<5 :
    number = input("Enter a positive integer number : ")
    digits = len(number)
    summ = 0
    if not number.isdigit():
        if number.count(",") == 1 and number.replace(",", "1").isnumeric() and digits >= 2 or number.count(".") == 1 and number.replace(".", "1").isnumeric() and digits >= 2:
            print("Please enter only integer number not float.")
        elif number.count("-") == 1 and number.index("-") == 0 and number.replace("-", "1").isnumeric():
            print("Please enter a positive number.")   
        else:
            print("Please Do not use any entries other than numeric values.")
    else:
        for i in range(digits):
            summ += int(number[i])**digits
            if summ == int(number):
                print(number, "is an Armstrong number.")
                times += 1
                break
            else:
                print(number, "is NOT an Armstrong number.")
                times += 1
                break