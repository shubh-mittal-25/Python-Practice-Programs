print ("PERFECT NO.\nA perfect number is a positive integer equal to the sum of its proper positive divisors (excluding the number itself).\nFor example, 6 is perfect because its divisors are 1, 2, and 3, and (1 + 2 + 3 = 6).\n")
number = int(input("Enter the number you want checked : "))
sum = 0

for i in range (1,number):
    if number % i == 0:
        sum += i

if (number == sum and number > 0):
    print (f"{number} is a Perfect number")
else :
    print (f"{number} is not a Perfect number")