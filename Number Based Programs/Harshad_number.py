print ("HARSHAD NUMBER\nA Harshad number (or Niven number) is an integer that is divisible by the sum of its digits.\nExamples include 18 ((1+8=9); (18 / 9 = 2)) and 1729\n")

number = int(input("Enter the number you want checked : "))
temp = number
sum = 0

while temp > 0 :
    digit = temp % 10
    sum += digit
    temp //= 10

if number % sum == 0:
    print (f"{number} is a Harshad number")
else :
    print (f"{number} is not a Harshad number")