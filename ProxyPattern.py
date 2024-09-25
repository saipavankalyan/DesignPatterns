# This is a simple implementation of the Proxy Pattern
# The Proxy Pattern provides a surrogate or placeholder for another object to control access to it.
# The Proxy Pattern is used when we want to provide controlled access to a particular object - this object might be remote, expensive to create, or in need of securing.
# Other proxy types include: Remote Proxy, Virtual Proxy, Protection Proxy, caching Proxy, and Synchronization Proxy, etc.

# This is an example of logging and checking access to a RealSubject object using a Proxy object

from abc import ABC, abstractmethod

class Subject(ABC):
    @abstractmethod
    def request(self):
        pass

class RealSubject(Subject):
    def request(self):
        print("RealSubject: Handling request")

class Proxy(Subject):
    def __init__(self):
        self.realSubject = RealSubject()

    def request(self):
        if self.checkAccess():
            self.realSubject.request()
            self.logAccess()

    def checkAccess(self):
        print("Proxy: Checking access prior to firing a real request.")
        return True

    def logAccess(self):
        print("Proxy: Logging the time of request.")

if __name__ == "__main__":
    proxy = Proxy()
    proxy.request()