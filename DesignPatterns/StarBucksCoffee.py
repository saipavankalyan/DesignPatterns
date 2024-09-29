# This is a simple implementation of the Decorator Pattern
# The Decorator Pattern attaches additional responsibilities to an object dynamically. Decorators provide a flexible alternative to subclassing for extending functionality.

from abc import ABC, abstractmethod

class Beverage(ABC):
    description = "Unknown Beverage"
    
    @abstractmethod
    def getDescription(self):
        pass
    
    @abstractmethod
    def cost(self):
        pass

class CondimentDecorator(Beverage):
    @abstractmethod
    def getDescription(self):
        pass

class Espresso(Beverage):
    def __init__(self):
        self.description = "Espresso"
    
    def getDescription(self):
        return self.description
    
    def cost(self):
        return 1.99

class HouseBlend(Beverage):
    def __init__(self):
        self.description = "House Blend Coffee"
    
    def getDescription(self):
        return self.description
    
    def cost(self):
        return .89

class DarkRoast(Beverage):
    def __init__(self):
        self.description = "Dark Roast Coffee"
    
    def getDescription(self):
        return self.description
    
    def cost(self):
        return .99

class Decaf(Beverage):
    def __init__(self):
        self.description = "Decaf Coffee"
    
    def getDescription(self):
        return self.description
    
    def cost(self):
        return 1.05

class Mocha(CondimentDecorator):
    def __init__(self, beverage):
        self.beverage = beverage
    
    def getDescription(self):
        return self.beverage.getDescription() + ", Mocha"
    
    def cost(self):
        return .20 + self.beverage.cost()

class Whip(CondimentDecorator):
    def __init__(self, beverage):
        self.beverage = beverage
    
    def getDescription(self):
        return self.beverage.getDescription() + ", Whip"
    
    def cost(self):
        return .10 + self.beverage.cost()

class Soy(CondimentDecorator):
    def __init__(self, beverage):
        self.beverage = beverage
    
    def getDescription(self):
        return self.beverage.getDescription() + ", Soy"
    
    def cost(self):
        return .15 + self.beverage.cost()

class SteamedMilk(CondimentDecorator):
    def __init__(self, beverage):
        self.beverage = beverage
    
    def getDescription(self):
        return self.beverage.getDescription() + ", Steamed Milk"
    
    def cost(self):
        return .10 + self.beverage.cost()

if __name__ == "__main__":
    beverage = Espresso()
    print(f"{beverage.getDescription()} ${beverage.cost()}")
    
    beverage2 = DarkRoast()
    beverage2 = Mocha(beverage2)
    beverage2 = Mocha(beverage2)
    beverage2 = Whip(beverage2)
    print(f"{beverage2.getDescription()} ${beverage2.cost()}")
    
    beverage3 = HouseBlend()
    beverage3 = Soy(beverage3)
    beverage3 = Mocha(beverage3)
    beverage3 = Whip(beverage3)
    print(f"{beverage3.getDescription()} ${beverage3.cost()}")
    
    beverage4 = Decaf()
    beverage4 = SteamedMilk(beverage4)
    beverage4 = Soy(beverage4)
    beverage4 = Mocha(beverage4)
    beverage4 = Whip(beverage4)
    print(f"{beverage4.getDescription()} ${beverage4.cost()}")
