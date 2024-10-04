from abc import ABC, abstractmethod
from enum import Enum

class VehicleType(Enum):
    TWO_WHEELER = 1
    FOUR_WHEELER = 2

class ParkingSpot():
    def __init__(self, spotId, x, y, type, vehicle=None):
        self.spotId = spotId
        self.x = x
        self.y = y
        self.vehicle = vehicle
        self.type = type
    
    def isAvailable(self):
        return self.vehicle == None

    def park(self, vehicle):
        self.vehicle = vehicle
    
    def leave(self):
        self.vehicle = None

class TwoWheelerSpot(ParkingSpot):
    def __init__(self, spotId, x, y, vehicle=None):
        super().__init__(spotId, x, y, VehicleType.TWO_WHEELER, vehicle)
        self.price = 10
    
    def park(self, vehicle):
        if vehicle.type == VehicleType.TWO_WHEELER:
            super().park(vehicle)
        else:
            print("Two wheeler spot is only for two wheelers")
    
    def leave(self):
        super().leave()

class FourWheelerSpot(ParkingSpot):
    def __init__(self, spotId, x, y, vehicle=None):
        super().__init__(spotId, x, y, VehicleType.FOUR_WHEELER, vehicle)
        self.price = 20
    
    def park(self, vehicle):
        if vehicle.type == VehicleType.FOUR_WHEELER:
            super().park(vehicle)
        else:
            print("Four wheeler spot is only for four wheelers")
    
    def leave(self):
        super().leave()

class ParkingSpotManager(ABC):
    def __init__(self):
        self.spots = []
        self.parkingStrategy = DefaultParkingStrategy()
    
    def addSpot(self, spot):
        self.spots.append(spot)
    
    def removeSpot(self, spot):
        self.spots.remove(spot)
    
    def addSpots(self, spots):
        self.spots.extend(spots)
    
    def removeSpots(self, spots):
        for spot in spots:
            self.spots.remove(spot)
    
    def getAvailableSpots(self):
        return [spot for spot in self.spots if spot.isAvailable()]

    def findAvailableSpot(self, vehicle):
        return self.parkingStrategy.findAvailableSpot(vehicle)

    def parkVehicle(self, vehicle):
        spot = self.findAvailableSpot()
        if spot:
            spot.park(vehicle)
            return spot
        return None

    def leaveSpot(self, spot):
        spot.leave()
    
class TwoWheelerSpotManager(ParkingSpotManager):
    def addSpots(self, spots):
        return super().addSpots(spots)
    
    def parkVehicle(self, vehicle):
        if vehicle.__class__.__name__ == "TwoWheeler":
            return super().parkVehicle(vehicle)
        else:
            print("Two wheeler spot is only for two wheelers")
    
    def leaveSpot(self, spot):
        super().leaveSpot(spot)

class FourWheelerSpotManager(ParkingSpotManager):
    def addSpots(self, spots):
        return super().addSpots(spots)
    
    def parkVehicle(self, vehicle):
        if vehicle.__class__.__name__ == "FourWheeler":
            return super().parkVehicle(vehicle)
        else:
            print("Four wheeler spot is only for four wheelers")
    
    def leaveSpot(self, spot):
        super().leaveSpot(spot)

class ParkingStrategy(ABC):
    @abstractmethod
    def findAvailableSpot(self, vehicle):
        pass

class NearestSpotParkingStrategy(ParkingStrategy):
    def findAvailableSpot(self, vehicle):
        pass

class DefaultParkingStrategy(ParkingStrategy):
    def findAvailableSpot(self, vehicle):
        for spot in self.spots:
            if spot.isAvailable():
                return spot


class Vehicle(ABC):
    def __init__(self, vehicleId, type):
        self.vehicleId = vehicleId
        self.type = type 

class TwoWheeler(Vehicle):
    def __init__(self, vehicleId):
        super().__init__(vehicleId, VehicleType.TWO_WHEELER)

class FourWheeler(Vehicle):
    def __init__(self, vehicleId):
        super().__init__(vehicleId, VehicleType.FOUR_WHEELER)
    
class Ticket():
    def __init__(self, ticketId, vehicle, spot, entryTime):
        self.ticketId = ticketId
        self.vehicle = vehicle
        self.spot = spot
        self.entryTime = entryTime

class ParkingSpotManagerFactory():
    @staticmethod
    def getSpotManager(type):
        if type == VehicleType.TWO_WHEELER:
            return TwoWheelerSpotManager()
        elif type == VehicleType.FOUR_WHEELER:
            return FourWheelerSpotManager()
        else:
            return None

class EntranceGate():
    def __init__(self, x, y):
        self.x = x
        self.y = y    

    def findAvailableSpot(self, vehicle):
        ParkingSpotManager = ParkingSpotManagerFactory.getSpotManager(vehicle.type)
        return ParkingSpotManager.findAvailableSpot(vehicle)
    
    def bookSpot(self, vehicle):
            spot = self.findAvailableSpot(vehicle)
            if spot:
                spot.park(vehicle)
                return spot
            else:
                print("No spots available")
                return None
