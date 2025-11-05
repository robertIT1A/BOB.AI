# Create an AI chat bot
import sys
import time
import random

open = input("Type START to start talking to our friendly AI chat bot named BOB_AI, Type QUIT to close the program >> ")

greetings = ["hi", "hello", "hey", "yo", "sup"]
greet_replies = [
            "Hey there! 👋",
            "Hello! How are you doing?",
            "Hi! Nice to see you!",
            "Yo! What's up?",
]

love = ["i love you", "love you", "ily","mahal kita"]
love_replies = [
    "I Love You Too ",
    "I Love You More",
    "I Love You So Much",
    "I Love You Very Much",
    "Mahal din kita",
    "Mas Mahal kita",
]


if open.upper() == "START":
    print("BOB_AI: Hello!, my name is BOB your friendly AI chat bot by Super_Junior.")
    print("BOB_AI: Before we start, let me know your frist name so I know how to call you in our future conversation.")
    print("\nType QUIT if you want to stop talking to BOB.")
    name = input("Type your name here >> ")

    if name.upper() == "QUIT":
        sys.exit()

    
    print(f"BOB_AI: Hello {name}! How can I help you:?")
    print("\nType QUIT if you want to stop talking to BOB.")
    
    
        
    while True:
        

        user_asn = input("User: ")
        if user_asn.upper() == "QUIT":
            print(f"BOB_AI: Goodbye {name}! Your my friend!")
            break


        reply = None

        if any(mahal in user_asn for mahal in love):
            reply = random.choice(love_replies)
            
        
        elif any(word in user_asn for word in greetings):
            reply = random.choice(greet_replies)


        


        elif user_asn in {"math", "mathematics"}:
            # operation = input("BOB_AI: What operation do you want to solve? ")


                def add(x,y):
                    return x + y
                def subtract(x,y):
                    return x - y
                def multiply(x,y):
                    return x * y
                def divide(x,y):
                    if y == 0:
                        return "Error! Division by zero."
                    return x / y
                
                while user_asn.upper() != "EXIT":
                    operation = input("Enter operation (+, -, x, /): ")
                    if operation in {"+","-", "x", "/"}:
                        try:
                            num1 = float(input("Enter the first number --> "))
                            num2 = float(input("Enter the second number --> "))
                        except ValueError:
                            print("Invalid input. Please Enter Numeric Value")
                    
                        if operation == "+":
                            result = add(num1, num2)
                        elif operation == "-":
                            result = subtract(num1, num2)
                        elif operation == "x":
                            result = multiply(num1, num2)
                        elif operation == "/":
                            result = divide(num1, num2)
                        
                        print(f"BOB_AI: Result {result}")
                    else:
                        print("Invalid input")
                        
                    print(f"BOB_AI: {name}, please type EXIT to end the {user_asn} or Continue if you want to ask me more regarding {user_asn} ")
                    user_asn = input("User: ")
                
        

        else:
            print(f"BOB_AI: I'm sorry, {name}, I can currently only help with math. How can I assist you with that?")
            
        print("BOB_AI:", reply)

else:
    print("Program closed.")
    sys.exit()





