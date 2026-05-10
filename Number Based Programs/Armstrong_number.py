print ("ARMSTRONG NUMBER\nAn Armstrong number (or narcissistic number) is a positive integer equal to the sum of its own digits,\neach raised to the power of the total number of digits.\nFor example, 153 is a 3-digit Armstrong number because 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153\n")
number = int(input("Enter the number you want checked : "))
temp = number
sum = 0
count = len(str(number))

while temp > 0 :
    digit = temp % 10
    sum += digit ** count
    temp //= 10

if (number == sum and number > 0):
    print (f"{number} is an Armstrong number")
else :
    print (f"{number} is not an Armstrong number")