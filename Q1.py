# Write a python script to display the number of days in a given month number
month=int(input("Enter a number :"))
match month:
 case month if month in (1,3,5,7,8,10,12):
  print("31 Days")
 case month if month in (4,6,9,11):
   print("30 days")
 case 2:
    print("28 or 29 days") 
 case _:
   print("Invalid Month number")    