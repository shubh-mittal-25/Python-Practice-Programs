def caesar (encode_or_decode , original_text, shift_amount):
    if encode_or_decode == "encode" or "decode":
        output_text = ""
        if encode_or_decode == "decode":
            shift_amount *= -1
        for letter in original_text:
            if letter in alphabet:
                position = alphabet.index(letter) + shift_amount
                position %= len(alphabet) #The remainder corrects the position to required index
                output_text += alphabet[position]
            else:
                output_text += letter
        print(f"Here is the {direction}d result: {output_text}")
    else :
        print("Invalid Input")

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print("WELCOME TO CAESAR CIPHER.")

should_continue = True

while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(direction,text,shift)

    restart = input("Type 'yes' if you want to go again. Otherwise, type 'no'.\n").lower()
    if restart == "no":
        should_continue = False
        print("Goodbye")




