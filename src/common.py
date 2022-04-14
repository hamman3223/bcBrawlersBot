from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver


def click_by_xpath(driver: webdriver, xpath: str, timeout: int = 10)\
        -> WebDriverWait:

    """
    Args:
        driver (_type_): _description_
        xpath (str): _description_
        timeout (int, optional): _description_. Defaults to 10.
    """
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
