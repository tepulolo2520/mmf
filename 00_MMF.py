# Functions go here 

def not_blank (question):
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
count = 0
MAX_TICKETS = 5 

name = not_blank("Name: ")

while name != "xxx"  and  count < MAX_TICKETS: 
    
    # tells user how many seats are left! 
    if count < 4:
        print( "You have {} seats ""Left".format (MAX_TICKETS - count))
      # Warns user that only one seat is left!
    else: 
        print("*** There is one seat left!! ***")
        
      # Get details...
    name = not_blank("Name: ")
    count += 1
    print()

    age = int_check("Age: ", 12, 130) 

# Calculate profit etc
if count == MAX_TICKETS: 
    print("You have sold al available tickets!")
else:
    print ("You have sold {} tickets.  \n" 
    "There are {} places still available" 
    .format (count, MAX_TICKETS - count))
