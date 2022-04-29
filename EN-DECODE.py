alpha = "a b c d e f g h i j k l m n o p q r s t u v w x y z"
alphabets = alpha.split()


def encrypt_text(txt, shf):
    en_text = []
    for letters in txt:
        if (alphabets.index(letters) + shf) >= 25:
            pos = alphabets.index(letters) + shf - 26
        else:
            pos = alphabets.index(letters) + shf
        en_text.append(alphabets[pos])
    print("Your encode message is : {}".format("".join(en_text)))


def decrypt_text(txt, shf):
    de_text = []
    for letters in txt:
        if alphabets.index(letters) - shf >= 0:
            pos = alphabets.index(letters) - shf
        else:
            pos = alphabets.index(letters) - shf + 26
        de_text.append(alphabets[pos])
    print("Your decode message is : {}".format("".join(de_text)))


while True:
    direction = input("Type 'encode' to ENCRIPT, type 'decode' to DECRYPT \n \tand 'exit' to QUIT : ")
    if direction.casefold() == "encode":
        text = input(" Type your message : \t").lower()
        shift = int(input(" Enter the number of shift : "))
        encrypt_text(text, shift)
    elif direction.casefold() == "decode":
        text = input(" Type your message : \t").lower()
        shift = int(input(" Enter the number of shift : "))
        decrypt_text(text, shift)
    else:
        break










