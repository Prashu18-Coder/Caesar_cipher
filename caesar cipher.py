alphabet = []
for i in range(26):
    alphabet.append(chr(ord('a')+i))
def encryption(plain_text,shift_key):
    cipher_text = ""
    for ch in plain_text:
        if ch in alphabet:
            pos = alphabet.index(ch)
            new_pos = (pos + shift_key)%26
            cipher_text += alphabet[new_pos]
        else:
            cipher_text += ch
    print(f"Here's is the text after encryption : {cipher_text}")

def decryption(cipher_text,shift_key):
    plain_text = ""
    for ch in cipher_text:
        if ch in alphabet:
            pos = alphabet.index(ch)
            new_pos = (pos - shift_key)%26
            plain_text += alphabet[new_pos]
        else:
            plain_text += ch
    print(f"Here's is the text after decryption : {plain_text}")
wanna_end = False
while not wanna_end :
    what_to_do = input("Type 'encrypt' for encryption and 'decrypt' for decryption:\n")
    text = input("type your message :")
    key = int(input("enter the shift key :"))
    if what_to_do == 'encrypt':
        encryption(plain_text = text, shift_key = key)
    elif what_to_do == 'decrypt':
        decryption(cipher_text = text, shift_key = key)
    play_again = input("enter 'yes' to continue,'no' to exit:")
    if play_again == 'no':
        wanna_end = True
        print("Have a nice day ! Bye")
    
