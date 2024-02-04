# Lynn Prout - SDEV220 1st 8 weeks Spring 2024
# M03 Programming Assignment- Lists and Functions
# Chapter 7 - 7.4, 7.5, 7.6, 7.7 - Chapter 9 - 9.1, 9.2

def seven_point_4_5_6_7():
    
# Creates a list named "things" with three string (only one cheese) elements.
    #Things to do 7.4
    things = ["mozzarella", "cinderella", "salmonella"]
    
# This section capitalizes the item in the list that is a person
# Note: the determination of which item in the list is capitalized is determined
# by the programmer reading the list and knowing that the 2nd item is the 
# person (0, 1, 2)
    things[1] = things[1].capitalize()
    print("Things to do 7.5")
    print(things)
    print("")

# This section capitalizes the first item in the list.
# Note: Once again, the item to be manipulated is determined by the programmer.
    things[0] = things[0].upper()
    print("Things to do 7.6")
    print(things)
    print("")

# This section deletes the (third item) disease element from the list.
    del things[2]
    print("Things to do 7.7")
    print(things)
    print("I humbly accept the Nobel Prize for making this Python program safer\
 by deleting a disease from a list.")
    print("")

seven_point_4_5_6_7()

# Beginning of Chapter 9 Things to do.

# This defines a function called "good"
def good(): # this is the list that the programmer entered for the function "good"
    return ['Harry', 'Ron', 'Hermione']

# Here the list returned from "good" is printed.
print("Things to do 9.1")
print(good())
print("")
    
# This defines a function called "get_odds" using a FOR loop and a range of 10
# and evaluates the range mathematically to create a group of odd number.    
def get_odds():
        for number in range(10):
            if number % 2 != 0:
                yield number

# This starts a counter to go through the for loop.
counter = 1

# This for loop finds and print the third value from the function "get_odds".
for number in get_odds():
    if counter == 3:
        print("Things to do 9.2")
        print("The third odd number is:", number)
        break # This "break" ends the for loop after it finds the third odd number.
    counter += 1
# end of nine_point_1_2()    