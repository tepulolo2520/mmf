import re 

# works ot wether string has numbers
# and separates string into amount and item 

test_strings =[
    "Popcorn",
    "2 pc",
    "1.5oJ",
    "4oJ",
]

for item in test_strings: 

    # regular expression to find if item starts with a number 
    number_regex = "^[1-9]"

    # if item has a number, separate it into two (number / item)
    if re.match(number_regex, item): 
        amount = int(item[0])
        desired_snack = item[1:]

    else:
        amount = 1
        desired_snack = item 

    # remove white space around snack 
    desired_snack = desired_snack.strip()

    # if item does not have a number in front, set number to 1

    # print order 
    print("Amount:", amount)
    print("Snack:", desired_snack)
    print("Lenght of snack:", len(desired_snack))
