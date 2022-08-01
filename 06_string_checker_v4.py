import re

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
            break 

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

        # check snack amount is valid (less than 5)
        if amount >= 5: 
            print("sorry - we have a four snacks maximum")
            snack_choice = "invalid choice"
        # add snack And amount to list
        # amount_snack = "{} {}".format(amount, snack_choice)

        snack_row.append(amount)
        snack_row.append(snack_choice)


        # check that snack is not the exit code before adding 
        if snack_choice != "xxx" and snack_choice != "invalid choice": 
            snack_order.append(snack_row)

# Show snacks ordrs 
print()
if len(snack_order) == 0:
    print("Snack Ordered: None")

else: 
    print("Snacks Ordered:")

    for item in snack_order:
        print(item)