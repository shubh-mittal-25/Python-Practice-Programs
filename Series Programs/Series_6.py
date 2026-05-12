# Series : 1^2 , 2^2 , 3^2 , ....... , n^2

n = int(input("Enter the number of values : "))
sum = 0
for i in range(1,n+1):
    num = i**2
    print(f"{i}^2",end=" , ")
    sum += num
print(f"\nSum = {sum}")