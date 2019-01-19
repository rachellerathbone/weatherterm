import os
from selenium import webdriver

# This class is responsible for getting data from the weather website. When the
# initializer defines the base URL and creates a PhantomJS driver, using the
# path where PhantomJS is installed.
class Request:
    def __init__(self, base_url):
        self._driver_path = os.path.join(os.curdir, 'phantomjs/bin/phantomjs')
        self._base_url = base_url
        self._driver = webdriver.PhantomJS(self._driver_path)

    # This formats the URL, adding the forecast option and the area.
    def fetch_data(self, forecast, area):
        url = self._base_url.format(forecast=forecast, area=area)
        # after that the webdriver performs a request and returns the page source.
        self._driver.get(url)

        # If the title of the markup returned is 404 Not Found, it will raise an
        # exception. Unfortunately, Selenium doesn't provider a proper way of
        # getting the HTTP Status code.
        if self._driver.title == '404 Not Found':
            error_message = ('Could not find the area that you '
                             'searching for')
            raise Exception(error_message)

        return self._driver.page_source
