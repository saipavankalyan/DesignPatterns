# This is a simple implementation of the Composite Pattern
# The Composite Pattern allows you to compose objects into tree structures to represent part-whole hierarchies. Composite lets clients treat individual objects and compositions of objects uniformly.
# The Composite Pattern allows to build structures of objects in the form of trees that contain both compositions of objects and individual objects as nodes.
# Using Composite structure, we can apply the same operations over both composites and individual objects.

# The requirement is to add Desseert Items to the Diner Menu as a sub Menu

from abc import ABC, abstractmethod

class MenuComponent(ABC):
    def add(self, menuComponent):
        raise NotImplementedError()
    
    def remove(self, menuComponent):
        raise NotImplementedError()
    
    def getChild(self, i):
        raise NotImplementedError()
    
    def getName(self):
        raise NotImplementedError()
    
    def getDescription(self):
        raise NotImplementedError()
    
    def getPrice(self):
        raise NotImplementedError()
    
    def isVegetarian(self):
        raise NotImplementedError()
    
    def print(self):
        raise NotImplementedError()

class MenuItem(MenuComponent):
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
    
    def print(self):
        print(" " + self.getName(), end="")
        if self.isVegetarian():
            print("(v)", end="")
        print(", " + str(self.getPrice()))
        print("     -- " + self.getDescription())

class Menu(MenuComponent):
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.menuComponents = []
    
    def add(self, menuComponent):
        self.menuComponents.append(menuComponent)
    
    def remove(self, menuComponent):
        self.menuComponents.remove(menuComponent)
    
    def getChild(self, i):
        return self.menuComponents[i]
    
    def getName(self):
        return self.name
    
    def getDescription(self):
        return self.description
    
    def print(self):
        print("\n" + self.getName(), end="")
        print(", " + self.getDescription())
        print("---------------------")
        
        for menuComponent in self.menuComponents:
            menuComponent.print()

class Waitress():
    def __init__(self, allMenus):
        self.allMenus = allMenus
    
    def printMenu(self):
        self.allMenus.print()

if __name__ == "__main__":
    pancakeHouseMenu = Menu("PANCAKE HOUSE MENU", "Breakfast")
    dinerMenu = Menu("DINER MENU", "Lunch")
    cafeMenu = Menu("CAFE MENU", "Dinner")
    dessertMenu = Menu("DESSERT MENU", "Dessert of course!")

    allMenus = Menu("ALL MENUS", "All menus combined")
    allMenus.add(pancakeHouseMenu)
    allMenus.add(dinerMenu)
    allMenus.add(cafeMenu)

    pancakeHouseMenu.add(MenuItem("K&B's Pancake Breakfast", "Pancakes with scrambled eggs, and toast", True, 2.99))
    pancakeHouseMenu.add(MenuItem("Regular Pancake Breakfast", "Pancakes with fried eggs, sausage", False, 2.99))
    pancakeHouseMenu.add(MenuItem("Blueberry Pancakes", "Pancakes made with fresh blueberries", True, 3.49))
    pancakeHouseMenu.add(MenuItem("Waffles", "Waffles, with your choice of blueberries or strawberries", True, 3.59))

    dinerMenu.add(MenuItem("Vegetarian BLT", "(Fakin') Bacon with lettuce & tomato on whole wheat", True, 2.99))
    dinerMenu.add(MenuItem("BLT", "Bacon with lettuce & tomato on whole wheat", False, 2.99))
    dinerMenu.add(MenuItem("Soup of the day", "Soup of the day, with a side of potato salad", False, 3.29))
    dinerMenu.add(MenuItem("Hotdog", "A hot dog, with saurkraut, relish, onions, topped with cheese", False, 3.05))

    cafeMenu.add(MenuItem("Veggie Burger and Air Fries", "Veggie burger on a whole wheat bun, lettuce, tomato, and fries", True, 3.99))
    cafeMenu.add(MenuItem("Soup of the day", "A cup of the soup of the day, with a side salad", False, 3.69))

    dessertMenu.add(MenuItem("Apple Pie", "Apple pie with a flakey crust, topped with vanilla ice cream", True, 1.59))
    dessertMenu.add(MenuItem("Cheesecake", "Creamy New York cheesecake, with a chocolate graham crust", True, 1.99))
    dessertMenu.add(MenuItem("Sorbet", "A scoop of raspberry and a scoop of lime", True, 1.89))

    dinerMenu.add(dessertMenu)

    waitress = Waitress(allMenus)

    waitress.printMenu()