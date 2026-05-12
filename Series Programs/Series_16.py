# Series : a^1/1! - a^2/2! + a^3/3! , ....... , n/n!

a = int(input("Enter the value of a : "))
n = int(input("Enter the number of values : "))
sum = 0
for i in range(1,n+1):
    f = 1
    for j in range (1,i+1):
        f=f*j
    num = a**i/f
    if i % 2 == 0:
        print(f"{a}^{i}/{i}!",end=" + ")
        sum -= num
    else:
        print(f"{a}^{i}/{i}!", end=" - ")
        sum += num
print(f"\nSum = {sum}")