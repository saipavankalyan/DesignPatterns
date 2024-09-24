# This is a simple implmentation of the Adapter Pattern
# The Adapter Pattern converts the interface of a class into another interface the clients expect. Adapter lets classes work together that couldn't otherwise because of incompatible interfaces.
# We use object adapter pattern here, where the adapter contains an instance of the class it adapts. The adapter implements the target interface and delegates the requests to the adaptee object.
# There is also a class adapter pattern where the adapter inherits from the adaptee class and implements the target interface but this uses multiple inheritance.

# In this example, we have a Duck class and a Turkey class. We want to make a Turkey look like a Duck so we create a TurkeyAdapter class that implements the Duck interface and uses a Turkey object to make the Turkey look like a Duck.

from abc import ABC, abstractmethod

# Target Interface
class Duck(ABC):
    @abstractmethod
    def quack(self):
        pass
    
    @abstractmethod
    def fly(self):
        pass

# Adaptee Interface
class Turkey(ABC):
    @abstractmethod
    def gobble(self):
        pass
    
    @abstractmethod
    def fly(self):
        pass

class MallardDuck(Duck):
    def quack(self):
        print("Quack")
    
    def fly(self):
        print("I'm flying")

class WildTurkey(Turkey):
    def gobble(self):
        print("Gobble gobble")
    
    def fly(self):
        print("I'm flying a short distance")

# Adapter
class TurkeyAdapter(Duck):
    def __init__(self, turkey):
        self.turkey = turkey
    
    def quack(self):
        self.turkey.gobble()
    
    def fly(self):
        for i in range(5):
            self.turkey.fly()

# Method expecting a Duck
def testDuck(duck):
    duck.quack()
    duck.fly()

if __name__ == "__main__":
    duck = MallardDuck()
    turkey = WildTurkey()
    turkeyAdapter = TurkeyAdapter(turkey)
    
    print("The Turkey says...")
    turkey.gobble()
    turkey.fly()
    
    print("\nThe Duck says...")
    testDuck(duck)
    
    print("\nThe TurkeyAdapter says...")
    testDuck(turkeyAdapter)