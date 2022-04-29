print("FIZZ BUZZ GAME")
x = int(input("Enter the Fizz condition : "))
y = int(input("Enter the Buzz condition : "))
input("PRESS ENTER TO START\n")
user_input = int(input("Enter the no. to find its FIZZ or BUZZ or FIZZBUZZ : "))
if user_input % x == 0 and user_input % y == 0:
    print("FIZZBUZZ")
elif user_input % x == 0:
    print("Fizz")
elif user_input % y == 0:
    print("Buzz")
else:
    print("Nothing")
