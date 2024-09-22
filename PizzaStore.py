# This is a simple implementation of the Factory Pattern
# The Factory Pattern defines an interface for creating an object, but lets subclasses alter the type of objects that will be created. Factory Method lets a class defer instantiation to subclasses.
# Factories encapsulate object creation
# Creators and Products

from abc import ABC, abstractmethod

# Abstract Creator
class PizzaStore(ABC):
    def orderPizza(self, type):
        pizza = self.createPizza(type)
        
        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()
        
        return pizza
    
    # Abstract factory method
    @abstractmethod
    def createPizza(self, type):
        pass

# Abstract Product
class Pizza(ABC):
    def __init__(self):
        self.name = ""
        self.dough = ""
        self.sauce = ""
        self.toppings = []

    def prepare(self):
        print("Preparing " + self.name)
        print("Tossing dough...")
        print("Adding sauce...")
        print("Adding toppings:")
        for topping in self.toppings:
            print(" " + topping)

    
    def bake(self):
        print("Bake for 25 minutes at 350")
    
    def cut(self):
        print("Cutting the pizza into diagonal slices")
    
    def box(self):
        print("Place pizza in official PizzaStore box")

# Concrete Products
class NYStyleCheesePizza(Pizza):
    def __init__(self):
        super().__init__()
        self.name = "NY Style Sauce and Cheese Pizza"
        self.dough = "Thin Crust Dough"
        self.sauce = "Marinara Sauce"
        self.toppings.append("Grated Reggiano Cheese")
    
class ChicagoStyleCheesePizza(Pizza):
    def __init__(self):
        super().__init__()
        self.name = "Chicago Style Deep Dish Cheese Pizza"
        self.dough = "Extra Thick Crust Dough"
        self.sauce = "Plum Tomato Sauce"
        self.toppings.append("Shredded Mozzarella Cheese")
    
    def cut(self):
        print("Cutting the pizza into square slices")

# Concrete Creators
class NYPizzaStore(PizzaStore):
    # Concrete factory method
    def createPizza(self, item):
        if item == "cheese":
            return NYStyleCheesePizza()
        else:
            return None
    
class ChicagoPizzaStore(PizzaStore):
    # Concrete factory method
    def createPizza(self, item):
        if item == "cheese":
            return ChicagoStyleCheesePizza()
        else:
            return None

if __name__ == "__main__":
    nyStore = NYPizzaStore()
    chicagoStore = ChicagoPizzaStore()
    
    pizza = nyStore.orderPizza("cheese")
    print(f"Ethan ordered a {pizza.name}\n")
    
    pizza = chicagoStore.orderPizza("cheese")
    print(f"Joel ordered a {pizza.name}\n")
