# Series : 1 - 2 + 3 - .......  n

n = int(input("Enter the number of values : "))
sum = 0
for i in range(1,n+1):
    num = i
    if i % 2 == 0:
        print(num,end=" + ")
        sum -= num
    else:
        print(num, end=" - ")
        sum += num
print(f"\nSum = {sum}")