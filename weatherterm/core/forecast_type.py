#  This model will represent all of the info that our app will scrape from the
#  weather website.
from enum import Enum, unique

# Enumerations can be created  using the syntax for creating classes. Create a
# class inheriting from enum.Enum containing a set of unique properties set to
# constant values. We have values for the four types of forecast that the
# application will provideself.

# Note that we are assiging contant values that are different from the property
# item of the enumeration, the reason being that later these values will be used
# to build the URL to make requests to the weather website.
@unique
class ForecastType(Enum):
    TODAY = 'today'
    FIVEDAYS = '5day'
    TENDAYS = '10day'
    WEEKEND = 'weekend'
