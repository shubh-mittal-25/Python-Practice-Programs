from math import factorial

print ("STRONG NO.\nA strong number (or Peterson number) is a special number where the sum of the factorials of its digits equals the original number itself.\nA well-known example is 145, because (1! + 4! + 5! = 1 + 24 + 120 = 145).\n")
number = int(input("Enter the number you want checked : "))
temp = number
sum = 0

while temp > 0 :
    digit = temp % 10
    sum += factorial(digit)
    temp //= 10

if (number == sum):
    print (f"{number} is a Strong number")
else :
    print (f"{number} is not a Strong number")