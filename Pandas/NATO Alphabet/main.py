import pandas
data = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_data_frame = pandas.DataFrame(data)

nato_dict = {row.letter:row.code for (index,row) in nato_data_frame.iterrows()}

word = input("Enter a word: ")
code_word = [nato_dict[letter.upper()] for letter in word]
print(code_word)


