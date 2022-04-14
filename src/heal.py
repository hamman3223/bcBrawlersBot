from src.common import click_by_xpath, get_element_text
from selenium.common.exceptions import NoSuchElementException


class Heal():

    def __init__(self, heal_struct, driver, keystrokes, buttons):

        """
            Args:

                heal_struct (Heal class)
                driver (webdriver class)
                keystrokes: dict
                buttons: dict

        """

        self.heal_struct = heal_struct
        self.driver = driver
        self.keystrokes = keystrokes
        self.buttons = buttons
        self.run()

    @staticmethod
    def do_heal(driver, buttons):

            click_by_xpath(
                driver=driver,
                xpath=buttons['heal-logo'],
                timeout=10
            )

            click_by_xpath(
                driver=driver,
                xpath=buttons['heal-now'],
                timeout=10
            )

    @staticmethod
    def checkForHeal(driver, buttons, ratio):

        if (ratio[1] - ratio[0]) <= 150:

            Heal.do_heal(
                driver=driver,
                buttons=buttons
            )

    @staticmethod
    def getRatio(heal_struct, driver, button):

            heal_ratio = get_element_text(
                driver=driver,
                xpath=button,
            )

            heal_struct.ratio = list(map(float, heal_ratio.split('/')))

            print(heal_struct.ratio)

    def run(self):

        while True:

                Heal.getRatio(
                    heal_struct=self.heal_struct,
                    driver=self.driver,
                    button=self.buttons["heal-ratio"]
                )

                Heal.checkForHeal(
                    driver=self.driver,
                    buttons=self.buttons,
                    ratio=self.heal_struct.ratio,
            )
