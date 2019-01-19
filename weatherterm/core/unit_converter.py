# By default, the temp unit used for weather.com is Fahrenheit, and we want to
# give the users of our application the option to use Celsius instead.
from .unit import Unit

# The initializer of this class gets two arguments; the default unit used by the
# parser and the destination unit. We define a dictionary containing the
# functions that will be used for temp unit conversion.
class UnitConverter:
    def __init__(self, parser_default_unit, dest_unit=None):
        self._parser_default_unit = parser_default_unit
        self.dest_unit = dest_unit
        self._convert_functions = {
            Unit.CELSIUS: self._to_celsius,
            Unit.FAHRENHEIT: self._to_fahrenheit,
        }

    # The convert method only gets one argument, the temp. Here the temp is a
    # string, so the first thing we need to try and do is convert it to a float
    # value, if it fails we will return 0.
    def convert(self, temp):

        try:
            temperature = float(temp)
        except ValueError:
            return 0

        # Verify if the destination unit is the same as the parser's default
        # unit or not. If it is, there is no need to perform any conversion so
        # we simply format the value and return it.
        if (self.dest_unit == self._parser_default_unit or
            self.dest_unit is None):
            return self._format_results(temperature)

        # If we do need to format the value we can lool up the _convert_functions
        # dictionary to find the conversions function we need to run. If we find
        # the function we are looking for, we invoke it and return the formatted
        # value.
        func = self._convert_functions[self.dest_unit]
        result = func(temperature)

        return self._format_results(result)

    # This is a utility method that formats the results for us. It checks if the
    # number is an integer; the value.is_interger() will return True if the number
    # is, for example, 10.0. If True, we will use the int function to convert
    # the value to 10; otherwise, the value is returned as a fixed-point number
    # with a precision of 1. The default precision of Python is 6.
    def _format_results(self, value):
        return int(value) if value.is_integer() else f'{value:.1f}'

    def _to_celsius(self, fahrenheit_temp):
        result = (fahrenheit_temp - 32) * 5 / 9

        return result

    def _to_fahrenheit(self, celsius_temp):
        result = (celsius_temp * 9 / 5) + 32

        return result
