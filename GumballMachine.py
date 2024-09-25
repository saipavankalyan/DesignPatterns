# This is a simple implementation of the State Pattern
# The State Pattern allows an object to alter its behavior when its internal state changes. The object will appear to change its class.

from abc import ABC, abstractmethod
from random import randint

class State(ABC):
    @abstractmethod
    def insertQuarter(self):
        pass
    
    @abstractmethod
    def ejectQuarter(self):
        pass
    
    @abstractmethod
    def turnCrank(self):
        pass
    
    @abstractmethod
    def dispense(self):
        pass

    @abstractmethod
    def refill(self, numberGumballs):
        pass

class NoQuarterState(State):
    def __init__(self, gumballMachine):
        self.gumballMachine = gumballMachine
    
    def insertQuarter(self):
        print("You inserted a quarter")
        self.gumballMachine.setState(self.gumballMachine.getHasQuarterState())
    
    def ejectQuarter(self):
        print("You haven't inserted a quarter")
    
    def turnCrank(self):
        print("You turned, but there's no quarter")
    
    def dispense(self):
        print("You need to pay first")
    
    def refill(self, numberGumballs):
        print("Machine is not empty")

class HasQuarterState(State):
    def __init__(self, gumballMachine):
        self.gumballMachine = gumballMachine    
    
    def insertQuarter(self):
        print("You can't insert another quarter")
    
    def ejectQuarter(self):
        print("Quarter returned")
        self.gumballMachine.setState(self.gumballMachine.getNoQuarterState())
    
    def turnCrank(self):
        print("You turned...")
        winner = randint(0, 9)
        if winner == 0 and self.gumballMachine.getCount() > 1:
            self.gumballMachine.setState(self.gumballMachine.getWinnerState())
        else:
            self.gumballMachine.setState(self.gumballMachine.getSoldState())
    
    def dispense(self):
        print("No gumball dispensed")
    
    def refill(self, numberGumballs):
        print("Machine is not empty")

class SoldState(State):
    def __init__(self, gumballMachine):
        self.gumballMachine = gumballMachine
    
    def insertQuarter(self):
        print("Please wait, we're already giving you a gumball")
    
    def ejectQuarter(self):
        print("Sorry, you already turned the crank")
    
    def turnCrank(self):
        print("Turning twice doesn't get you another gumball!")
    
    def dispense(self):
        self.gumballMachine.releaseBall()
        if self.gumballMachine.getCount() > 0:
            self.gumballMachine.setState(self.gumballMachine.getNoQuarterState())
        else:
            print("Oops, out of gumballs!")
            self.gumballMachine.setState(self.gumballMachine.getSoldOutState())
    
    def refill(self, numberGumballs):
        print("Machine is not empty")

class WinnerState(State):
    def __init__(self, gumballMachine):
        self.gumballMachine = gumballMachine
    
    def insertQuarter(self):
        print("Please wait, we're already giving you a gumball")
    
    def ejectQuarter(self):
        print("Sorry, you already turned the crank")
    
    def turnCrank(self):
        print("Turning twice doesn't get you another gumball!")
    
    def dispense(self):
        print("YOU'RE A WINNER! You get two gumballs for your quarter")
        self.gumballMachine.releaseBall()
        if self.gumballMachine.getCount() == 0:
            self.gumballMachine.setState(self.gumballMachine.getSoldOutState())
        else:
            self.gumballMachine.releaseBall()
            if self.gumballMachine.getCount() > 0:
                self.gumballMachine.setState(self.gumballMachine.getNoQuarterState())
            else:
                print("Oops, out of gumballs!")
                self.gumballMachine.setState(self.gumballMachine.getSoldOutState())
    
    def refill(self, numberGumballs):
        print("Machine is not empty")


class SoldOutState(State):
    def __init__(self, gumballMachine):
        self.gumballMachine = gumballMachine
    
    def insertQuarter(self):
        print("Sorry, the machine is sold out")
    
    def ejectQuarter(self):
        print("Sorry, the machine is sold out")
    
    def turnCrank(self):
        print("Sorry, the machine is sold out")
    
    def dispense(self):
        print("Sorry, the machine is sold out")
    
    def refill(self, numberGumballs):
        print("Machine is being refilled with", numberGumballs, "gumballs")
        self.gumballMachine.count = numberGumballs
        self.gumballMachine.setState(self.gumballMachine.getNoQuarterState())

# Context
class GumballMachine:
    def __init__(self, numberGumballs):
        self.soldOutState = SoldOutState(self)
        self.noQuarterState = NoQuarterState(self)
        self.hasQuarterState = HasQuarterState(self)
        self.soldState = SoldState(self)
        self.winnerState = WinnerState(self)
        
        self.count = numberGumballs
        if self.count > 0:
            self.state = self.noQuarterState
        else:
            self.state = self.soldOutState
    
    def insertQuarter(self):
        self.state.insertQuarter()
    
    def ejectQuarter(self):
        self.state.ejectQuarter()
    
    def turnCrank(self):
        self.state.turnCrank()
        self.state.dispense()
    
    def refill(self, numberGumballs):
        self.state.refill(numberGumballs)
    
    def setState(self, state):
        self.state = state
    
    def releaseBall(self):
        print("A gumball comes rolling out the slot...")
        if self.count != 0:
            self.count -= 1
    
    def __str__(self):
        return "Gumball Machine: " + str(self.count) + " gumballs"
    
    def getCount(self):
        return self.count
    
    def getSoldOutState(self):
        return self.soldOutState
    
    def getNoQuarterState(self):
        return self.noQuarterState
    
    def getHasQuarterState(self):
        return self.hasQuarterState
    
    def getSoldState(self):
        return self.soldState

    def getWinnerState(self):
        return self.winnerState

if __name__ == "__main__":
    gumballMachine = GumballMachine(5)
    gumballMachine.insertQuarter()
    gumballMachine.turnCrank()
    gumballMachine.insertQuarter()
    gumballMachine.ejectQuarter()
    gumballMachine.turnCrank()
    gumballMachine.insertQuarter()
    gumballMachine.turnCrank()
    gumballMachine.insertQuarter()
    gumballMachine.turnCrank()
    gumballMachine.insertQuarter()
    gumballMachine.turnCrank()
    print(gumballMachine)
    gumballMachine.insertQuarter()
    gumballMachine.turnCrank()
    gumballMachine.refill(5)
    print(gumballMachine)
    gumballMachine.insertQuarter()
    gumballMachine.turnCrank()
