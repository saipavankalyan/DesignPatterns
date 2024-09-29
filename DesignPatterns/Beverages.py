# This is a simple implementation of the Template Method Pattern
# The Template Method Pattern defines the skeleton of an algorithm in a method, deferring some steps to subclasses. Template Method lets subclasses redefine certain steps of an algorithm without changing the algorithm's structure.
# Hooks are methods that are declared in the abstract class, but only given an empty or default implementation. This gives subclasses the ability to "hook into" the algorithm at various points, if they wish; a subclass is also free to ignore the hook.
# The strategy method and template method both encapsulate algorithms, but the strategy pattern uses composition to delegate the implementation to another object, while the template method uses inheritance to implement the algorithm.
# The factory method pattern is a specialization of the template method pattern.

from abc import ABC, abstractmethod
from typing import final

class CaffeineBeverage(ABC):
    # template method
    @final
    def prepareRecipe(self):
        self.boilWater()
        self.brew()
        self.pourInCup()
        if self.customerWantsCondiments():
            self.addCondiments()
    
    def boilWater(self):
        print("Boiling water")
    
    def pourInCup(self):
        print("Pouring into cup")
    
    @abstractmethod
    def brew(self):
        pass
    
    @abstractmethod
    def addCondiments(self):
        pass
    
    # hook method - concrete method in the abstract class that does nothing or has a default behavior
    def customerWantsCondiments(self):
        return True

class Tea(CaffeineBeverage):
    def brew(self):
        print("Steeping the tea")
    
    def addCondiments(self):
        print("Adding lemon")

    def customerWantsCondiments(self):
        answer = input("Would you like lemon with your tea? (y/n)")
        if answer.lower().startswith('y'):
            return True
        else:
            return False

class Coffee(CaffeineBeverage):
    def brew(self):
        print("Dripping coffee through filter")
    
    def addCondiments(self):
        print("Adding sugar and milk")

    def customerWantsCondiments(self):
        answer = input("Would you like sugar and milk with your coffee? (y/n)")
        if answer.lower().startswith('y'):
            return True
        else:
            return False

if __name__ == "__main__":
    tea = Tea()
    coffee = Coffee()
    
    print("\nMaking tea...")
    tea.prepareRecipe()
    
    print("\nMaking coffee...")
    coffee.prepareRecipe()