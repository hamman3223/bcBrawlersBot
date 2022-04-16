from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver

from src.common import click_by_xpath

class Fight():

    def __init__(self, driver: webdriver, buttons: dict):

        """
            Args:

                driver: webdriver class
                buttons: dict

        """

        self.driver = driver
        self.buttons = buttons
        self.run()

    @staticmethod
    def getTimeout(xpath: str, driver: webdriver) \
        -> int or bool:

        try:

            timer = driver.find_element_by_xpath(
                "/html/body/div[1]/div/div[2]/div[1]/div[4]/div[3]/span"
            )

            if timer.text:

                timer = list(map(int, timer.text.split(":")))

                return 60 * timer[0] + timer[1] + 20

        except NoSuchElementException as noSuchElement:

            return False

    def run(self) \
        -> None:

        timeout = Fight.getTimeout(
            xpath=self.buttons["go-brawl-timeout"],
            driver=self.driver
        )

        if not timeout:

            timeout = 3600

        while True:

            click_by_xpath(
                driver=self.driver,
                xpath=self.buttons["go-brawl"],
                timeout=timeout,
            )

            click_by_xpath(
                driver=self.driver,
                xpath=self.buttons['continue'],
                timeout=20
            )

            print("I got into a fight!!")
