import random

#To create the Pizza class and control all of it's methods and interactions
'''
function will call and create a empty pizza, then successive user inputs
will populate the pizza attributes and total the cost
'''

#make sub classes for sauces, cheese, toppings
class Pizza:
    def __init__(self, size = [], sauce = [], cheese = [], toppings = [], specialYorN = ''):
        self.size = size
        self.sauce = sauce
        self.cheese = cheese
        self.toppings = toppings
        self.price = 0.00
        self.specialYorN = specialYorN

    #Explain the pizza options
    def __repr__(self):
        return print(
        '''
        Pizza order number {order}
        A {size} pizza topped with {sauce}, {cheese}, {toppings}
        '''
        .format(order = self.orderNumber,
                size = self.size,
                sauce = self.sauce,
                cheese = self.cheese,
                toppings = self.toppings
                )   
        )
    

    #Method to let the customer know what they ordered
    def customerOrder(self):
        # temp variables to hold everything on the pizza
        pass
        #print out the size and then a string with all of the cheese, sauce and topping options

    #Method to calculate cost of a special pizza
    def specialCost(self):
        self.price += self.size[1]
        

    #Method to calculate the cost of custom pizza
    def cost(self):
        total = 0
        #cost of the size
        total += self.size[1]
        #cost of the sauce(s)
        for i in range(len(self.sauce)):
            total += self.sauce[i][1]
        #cost of the cheese(s)
        for i in range(len(self.cheese)):
            total += self.cheese[i][1]
        #cost of the topping(s)
        for i in range(len(self.toppings)):
            total += self.toppings[i][1]
        self.price = total
        return

    #Special Menu Method
    def specialPizza(self, choice):
        match choice:
            case 'Meatazza':
                #create a meatazza pizza
                self.sauce.append(pizzaSauce[3])
                self.cheese.append(pizzaCheese[0])
                self.cheese.append(pizzaCheese[1])
                self.toppings.append(pizzaToppings[0])
                self.toppings.append(pizzaToppings[2])
                self.toppings.append(pizzaToppings[1])
                self.toppings.append(pizzaToppings[3])
                self.toppings.append(pizzaToppings[4])
                self.price = 5.00
                self.specialYorN = 'Meatazza'
            case 'Green belt':
                #create a green belt pizza
                self.sauce.append(pizzaSauce[0])
                self.sauce.append(pizzaSauce[1])
                self.cheese.append(pizzaCheese[1])
                self.toppings.append(pizzaToppings[9])
                self.toppings.append(pizzaToppings[13])
                self.toppings.append(pizzaToppings[6])
                self.toppings.append(pizzaToppings[12])
                self.toppings.append(pizzaToppings[15])
                self.price = 4.50
                self.specialYorN = 'Green belt'

            case 'PySpecial':
                #create a PySpecial
                self.sauce.append(pizzaSauce[3])
                self.cheese.append(pizzaCheese[3])
                self.cheese.append(pizzaCheese[1])
                self.toppings.append(pizzaToppings[5])
                self.toppings.append(pizzaToppings[0])
                self.toppings.append(pizzaToppings[2])
                self.toppings.append(pizzaToppings[10])
                self.toppings.append(pizzaToppings[6])
                self.price = 8.00
                self.specialYorN = 'PySpecial'

            case 'Mysterios':
                #create mysterios pizza
                self.sauce.append(pizzaSauce[random.randint(0, (len(pizzaSauce)-1))])
                self.cheese.append(pizzaCheese[random.randint(0, (len(pizzaCheese)-1))])
                self.cheese.append(pizzaCheese[random.randint(0, (len(pizzaCheese)-1))])
                self.toppings.append(pizzaToppings[random.randint(0, (len(pizzaToppings)-1))])
                self.toppings.append(pizzaToppings[random.randint(0, (len(pizzaToppings)-1))])
                self.toppings.append(pizzaToppings[random.randint(0, (len(pizzaToppings)-1))])
                self.toppings.append(pizzaToppings[random.randint(0, (len(pizzaToppings)-1))])
                self.price = 3.75
                self.specialYorN = 'Mysterios'

    #choosing sauce(s)
    def addSauce(self, itemnum):
        self.sauce.append(pizzaSauce[itemnum])

    #choosing cheese(s)
    def addCheese(self, itemnum):
        self.cheese.append(pizzaCheese[itemnum])

    #choosing topping(s) (max 4)
    def addTopping(self, itemnum):
        self.toppings.append(pizzaToppings[itemnum])


    #Method to update pizza size
    def sizePicker(self, number):
        match number:
            case 1:
                self.size = pizzaSize[0]
                #Size small
            case 2:
                self.size = pizzaSize[1]
                #Size medium
            case 3:
                self.size = pizzaSize[2]
                #Size large
            case 4:
                self.size = pizzaSize[3]
                #Size chonky                

    #Method to update sauce options
    def saucePicker(self, number):
        match number:
            case 1:
                self.sauce
                

#Pizza variables to be used when creating a pizza
#pizza sizes
pizzaSize = [
    ['small', 8.99], #0
    ['medium', 12.99], #1
    ['large', 16.99], #2
    ['chonky', 21.99] #3
]

#dictionaries to control all pizza variables
#pizza sauces
pizzaSauce = [
    ['tomato and basil', 0.50], #0
    ['garlic and herb', 0.60], #1
    ['sweet bbq', 0.75], #2
    ['fire roasted', 1.00] #3
]

#cheese options
pizzaCheese = [
    ['cheddar', 1.00,], #0
    ['mozzarella', 2.00,], #1
    ['pepperjack', 2.00,], #2
    ['stracciata', 4.00] #3
]

#pizza toppings 
pizzaToppings = [
    ['pepperoni', 0.50], #0
    ['sliced ham', 0.50], #1
    ['meatballs', 0.50], #2
    ['bacon', 0.50], #3
    ['chicken', 0.50], #4
    ['sausage', 0.50], #5
    ['onions', 0.10], #6
    ['jalepenos', 0.20], #7
    ['pineapple', 0.15], #8
    ['mushrooms', 0.40], #9 
    ['chorizo', 0.70], #10
    ['prawns', 0.65], #11
    ['rocket', 0.55], #12
    ['olives', 0.10], #13
    ['anchoives', 0.25], #14
    ['artichoke', 0.60], #15
    ['egg', 0.80], #16 
    ['spinach', 0.30], #17
    ['tomatoes', 0.30], #18
    ['garlic', 0.40] #19
]