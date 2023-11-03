import logging
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.core import config

from helper_functions.helper_file import helper


class HomePage:
    SEARCH_BAR = (By.XPATH, "//input[@type='text']")
    SEARCH_TEXT = (By.XPATH, "//span[contains(@class,'a-color-state a-text-bold')]")
    SIGN_IN = (By.XPATH, "//span[contains(text(),'Hello, sign in')]//ancestor::a")
    USER_AFTER_LOGIN = (By.XPATH, "//span[@id='nav-link-accountList-nav-line-1']")
    SIGN_IN1 = (By.XPATH, "//span[@class='nav-action-inner'][contains(.,'Sign in')]")

    def __init__(self, browser):
        self.browser = browser.driver

    def navigate_to_amazon_page(self, url):
        self.browser.get(url)
        logging.info("Title of the webpage is "+self.browser.title)
        time.sleep(10)

    def search_with_value(self, value):
        helper(self.browser).fill_the_value_and_click_enter(self.SEARCH_BAR, value)
        time.sleep(3)

    def clicks_on_button(self, button):
        helper(self.browser).move_to_element(self.SIGN_IN)
        helper(self.browser).click_element(self.SIGN_IN1)
        logging.info("signin clicked")

    def verify_user_is_logged_in(self):
        value = helper(self.browser).get_text(self.USER_AFTER_LOGIN)
        assert "Hello, Swamynath" == value
