from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.common.exceptions import TimeoutException


def click_by_xpath(driver: webdriver, xpath: str, timeout: int = 10)\
        -> WebDriverWait:

    """
    Args:
        driver (_type_)
        xpath (str)
        timeout (int, optional): Defaults to 10.
    """

    try:

        inited_button = WebDriverWait(
            driver=driver,
            timeout=timeout,
        ).until(
            EC.presence_of_element_located((
                By.XPATH, xpath
            ))
        )

        inited_button.click()

        return inited_button

    except TimeoutException as timeout:

        pass

def get_element_text(driver: webdriver, xpath: str, timeout: int = 10):

    try:

        inited_button = WebDriverWait(
            driver=driver,
            timeout=timeout,
        ).until(
            EC.presence_of_element_located((
                By.XPATH, xpath
            ))
        )

        return inited_button.text

    except TimeoutException as timeout:
        pass
