from argparse import Action

from weatherterm.core import Unit

# This class inherits from argparse.Action and overrides the __call__ method,
# which will be called when the argument value is parsed. This is going to be
# set to the destination atrribute.
# The parser parameter will be an instance of ArgumentParser. THe namespace is
# an instance of argparser.Namespace. This is a simple class containing all the
# attributes defined in the ArgumentParser obj.
# The values parameter is the value that the user has passed on the command line
# (C or F). For the unit argument, the value of option_string will be -u.
class SetUnitAction(Action):

    def __call__(self, parser, namespace, values, option_string=None):
        # Enumerations in Python allow us to access their members and attributes
        # using item access.
        unit = Unit[values.upper()]
        # After getting the correct the enumeration member, set the value of the
        # property specified by self.dest in the namespace obj.
        setattr(namespace, self.dest, unit)
