alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(text, shift):
    newtext = ""
    for n in text:
        if n in alphabet:
            shifted_index = alphabet.index(n) + shift
            if shifted_index > 26:
                shifted_index = shifted_index % 26
            newtext += alphabet[shifted_index]
        else:
            newtext += n
    print(f"The encoded text is {newtext}")
        
def decrypt(text, shift):
    newtext = ""
    for n in text:
        if n in alphabet:
            shifted_index = alphabet.index(n) - shift
            if shifted_index < 26 and shift > 26:
                shifted_index = shifted_index + 26
            newtext += alphabet[shifted_index]
        else:
            newtext += n
    print(f"The encoded text is {newtext}")
    
if __name__ == "__main__":
    loop = True
    while loop:
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))

        if direction == 'encode':
            encrypt(text, shift)
        elif direction == 'decode':
            decrypt(text, shift)
        go = input("Do you want to cipher//decipher again? enter 'no' to exit the loop: ")
        if go == 'no':
            exit()