

# string checking functions, takes in 
# question and list of valid responses 
def string_checker  (question, to_check) : 

    valid = False 
    while not valid:

        response = input (question). lower()
        
        if response in to_check:
            return response 
        
    else: 
        for item in to_check:
        #checks if response is first letter of 
        #an item in the list 
            if response == item[0]:
                return response
        #note: returns the entire response