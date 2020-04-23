age = input("Are you a cigarette addict older than 75 years old? (Yes/No) : ").title()
chronic = input("Do you have a severe chronic disease? (Yes/No) : ").title()
immune = input("Is your immune system too weak? (Yes/No) : ").title()
age = True if age == "Yes" else False
chronic = True if chronic == "Yes" else False
immune = True if immune == "Yes" else False
print("You are in risky group") if age or chronic or immune else print("You are not in risky group")