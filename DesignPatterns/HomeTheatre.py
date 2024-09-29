# This is a simple implementation of the Facade Pattern
# The Facade Pattern provides a unified interface to a set of interfaces in a subsystem. Facade defines a higher-level interface that makes the subsystem easier to use.
# Can implement more than one Facade for a subsystem

class Amplifier:
    def on(self):
        print("Amplifier is on")
    
    def off(self):
        print("Amplifier is off")
    
    def setCD(self):
        print("CD is set")
    
    def setDVD(self):
        print("DVD is set")
    
    def setStereoSound(self):
        print("Stereo sound is set")
    
    def setSurroundSound(self):
        print("Surround sound is set")
    
    def setTuner(self):
        print("Tuner is set")
    
    def setVolume(self, volume):
        print(f"Volume is set to {volume}")

class Tuner:
    def on(self):
        print("Tuner is on")
    
    def off(self):
        print("Tuner is off")
    
    def setAM(self):
        print("AM is set")
    
    def setFM(self):
        print("FM is set")
    
    def setFrequency(self, frequency):
        print(f"Frequency is set to {frequency}")

class DVDPlayer:
    def on(self):
        print("DVD Player is on")
    
    def off(self):
        print("DVD Player is off")
    
    def play(self, movie):
        print(f"DVD is playing {movie}")
    
    def stop(self):
        print("DVD is stopped")
    
    def eject(self):
        print("DVD is ejected")

class Projector:
    def on(self):
        print("Projector is on")
    
    def off(self):
        print("Projector is off")
    
    def wideScreenMode(self):
        print("Wide screen mode is set")
    
    def tvMode(self):
        print("TV mode is set")

class TheaterLights:
    def on(self):
        print("Theater lights are on")
    
    def off(self):
        print("Theater lights are off")
    
    def dim(self, level):
        print(f"Theater lights are dimmed to {level}")

class Screen:
    def up(self):
        print("Screen is up")
    
    def down(self):
        print("Screen is down")

class PopcornPopper:
    def on(self):
        print("Popcorn popper is on")
    
    def off(self):
        print("Popcorn popper is off")
    
    def pop(self):
        print("Popcorn is popping")
    
    def stop(self):
        print("Popcorn is stopped")

class HomeTheatreFacade:
    def __init__(self, amp, tuner, dvd, projector, lights, screen, popper):
        self.amp = amp
        self.tuner = tuner
        self.dvd = dvd
        self.projector = projector
        self.lights = lights
        self.screen = screen
        self.popper = popper
    
    def watchMovie(self, movie):
        print("Get ready to watch a movie...")
        self.popper.on()
        self.popper.pop()
        self.lights.dim(10)
        self.screen.down()
        self.projector.on()
        self.projector.wideScreenMode()
        self.amp.on()
        self.amp.setDVD()
        self.amp.setSurroundSound()
        self.amp.setVolume(5)
        self.dvd.on()
        self.dvd.play(movie)
    
    def endMovie(self):
        print("Shutting movie theater down...")
        self.popper.off()
        self.lights.on()
        self.screen.up()
        self.projector.off()
        self.amp.off()
        self.dvd.stop()
        self.dvd.eject()
        self.dvd.off()

if __name__ == "__main__":
    amp = Amplifier()
    tuner = Tuner()
    dvd = DVDPlayer()
    projector = Projector()
    lights = TheaterLights()
    screen = Screen()
    popper = PopcornPopper()
    
    homeTheatre = HomeTheatreFacade(amp, tuner, dvd, projector, lights, screen, popper)
    print("<----Let's watch a movie!---->")
    homeTheatre.watchMovie("Raiders of the Lost Ark")
    print("<----Movie is over!---->")
    homeTheatre.endMovie()