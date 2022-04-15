from src.common import click_by_xpath,\
    get_element_text, check_element_existence


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
    def do_heal(driver, buttons):
        try:

            heal_logo = check_element_existence(
                driver=driver,
                xpath=buttons["heal-logo"],
            )

            if not driver.find_element_by_css_selector('.sc-fmrZth') \
                    and heal_logo:

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

                print('Brawler healed')

        except Exception as globalException:

            driver.refresh()

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

        if heal_ratio:

            heal_struct.ratio = list(map(float, heal_ratio.split('/')))

            return True

        return False

    def run(self):

        while True:

            if Heal.getRatio(
                heal_struct=self.heal_struct,
                driver=self.driver,
                button=self.buttons["heal-ratio"]
            ):

                Heal.checkForHeal(
                    driver=self.driver,
                    buttons=self.buttons,
                    ratio=self.heal_struct.ratio,
                )
