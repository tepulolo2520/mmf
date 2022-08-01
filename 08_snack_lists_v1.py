#Intialise snack list
import pandas

all_names = ['Rangi', 'Manaia', 'Talia', 'Arihi', 'Fetu']
all_tickets = []

# Snack Lists
popcorn = []
mms = []
pita_chips = []
water = []
orange_juice = []

snack_lists = [popcorn, mms, pita_chips, water, orange_juice]

snack_menu_dict = {
    'Popcorn': popcorn,
    'Water': water,
    'Pita Chips': pita_chips,
    'M&Ms': mms,
    'Orange Juice': orange_juice
    }

test_data = [
    [[2, 'Popcorn'], [1, 'Pita Chips'], [1, 'Orange Juice']],
    [[]],
    [[1, 'Water']],
    [[1, 'Popcorn'], [1, 'Orange Juice']],
    [[1, 'M&Ms'], [1, 'Pita Chips'], [3, 'Orange Juice']]
]

count = 0 
for client_order in test_data:

    # Assume no snacks have been bought...
    for item in snack_lists:
        item.append(0)

    # print(snack_lists)

    # get order (hard coded for easy testing)...
    snack_order = test_data[count]
    count += 1

    for item in snack_order:
        if len(item) > 0:
            to_find = (item[1])
            amount = (item[0])
            add_list = snack_menu_dict[to_find]
            print("add list", add_list)
            
            add_list[-1] = amount

         
print ()
print("popcorn: ", snack_lists[0])
print("M&MS: ", snack_lists[1])
print("pita chips: ", snack_lists [2])
print("Water: ", snack_lists[3])
print("print orange juice:", snack_lists[4])
