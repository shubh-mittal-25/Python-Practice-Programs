with open("file1.txt") as f1:
    list1 = f1.readlines()

with open("file2.txt") as f2:
    list2 = f2.readlines()

list1 = [int(i) for i in list1]
list2 = [int(i) for i in list2]

result = [num for num in list1 if num in list2]
print(result)