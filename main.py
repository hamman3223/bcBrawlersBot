from selenium.webdriver.common.keys import Keys
from src.getDriver import check_os
from auth.bcBrawlers import bcBrawAuthorize
from auth.waxWallet import waxAuthorize, waxAuthorizationError
from selenium import webdriver
import os
from os.path import join as path_join

os_types = ['nt', 'posix']

buttons = {
    "play": "/html/body/div[1]/div/button/div",
    "heal": "/html/body/div[1]/div/div[2]/div[1]/div[2]/div[1]",
    "heal_now": "/html/body/div[1]/div/div[2]/div[2]/div/div[4]/button/div",
    "login": "/html/body/div[1]/div/button/div",
    "billing": "/html/body/div/div/div[1]/div[1]/div[1]",
}

''' 
    NOTE for MOVE_SLIDER logic

    outerText - to get proportion of ...
    "/html/body/div[1]/div/div[2]/div[1]/div[4]/div[2]/div[2]/span" - xPath to heal proportion
'''

keystrokes = {
    "slider": Keys.TAB*2,
    "slider_alternative": Keys.TAB*5,
    # "move_slider":
}

def getDriver(os_type: str):
    
    ''' 
    Argument: Take returned variable from check_os "posix" or "nt"
    
    Returns: webdriver object related to OS type
    '''
    
    if os_type == os_types[0]: return webdriver.Firefox(
        executable_path=path_join(os.getcwd(), "drivers", "geckodriver.exe"),
        service_log_path=os.devnull,
    
    )
    if os_type == os_types[1]: return webdriver.Firefox(
        executable_path=path_join(os.getcwd(), "drivers", "geckodriver_macos"),
        service_log_path=os.devnull,
    )
    
if __name__ == "__main__":
    
    try:

        os_types = ['nt', 'posix']
        
        driver = getDriver(
            check_os(os_types=os_types)
        )
        
        waxAuthorize(
            driver=driver,
            keystrokes=keystrokes,
            buttons=buttons,
        )
        
        
        driver.get("https://play.bcbrawlers.com/")
        bcBrawAuthorize(
            driver=driver,
            keystrokes=keystrokes,
            buttons=buttons,
        )

    except KeyboardInterrupt as Inerrupt:
        
        driver.close()
        
    except waxAuthorizationError as waxAuthError:
        
        print(waxAuthError)
        driver.close()
        

        
        

