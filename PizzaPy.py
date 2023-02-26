# PizzaPy python terminal program project

#import needed files
from Menu import menuPrinter

#print menu for user to read
menuPrinter()


'''
This file to contain the main program, will be linking to other programs
for practice and to keep this clear.

'''

#customer will be asked a series of questions to create their pizza

#greeting
def greeter():
    print(
    '''
    Welcome to PizzaPy
    Please navigate the questions using the numbers on your keyboard
    '''
    )

#one of our specials or a custom pizza?
def specialOrCustom():
    choice = ''
    #function to repeat input string
    def getInput():
        print('Would you like a one of our specials or do you want to make your own pizzaPy?')
        choice = input('1. Order from the specials menu \n 2. Order a custom pizza\n 3. Cancel')
        return choice

    getInput()
    #check if input is valid, if not repeat question and give customer option to cancel/break out of loop
    if int(choice) != 1 or 2 or 3:
        getInput()
    if int(choice) == 3:
        return
    
    #specials option
    if int(choice) == 1:
        specialOrder()

    if int(choice) == 2:
        customOrder()
       
#if special, ask for size and then create pizza order

#if custom ask for pizza size

#ask for sauce option (max 2)

#ask for cheese option (max 2)

#ask for topping options (max 4)

#total cost, repeat order with price back to customer

#ask customer of they accept

#if yes, ask for payment

#if no cancel order and give option to start again