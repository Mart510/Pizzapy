# PizzaPy python terminal program project

#import needed files
from Menu import menuPrinter
import PizzaMaker


#print menu for user to read
menuPrinter()

'''
This file to contain the main program, will be linking to other programs
for practice and to keep this clear.

'''

#function to order a special or custom pizza
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
        return 'Special'

    if int(choice) == 2:
        return 'Custom'

#function to choose pizza size
def choosePizzaSize():
    #Get their pizza size
    pizzaSize = 0
    while pizzaSize != 1 or 2 or 3 or 4:
        pizzaSize = input('What size would you like?\n 1. Small, 2. Medium, 3. Large, 4. Chonky')
    PizzaMaker.Pizza.sizePicker(pizzaSize)

#global variables
orderList = [] #Keeps track of all orders

#customer will be asked a series of questions to create their pizza

#greeting
def greeter():
    print(
    '''
    Welcome to PizzaPy
    Please navigate the questions using the numbers on your keyboard\n
    '''
    )

######################################################
#program start
######################################################

greeter()

#intialise pizza
order = PizzaMaker.Pizza()
orderList.append(order)

#ask if they want a special or a custom pizza
match specialOrCustom():
    case 'Special':
        choice = ''
        #ask for size then create a special pizza
        def getInput():
            print(
                '''
                Today's specials are:
                The Meatazza, a meat lovers feast
                The Greenbelt, dedcadence of the forest (vegetarian friendly)
                The PySpecial, our chef's favourite featuring award winning Stracciata italian cheese
                The Mysterios, a pizza created at random in a size of your choosing, great for lovers of all things pizza
                '''
                )
            choice = input('1. Meatazza, 2. Greenbelt, 3. PySecial, 4. Mysterios, 5. Cancel order')
            return choice
        getInput()
        #check if input is valid, if not repeat question and give customer option to cancel/break out of loop
        if int(choice) != 1 or 2 or 3 or 4 or 5:
            getInput()           
        if int(choice) == 5:

        match int(choice):
            case 1:
                order.specialPizza('Meatazza')
            case 2:
                order.specialPizza('Green belt')
            case 3:
                order.specialPizza('PySpecial')
            case 4:
                PizzaMaker.Pizza.specialPizza('Mysterios')
            
        #Set pizza size
        choosePizzaSize()

        #Let them know what they have ordered and how much, give them a chance to decline the order

        print('Your total is {price}').format(price = order.price)


    case 'Custom':
        #ask for size and start making a custom pizza





#if special, ask for size and then create pizza order
def specialOrder():
    choice = ''
    #get the pizza they want
    def getInput():
        print(
            '''
            Today's specials are:
            The Meatazza, a meat lovers feast
            The Greenbelt, dedcadence of the forest (vegetarian friendly)
            The PySpecial, our chef's favourite featuring award winning Stracciata italian cheese
            The Mysterios, a pizza created at random in a size of your choosing, great for lovers of all things pizza
            '''
            )
        choice = input('1. Meatazza, 2. Greenbelt, 3. PySecial, 4. Mysterios, 5. Cancel order')
        return choice
    getInput()
    #check if input is valid, if not repeat question and give customer option to cancel/break out of loop
    if int(choice) != 1 or 2 or 3 or 4 or 5:
        getInput()
    if int(choice) == 5:
        return
    #get pizza size
    
        
    #create pizza

    #give price

'''
#if custom ask for pizza size

#ask for sauce option (max 2)

#ask for cheese option (max 2)

#ask for topping options (max 4)

#total cost, repeat order with price back to customer

#ask customer of they accept

#if yes, ask for payment

#if no cancel order and give option to start again