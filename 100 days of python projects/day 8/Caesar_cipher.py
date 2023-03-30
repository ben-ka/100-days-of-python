import art
ALPHABET = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']           # list of letters
print (art.logo)
def main():  
   
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()            # inputs which direction the encryption
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    if direction == 'encode':
        encrypt(text,shift)
    if direction == 'decode':
        decrypt(text,shift)
    play_again = input("do you want to go again? (y/n) ").lower()
    if play_again =="y":
        main()


def encrypt(text,shift):
    cipher_text =""
    for letter in text:
        if letter in ALPHABET:
            for i in range(len(ALPHABET)):
                if letter == ALPHABET[i]:           # checks the index of the letter
                    letter_position = i
            if letter_position+shift < len(ALPHABET):     # checks if we should add the shift or start from the beginning
                cipher_text += ALPHABET[letter_position+shift]
            elif  letter_position+shift >= len(ALPHABET):
                how_close_to_end = len(ALPHABET) -  letter_position 
                cipher_text +=ALPHABET[shift -how_close_to_end]
        else:
            cipher_text +=letter
    print(f"the encoded text is: {cipher_text}"   )     


def decrypt(text,shift):
    cipher_text =""
    for letter in text:
        if letter in ALPHABET:
            for i in range(len(ALPHABET)):
                if letter == ALPHABET[i]:           # checks the index of the letter
                    letter_position = i
            if letter_position-shift >= 0:     # checks if we should add the shift or start from the beginning
                cipher_text += ALPHABET[letter_position-shift]
            elif  letter_position - shift < 0 :
                how_close_to_start = letter_position -shift 
                cipher_text +=ALPHABET[how_close_to_start]
        else:
            cipher_text +=letter
    print(f"the decoded text is: {cipher_text}"   )     



main()