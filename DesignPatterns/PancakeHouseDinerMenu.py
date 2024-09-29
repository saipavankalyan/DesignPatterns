# This is a simple implementation of the Iterator Pattern
# The Iterator Pattern provides a way to access the elements of an aggregate object sequentially without exposing its underlying representation.

from abc import ABC, abstractmethod

class Iterator(ABC):
    @abstractmethod
    def hasNext(self):
        pass
    
    @abstractmethod
    def next(self):
        pass

class MenuItem():
    def __init__(self, name, description, vegetarian, price):
        self.name = name
        self.description = description
        self.vegetarian = vegetarian
        self.price = price

    def getName(self):
        return self.name
    
    def getDescription(self):
        return self.description
    
    def getPrice(self):
        return self.price
    
    def isVegetarian(self):
        return self.vegetarian

class DinerMenuIterator(Iterator):
    def __init__(self, items):
        # array of menu items
        self.items = items
        self.position = 0
    
    def next(self):
        menuItem = self.items[self.position]
        self.position += 1
        return menuItem
    
    def hasNext(self):
        if self.position >= len(self.items) or self.items[self.position] == None:
            return False
        else:
            return True

class PancakeHouseMenuIterator(Iterator):
    # uses dictionary to store menu items with key as name
    def __init__(self, items):
        self.items = items
        self.keys = list(items.keys())
        self.position = 0
    
    def next(self):
        menuItem = self.items[self.keys[self.position]]
        self.position += 1
        return menuItem

    def hasNext(self):
        if self.position >= len(self.keys):
            return False
        else:
            return True

class DinerMenu():
    def __init__(self):
        self.menuItems = []
        self.addItem("Vegetarian BLT", "(Fakin') Bacon with lettuce & tomato on whole wheat", True, 2.99)
        self.addItem("BLT", "Bacon with lettuce & tomato on whole wheat", False, 2.99)
        self.addItem("Soup of the day", "Soup of the day, with a side of potato salad", False, 3.29)
        self.addItem("Hotdog", "A hot dog, with saurkraut, relish, onions, topped with cheese", False, 3.05)
    
    def addItem(self, name, description, vegetarian, price):
        menuItem = MenuItem(name, description, vegetarian, price)
        self.menuItems.append(menuItem)
    
    def createIterator(self):
        return DinerMenuIterator(self.menuItems)

class PancakeHouseMenu():
    def __init__(self):
        self.menuItems = {}
        self.addItem("K&B's Pancake Breakfast", "Pancakes with scrambled eggs, and toast", True, 2.99)
        self.addItem("Regular Pancake Breakfast", "Pancakes with fried eggs, sausage", False, 2.99)
        self.addItem("Blueberry Pancakes", "Pancakes made with fresh blueberries", True, 3.49)
        self.addItem("Waffles", "Waffles, with your choice of blueberries or strawberries", True, 3.59)
    
    def addItem(self, name, description, vegetarian, price):
        menuItem = MenuItem(name, description, vegetarian, price)
        self.menuItems[name] = menuItem
    
    def createIterator(self):
        return PancakeHouseMenuIterator(self.menuItems)

class Waitress():
    def __init__(self, pancakeHouseMenu, dinerMenu):
        self.pancakeHouseMenu = pancakeHouseMenu
        self.dinerMenu = dinerMenu
    
    def printMenu(self):
        pancakeIterator = self.pancakeHouseMenu.createIterator()
        dinerIterator = self.dinerMenu.createIterator()
        print("MENU\n----\nBREAKFAST")
        self.printMenuItems(pancakeIterator)
        print("\nLUNCH")
        self.printMenuItems(dinerIterator)
    
    def printMenuItems(self, iterator):
        while iterator.hasNext():
            menuItem = iterator.next()
            print(f"{menuItem.getName()}, {menuItem.getPrice()} -- {menuItem.getDescription()}")
    
if __name__ == "__main__":
    pancakeHouseMenu = PancakeHouseMenu()
    dinerMenu = DinerMenu()
    waitress = Waitress(pancakeHouseMenu, dinerMenu)
    waitress.printMenu()
    