from src.common import click_by_xpath


class Heal():

    def __init__(self, driver, keystrokes, buttons):

        self.driver = driver
        self.keystrokes = keystrokes
        self.buttons = buttons
        self.getRatio()

    def getRatio(self):

        self.ratio = click_by_xpath(
            timeout=20,
            driver=self.driver,
            xpath=self.buttons["heal-ratio"],
        )

        self.ratio = self.ratio.text
