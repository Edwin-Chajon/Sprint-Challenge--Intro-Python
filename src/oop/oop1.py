# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class

class Vehicle:
    pass

# from vehicle
class FlightVehicle(Vehicle):
    pass

# from Flight Vehicle
class Airplane(FlightVehicle):
    pass
class Starship(FlightVehicle):
    pass

# from vehicle
class GroundVehicle(Vehicle):
    pass

# from ground vehicle
class Car(GroundVehicle):
    pass

class Motorcycle(GroundVehicle):
    pass



