def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def Multiply(a,b):
    return a*b
def Divide(a,b):
    return a/b

print("Select Operation:")
print("1.Addition")
print("2.Subtraction")
print("3.Multipliction")
print("4.Division")

while True:
    choice = input("Enter Choice (1/2/3/4): ")
    
    if choice in['1','2','3','4']:
        num1=float(input("ENTER THE FIRST NUMBER:"))
        num2=float(input("ENTER THE SECOND NUMBER:"))
        
        if choice == '1':
            print(f"{num1} + {num2} = {add(num1,num2)}")
            

        elif choice == '2':
                print(f"{num1} - {num2} = {subtract(num1,num2)}")

        elif choice == '3':
                    print(f"{num1} * {num2} = {Multiply(num1,num2)}") 

        elif choice == '4':
            if num2 !=0:
                print(f"{num1} / {num2} = {Divide(num1,num2)}")
            else:
                print("Error! Division by zero.")
                
        next_calculation = input("Do you want to perform another calculation? (yes/no):")
        if next_calculation.lower() !='yes':
            break
    else:
        print("Invalid Input")

        calculator()       
        

                    

        

                        


    
