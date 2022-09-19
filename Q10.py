"""Write a program to display day name on the basis of user’s liking of a colour. Ask
user for his favorite colour. User can answer in a sentence like “I like red colour”.
Assuming all colour name entered by user is in lowercase. Use match case to display
day name associated with the colour.
a. Yellow - Monday
b. Blue - Tuesday
c. Orange - Wednesday
d. White - Thursday
e. Black - Friday
f. Red - Saturday
g. All other colours - Sunday"""

print("What is your favorite colour :")
color=str(input())
print("i like ",color,"colour")
match(color):
    case "Yellow":print("Monday")
    case "Blue":print("Tuesday")
    case "Orange":print("Wednesday")
    case "White":print("Thursday")
    case "Black":print("Friday")
    case "Red":print("Saturday")
    case "Green":print("Sundaay")
