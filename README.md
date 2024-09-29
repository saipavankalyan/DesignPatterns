## Design Principles

1. Identify the aspects of your application that vary and separate them from what stays the same
2. Program to an interface, not an implementation
3. Favor compositon over inheritance
   - Creating systems using composition gives you a lot more flexibility. You can change the behavior of objects at runtime by composing them in different ways.
4. Strive for loosely coupled designs between objects that interact
5. Classes should be open for extension but closed for modification
   - Designs that are resilient to change and flexible enough to take on new functionality to meet changing requirements
6. Depend on abstractions. Do not depend on concrete classes
   - High level modules should not depend on low level modules. Both should depend on abstractions.
   - No variable should hold a reference to a concrete class
   - No class should derive from a concrete class
   - No method should override an implemented method of any of its base classes
7. Principle of least knowledge - talk only to your immediate friends
8. Don't call us, we'll call you - Hollywood Principle
9. A class should have only one reason to change

## SOLID Principles

- Single Responsibility Principle - A class should have only one reason to change
- Open/Closed Principle - Classes should be open for extension but closed for modification
- Liskov Substitution Principle - Derived classes must be substitutable for their base classes
- Interface Segregation Principle - A client should never be forced to implement an interface that it doesn't use
- Dependency Inversion Principle - High level modules should not depend on low level modules. Both should depend on abstractions.

## Design Patterns

- Creational
  - [Singleton](./DesignPatterns/ChoclateBoiler.py)
  - [Factory Method](./DesignPatterns/PizzaStore.py)
  - [Abstract Factory](./DesignPatterns/PizzaStoreV2.py)
- Structural
  - [Adapter](./DesignPatterns/DuckTurkey.py)
  - [Composite](./DesignPatterns/PancakeHouseDinerMenuV2.py)
  - [Decorator](./DesignPatterns/StarbuzzCoffee.py)
  - [Facade](./DesignPatterns/HomeTheatre.py)
- Behavioral
  - [Template Method](./DesignPatterns/Beverages.py)
  - [Strategy](./DesignPatterns/Duck.py)
  - [Observer](./DesignPatterns/WeatherStation.py)
  - [Command](./DesignPatterns/HomeAutomation.py)
  - [State](./DesignPatterns/GumballMachine.py)
  - [Iterator](./DesignPatterns/PancakeHouseDinerMenu.py)
  - [Proxy](./DesignPatterns/ProxyPattern.py)
