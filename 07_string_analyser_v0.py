import re

number_regex = "^[1-9]"

desired_snack = "7 mms"

# if item has a number, separate it into two (number / item)
if re.match(number_regex, desired_snack): 
    amount = int(desired_snack[0])
    desired_snack = desired_snack[1:]

else:
    amount = 1


print("amount", amount)
print("Item: {}".format(desired_snack))