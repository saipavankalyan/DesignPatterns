# This is a simple implementation of the Abstract Factory Pattern
# The Abstract Factory Pattern provides an interface for creating families of related or dependent objects without specifying their concrete classes.

from abc import ABC, abstractmethod

# Abstract Factory
class PizzaIngredientFactory(ABC):
    @abstractmethod
    def createDough(self):
        pass
    
    @abstractmethod
    def createSauce(self):
        pass
    
    @abstractmethod
    def createCheese(self):
        pass
    
    @abstractmethod
    def createVeggies(self):
        pass
    
    @abstractmethod
    def createPepperoni(self):
        pass
    
    @abstractmethod
    def createClam(self):
        pass

# Concrete Factories
class NYPizzaIngredientFactory(PizzaIngredientFactory):
    def createDough(self):
        return ThinCrustDough()
    
    def createSauce(self):
        return MarinaraSauce()
    
    def createCheese(self):
        return ReggianoCheese()
    
    def createVeggies(self):
        veggies = [Garlic(), Onion(), Mushroom(), RedPepper()]
        return veggies
    
    def createPepperoni(self):
        return SlicedPepperoni()
    
    def createClam(self):
        return FreshClams()

class ChicagoPizzaIngredientFactory(PizzaIngredientFactory):
    def createDough(self):
        return ThickCrustDough()
    
    def createSauce(self):
        return PlumTomatoSauce()
    
    def createCheese(self):
        return MozzarellaCheese()
    
    def createVeggies(self):
        veggies = [BlackOlives(), Spinach(), Eggplant()]
        return veggies
    
    def createPepperoni(self):
        return SlicedPepperoni()
    
    def createClam(self):
        return FrozenClams()

# Abstract sub Products
class Dough(ABC):
    @abstractmethod
    def __str__(self):
        pass

class Sauce(ABC):
    @abstractmethod
    def __str__(self):
        pass

class Cheese(ABC):
    @abstractmethod
    def __str__(self):
        pass

class Veggies(ABC):
    @abstractmethod
    def __str__(self):
        pass

class Pepperoni(ABC):
    @abstractmethod
    def __str__(self):
        pass

class Clams(ABC):
    @abstractmethod
    def __str__(self):
        pass

# Concrete Products
class ThinCrustDough(Dough):
    def __str__(self):
        return "Thin Crust Dough"

class ThickCrustDough(Dough):
    def __str__(self):
        return "Thick Crust Dough"

class MarinaraSauce(Sauce):
    def __str__(self):
        return "Marinara Sauce"

class PlumTomatoSauce(Sauce):
    def __str__(self):
        return "Plum Tomato Sauce"

class ReggianoCheese(Cheese):
    def __str__(self):
        return "Reggiano Cheese"

class MozzarellaCheese(Cheese):
    def __str__(self):
        return "Mozzarella Cheese"

class Garlic(Veggies):
    def __str__(self):
        return "Garlic"

class Onion(Veggies):
    def __str__(self):
        return "Onion"

class Mushroom(Veggies):
    def __str__(self):
        return "Mushroom"

class RedPepper(Veggies):
    def __str__(self):
        return "Red Pepper"

class BlackOlives(Veggies):
    def __str__(self):
        return "Black Olives"

class Spinach(Veggies):
    def __str__(self):
        return "Spinach"

class Eggplant(Veggies):
    def __str__(self):
        return "Eggplant"

class SlicedPepperoni(Pepperoni):
    def __str__(self):
        return "Sliced Pepperoni"

class FrozenClams(Clams):
    def __str__(self):
        return "Frozen Clams"

class FreshClams(Clams):
    def __str__(self):
        return "Fresh Clams"

# Abstract Product
class Pizza(ABC):
    def __init__(self):
        self.name = ""
        self.dough = ""
        self.sauce = ""
        self.cheese = ""
        self.veggies = []
        self.pepperoni = ""
        self.clam = ""
    
    @abstractmethod
    def prepare(self):
        pass
    
    def bake(self):
        print("Bake for 25 minutes at 350")
    
    def cut(self):
        print("Cutting the pizza into diagonal slices")
    
    def box(self):
        print("Place pizza in official PizzaStore box")

# Concrete Products
class CheesePizza(Pizza):
    def __init__(self, ingredientFactory):
        self.name = "Cheese Pizza"
        self.ingredientFactory = ingredientFactory
    
    def prepare(self):
        print(f"Preparing {self.name}")
        self.dough = self.ingredientFactory.createDough()
        self.sauce = self.ingredientFactory.createSauce()
        self.cheese = self.ingredientFactory.createCheese()
        print(f"Adding {self.dough}")
        print(f"Adding {self.sauce}")
        print(f"Adding {self.cheese}")

class ClamPizza(Pizza):
    def __init__(self, ingredientFactory):
        self.name = "Clam Pizza"
        self.ingredientFactory = ingredientFactory
    
    def prepare(self):
        print(f"Preparing {self.name}")
        self.dough = self.ingredientFactory.createDough()
        self.sauce = self.ingredientFactory.createSauce()
        self.cheese = self.ingredientFactory.createCheese()
        self.clam = self.ingredientFactory.createClam()
        print(f"Adding {self.dough}")
        print(f"Adding {self.sauce}")
        print(f"Adding {self.cheese}")
        print(f"Adding {self.clam}")

class PizzaStore(ABC):
    def orderPizza(self, type):
        pizza = self.createPizza(type)
        
        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()
        
        return pizza
    
    @abstractmethod
    def createPizza(self, type):
        pass

class NYPizzaStore(PizzaStore):
    def createPizza(self, item):
        ingredientFactory = NYPizzaIngredientFactory()
        
        if item == "cheese":
            return CheesePizza(ingredientFactory)
        elif item == "clam":
            return ClamPizza(ingredientFactory)
        else:
            return None

class ChicagoPizzaStore(PizzaStore):
    def createPizza(self, item):
        ingredientFactory = ChicagoPizzaIngredientFactory()
        
        if item == "cheese":
            return CheesePizza(ingredientFactory)
        elif item == "clam":
            return ClamPizza(ingredientFactory)
        else:
            return None

if __name__ == "__main__":
    nyStore = NYPizzaStore()
    chicagoStore = ChicagoPizzaStore()
    
    pizza = nyStore.orderPizza("cheese")
    print(f"Ethan ordered a {pizza.name}\n")
    
    # pizza = chicagoStore.orderPizza("cheese")
    # print(f"Joel ordered a {pizza.name}\n")
    
    # pizza = nyStore.orderPizza("clam")
    # print(f"Ethan ordered a {pizza.name}\n")
    
    pizza = chicagoStore.orderPizza("clam")
    print(f"Joel ordered a {pizza.name}\n")
