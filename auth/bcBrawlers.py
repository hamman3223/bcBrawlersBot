from src.common import click_by_xpath


class bcBrawAuthorize():

    def __init__(self, driver, buttons):

        self.driver = driver
        self.buttons = buttons
        self.run()

    def run(self):

        ''' Wait until login button appear '''

        login_button = click_by_xpath(
            driver=self.driver,
            xpath=self.buttons["login"],
            timeout=20,
        )

        click_by_xpath(
            driver=self.driver,
            xpath=self.buttons["wax_cloud_login"],
            timeout=10,
        )

        login_button.click()
