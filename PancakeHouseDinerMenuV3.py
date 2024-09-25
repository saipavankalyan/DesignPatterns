# This is a simple implementation of the Composite Iterator Pattern
# The Composite Iterator Pattern allows you to iterate over a collection of objects that may be either a single object or a collection of objects.


# Waitress has the ability to print all menus and print only vegetarian menu items
from abc import ABC, abstractmethod

class Iterator(ABC):
    @abstractmethod
    def hasNext(self):
        pass
    
    @abstractmethod
    def next(self):
        pass

class CompositeIterator(Iterator):
    def __init__(self, menuComponents):
        self.stack = []
        self.stack.append(iter(menuComponents))
    
    def next(self):
        if self.hasNext():
            iterator = self.stack[-1]
            menuComponent = next(iterator)
            if isinstance(menuComponent, Menu):
                self.stack.append(iter(menuComponent.menuComponents))
            return menuComponent
        else:
            return None
    
    def hasNext(self):
        while len(self.stack) > 0:
            iterator = self.stack[-1]
            try:
                next_item = next(iterator)
                self.stack[-1] = iter([next_item] + list(iterator))
                return True
            except StopIteration:
                self.stack.pop()
        return False

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
    
    @abstractmethod
    def createIterator(self):
        pass

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
    
    def createIterator(self):
        return iter([])

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
    
    def createIterator(self):
        return CompositeIterator(self.menuComponents)

class Waitress():
    def __init__(self, allMenus):
        self.allMenus = allMenus
    
    def printMenu(self):
        self.allMenus.print()
    
    def printVegetarianMenu(self):
        iterator = self.allMenus.createIterator()
        print("\nVEGETARIAN MENU\n---")
        while iterator.hasNext():
            menuComponent = iterator.next()
            try:
                if menuComponent.isVegetarian():
                    menuComponent.print()
            except NotImplementedError:
                pass

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
    pancakeHouseMenu.add(MenuItem("Waffles", "Waffles with your choice of blueberries or strawberries", True, 3.59))
    
    dinerMenu.add(MenuItem("Vegetarian BLT", "(Fakin') Bacon with lettuce & tomato on whole wheat", True, 2.99))
    dinerMenu.add(MenuItem("BLT", "Bacon with lettuce & tomato on whole wheat", False, 2.99))
    dinerMenu.add(MenuItem("Soup of the day", "Soup of the day, with a side of potato salad", False, 3.29))
    dinerMenu.add(MenuItem("Hotdog", "A hot dog, with saurkraut, relish, onions, topped with cheese", False, 3.05))
    dinerMenu.add(MenuItem("Steamed Veggies and Brown Rice", "Steamed vegetables over brown rice", True, 3.99))
    
    dinerMenu.add(dessertMenu)
    
    dessertMenu.add(MenuItem("Apple Pie", "Apple pie with a flakey crust, topped with vanilla ice cream", True, 1.59))
    dessertMenu.add(MenuItem("Cheesecake", "Creamy New York cheesecake, with a chocolate graham crust", True, 1.99))
    dessertMenu.add(MenuItem("Sorbet", "A scoop of raspberry and a scoop of lime", True, 1.89))
    
    cafeMenu.add(MenuItem("Veggie Burger and Air Fries", "Veggie burger on a whole wheat bun, lettuce, tomato, and fries", True, 3.99))
    cafeMenu.add(MenuItem("Soup of the day", "A cup of the soup of the day, with a side salad", False, 3.69))

    waitress = Waitress(allMenus)

    waitress.printMenu()
    waitress.printVegetarianMenu()
