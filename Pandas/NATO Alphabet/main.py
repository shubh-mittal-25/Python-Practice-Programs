import pandas

nato_data_frame = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_dict = {row.letter:row.code for (index,row) in nato_data_frame.iterrows()}

def generate_phonetic():
    word = input("Enter a word: ")
    try:
        code_word = [nato_dict[letter.upper()] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(code_word)

generate_phonetic()


