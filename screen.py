import operation as op


def start():
    options = [1, 2, 3, 4, 5]
    print("Select an options")
    print("\t1. Addition")
    print("\t2. Subtraction")
    print("\t3. Multiplication")
    print("\t4. Division")




    while True:
        selectOption = input("Enter your choice here: ")
        selection = int(selectOption)
        if selection  in options:
            firstNumber = input("Enter first number: ")
            secondNumber = input("Enter second number: ")
            firstInt = int(firstNumber)
            secondInt = int(secondNumber)
            
            if selection == 1: 
                print("Addition of first and second number is : ",op.addition(firstInt, secondInt))
            elif selection == 2:
                print("Subtraction of first and second number is : ",op.subtraction(firstInt, secondInt))
            elif selection == 3:
               print("Multiplication of first and second number is : ",op.multiplication(firstInt, secondInt))
            elif selection == 4:
                print("Division of first and second number is : ",op.division(firstInt, secondInt))
            else:
                print("default behavior")
            

            calculation = input("Would you like to perform next calculation ? (yes/no): ")
            if calculation == "no":
                break
        else:
            print("Invalid choice")

      
