def take_input(a, b, sys):
    if sys == "+":
        return a+b
    elif sys == "-":
        return a-b
    elif sys == "*":
        return a*b
    elif sys == "/":
        return a/b
    else:
        print("Wrong inputs")

    
x = float(input("What is your first number ? : "))
sys = input("Choose your operator : +, -, *, / : ")
y = float(input("Whats is your second number ? : "))
print(f"The result is : {take_input(x, y, sys)}")
