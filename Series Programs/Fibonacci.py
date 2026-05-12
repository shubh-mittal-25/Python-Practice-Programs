# Series : 0 , 1 , 1 , 2 , 3 , 5 , 8 ........ n

print("FIBONNACI SERIES : The Fibonacci series is a sequence where each number is the sum of the two preceding ones, usually starting from 0 and 1.\nIt follows the pattern: (0, 1, 1, 2, 3, 5, 8, 13, 21, 34,.........)")
n = int(input("Enter the number of values : "))
a=0
b=1
print(f"{a} , {b} , ", end ="")
sum = a+b
for i in range(3,n+1):
    temp = a
    a = b
    b = temp + b
    print(f"{b}", end=" , ")
    sum += b
print(f"\nSum = {sum}")