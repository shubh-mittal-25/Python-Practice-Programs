print ("SPY NUMBER\nA spy number is a positive integer where the sum of its individual digits equals the product of its digits.\n. For example, 1124 is a spy number because (1+1+2+4=8) and (1 x 1 x 2 x 4=8).\n")

number = int(input("Enter the number you want checked : "))
temp = number
sum = 0
product = 1

while temp > 0 :
    digit = temp % 10
    sum += digit
    product *= digit
    temp //= 10

if (product == sum and number > 0):
    print (f"{number} is a Spy number")
else :
    print (f"{number} is not a Spy number")