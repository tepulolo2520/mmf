# import statements
import re

#function goes here

# checks that ticket name is not blank
def not_blank(question):
    
    valid= False 

    while not valid:
            response = input (question) 
            
            if response !="":
                return response
                  
            else: 
             print("sorry - this can't be blank")

#checks for an interger more than 0
def int_check (question) :

    
    error =  "Please enter a whole number that is more than zero"
    
    valid = False 
    while not valid:

        # ask user for number and check if its valid 
        try: 
            response = int(input(question)) 
            # return response 

            if response > 0: 
                return response 
            else:         
                print( error )

        # if an interger is not entered, display an error 
        except ValueError:
            print(error)


# Function goes here 
def string_check(choice, options):  

    for var_list in options:

        # if the snack is in the lists, return the full 
        if choice in var_list:

            # Get full name of snack and put it 
            # in title case so it looks nice when outputted
            chosen = var_list [0] .title()
            is_valid = "yes"
            break 

        # if chosen option is not valid, set is_valid to no
        else: 
            is_valid = "no" 

        # if the snack is not OK -ask question again.
        if is_valid == "yes":
            return chosen
        else:
            return "invalid choice"
#************ MAIN ROUTINE ***************

# set up dictionaries / list needed to hold data
valid_snacks = [
    ["popcorn", "p" "corn", "a"],
    ["mms", "M&M's", "m&m's", "m", "b"], # first item is mms
    ["pita chips", "chips","pc", "pita", "c"],
    ["water", "w", "d"] 
]


# valid options for yes / no questions 
yes_no = [
    ["yes","y"],
    ["no", "n"]
]

# holds snacks order for a single user. 
snack_order = []

ticket_count = 0
ticket_sales = 0
MAX_TICKETS = 5

number_regex = "^[1-9]"

# ask user if they have used the program before & show instruction

# loop to get ticket details
#start of loop

# initialise loop so that it runs at least once 
name =""
while name !="xxx" and ticket_count < MAX_TICKETS : 

    # tells user how many seats are left
    if ticket_count < MAX_TICKETS - 1:
        print("you have {} seats"
        "left".format(MAX_TICKETS - ticket_count)) 


    # warns user that one seat is left!
    else:
        print("*** Ther is ONE seat left!***")
    
    # get details...

    # get name (can't be blank)
    name = not_blank("Name: ")

    #end of the loop if the exit code is entered
    if name == "xxx":
        break 

    # get age (between 12 and 130 
    age = int_check("age: ") 

    # check that age is valid...
    if age < 12: 
        print("sorry you're too young for this movie")
        continue
    elif age > 130:
        print ("That is very old - it looks like a mistake")
        continue
    
    if age < 16: 
        ticket_price = 7.5 
    elif age < 65:
        ticket_price = 10.5 
    else:
        ticket_price = 6.5 

    ticket_count += 1

