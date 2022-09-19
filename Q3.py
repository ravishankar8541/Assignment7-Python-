""" Write a menu driven program with the following options:
a. Check whether a given set of three numbers are lengths of an isosceles
triangle or not
b. Check whether a given set of three numbers are lengths of sides of a right
angled triangle or not
c. Check whether a given set of three numbers are equilateral triangle or not
d. Exit."""
print("1.isosceles triangle")
print("2.angled triangle")
print("3.equilateral triangle")
print("4.Exit")
print("Enter your choice :")
choice=int(input())
match choice:
 case 1:
        print("Enter the value of 3 side :")
        x,y,z=int(input()),int(input()),int(input())
        if x==y or y==z or x==z:
            print("isosceles triangle")
        else:
           print("Not isosceles triangle")  
 case 3:
          print("Enter the value of 3 side :")
          x,y,z=int(input()),int(input()),int(input())
          if x==y and y==z and x==z:
           print("Equilateral triangle")
          else:
            print("Not Equilateral triangle") 
 case 2:
         print("Enter the value of 3 side :")
         x,y,z=int(input()),int(input()),int(input())
         if z*z==x*x+y*y:
            print("Right angled triangle")
         else:
            print("Not Right angled triangle ")
 case 4:     
    exit() 
 case _:
    print("Invalid Keyword")      



