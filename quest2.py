#RAMANDEEP SINGH
#22076254
RED = "red"
BLUE = "blue"
YELLOW = "yellow"

clr1 = input("Enter the first color (red/blue/yellow)")
clr2 = input("Enter the second color (red/blue/yellow)")


if clr1 not in (RED, BLUE, YELLOW):
    print("Error: Invalid Color1")

elif clr2 not in (RED, BLUE, YELLOW):
    print("Error: Invalid Color2")
  
elif clr1==clr2:
    print("Error: The two colors you entered are same")

else:
    if clr1 == RED:
        if clr2 == BLUE:
            print("Purple")
        else:
            print("Orange")
    elif clr1 == BLUE:
        if clr2 == RED:
            print("Purple")
        else:
            print("Green")
    else:
        if clr2 == RED:
            print("Orange")
        else:
            print("Green")