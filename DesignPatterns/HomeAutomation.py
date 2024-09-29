# This is a simple implementation of the Command Pattern
# The Command Pattern encapsulates a request as an object, thereby allowing for parameterization of clients with different requests, queuing of requests, and logging of requests, and supporting undoable operations.
# Can also support logging using store and load methods

from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass

class NoCommand(Command):
    def execute(self):
        pass

    def undo(self):
        pass

class MacroCommand(Command):
    def __init__(self, commands):
        self.commands = commands

    def execute(self):
        for command in self.commands:
            command.execute()

    def undo(self):
        for command in self.commands:
            command.undo()

class Light:
    def __init__(self, location):
        self.location = location

    def on(self):
        print("Light is on in the " + self.location)

    def off(self):
        print("Light is off in the " + self.location)
    
class LightOnCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.on()

    def undo(self):
        self.light.off()

class LightOffCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.off()

    def undo(self):
        self.light.on()

class Stereo:
    def __init__(self, location):
        self.location = location

    def on(self):
        print(f"Stereo is on in the {self.location}")

    def off(self):
        print(f"Stereo is off in the {self.location}")

    def setCD(self):
        print(f"Stereo is set for CD input in the {self.location}")

    def setDVD(self):
        print(f"Stereo is set for DVD input in the {self.location}")

    def setRadio(self):
        print(f"Stereo is set for Radio input in the {self.location}")

    def setVolume(self, volume):
        print(f"Stereo volume set to {volume} in the {self.location}")

class StereoOnWithCDCommand(Command):
    def __init__(self, stereo):
        self.stereo = stereo

    def execute(self):
        self.stereo.on()
        self.stereo.setCD()
        self.stereo.setVolume(11)

    def undo(self):
        self.stereo.off()

class StereoOffCommand(Command):
    def __init__(self, stereo):
        self.stereo = stereo

    def execute(self):
        self.stereo.off()

    def undo(self):
        self.stereo.on()
        self.stereo.setCD()
        self.stereo.setVolume(11)

class CeilingFan:
    HIGH = 3
    MEDIUM = 2
    LOW = 1
    OFF = 0

    def __init__(self, location):
        self.location = location
        self.speed = self.OFF

    def high(self):
        self.speed = self.HIGH
        print(f"{self.location} ceiling fan is on high")

    def medium(self):
        self.speed = self.MEDIUM
        print(f"{self.location} ceiling fan is on medium")

    def low(self):
        self.speed = self.LOW
        print(f"{self.location} ceiling fan is on low")

    def off(self):
        self.speed = self.OFF
        print(f"{self.location} ceiling fan is off")

    def getSpeed(self):
        return self.speed

class CeilingFanHighCommand(Command):
    def __init__(self, ceilingFan):
        self.ceilingFan = ceilingFan
        self.prevSpeed = ceilingFan.getSpeed()

    def execute(self):
        self.prevSpeed = self.ceilingFan.getSpeed()
        self.ceilingFan.high()

    def undo(self):
        if self.prevSpeed == CeilingFan.HIGH:
            self.ceilingFan.high()
        elif self.prevSpeed == CeilingFan.MEDIUM:
            self.ceilingFan.medium()
        elif self.prevSpeed == CeilingFan.LOW:
            self.ceilingFan.low()
        elif self.prevSpeed == CeilingFan.OFF:
            self.ceilingFan.off()

class CeilingFanMediumCommand(Command):
    def __init__(self, ceilingFan):
        self.ceilingFan = ceilingFan
        self.prevSpeed = ceilingFan.getSpeed()

    def execute(self):
        self.prevSpeed = self.ceilingFan.getSpeed()
        self.ceilingFan.medium()

    def undo(self):
        if self.prevSpeed == CeilingFan.HIGH:
            self.ceilingFan.high()
        elif self.prevSpeed == CeilingFan.MEDIUM:
            self.ceilingFan.medium()
        elif self.prevSpeed == CeilingFan.LOW:
            self.ceilingFan.low()
        elif self.prevSpeed == CeilingFan.OFF:
            self.ceilingFan.off()

