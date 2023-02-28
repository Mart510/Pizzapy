#To create the Pizza class and control all of it's methods and interactions
'''
function will call and create a empty pizza, then successive user inputs
will populate the pizza attributes and total the cost
'''

#make sub classes for sauces, cheese, toppings
class Pizza:
    def __init__(self, size = [], sauce = [], cheese = [], toppings = []):
        self.size = size
        self.sauce = sauce
        self.cheese = cheese
        self.toppings = toppings
        self.price = 0.00

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
    #Method to count order number
    def counter(self):
        self.orderNumber += 1

    #Special Menu Method
    def special(self, choice):
        match choice:
            case 'Meatazza':
                #create a meatazza pizza

            case 'Green belt':
                #create a green belt pizza

            case 'PySpecial':
                #create a PySpecial
                
            case 'Mysterios':
                #create mysterios pizza


    #Method to update pizza size
    def sizePicker(self, number):
        match number:
            case 1:
                self.size = pizzaSize[0].append()
                #self.price += pizzaSize.get('small')
            case 2:
                self.size = pizzaSize[1].append()
                #self.price += pizzaSize.get('medium')
            case 3:
                self.size = pizzaSize[2].append()
                #self.price += pizzaSize.get('large')
            case 4:
                self.size = pizzaSize[3].append()
                #self.price += pizzaSize.get('chonky')                

    #Method to update sauce options
    def saucePicker(self, number):
        match number:
            case 1:
                self.sauce
                

    #Method to update toppings

    #Method to calculate price

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
pizzaCheese = {
    'cheddar': 1.00,
    'mozzarella': 2.00,
    'pepperjack': 2.00,
    'stracciata': 4.00
}

#pizza toppings 
pizzaToppings = {
    'pepperoni': 0.50,
    'sliced ham': 0.50,
    'meatballs': 0.50,
    'bacon': 0.50,
    'chicken': 0.50,
    'sausage': 0.50,
    'onions': 0.10,
    'jalepenos': 0.20,
    'pineapple': 0.15,
    'mushrooms': 0.40,
    'chorizo': 0.70,
    'prawns': 0.65,
    'rocket': 0.55,
    'olives': 0.10,
    'anchoives': 0.25,
    'artichoke': 0.60,
    'egg': 0.80,
    'spinach': 0.30,
    'tomatoes': 0.30,
    'garlic': 0.40
}

#function to create pizza


#choosing size




#choosing sauce(s)

#choosing cheese(s)

#choosing topping(s) (max 4)
