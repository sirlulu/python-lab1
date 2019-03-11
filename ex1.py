#ex1

while True:
    num1 = int(input("Insert the first number: \n"))
    num2 = int(input("Insert the second number: \n"))

    print("The sum of %d and %d is %d" %(num1,num2,num1+num2))
    if(input("Do you want to continue?\n")== 'no'):
        False