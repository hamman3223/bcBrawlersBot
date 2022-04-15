import json
import os
from src.common import click_by_xpath


''' Custom exception to infrom about invalid token '''


class waxAuthorizationError(Exception):

    def __init__(self):

        super().__init__("Something went wrong with"
                         " authorization in wax wallet")


class waxAuthorize():

    def __init__(self, driver, buttons):

        self.driver = driver
        self.buttons = buttons

        ''' Load auth token from authorization.json
                that stores Wax Wallet auth token
        '''
        with open(
            os.path.join(os.getcwd(), "authorization.json"),
            "r"
        ) as auth_file:

            self.auth_token = json.load(auth_file)

        self.run()

    def run(self):

        self.driver.get("https://wallet.wax.io")
        self.driver.add_cookie(
            self.auth_token["auth_token"]
        )
        self.driver.refresh()

        billing = click_by_xpath(
            driver=self.driver,
            xpath=self.buttons["billing"],
            timeout=20,
        )

        ''' Firstly validate existence of billing!!!!  '''
        if len(billing.text) <= 15:

            return True

        else:

            raise waxAuthorizationError
