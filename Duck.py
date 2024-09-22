# This is a simple implementation of the Strategy Pattern
# The Strategy Pattern defines a family of algorithms, encapsulates each one, and makes them interchangeable. Strategy lets the algorithm vary independently from clients that use it.


from abc import ABC, abstractmethod

class Duck(ABC):
    def __init__(self, flyBehavior, quackBehavior):
        self.FlyBehavior = flyBehavior
        self.QuackBehavior = quackBehavior
    
    @abstractmethod
    def display(self):
        pass
    
    def performFly(self):
        self.FlyBehavior.fly()
    
    def performQuack(self):
        self.QuackBehavior.quack()
    
    def swim(self):
        print("All ducks float, even decoys!")
    
    def setFlyBehavior(self, fb):
        self.FlyBehavior = fb
    
    def setQuackBehavior(self, qb):
        self.QuackBehavior = qb

class FlyBehavior(ABC):
    @abstractmethod
    def fly(self):
        pass

class QuackBehavior(ABC):
    @abstractmethod
    def quack(self):
        pass

class FlyWithWings(FlyBehavior):
    def fly(self):
        print("I'm flying!")

class FlyNoWay(FlyBehavior):
    def fly(self):
        print("I can't fly")

class FlyRocketPowered(FlyBehavior):
    def fly(self):
        print("I'm flying with a rocket!")

class Quack(QuackBehavior):
    def quack(self):
        print("Quack")

class Squeak(QuackBehavior):
    def quack(self):
        print("Squeak")

class MuteQuack(QuackBehavior):
    def quack(self):
        print("<< Silence >>")

class MallardDuck(Duck):
    def __init__(self):
        super().__init__(FlyWithWings(), Quack())
    
    def display(self):
        print("I'm a real Mallard duck")

class ModelDuck(Duck):
    def __init__(self):
        super().__init__(FlyNoWay(), Quack())
    
    def display(self):
        print("I'm a model duck")

if __name__ == "__main__":
    mallard = MallardDuck()
    mallard.display()
    mallard.performFly()
    mallard.performQuack()
    mallard.swim()
    
    model = ModelDuck()
    model.display()
    model.performFly()
    model.setFlyBehavior(FlyRocketPowered())
    model.performFly()
    model.performQuack()
    model.setQuackBehavior(Squeak())
    model.performQuack()
    model.swim()