class BaseObject:
    def __init__(self, driver):
        """
        Initialize the class instance with a driver object.

        Args:
            driver: The driver object used for interacting with the browser.
        """
        self.driver = driver

    def open_link(self, link):
        """ Opens a link in the browser.
        Args:
            link (str): The link to open in the browser.
        Returns:
            None
        """
        self.driver.get(f'https://{link}')
