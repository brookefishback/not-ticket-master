import time

#WELCOME MESSAGE AND CONCERT LIST
print ("Welcome to Ticketmaster Killer - we're like Ticketmaster, but way better!")
time.sleep(3)

print ("Check out our upcoming concerts below:")
time.sleep(2)

print ('1. The Rolling Stones - July 8th | $120')
print ('2. Nirvana - July 12th | $160')
print ('3. Pink Floyd - July 27th | $130')
time.sleep(3)

#USER SELECTION PROMPT AND IF STATEMENTS
print("We know it's hard to choose, but which concert would you like to attend?")
time.sleep(2)

concert_selection = input("Enter the number of the concert you'd like to attend: ")
time.sleep(2)

if concert_selection == '1':
    print("You can't go wrong with The Rolling Stones! We'll need a few more things from you to complete your order")

if concert_selection == '2':
    print("You can't go wrong with Nirvana! We'll need a few more things from you to complete your order")

if concert_selection == '3':
    print("You can't go wrong with Pink Floyd! We'll need a few more things from you to complete your order.")

time.sleep(2)

#ORDER PROCESSING
customer_name = input('Please enter your first and last name: ')
customer_shirt_size = input('Please enter your t-shirt size: ')
customer_card_number = input('Please enter your credit card number: ')
time.sleep(2)

#CONVENIENCE FEE WARNING
print ("Thanks for your order! Before we process your payment, we wanted to let you know there is a 20% convenience fee.")
time.sleep(2)

#UPDATED PRICING
if concert_selection == '1':
    print ('With the 20% convenience fee, The Rolling Stones tickets will be $144')

if concert_selection == '2':
    print ('With the 20% convenience fee, Nirvana tickets will be $192')

if concert_selection == '1':
    print ('With the 20% convenience fee, Pink Floyd tickets will be $156')

order_processing = input("Would you like us to run your card for the above total? Please select Y or N.")

if order_processing == 'Y':
    quit()

if order_processing == 'N':
    quit()