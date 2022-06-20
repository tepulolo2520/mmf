# import statements 


# functions go here 


# checks that input is not blank
def not_blank (question, error_message ):
      valid= False 

      while not valid:
            response = input(question) 
            
            if response !="":
                  return response
                  
            else: 
                  print(error_message)


# checks for numbers between a high and low number
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



# initialise loop so that it runs at least once 
name = ""
count = 0
MAX_TICKETS = 5

while name != "xxx"  and  count < MAX_TICKETS: 
    print ("You have {} seats left".format(MAX_TICKETS - count))

# Get details...
    print()
    name = not_blank("Name: ", "Don't be shy")
    if name == "xxx":
        break

    count += 1
    print()

    # main routine goes here 
    age = int_check("Age: ", 12,  130) 




# end of the loop if the exit code is entered
if count == MAX_TICKETS: 
    print("You have sold all available tickets!")
else:
    print ("You have sold {} tickets. There are {} places still available".format (count, MAX_TICKETS - count))



