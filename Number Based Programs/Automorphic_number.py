print ("AUTOMORPHIC NUMBER\nAn automorphic number (or circular number) is a natural number whose square ends in the same digits as the number itself.\nExamples include (5^2=25), (6^2=36), and (25^2=625)\n")

number = int(input("Enter the number you want checked : "))
square = number ** 2

if str(square).endswith(str(number)):
    print (f"{number} is an Automorphic number")
else :
    print (f"{number} is not an Automorphic number")