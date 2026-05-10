print ("PRIME NO.\nA prime number is a natural number greater than 1 that has exactly two distinct positive divisors: 1 and itself\n")
number = int(input("Enter the number you want checked : "))
check = True

for i in range (2,number):
    if number % i == 0:
        check = False
        break

if (check == True):
    print (f"{number} is a Prime number")
else :
    print (f"{number} is not a Prime number")