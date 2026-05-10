print ("PALINDROME NUMBER\nA Palindrome number is an integer that remains the same when its digits are reversed, reading the same forward and backward.\nExample 121, 1331, 55.\n")
number = int(input("Enter the number you want checked : "))
temp = number
reverse = 0
count = len(str(number))

while temp > 0 :
    digit = temp % 10
    reverse = reverse * 10 + digit
    temp //= 10

if (number == reverse):
    print (f"{number} is a Palindrome number")
else :
    print (f"{number} is not a Palindrome number")