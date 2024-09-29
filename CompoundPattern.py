# This is a simple implementation of the Compound Pattern
# The Compound Pattern is a combination of two or more patterns to solve a recurring or general problem

# This is not a compound pattern but just a set of patterns working together
from abc import ABC, abstractmethod

# This is an observer pattern
class QuackObservable(ABC):
    @abstractmethod
    def registerObserver(self, observer):
        pass

    @abstractmethod
    def notifyObservers(self):
        pass

class Quackable(QuackObservable):
    @abstractmethod
    def quack(self):
        pass

class Observable(QuackObservable):
    def __init__(self, duck):
        self.observers = []
        self.duck = duck

    def registerObserver(self, observer):
        self.observers.append(observer)

    def notifyObservers(self):
        for observer in self.observers:
            observer.update(self.duck)

class Observer(ABC):
    @abstractmethod
    def update(self, duck):
        pass

class Quackologist(Observer):
    def update(self, duck):
        print("Quackologist: " + duck.__class__.__name__ + " just quacked")

class MallardDuck(Quackable):
    def __init__(self):
        self.observable = Observable(self)

    def quack(self):
        print("Quack")
        self.notifyObservers()

    def registerObserver(self, observer):
        self.observable.registerObserver(observer)
    
    def notifyObservers(self):
        self.observable.notifyObservers()

class RedheadDuck(Quackable):
    def __init__(self):
        self.observable = Observable(self)

    def quack(self):
        print("Quack")
        self.notifyObservers()
    
    def registerObserver(self, observer):
        self.observable.registerObserver(observer)
    
    def notifyObservers(self):
        self.observable.notifyObservers()

class DuckCall(Quackable):
    def __init__(self):
        self.observable = Observable(self)

    def quack(self):
        print("Kwak")
        self.notifyObservers()
    
    def registerObserver(self, observer):
        self.observable.registerObserver(observer)
    
    def notifyObservers(self):
        self.observable.notifyObservers()

class RubberDuck(Quackable):
    def __init__(self):
        self.observable = Observable(self)

    def quack(self):
        print("Squeak")
        self.notifyObservers()
    
    def registerObserver(self, observer):
        self.observable.registerObserver(observer)
    
    def notifyObservers(self):
        self.observable.notifyObservers()

class Goose:
    def honk(self):
        print("Honk")

# This is an adapter pattern
class GooseAdapter(Quackable):
    def __init__(self, goose):
        self.goose = goose
        self.observable = Observable(self)

    def quack(self):
        self.goose.honk()
        self.notifyObservers()
    
    def registerObserver(self, observer):
        self.observable.registerObserver(observer)
    
    def notifyObservers(self):
        self.observable.notifyObservers()

# This is a decorator pattern
class QuackCounter(Quackable):
    numberOfQuacks = 0

    def __init__(self, duck):
        self.duck = duck

    def quack(self):
        self.duck.quack()
        QuackCounter.numberOfQuacks += 1

    @staticmethod
    def getQuacks():
        return QuackCounter.numberOfQuacks
    
    def registerObserver(self, observer):
        self.duck.registerObserver(observer)
    
    def notifyObservers(self):
        self.duck.notifyObservers()

# This is a abstract factory pattern
class AbstractDuckFactory(ABC):
    @abstractmethod
    def createMallardDuck(self):
        pass

    @abstractmethod
    def createRedheadDuck(self):
        pass

    @abstractmethod
    def createDuckCall(self):
        pass

    @abstractmethod
    def createRubberDuck(self):
        pass

class CountingDuckFactory(AbstractDuckFactory):
    def createMallardDuck(self):
        return QuackCounter(MallardDuck())

    def createRedheadDuck(self):
        return QuackCounter(RedheadDuck())

    def createDuckCall(self):
        return QuackCounter(DuckCall())

    def createRubberDuck(self):
        return QuackCounter(RubberDuck())

# This is a composite pattern
class Flock(Quackable):
    def __init__(self):
        self.quackers = []
        self.observable = Observable(self)

    def add(self, quacker):
        self.quackers.append(quacker)

    def quack(self):
        # This is an iterator pattern
        for quacker in self.quackers:
            quacker.quack()
            self.notifyObservers()
    
    def registerObserver(self, observer):
        self.observable.registerObserver(observer)
    
    def notifyObservers(self):
        self.observable.notifyObservers()

class DuckSimulator:
    def run_simulation(self, duckFactory):
        mallardDuck = duckFactory.createMallardDuck()
        redheadDuck = duckFactory.createRedheadDuck()
        duckCall = duckFactory.createDuckCall()
        rubberDuck = duckFactory.createRubberDuck()
        gooseDuck = GooseAdapter(Goose())

        flockOfDucks = Flock()
        
        flockOfDucks.add(redheadDuck)
        flockOfDucks.add(duckCall)
        flockOfDucks.add(rubberDuck)
        flockOfDucks.add(gooseDuck)

        flockOfMallards = Flock()
        for i in range(3):
            flockOfMallards.add(duckFactory.createMallardDuck())

        flockOfDucks.add(flockOfMallards)

        quackologist = Quackologist()
        flockOfDucks.registerObserver(quackologist)

        print("\nDuck Simulator")
        self.simulate(flockOfDucks)


        print("The ducks quacked " + str(QuackCounter.getQuacks()) + " times")

    def simulate(self, duck):
        duck.quack()

if __name__ == "__main__":
    duckSimulator = DuckSimulator()
    duckFactory = CountingDuckFactory()
    duckSimulator.run_simulation(duckFactory)

'''
What did we do?
    We started with a bunch of Quackables...
    
    A goose came along and wanted to act like a Quackable too. So we
    used the Adapter Pattern to adapt the goose to a Quackable. Now, you can call quack() on
    a goose wrapped in the adapter and it will honk!

    Then, the Quackologists decided they wanted to count quacks. So we
    used the Decorator Pattern to add a QuackCounter decorator that keeps track of the number
    of times quack() is called, and then delegates the quack to the Quackable it’s wrapping.

    But the Quackologists were worried they’d forget to add the
    QuackCounter decorator. So we used the Abstract Factory Pattern to create ducks
    for them. Now, whenever they want a duck, they ask the factory for one, and it hands back
    a decorated duck. (And don’t forget, they can also use another duck factory if they want an
    un-decorated duck!)

    We had management problems keeping track of all those ducks and
    geese and quackables. So we used the Composite Pattern to group quackables
    into Flocks. The pattern also allows the quackologist to create sub-Flocks to manage duck
    families. We used the Iterator Pattern in our implementation by using java.util’s iterator in
    ArrayList.

    The Quackologists also wanted to be notified when any quackable
    quacked. So we used the Observer Pattern to let the Quackologists register as Quackable
    Observers. Now they’re notified every time any Quackable quacks. We used iterator again
    in this implementation. The Quackologists can even use the Observer Pattern with their
    composites.
'''