from src.common import click_by_xpath, \
    get_element_text, check_element_existence, click_if_clickable

from time import sleep

from selenium import webdriver
from structs.heal import HealInfo

class Heal():
    
    def __init__(self, heal_struct, driver, buttons):
    
        """
            Args:

                heal_struct (Heal class)
                driver (webdriver class)
                keystrokes: dict
                buttons: dict

        """

        self.heal_struct = heal_struct
        self.driver = driver
        self.buttons = buttons
        self.run()

    @staticmethod
    def do_heal(driver: webdriver, buttons: dict) \
        -> None:

        try:

            heal_logo = check_element_existence(
                driver=driver,
                xpath=buttons["heal-logo"],
            )

            if heal_logo and not heal_logo.get_attribute("alt")=="swap gear":

                _, heal_logo_state = click_if_clickable(
                    driver=driver,
                    xpath=buttons['heal-logo'],
                    timeout=10
                )

                if heal_logo_state:

                    click_by_xpath(
                        driver=driver,
                        xpath=buttons['heal-now'],
                        timeout=30
                    )

                    print('Brawler healed')

                    sleep(6)
                    driver.refresh()

        except Exception as globalException:
            
            print(f"Some troubles with do_heal() func {globalException}")

            pass

    @staticmethod
    def checkForHeal(driver: webdriver, buttons: dict, ratio: list) \
        -> None:

        if (ratio[1] - ratio[0]) <= 150:
            
            # Revoke function do_heal() if heal points less or equal than 150
            Heal.do_heal(
                driver=driver,
                buttons=buttons
            )

    @staticmethod
    def getRatio(heal_struct: HealInfo , driver: webdriver, button: dict)\
        -> bool:

        try:
            
            # check existence of heal ratio button
            heal_ratio = get_element_text(
                driver=driver,
                xpath=button,
            )

            # if heal ratio exists, then get the value
            if heal_ratio:
                
                # convert string to list and push into heal_struct
                heal_struct.ratio = list(map(float, heal_ratio.split('/')))

                return True

            return False

        except Exception as globalException:

            print(f"Some trouble with getRatio() function {globalException}")

            return False

    def run(self):

        while True:
            
            # Firstly get heal ratio
            if Heal.getRatio(
                heal_struct=self.heal_struct,
                driver=self.driver,
                button=self.buttons["heal-ratio"]
            ):

                # Then top up amount of heal points 
                Heal.checkForHeal(
                    driver=self.driver,
                    buttons=self.buttons,
                    ratio=self.heal_struct.ratio,
                )