class CeilingFanOffCommand(Command):
    def __init__(self, ceilingFan):
        self.ceilingFan = ceilingFan
        self.prevSpeed = ceilingFan.getSpeed()

    def execute(self):
        self.prevSpeed = self.ceilingFan.getSpeed()
        self.ceilingFan.off()

    def undo(self):
        if self.prevSpeed == CeilingFan.HIGH:
            self.ceilingFan.high()
        elif self.prevSpeed == CeilingFan.MEDIUM:
            self.ceilingFan.medium()
        elif self.prevSpeed == CeilingFan.LOW:
            self.ceilingFan.low()
        elif self.prevSpeed == CeilingFan.OFF:
            self.ceilingFan.off()

class RemoteControl:
    def __init__(self):
        self.slotsCount = 7
        self.onCommands = [NoCommand()] * self.slotsCount
        self.offCommands = [NoCommand()] * self.slotsCount
        self.undoCommand = NoCommand()


    def setCommand(self, slot, onCommand, offCommand):
        self.onCommands.insert(slot, onCommand)
        self.offCommands.insert(slot, offCommand)

    def onButtonWasPushed(self, slot):
        self.onCommands[slot].execute()
        self.undoCommand = self.onCommands[slot]

    def offButtonWasPushed(self, slot):
        self.offCommands[slot].execute()
        self.undoCommand = self.offCommands[slot]

    def undoButtonWasPushed(self):
        self.undoCommand.undo()
    
    def __str__(self):
        res = "\n------ Remote Control ------\n"
        for i in range(self.slotsCount):
            res += f"[slot {i}] {self.onCommands[i].__class__.__name__}    {self.offCommands[i].__class__.__name__}\n"
        return res

if __name__ == "__main__":
    remote = RemoteControl()
    LivingRoomLight = Light("Living Room")
    LivingRoomLightOn = LightOnCommand(LivingRoomLight)
    LivingRoomLightOff = LightOffCommand(LivingRoomLight)
    BedRoomStereo = Stereo("Bed Room")
    BedRoomStereoOnWithCD = StereoOnWithCDCommand(BedRoomStereo)
    BedRoomStereoOff = StereoOffCommand(BedRoomStereo)
    LivingRoomCeilingFan = CeilingFan("Living Room")
    LivingRoomCeilingFanHigh = CeilingFanHighCommand(LivingRoomCeilingFan)
    LivingRoomCeilingFanMedium = CeilingFanMediumCommand(LivingRoomCeilingFan)
    LivingRoomCeilingFanOff = CeilingFanOffCommand(LivingRoomCeilingFan)
    partyOnMacro = MacroCommand([LivingRoomLightOn, BedRoomStereoOnWithCD, LivingRoomCeilingFanHigh])
    partyOffMacro = MacroCommand([LivingRoomLightOff, BedRoomStereoOff, LivingRoomCeilingFanOff])

    remote.setCommand(0, LivingRoomLightOn, LivingRoomLightOff)
    remote.setCommand(1, BedRoomStereoOnWithCD, BedRoomStereoOnWithCD)
    remote.setCommand(2, LivingRoomCeilingFanHigh, LivingRoomCeilingFanOff)
    remote.setCommand(3, LivingRoomCeilingFanMedium, LivingRoomCeilingFanOff)
    remote.setCommand(4, partyOnMacro, partyOffMacro)

    print(remote)

    remote.onButtonWasPushed(0)
    remote.offButtonWasPushed(0)
    remote.undoButtonWasPushed()
    remote.onButtonWasPushed(1)
    remote.offButtonWasPushed(1)
    remote.undoButtonWasPushed()
    remote.onButtonWasPushed(2)
    remote.offButtonWasPushed(2)
    remote.undoButtonWasPushed()
    remote.onButtonWasPushed(3)
    # remote.offButtonWasPushed(3)
    remote.undoButtonWasPushed() 
    print("Party On")
    remote.onButtonWasPushed(4)
    print("Party Off")
    remote.undoButtonWasPushed()