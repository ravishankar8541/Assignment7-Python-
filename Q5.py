"""Write a program which takes a number from user. Print Saurabh Shukla if the number
is even, print Prateek Jain if the number is negative odd number and print Aditya
Choudhary if number is positive odd number"""

n=int(input("Enter a number :"))
match(n):
    case n if n%2==0 :print("Saurabh Shukla ")
    case n if n%2 and n>0 :
        if n>0:
           print("Aditya Chaudhary")  
    case n if n%2 and n<0:
             print("print Prateek Jain")
