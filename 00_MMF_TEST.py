# import statements 
import re
import pandas 


# function goes here 

# checks that ticket name is not blank 
def not_blank(question):
    valid= False 

    while not valid:
            response = input (question) 
            
            if response !="":
                return response
                  
            else: 
             print("sorry - this can't be blank")

def int_check (question, low_num, high_num) :

    
    error =  "Please enter a whole number between {} and {}".format(low_num, high_num)
    
    valid = False 
    while not valid:

        # ask user for number and check if its valid 
        try: 
            response = int(input(question)) 
            # return response 

            if low_num <= response <= high_num: 
                return response 
            else:         
                print( error )

        # if an interger is not entered, display an error 
        except ValueError:
            pass



#Main routine goes here 
name = ""

ticket_count = 0
profit = 0

MAX_TICKETS = 5

while name != "xxx"  and  ticket_count < MAX_TICKETS: 
    
   
    # tells user how many seat are left 
    if ticket_count < MAX_TICKETS - 4 :
        print ("You have {} seats left".format (MAX_TICKETS - ticket_count))

    name = input ("Name: ")

    # If name is exit code, break out loop
    if name == "xxx": 
        break 

    age = int (input("Age: "))

    if age < 16:
        ticket_price = 7.5
    elif age < 65:
        ticket_price = 10.5
    else: 
        ticket_price = 6.5

    profit_made = ticket_price - 5 
    profit += profit_made 

    print ("{} : ${: .2f}" .format(name, ticket_price))
    ticket_count += 1

print ("Profit from Tickets: ${:.2f}".format(profit))

# check that age is valid...
if age < 12: 
    print("sorry you're too young for this movie")
elif age > 130:
    print ("That is very old - it looks like a mistake")
    

if age < 16: 
    ticket_price = 7.5 
elif age < 65:
    ticket_price = 10.5 
else:
    ticket_price = 6.5 

ticket_count += 1 


