print ("HCF.\nThe Highest Common Factor (HCF), also known as the Greatest Common Divisor (GCD),\nis the largest positive integer that divides two or more numbers without leaving a remainder\n")

count = int(input("Enter how many numbers  : "))
number = []
hcf = 1

for i in range(count):
    number.append(int(input(f"Enter number {i+1} : ")))

for i in range (1,min(number)+1):
    check = True
    for n in number:
        if n % i != 0:
            check = False
            break

    if check == True:
        hcf = i

print (f"HCF = {hcf}")

