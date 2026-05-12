# Series : 1^n , 2^n , 3^n , ....... , n^n

n = int(input("Enter the number of values : "))
sum = 0
for i in range(1,n+1):
    num = i**n
    print(f"{i}^{n}",end=" , ")
    sum += num
print(f"\nSum = {sum}")