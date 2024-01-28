# MOD2-4 Guess
# Chapter 6.2 For loop Number guess, Spring SDEV220
# Lynn E. Prout 1/28/2024

guess_me = 7 # variable set to 7
number = 1   # variable set to 1

while number <= guess_me:    # start of While loop
    if number < guess_me:    # compares the two variables to see -
                             # if "number" is less than "guess_me"
        print('too low')  
    elif number == guess_me: # checks to see if the two variables are equal
        print('found it!')
        break                # This will exit the loop when the elif statement is true
    else:              
        print('oops')        # This section will not process because -
        break                # the elif statement above becomes true as the loop runs- 
                             # and then breaks before it can get to this section
                             
    number += 1              # This adds 1 to the variable "number"

