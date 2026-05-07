print("--------------------------------------")
print("WELCOME TO THE PIZZA PRICE CALCULATOR")
print("--------------------------------------\n")

size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
veggies = input("Do you want veggies on your pizza? Y or N: ")
mushroom =  input("Do you want mushrooms on your pizza? Y or N: ")
bill = 0

#Size
if size == 'S':
    bill += 15
elif size == 'M':
    bill += 20
elif size == 'L':
    bill += 25
else :
    print("You typed the wrong inputs")

#Pepperoni
if pepperoni == 'Y':
    if size == 'S':
        bill += 2
    else :
        bill += 3

#Extra Cheese
if extra_cheese == 'Y':
    bill += 1

#Veggies
if veggies == 'Y':
    bill += 1

#Mushrooms
if mushroom == 'Y':
    bill += 1

print(f"Your final bill is: ${bill}.")