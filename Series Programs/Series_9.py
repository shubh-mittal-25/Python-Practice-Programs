# Series : 1 , 1/2 , 1/3 , ....... , 1/n

n = int(input("Enter the number of values : "))
sum = 0
for i in range(1,n+1):
    num = 1/i
    print(f"1/{i}",end=" , ")
    sum += num
print(f"\nSum = {sum}")