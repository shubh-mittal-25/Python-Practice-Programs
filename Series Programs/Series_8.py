# Series : a^1 , a^2 , a^3 , ....... , a^n

a = int(input("Enter the value of a : "))
n = int(input("Enter the number of values : "))
sum = 0
for i in range(1,n+1):
    num = a**i
    print(f"{a}^{i}",end=" , ")
    sum += num
print(f"\nSum = {sum}")