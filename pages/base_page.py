from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException


class BasePage:
    def __init__(self, browser: webdriver, url: str, timeout: int = 10) -> None:
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self) -> None:
        self.browser.get(self.url)

    def is_element_present(self, how: str, what: str) -> bool:
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True