# Create an AI chat bot

open = input("Type START to start talking to our friendly AI chat bot named BOB_AI, Type QUIT to close the program >> ")

if open.upper() == "START":
    print("BOB_AI: Hello!, my name is BOB your friendly AI chat bot by Super_Junior.")
    print("BOB_AI: Before we start, let me know your frist name so I know how to call you in our future conversation.")
    print("\nType QUIT if you want to stop talking to BOB.")
    name = input("Type your name here >> ")
    while True:
        if name.upper() == "QUIT":
            exit

        else:
            print(f"BOB_AI: Hello {name}! How can I help you:?")
            print("\nType QUIT if you want to stop talking to BOB.")
            user_asn = input("User: ")
            while user_asn.upper() != "EXIT":
                if user_asn in {"math", "mathematics"}:
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

                        operation = input("Enter operation (+, -, x, /): ")
                        if operation in {"+","-", "x", "/"}:
                            try:
                                num1 = float(input("Enter the first number -->" ))
                                num2 = float(input("Enter the second number -->" ))
                            except ValueError:
                                print("Invalid input. Please Enter Numeric Value")
                        
                        if operation == "+":
                            print("Result:",add(num1, num2))
                        elif operation == "-":
                            print("Result:",subtract(num1, num2))
                        elif operation == "x":
                            print("Result:",multiply(num1, num2))
                        elif operation == "/":
                            print("Result:",divide(num1, num2))
                        else:
                            print("Invalid input")
                print(f"BOB_AI: {name}, what do you want to do next? ")
                user_asn = input("User: ")








            # if operation in ['add', "addition", '+']:
            #     def add(x,y):
            #         return x + y
            #     def calculator():
            #         calculator ()
            #         num1 = float(input("Enter the first number -->"))
            #         num2 = float(input("Enter the second number -->"))
            #         print("Result:",add(num1, num2))





