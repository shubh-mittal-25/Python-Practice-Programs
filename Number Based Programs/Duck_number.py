print ("DUCK NUMBER\nA Duck Number is a positive number that contains at least one zero (0),\n")

number = int(input("Enter the number you want checked : "))
temp = number
check = False

while temp > 0 :
    digit = temp % 10
    if digit == 0:
        check = True
        break
    temp //= 10

if check == True:
    print (f"{number} is a Duck number")
else :
    print (f"{number} is not a Duck number")