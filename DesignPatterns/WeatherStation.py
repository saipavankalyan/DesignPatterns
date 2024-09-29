# This is a simple implementation of the Observer Pattern
# The Observer Pattern defines a one-to-many dependency between objects so that when one object changes state, all of its dependents are notified and updated automatically.

from abc import ABC, abstractmethod

class Subject(ABC):
    @abstractmethod
    def registerObserver(self, o):
        pass
    
    @abstractmethod
    def removeObserver(self, o):
        pass
    
    @abstractmethod
    def notifyObservers(self):
        pass

class Observer(ABC):
    @abstractmethod
    def update(self, temp, humidity, pressure):
        pass

class DisplayElement(ABC):
    @abstractmethod
    def display(self):
        pass

class WeatherData(Subject):
    def __init__(self):
        self.observers = []
        self.temperature = 0
        self.humidity = 0
        self.pressure = 0
    
    def registerObserver(self, o):
        self.observers.append(o)
    
    def removeObserver(self, o):
        self.observers.remove(o)
    
    def notifyObservers(self):
        for observer in self.observers:
            observer.update(self.temperature, self.humidity, self.pressure)
    
    def measurementsChanged(self):
        self.notifyObservers()
    
    def setMeasurements(self, temperature, humidity, pressure):
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure
        self.measurementsChanged()

class CurrentConditionsDisplay(Observer, DisplayElement):
    def __init__(self, weatherData):
        self.temperature = 0
        self.humidity = 0
        self.weatherData = weatherData
        weatherData.registerObserver(self)
    
    def update(self, temperature, humidity, pressure):
        self.temperature = temperature
        self.humidity = humidity
        self.display()
    
    def display(self):
        print(f"Current conditions: {self.temperature}F degrees and {self.humidity}% humidity")

class StatisticsDisplay(Observer, DisplayElement):
    def __init__(self, weatherData):
        self.maxTemp = 0
        self.minTemp = 200
        self.tempSum = 0
        self.numReadings = 0
        self.weatherData = weatherData
        weatherData.registerObserver(self)
    
    def update(self, temperature, humidity, pressure):
        self.tempSum += temperature
        self.numReadings += 1
        
        if temperature > self.maxTemp:
            self.maxTemp = temperature
        
        if temperature < self.minTemp:
            self.minTemp = temperature
        
        self.display()
    
    def display(self):
        avgTemp = self.tempSum / self.numReadings
        print(f"Avg/Max/Min temperature = {avgTemp}/{self.maxTemp}/{self.minTemp}")

class ForecastDisplay(Observer, DisplayElement):
    def __init__(self, weatherData):
        self.currentPressure = 29.92
        self.lastPressure = 0
        self.weatherData = weatherData
        weatherData.registerObserver(self)
    
    def update(self, temperature, humidity, pressure):
        self.lastPressure = self.currentPressure
        self.currentPressure = pressure
        self.display()
    
    def display(self):
        if self.currentPressure > self.lastPressure:
            print("Improving weather on the way!")
        elif self.currentPressure == self.lastPressure:
            print("More of the same")
        elif self.currentPressure < self.lastPressure:
            print("Watch out for cooler, rainy weather")

class HeatIndexDisplay(Observer, DisplayElement):
    def __init__(self, weatherData):
        self.heatIndex = 0.0
        self.weatherData = weatherData
        weatherData.registerObserver(self)
    
    def update(self, temperature, humidity, pressure):
        self.heatIndex = self.computeHeatIndex(temperature, humidity)
        self.display()
    
    def display(self):
        print(f"Heat index is {self.heatIndex}")
    
    def computeHeatIndex(self, t, rh):
        index = (16.923 + (0.185212 * t) + (5.37941 * rh) - (0.100254 * t * rh) + (0.00941695 * (t * t)) + (0.00728898 * (rh * rh)) + (0.000345372 * (t * t * rh)) - (0.000814971 * (t * rh * rh)) + (0.0000102102 * (t * t * rh * rh)) - (0.000038646 * (t * t * t)) + (0.0000291583 * (rh * rh * rh)) + (0.00000142721 * (t * t * t * rh)) + (0.000000197483 * (t * rh * rh * rh)) - (0.0000000218429 * (t * t * t * rh * rh)) + 0.000000000843296 * (t * t * rh * rh * rh)) - (0.0000000000481975 * (t * t * t * rh * rh * rh))
        return index

if __name__ == "__main__":
    weatherData = WeatherData()
    
    currentDisplay = CurrentConditionsDisplay(weatherData)
    statisticsDisplay = StatisticsDisplay(weatherData)
    forecastDisplay = ForecastDisplay(weatherData)
    heatIndexDisplay = HeatIndexDisplay(weatherData)
    
    weatherData.setMeasurements(80, 65, 30.4)
    weatherData.setMeasurements(82, 70, 29.2)
    weatherData.setMeasurements(78, 90, 29.2)