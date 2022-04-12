from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class bcBrawAuthorize():
    
    def __init__(self, driver, keystrokes, buttons):
        
        self.driver = driver
        self.keystrokes = keystrokes
        self.buttons = buttons
        self.run()
        
    def run(self):

            ''' Wait until login button appear '''
            login_button = WebDriverWait(
                self.driver,
                10,
            ).until(
                EC.presence_of_element_located((
                    By.XPATH, self.buttons["login"]
                ))
            )
            # Click on login button
            login_button.click()
            
            ''' Wait until user authorize and
                    will see play button
            '''
            
            play_button = WebDriverWait(
                self.driver,
                10,
            ).until(
                EC.text_to_be_present_in_element((
                    By.XPATH, self.buttons["play"]
                ), "Play")
            ).click()
            
            
            
            