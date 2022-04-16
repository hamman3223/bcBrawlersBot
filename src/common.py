from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException


def click_by_xpath(driver: webdriver, xpath: str, timeout: int = 10)\
        -> WebDriverWait:

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

        print(f"Got timeout with xpath: {xpath}")

    except ElementClickInterceptedException as NotClickable:
        
        print(f'Elemt {xpath} not clickable error')

        pass

    except Exception as globalException:

        print(f"globalException - '{globalException}' - in click_by_xpath() func with xpath: {xpath}")

        pass

def click_if_clickable(driver: webdriver, xpath: str, timeout: int = 10)\
        -> WebDriverWait:

    try:

        inited_button = WebDriverWait(
            driver=driver,
            timeout=timeout,
        ).until(
            EC.element_to_be_clickable((
                By.XPATH, xpath
            ))
        )

        inited_button.click()

        return inited_button, True

    except TimeoutException as timeout:

        print(f"Got timeout with xpath: {xpath}")

    except ElementClickInterceptedException as NotClickable:
        
        print(f'Elemt {xpath} not clickable error')

        pass

    except Exception as globalException:

        print(f"globalException - '{globalException}' - in click_by_xpath() func with xpath: {xpath}")

        pass


def get_element_text(driver: webdriver, xpath: str, timeout: int = 10) \
    -> str:

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

        return False

    except Exception as globalException:
        
        print(f"globalException - '{globalException}' - in get_element_text() func with xpath: {xpath}")

        return False


def check_element_existence(driver: webdriver, xpath: str, timeout: int = 10) \
    -> WebDriverWait:

    try:

        inited_button = WebDriverWait(
            driver=driver,
            timeout=timeout,
        ).until(
            EC.presence_of_element_located((
                By.XPATH, xpath
            ))
        )

        return inited_button

    except Exception as globalException:
        
        print(f"globalException '{globalException}' in get_element_text() func with xpath: {xpath}")

        return False
