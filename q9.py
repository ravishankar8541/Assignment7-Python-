"""Write a python script to check whether a given year is
a. Non century leap year
b. Century leap year
c. Non century non leap year
d. Century non leap year"""

print("Enter the year :")
year=int(input())
match(year):
    case year if year%100 :print("Non century leap year ")
    case year if year%100==0 and year%400:print("Century leap year")
    case year if year%100 and year%4:print("Non century non leap year")
    case year if year%100 and year%4==0:print("non Century leap year")
  