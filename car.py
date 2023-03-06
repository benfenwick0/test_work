import pytest

class Car:

    def __init__(self, make, weight, color, currentSpeed, maxSpeed, fuelLevel):
        self.make = make
        self.weight = weight
        self.color = color
        self.currentSpeed = currentSpeed
        self.maxSpeed = maxSpeed
        self.fuelLevel = fuelLevel

    def accelerate(self):
        self.currentSpeed += 1
        self.fuelLevel -= 1

    def brake(self):
        self.currentSpeed -= 1

    def refuel(self):
        self.fuelLevel += 10