# This is an enumeration for the temperature units.
from enum import auto, unique
from .base_enum import BaseEnum

# This class inherits from the BaseEnum class and every property is set to auto()
# meaning the value for every item in the enumeration will be set automatically
# for us. Since the unit class inherits from BaseEnum, every time auto() is
# called the _generate_next_value_ method on BaseEnum will be invoked and will
# return the name of the property itself.
@unique
class Unit(BaseEnum):
    CELSIUS = auto()
    FAHRENHEIT = auto()
