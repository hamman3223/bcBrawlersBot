from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import json
import os


''' Custom exception to infrom about invalid token '''
class waxAuthorizationError(Exception):
    
    def __init__(self, token):

        self.token = token
        super().__init__("Something went wrong"\
            ," when we try to authorize with token"\
                ,self.token)

class waxAuthorize():
    
    def __init__(self, driver, keystrokes, buttons):
        
        self.driver = driver
        self.keystrokes = keystrokes
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
        
        billing = WebDriverWait(
                self.driver,
                30,
            ).until(
                EC.presence_of_element_located((
                    By.XPATH, self.buttons["billing"]
                ))
            )
        
        ''' Firstly validate existence of billing!!!!  '''       
        if len(billing.text) <= 15:
            
            return billing.text

        raise waxAuthorizationError(self.token['auth_token'])