name = ""

ticket_count = 0
profit = 0

MAX_TICKETS = 5

while name != "xxx"  and  ticket_count < MAX_TICKETS: 
    
   
    # tells user how many seat are left 
    if ticket_count < MAX_TICKETS - 4 :
        print ("You have {} seats left".format (MAX_TICKETS - ticket_count))

    name = input ("Name: ")

    # If name is exit code, break out loop
    if name == "xxx": 
        break 

    age = int (input("Age: "))

    if age < 16:
        ticket_price = 7.5
    elif age < 65:
        ticket_price = 10.5
    else: 
        ticket_price = 6.5

    profit_made = ticket_price - 5 
    profit += profit_made 

    print ("{} : ${: .2f}" .format(name, ticket_price))
    ticket_count += 1

print ("Profit from Tickets: ${:.2f}".format(profit))

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
 
# End of ticket loop

# Calculate profit etc...
if ticket_count == MAX_TICKETS: 
    print ("You have sold all the available tickets!")
else:
    print("you have sold {} tickets.  \n"
          "There are {} places still available"
          .format (ticket_count, MAX_TICKETS -ticket_count ) )
