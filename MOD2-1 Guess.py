# MOD2-1 Guess
# Chapter 4.1 Number guess, Spring SDEV220
# Lynn E. Prout 1/28/2024

def FourPointOne():  
    
    secret = (9)
    
    print("Guess a number between 1 and 10")

    guess = (9)
              
    if guess > secret:  # checks if variable "guess" is greater than variable "secret"
           
            print("☝Too high☝") # prints too high message
        
    elif guess < secret: # checks if variable "guess" is less than variable "secret"
            
            print("☟Too low☟") # prints too low message

    else: # if variable "guess" is equal variable "secret", prints message "just right"
        
            print("ミ✫Just Right✫彡")               

FourPointOne()