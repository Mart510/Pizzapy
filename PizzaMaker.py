#To create the Pizza class and control all of it's methods and interactions
'''
function will call and create a empty pizza, then successive user inputs
will populate the pizza attributes and total the cost
'''
class Pizza:
    def __init__(self, size = {}, sauce = {}, cheese = {}, toppings = {}):
        self.size = size
        self.sauce = sauce
        self.cheese = cheese
        self.toppings = toppings
        self.price = 0.00
        self.orderNumber = 0

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
    
    #Method to update pizza size
    def sizePicker(self, number):
        match number:
            case 1:
                self.size = pizzaSize('small')
                self.price += pizzaSize.get('small')


    #Method to update sauce options

    #Method to update toppings

    #Method to calculate price

#Pizza variables to be used when creating a pizza
#pizza sizes
pizzaSize = {
    'small': 8.99,
    'medium': 12.99,
    'large': 16.99,
    'chonky': 21.99
}

#dictionaries to control all pizza variables
#pizza sauces
pizzaSauce = {
    'tomato and basil': 0.50,
    'garlic and herb': 0.60,
    'sweet bbq': 0.75,
    'fire roasted': 1.00
}

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
