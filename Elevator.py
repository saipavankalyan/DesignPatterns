from abc import ABC, abstractmethod
from enum import Enum
from collections import deque
# import heapq

class Direction(Enum):
    UP = 1
    DOWN = 2

class Status(Enum):
    IDLE = 1
    MOVING = 2

class Display:
    def __init__(self):
        self.floor = 0
        self.direction = None
    
    def show(self):
        return self.floor + " " + self.direction

    def set_display(self, floor, direction):
        self.floor = floor
        self.direction = direction

class Door:
    def __init__(self):
        self.is_open = False
    
    def open(self):
        self.is_open = True
    
    def close(self):
        self.is_open = False

class ElevatorCreator:
    elevator_controllers = []

    @staticmethod
    def create_elevator_controller(count):
        for i in range(count):
            elevator_car = ElevatorCar(i)
            elevator_controller = ElevatorController(elevator_car)
            ElevatorCreator.elevator_controllers.append(elevator_controller)
        
        return ElevatorCreator.elevator_controllers


class InternalButtonDispatcher:
    elevator_controller_list = ElevatorCreator.elevator_controllers

    def submit_internal_request(self, elevator_id, floor, dir):
        for controller in InternalButtonDispatcher.elevator_controller_list:
            if controller.elevator_car.id == elevator_id:
                controller.submit_new_request(floor, dir)


class InternalButtons:
    
    def __init__(self, elevator_car):
        self.dispatcher = InternalButtonDispatcher()
        self.buttons = [i for i in range(10)]
        self.button_selected = None
        self.elevator_car = elevator_car


    def press_button(self, floor):
        self.button_selected = floor
        if floor > self.elevator_car.currentFloor:
            self.dispatcher.submit_internal_request(self.button_selected, floor, Direction.UP)
        else:
            self.dispatcher.submit_internal_request(self.button_selected, floor, Direction.DOWN)


class ElevatorCar:
    def __init__(self, id):
        self.id = id
        self.display = Display()
        self.currentFloor = 0
        self.direction = Direction.UP
        self.status = Status.IDLE
        self.doors = Door()
        self.internalButtons = InternalButtons()
    
    def show_display(self):
        return self.display.show()

    def set_display(self):
        return self.display.set_display(self.currentFloor, self.direction)

    def moveElevator(self, dir, dest_floor):
        start_floor = self.currentFloor
        if dir == Direction.UP:
            for i in range(start_floor, dest_floor + 1):
                self.currentFloor = i
                self.set_display()
                self.show_display()
                if i == dest_floor:
                    return True
        else:
            for i in range(start_floor, dest_floor - 1, -1):
                self.currentFloor = i
                self.set_display()
                self.show_display()
                if i == dest_floor:
                    return True
        
        return False

class ElevatorController:
    '''
    One to One relationship between ElevatorController and ElevatorCar
    Each controller controls its own elevator car which is a dumb object
    '''
    def __init__(self, elevator_car):
        self.elevator_car = elevator_car
        self.up_minheap = []
        self.down_maxheap = []
        self.pending_requests = deque()

    def submit_new_request(self, floor, direction):
        if direction == Direction.UP:
            self.up_minheap.append(floor)
        else:
            self.down_maxheap.append(floor)
        
        self.process_request()
    
    def process_request(self):
        pass
        
class ExternalDispatcher:
    elevator_controller_list = ElevatorCreator.elevator_controllers
    def __init__(self, strategy):
        self.strategy = strategy

    def submit_external_request(self, floor, direction):
        self.strategy.process(ExternalDispatcher.elevator_controller_list, floor, direction)    


class AssignStrategy(ABC):
    @abstractmethod
    def process(self, elevator_controller_list, floor, direction):
        pass

class OddEvenStrategy(AssignStrategy):
    def process(self, elevator_controller_list, floor, direction):
        for elevator_controller in elevator_controller_list:
            elevator_id = elevator_controller.elevator_car.id
            if elevator_id % 2 == 0 and floor % 2 == 0:
               elevator_controller.submit_new_request(floor, direction)
            elif elevator_id % 2 == 1 and floor % 2 == 1:
                elevator_controller.submit_new_request(floor, direction)

class FixedStrategy(AssignStrategy):
    def process(self, elevator_controller_list, floor, direction):
        # assign the request to the first elevator
        elevator_controller_list[0].submit_new_request(floor, direction)

class Floor:
    def __init__(self, floor_number):
        self.floor_number = floor_number
        self.external_dispatcher = ExternalDispatcher()
    
    def press_button(self, direction):
        self.external_dispatcher.submit_external_request(self.floor_number, direction)

class Building:
    def __init__(self, floors):
        self.floors = floors
    
    def add_floor(self, floor):
        self.floors.append(floor)
    
    def remove_floor(self, floor):
        self.floors.remove(floor)
    
    def get_floors(self):
        return self.floors

class ElevatorSystem:
    floors = []
    for i in range(10):
        floors.append(Floor(i))
    building = Building(floors)