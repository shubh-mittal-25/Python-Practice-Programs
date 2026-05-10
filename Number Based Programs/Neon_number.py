print ("NEON NUMBER\nA neon number is a positive integer where the sum of the digits of its square is equal to the original number.\nFor example, (9) is a neon number because (9^2 = 81) and (8 + 1 = 9).\n")

number = int(input("Enter the number you want checked : "))
square = number ** 2
temp = square
sum = 0

while temp > 0 :
    digit = temp % 10
    sum += digit
    temp //= 10

if number == sum:
    print (f"{number} is a Neon number")
else :
    print (f"{number} is not a Neon number")