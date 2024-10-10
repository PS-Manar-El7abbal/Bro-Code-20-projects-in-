#python temperature converter
from msvcrt import kbhit


unit=input("Is this temperature in celecius or fahrenhait (C/F)")
temp=float(input("Enter the temperature "))

if unit=="C":
    temp=round((9*temp)/5+32,1)
    print(f"The temperature in fahrinheit is :{temp} F ")
    
elif unit=="F":
     temp=round((temp-32)*5/9,1)
     print(f"The temperature in celicius is :{temp} C")
     
else:
    print(f"The {unit} is not valid unit")
