# import statements


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

#************ MAIN ROUTINE ***************

# set up dictionaries / list needed to hold data

# ask user if they have used the program before & show instruction

# loop to get ticket details
#start of loop

# initialise loop so that it runs at least once 
MAX_TICKETS = 5

name =""
ticket_count = 0
ticket_sales = 0

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
    age = int_check("age: ", 12, 130) 

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