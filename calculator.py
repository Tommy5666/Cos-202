print("===== MATHEMATICAL CALCULATOR =====")

while True:
    print("\nChoose an operation")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Modulus (%)")
    print("6. Power (**)")
    print("7. Floor Division (//)")
    print("8. Clear")
    print("9. OFF")

    choice = input("Enter choice: ")

    if choice == "9":
        print("Calculator OFF")
        break

    if choice == "8":
        print("\n" * 50)
        continue

    if choice in ["1","2","3","4","5","6","7"]:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == "1":
            print("Answer =", num1 + num2)

        elif choice == "2":
            print("Answer =", num1 - num2)

        elif choice == "3":
            print("Answer =", num1 * num2)

        elif choice == "4":
            if num2 != 0:
                print("Answer =", num1 / num2)
            else:
                print("Cannot divide by zero")

        elif choice == "5":
            print("Answer =", num1 % num2)

        elif choice == "6":
            print("Answer =", num1 ** num2)

        elif choice == "7":
            print("Answer =", num1 // num2)

    else:
        print("Invalid Choice")