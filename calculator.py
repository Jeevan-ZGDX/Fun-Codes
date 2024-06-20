# ********************* HOW TO BUILD A SIMPLE CALCULATION IN PYTHON STEP BY STEP ***************************
# 1. ADD
# 2. SUBTRACT
# 3. MULTIPLY
# 4. DIVIDE
# 5. POWER
# 6. INTEGRATION
# 7. DIFFRENTIATION

print("Select an operation to perfom: ")
print("1. ADD")
print("2. SUBTRACT")
print("3. MULTIPLY")
print("4. DIVIDE")
print("5. POWER")
print("6. INTEGRATION")
print("7. DIFFRENTIATION")

operation = input()

if operation == "1":
    num1 = input("Enter frist number: ")
    num2 = input("Enter second number: ")
    print("The sum is " , int(num1) + int(num2))
elif operation == "2":
    num1 = input("Enter frist number: ")
    num2 = input("Enter second number: ")
    print("The subtraction is " , int(num1) - int(num2))
elif operation == "3":
    num1 = input("Enter frist number: ")
    num2 = input("Enter second number: ")
    print("The product is " , int(num1) * int(num2))
elif operation == "4":
    num1 = input("Enter frist number: ")
    num2 = input("Enter second number: ")
    print("The quotient is " , int(num1) / int(num2))
elif operation == "5":
    num1 = input("Enter base number: ")
    num2 = input("Enter power number: ")
    print("The answer is " , int(num1) ** int(num2))
elif operation == "6":
    LL = int(input("Enter lower limit number: "))
    HL = int(input("Enter higher limit number: "))
    Z = HL - LL
    X = int(input("Enter the power value: "))
    N = X + 1
    J = (Z ** N)/N
    print("integrated value: ", J)
elif operation == "7":
    main_num = int(input("Enter a sub value: "))
    power = int(input("Enter a power value: "))
    A = power - 1
    B = (main_num ** A)
    L = B * power
    print("The Diffrentiation is: ", L)
else:
    print("Invalid Entry")
