

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


# valid snacks hold list of all snack
# Each item in valid snacks is a list with 
# valid options for each snack <full name, letter code (a, e)
# , and possible abbreviations etc>
