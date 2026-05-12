# Series : 1 , 4 , 7 , ....... , n

n = int(input("Enter the number of values : "))
sum = 0
for i in range(1,n+1):
    num = (i*3)-2
    print(num,end=" , ")
    sum += num
print(f"\nSum = {sum}")