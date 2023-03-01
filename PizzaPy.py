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
        return choice
    
    #specials option
    if int(choice) == 1:
        return 'Special'

    if int(choice) == 2:
        return 'Custom'

#function to choose pizza size
def choosePizzaSize():
    #Get their pizza size
    pizzaSize = 0
    while pizzaSize != range(1, 4):
        pizzaSize = input('What size would you like?\n 1. Small, 2. Medium, 3. Large, 4. Chonky')
    order.sizePicker(pizzaSize)

#function to choose sauce option(s)
def sauce():
    sauceChoice = 0
    while sauceChoice != range(1, 4):
        sauceChoice = input('What sauce would you like?\n 1. Tomato and basil, 2. Garlic and herb, 3. Sweet BBQ, 4. Fire roasted tomato sauce')
    order.addSauce((sauceChoice-1))


#function to add cheese option(s)
def cheese():
    cheeseChoice = 0
    while cheeseChoice != range(1, 4):
        cheeseChoice = input('What cheese would you like?\n 1. Cheddar, 2. Mozzarella, 3. Pepperjack, 4. Stracciata')
    order.addCheese((cheeseChoice-1))        


#function to add topping(s)
def toppings():
    toppingChoice = 0
    while toppingChoice != range(1, 20):
        toppingChoice = input('1. Pepperoni, 2. Sliced ham, 3. Meatballs, 4. Bacon\n 5. Chicken, 6. Sausage, 7. Onions, 8. Jalepenos\n 9. Pineapple, 10. Mushrooms, 11. Chorizo, 12. Prawns\n 13. Rocket, 14. Olives, 15. Anchoives, 16. Artichoke\n 17. Egg, 18. Spinach, 19. Tomatoes, 20. Garlic\n 21. No more please')
        if toppingChoice == 21:
            break
    order.addTopping((toppingChoice-1))

#global variables
orderList = [] #Keeps track of all orders

#customer will be asked a series of questions to create their pizza

######################################################
#program start
######################################################

#greeting
print(
'''
Welcome to PizzaPy
Please navigate the questions using the numbers on your keyboard\n
'''
)


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
        #if int(choice) == 5:
            #exit function to create

        match int(choice):
            case 1:
                order.specialPizza('Meatazza')
            case 2:
                order.specialPizza('Green belt')
            case 3:
                order.specialPizza('PySpecial')
            case 4:
                order.specialPizza('Mysterios')
            
        #Set pizza size
        choosePizzaSize()
        #calculate cost
        order.specialCost()

        if order.specialYorN == 'Meatazza' or 'Green belt' or 'PySpecial':
            #if the pizza they have ordered is not a Mysterios
            #Let them know what they have ordered and how much
            print('So that is a {pizzasize} {pizzaname}\n').format(pizzasize = order.size, pizzaname = order.specialYorN)
            print('Your total is {price}').format(price = order.price)

        if order.specialYorN == 'Myseterios':
            #let them know what is on their pizza
            #Let them know the price
            print('So your {pizzasize} Mysterios has the following toppings:\n').format(pizzasize = order.size)
            print('{sauce}, {cheese1}, {cheese2}, {topping1}, {topping2}, {topping3}, {topping4},').format(sauce = order.sauce[0], cheese1 = order.cheese[0][0], cheese2 = order.cheese[1][0], topping1 = order.toppings[0][0], topping2 = order.toppings[1][0], topping3 = order.toppings[2][0], topping4 = order.toppings[3][0])


    case 'Custom':
        #ask for size and start making a custom pizza
        choosePizzaSize()
        

        #ask for sauce options
        sauce()
        #second sauce?
        tempChoice = 0
        while tempChoice != 1 or 2:
            tempChoice = input('Would you like a second sauce?\n 1. Yes, 2. No')
        if tempChoice == 1: #yes
            sauce()
               
        #ask for cheese options
        cheese()
        #second cheese?
        tempChoice = 0
        while tempChoice != 1 or 2:
            tempChoice = input('Would you like a second cheese option?\n 1. Yes, 2. No')
        if tempChoice == 1: #yes
            cheese()

        #ask for topping options
        print('Now please choose up to 4 toppings')
        for i in range(0,3):
            order.toppings()




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
'''