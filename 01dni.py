# 2-num calculator 

num1=float(input("Enter the first number: "))
num2=float(input("Enter the second number: "))
print("\n")

while True:
    print("ARITHMETIC OPERATIONS AVAILABLE:\n")
    print("1- Addition\n2- Subtraction\n3- Multiplication\n4- Division\n5- Exponent\n6- Exit\n")
    operation=int(input("Enter the choice for arithmatic operation to be performed: "))
    
    if operation==1:
        print("Addition: ",num1," + ",num2, " = ",num1+num2,"\n")
    elif operation==2:
        print("Subtraction: ",num1," - ",num2, " = ",num1-num2,"\n")
        print("Subtraction: ",num2," - ",num1, " = ",num2-num1,"\n")
    elif operation==3:
        print("Multiplication: ",num1," x ",num2," = ",num1*num2,"\n")
    elif operation==4:
        if num2 != 0:
            print("Division: ",num1," / ",num2," = ",num1/num2,"\n")
        else:
                print("Error! Division by zero.")
    elif operation==5:
    
        pwr=int(input("Enter the power of: "))
        if pwr==abs(pwr):
            print("Exponent: ",num1," to the power of ",pwr," = ",num1**pwr,"\n","         ",num2," to the power of ",pwr," = ",num2**pwr,"\n")
        else:
            print("Unable to compute power due to given input (must be positive integer)\n")
        
    elif operation==6:
        print("Exited")
        break
    else:
        print('Invalid Choice\n')
