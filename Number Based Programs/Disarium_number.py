print ("DISARIUM NUMBER\nA Disarium number is a number where the sum of its digits, each raised to the power of its respective 1-indexed position from the left, equals the original number\nFor instance, (135) is a Disarium number because (1^1 + 3^2 + 5^3 = 1 + 9 + 125 = 135).\n")

number = int(input("Enter the number you want checked : "))
temp = number
sum = 0
count = len(str(number))

while temp > 0 :
    digit = temp % 10
    sum += digit ** count
    temp //= 10
    count -= 1

if number == sum:
    print (f"{number} is a Disarium number")
else :
    print (f"{number} is not a Disarium number")