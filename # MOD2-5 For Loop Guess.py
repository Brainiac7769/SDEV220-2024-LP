# MOD2-5 For Loop Guess
# Chapter 6.3 For loop guess, Spring SDEV220
# Lynn E. Prout 1/28/2024

guess_me = 5                 # Variable set to 5

for number in range(10):     # for loop to compare the numbers 0 thru 9 to the variable "guess_me"
    if number < guess_me:    # checks for less than condition
        print('too low')
    elif number == guess_me: # Once the loop get to 5, this becomes true, the print statement -
        print('found it!')   # executes, and then the loop breaks.
        break                
    else:
        print('oops')
        break                # This section does not execute because the for loop above breaks-
                             # once the elif comparison is true.