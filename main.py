from car import Car
import pytest

car_1 = Car("Ford", 1500, "red", 30, 100, 50)
car_2 = Car("BMW", 1650, "blue", 60, 140, 75)

print(f"The first car's make is: {car_1.make}, the weight is {car_1.weight}g, the color of the car is {car_1.color},"
      f" the current speed of the car is "
      f"{car_1.currentSpeed}mph, the max speed is {car_1.maxSpeed}mph and the fuel level is {car_1.fuelLevel}%")

print(f"The first car's make is: {car_2.make}, the weight is {car_2.weight}g, the color of the car is {car_2.color},"
      f" the current speed of the car is "
      f"{car_2.currentSpeed}mph, the max speed is {car_2.maxSpeed}mph and the fuel level is {car_2.fuelLevel}%")

car_1.accelerate()
car_1.accelerate()
car_1.accelerate()
car_2.refuel()
car_2.brake()
car_2.brake()

print(f"The first car's make is: {car_1.make}, the weight is {car_1.weight}g, the color of the car is {car_1.color},"
      f" the current speed of the car is "
      f"{car_1.currentSpeed}mph, the max speed is {car_1.maxSpeed}mph and the fuel level is {car_1.fuelLevel}%")

print(f"The first car's make is: {car_2.make}, the weight is {car_2.weight}g, the color of the car is {car_2.color},"
      f" the current speed of the car is "
      f"{car_2.currentSpeed}mph, the max speed is {car_2.maxSpeed}mph and the fuel level is {car_2.fuelLevel}%")
