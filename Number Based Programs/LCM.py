print ("LCM.\nThe Least Common Multiple (LCM) of two or more integers is the smallest positive integer that is divisible by each of the given numbers\n")

count = int(input("Enter how many numbers  : "))
number = []

for i in range(count):
    number.append(int(input(f"Enter number {i+1} : ")))

lcm = number[0]

for i in number[1:]:
    max_num = max(lcm, i)

    while True:
        if max_num % lcm == 0 and max_num % i == 0:
            lcm = max_num
            break
        max_num += 1


print (f"LCM = {lcm}")