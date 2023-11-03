import logging

from selenium.webdriver.common.by import By
from helper_functions.helper_file import helper


class search:
    SEARCH_TEXT = (By.XPATH, "//span[contains(@class,'a-color-state a-text-bold')]")

    def __init__(self, browser):
        self.browser = browser.driver

    def verify_search_results(self, value):
        pass



