year = int(input("Enter a 4 digit year: "))
div_4 = year % 4 == 0
div_100 = year % 100 == 0
div_400 = year % 400 == 0

if ((div_4 and not div_100) or (div_4 and div_100 and div_400)):
  print(year, "is a leap year.")
else:
  print(year, "is NOT a leap year.")

if div_4 == True:
  print(year, "is evenly divisible by   4 ?  Yes")
else:
  print(year, "is evenly divisible by   4 ?  No")
if div_100 == True:
  print(year, "is evenly divisible by 100 ?  Yes")
else:
  print(year, "is evenly divisible by 100 ?  No")
if div_400 == True:
  print(year, "is evenly divisible by 400 ?  Yes")
else:
  print(year, "is evenly divisible by 400 ?  No")