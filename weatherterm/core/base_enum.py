# This is an enumeration to represent the temperature units that the user will
# be able to choose from in the command line. This enumeration will contain
# Celsius and Fahrenheit items.
from enum import Enum

# This is a very simple class inheriting from Enum. The only thing it does is
# overrides the method _generate_next_value_so that every enumeration that
# inherits from BaseEnum and has properties with the value set to auto() will
# automatically get the same value as the property name.
class BaseEnum(Enum):

    def _generate_next_value_(name, start, count, last_value):
        return name
