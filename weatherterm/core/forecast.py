from datetime import date
from .forecast_type import ForecastType


# This class represents the weather forecast data that the parser returns
class Forecast:
    def __init__(
            self,
            current_temp,
            humidity,
            wind,
            high_temp=None,
            low_temp=None,
            description='',
            forecast_date=None,
            forecast_type=ForecastType.TODAY):
        self._current_temp = current_temp
        self._high_temp = high_temp
        self._low_temp = low_temp
        self._humidity = humidity
        self._wind = wind
        self._description = description
        self._forecast_type = forecast_type

        if forecast_date is None:
            self.forecast_date = date.today()
        else:
            self._forecast_date = forecast_date

    # The @property decorator will turn the method into a getter for the
    #  _forecast_date.setter will turn the method into a setter. The setter
    # was defined in this file because, every time we need to set the date in
    # an instance of Forecast, we need to make sure that it will be formatted
    #  accordingly.
    @property
    def forecast_date(self):
        return self._forecast_date

    # We call the strftime method, passing the format codes %a (weekday),
    # %b (monthly), and d% (day of the month).
    @forecast_date.setter
    def forecast_date(self, forecast_date):
        self._forecast_date = forecast_date.strftime("%a %b %d")

    @property
    def current_temp(self):
        return self._current_temp

    @property
    def humidity(self):
        return self._humidity

    @property
    def wind(self):
        return self._wind

    @property
    def description(self):
        return self._description

    # Lastly, we override the __str__ method to allow us to format the output
    # the way we would like when using the print, format, and str functions.
    def __str__(self):
        temperature = None
        offset = ' ' * 4

        if self._forecast_type == ForecastType.TODAY:
            temperature = (f'{offset}{self._current_temp}\xb0\n'
                           f'{offset}High {self._high_temp}\xb0 / '
                           f'Low {self._low_temp}\xb0 ')
        else:
            temperature = (f'{offset}High {self._high_temp}\xb0 / '
                           f'Low {self._low_temp}\xb0 ')

        return (f'>> {self.forecast_date}\n'
                f'{temperature}'
                f'({self._description})\n'
                f'{offset}Wind: '
                f'{self._wind} / Humidity: {self._humidity}\n')
