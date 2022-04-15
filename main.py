import os
from os.path import join as path_join

from selenium.webdriver.common.keys import Keys
from selenium import webdriver

from selenium.webdriver.firefox.options import Options

from structs.heal import HealInfo

from src.getDriver import check_os
from src.heal import Heal
from src.fight import Fight

from auth.bcBrawlers import bcBrawAuthorize
from auth.waxWallet import waxAuthorize, waxAuthorizationError

from threading import Thread

os_types = ['Windows', 'Linux', "Darwin"]

buttons = {
    "play": "/html/body/div[1]/div/button/div",

    "heal-ratio": "/html/body/div[1]/div/div[2]/div[1]/div[4]/div[2]/div[2]/span",

    "heal-logo": "/html/body/div[1]/div/div[2]/div[1]/div[2]/div[1]/img",
    "heal-now": "/html/body/div[1]/div/div[2]/div[2]/div/div[4]/button/div",
    "login": "/html/body/div[1]/div/button/div",
    "billing": "/html/body/div/div/div[1]/div[1]/div[1]",
    "wax_cloud_login": "/html/body/div[1]/div[1]/div/div[2]/div[1]/div[2]",

    "go-brawl": "/html/body/div[1]/div/"
    "div[2]/div[1]/div[4]/div[3]/button[2]/div",

    "go-brawl-timeout": "/html/body/div[1]/div/"
    "div[2]/div[1]/div[4]/div[3]/div",

    "continue": "/html/body/div[1]/div/div[2]/div[2]/div/div[3]/button/div",
}


def getDriver(os_type: str, options):

    '''
    Argument: Take returned variable from check_os "posix" or "nt"

    Returns: webdriver object related to OS type
    '''

    if os_type == os_types[0]: return webdriver.Firefox(
        options=options,
        executable_path=path_join(os.getcwd(), "drivers", "geckodriver.exe"),
        service_log_path=os.devnull,

    )
    if os_type == os_types[1]: return webdriver.Firefox(
        options=options,
        executable_path=path_join(os.getcwd(), "drivers", "geckodriver_linux"),
        service_log_path=os.devnull,
    )
    if os_type == os_types[2]: return webdriver.Firefox(
        options=options,
        executable_path=path_join(os.getcwd(), "drivers", "geckodriver_macos"),
        service_log_path=os.devnull,
    )


if __name__ == "__main__":

    try:

        heal_info = HealInfo()

        options = Options()
        options.headless = True
        driver = getDriver(
            os_type=check_os(os_types=os_types),
            options=options,
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

        ''' Put Heal logic into single thread '''

        heal = Thread(target=Heal,
                      args=(heal_info, driver, keystrokes, buttons),
                      )

        fight = Thread(target=Fight,
                       args=(driver, buttons),
                       )

        heal.start()
        fight.start()

    except KeyboardInterrupt:

        driver.close()

    except waxAuthorizationError as waxAuthError:

        print(waxAuthError)
        driver.close()
