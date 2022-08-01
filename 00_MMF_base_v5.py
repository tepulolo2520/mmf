# import statements
from logging.config import valid_ident
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

# Checks that we have not sold too many tickets
def check_tickets(tickets_sold, ticket_limit):
    # tells user how many seats are left
    if ticket_count < ticket_limit - 1:
        print("you have {} seats"
        "left".format(ticket_limit - ticket_count)) 


    # warns user that one seat is left!
    else:
        print("*** There is ONE seat left!***")

    return ""
    
    # get details...

def get_ticket_price():
    # get age (between 12 and 130 
    age = int_check("age: ") 

    # check that age is valid...
    if age < 12: 
        print("sorry you're too young for this movie")
        return("invalid ticket price")
    elif age > 130:
        print ("That is very old - it looks like a mistake")
        return("invalid ticket price")
    
    if age < 16: 
        ticket_price = 7.5 
    elif age < 65:
        ticket_price = 10.5 
    else:
        ticket_price = 6.5 

    return ticket_price


# Function goes here 
def string_check(choice, options):  

    is_valid = ""
    chosen = ""

    for var_list in options:

        # if the snack is in the lists, return the full 
        if choice in var_list:

            # Get full name of snack and put it 
            # in title case so it looks nice when outputted
            chosen = var_list[0].title()
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



def get_snack():

    # regular expression to find if item starts with a number 
    number_regex = "^[1-9]"
    # valid snacks hold list of all snack
    # Each item in valid snacks is a list with 
    # valid options for each snack <full name, letter code (a, e)
    # , and possible abbreviations etc>
    valid_snacks = [
        ["popcorn", "p" "corn", "a"],
        ["M&M's", "m&m's", "mms", "m", "b"], # first item is M&M
        ["pita chips", "chips","pc", "pita", "c"],
        ["water", "w", "d"] 
    ]


    # valid options for yes / no questions 
    yes_no = [
        ["yes","y"],
        ["no", "n"]
    ]

    # ask user if they want a snack 
    check_snack = "invalid choice"
    while check_snack == "invalid choice": 
        want_snack = input("Do you want to order snacks? ").lower()
        check_snack = string_check(want_snack, yes_no)

    # If the say yes, ask what snacks they want (and add to our snacks)
    if check_snack == "Yes":

        # holds snacks order for a single user. 
        snack_order = []

        desired_snack = ""
        while desired_snack != "xxx": 

            snack_row = []

            # ask user for desired snack and put it lowercase 
            desired_snack = input("Snack: ").lower()

            if desired_snack == "xxx": 
                return snack_order 

            # if item has a number, separate it into two (number / item)
            if re.match(number_regex, desired_snack): 
                amount = int(desired_snack[0])
                desired_snack = desired_snack[1:]

            else:
                amount = 1
                desired_snack = desired_snack

            # remove spaces around snack
            desired_snack = desired_snack.strip()
            
            # remove white space around snack
            snack_choice = string_check(desired_snack, valid_snacks)
            if snack_choice == "invalid choice":
                print("please enter a valid snack")


            # check snack amount is valid (less than 5)
            if amount >= 5: 
                print("sorry - we have a four snacks maximum")
                snack_choice = "invalid choice"
            # add snack And amount to list
            # amount_snack = "{} {}".format(amount, snack_choice)

            # check if snack is valid
            snack_choice = string_check(desired_snack, valid_snacks)
            print ("snack Choice: ", snack_choice)
            snack_row.append(amount)
            snack_row.append(snack_choice)


            # check that snack is not the exit code before adding 
            if snack_choice != "xxx" and snack_choice != "invalid choice": 
                snack_order.append(snack_row)



#************ MAIN ROUTINE ***************

# set up dictionaries / list needed to hold data


# valid options for yes / no questions 
yes_no = [
    ["yes","y"],
    ["no", "n"]
]

# holds snacks order for a single user. 

MAX_TICKETS = 5

name =""
ticket_count = 0
ticket_sales = 0


# ask user if they have used the program before & show instruction

# loop to get ticket details
#start of loop

# initialise loop so that it runs at least once 

while name !="xxx" and ticket_count < MAX_TICKETS : 

    check_tickets(ticket_count, MAX_TICKETS)

    # get name (can't be blank)
    name = not_blank("Name: ")

    #end of the loop if the exit code is entered
    if name == "xxx":
        break 

    ticket_price = get_ticket_price()

    if ticket_price == "invalid ticket price":
        continue

    ticket_count += 1
    ticket_sales += ticket_price

    # get snacks

    check_snack = "invalid choice"
    while check_snack == "invalid choice": 
        want_snack = input("Do you want to order snacks? ").lower()
        check_snack = string_check(want_snack, yes_no)

        print("Want snack", check_snack)

    # If the say yes, ask what snacks they want (and add to our snacks)
    if check_snack == "Yes":
        snack_order = get_snack()
    else:
        snack_order = []
        
    for item in snack_order:
            print(item)

print("we are done")
