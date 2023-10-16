import math

while True:
    print("Welcome to Simple Calculator")
    print("Your options are:")
    print("1) Addition (+)")
    print("2) Subtraction (-)")
    print("3) Multiplication (*)")
    print("4) Division (/)")
    print("5) Exponentiation (^)")
    print("6) Square Root (√)")
    print("7) Quit")

    choice = input("Choose an option (1/2/3/4/5/6/7): ")

    if choice == "7":
        print("Thank you for using the calculator.")
        break

    if choice in {'1', '2', '3', '4', '5', '6'}:
        try:
            num1 = float(input("Enter the first number: "))
            if choice != '6':
                num2 = float(input("Enter the second number: "))
            if choice == '1':
                result = num1 + num2
            elif choice == '2':
                result = num1 - num2
            elif choice == '3':
                result = num1 * num2
            elif choice == '4':
                if num2 == 0:
                    result = "Cannot divide by zero"
                else:
                    result = num1 / num2
            elif choice == '5':
                result = num1**num2
            elif choice == '6':
                if num1 < 0:
                    result = "Cannot calculate the square root of a negative number"
                else:
                    result = math.sqrt(num1)
            print(f"Result: {result}")
        except ValueError:
            print("Invalid input. Please enter valid numbers.")
    else:
        print("Invalid choice. Please select a valid option.")
