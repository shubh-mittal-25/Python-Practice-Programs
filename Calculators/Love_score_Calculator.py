def calculate_love_score(name1,name2):
    n = name1.lower() + name2.lower()
    true_occurence = 0
    love_occurence = 0
    for letter in n:
        if letter == 't' or letter == 'r' or letter == 'u' or letter == 'e':
            true_occurence += 1
        if letter == 'l' or letter == 'o' or letter == 'v' or letter == 'e':
            love_occurence += 1
    score = (true_occurence*10) + love_occurence
    print(f"Love Score = {score}")

one = input("Enter the first name : ")
two = input("Enter the second name : ")
calculate_love_score(one,two)