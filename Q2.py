""" Write a menu driven program to perform following operations - Addition, Subtraction,
Multiplication, Division"""
print("1. Addition ")
print("2. Subtraction")
print("3. Multiplication")
print("4. Divison")
print("5.Exit")
print("Enter your choice :")
choice=int(input())
match choice:
    case 1:
        print("Enter two number :")
        x,y=int(input()),int(input())
        print("Sum =",x+y)
    case 2:    
        print("Enter two number :")
        x,y=int(input()),int(input())
        print("Difference =",x-y)
    case 3:
        print("Enter two number :")
        x,y=int(input()),int(input)  
        print("Multiplication =",x*y)
    case 4:
        print("Enter two number :")
        x,y=int(input()),int(input())  
        print("Division =",x/y)   
    case 5:
        exit()    
    case _:
     print("Invalid choice please enter correct keyword")     
