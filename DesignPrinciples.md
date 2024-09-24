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
