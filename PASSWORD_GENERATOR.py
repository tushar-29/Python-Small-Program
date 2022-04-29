import random
let = "a b c d e f g h i j k l m n o p q r s t u v w x y z A B C D E F G H I J K L MO P Q R S T U V W X Y Z"
letters = let.split()
sym = "! @ # $ % ^ & * ( ) + _ > < ?"
symbol = sym.split()
num = "1 2 3 4 5 6 7 8 9 0"
number = num.split()

def generate_password(no_letters=5, no_symbol=2, no_number=3):
    password_list = []
    for i in range(0, no_letters):
        password_list.append(random.choice(letters))
    for i in range(0, no_symbol):
        password_list.append(random.choice(symbol))
    for i in range(0, no_number):
        password_list.append(random.choice(number))
    random.shuffle(password_list)
    password = "".join(password_list)
    return password


if __name__ == "__main__":
    print("WELCOME TO PASSWORD GENERATOR")
    no_letters = int(input("Enter no. of letter required in the password : "))
    no_symbol = int(input("Enter the no. of symbol required in the password : "))
    no_number = int(input("Enter the no. of numerical required in the password : "))
    pass_d = generate_password(no_letters, no_symbol, no_number)
    print(pass_d)

