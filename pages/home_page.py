import os
import time

from locators.locators import ZultysLocators
from base_object.base import BaseObject


class MxHomePage(BaseObject):

    def open_main_page(self):
        """ Opens the main page of the MX website."""
        self.open_link('mxkiev.zultys.com')

    def main_page_download(self, locator):
        """
        Open the main page and click on the element specified by the locator.
        Args:
            locator (tuple): The locator of the element to click on.
        """
        self.open_main_page()
        self.driver.find_element(*locator).click()
        time.sleep(30)
