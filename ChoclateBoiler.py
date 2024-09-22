# This is a simple implementation of the Singleton Pattern
# The Singleton Pattern ensures a class has only one instance and provides a global point of access to it.

import threading

class ChocolateBoiler:
    __uniqueInstance = None
    __lock = threading.Lock()  # Lock object to ensure thread safety
    __empty = True
    __boiled = False
    
    # def __new__(cls):
    #     if cls.__uniqueInstance is None:
    #         cls.__uniqueInstance = super(ChocolateBoiler, cls).__new__(cls)
    #     return cls.__uniqueInstance

    @classmethod
    def getInstance(cls):
        if cls.__uniqueInstance is None:
            with cls.__lock:  # Ensure that only one thread can execute this block at a time
                if cls.__uniqueInstance is None:  # Double-checked locking
                    cls.__uniqueInstance = cls()
        return cls.__uniqueInstance
    
    def fill(self):
        if self.isEmpty():
            self.__empty = False
            self.__boiled = False
            print("Fill the boiler with a milk/chocolate mixture")
    
    def drain(self):
        if not self.isEmpty() and self.isBoiled():
            print("Drain the boiled milk and chocolate")
            self.__empty = True
    
    def boil(self):
        if not self.isEmpty() and not self.isBoiled():
            print("Bring the contents to a boil")
            self.__boiled = True
    
    def isEmpty(self):
        return self.__empty
    
    def isBoiled(self):
        return self.__boiled
    

# Test the ChocolateBoiler class
if __name__ == "__main__":
    boiler = ChocolateBoiler.getInstance()
    boiler.fill()
    boiler.boil()
    boiler.drain()
