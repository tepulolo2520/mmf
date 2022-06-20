# funtion goes here 

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

# main routine goes here 
age = int_check("Age: ", 12, 130) 