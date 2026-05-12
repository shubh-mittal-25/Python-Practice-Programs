# Series : 1/1! , 2/2! , 3/3! , ....... , n/n!

n = int(input("Enter the number of values : "))
sum = 0
for i in range(1,n+1):
    f = 1
    for j in range (1,i+1):
        f=f*j
    num = i/f
    print(f"{i}/{i}!",end=" , ")
    sum += num
print(f"\nSum = {sum}")