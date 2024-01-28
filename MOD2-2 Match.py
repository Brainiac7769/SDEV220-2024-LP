# MOD2-2 Match
# Chapter 4.2 Match, Spring SDEV220
# Lynn E. Prout 1/28/2024

def FourPointTwo():  
    
    small = False # Assign True or False to the variable "small"
    green = False # Assign True or False to the variable "green" 
                                                          
    choices = ["cherry", "pea", "watermelon", "pumpkin"] # Items to be matched to the variables small and green

    if small and green:          # checks if both variables are true
        if "pea" in choices:
            print("Both conditions, small and green, are true", "= pea")
            
    elif small and not green:    # checks if small is true and green is false
        if "cherry" in choices:
            print("Small is true and green is false,", "= cherry")
            
    elif not small and green:    # checks if small is false and green is true
        if "watermelon" in choices:
            print("Small is false and green is true,", "= watermelon")
            
    elif not small and not green: # checks if both variables are false
        if "pumpkin" in choices:
            print("Small is false and green is false,", "= pumpkin")
              
FourPointTwo()