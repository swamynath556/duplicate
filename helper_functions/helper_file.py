import logging

from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By


class helper:

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator):
        return self.driver.find_element(*locator)

    def click_element(self, locator):
        self.driver.find_element(*locator).click()

    def fill_the_value(self, locator, value):
        self.driver.find_element(*locator).send_keys(value)

    def fill_the_value_and_click_enter(self, locator, value):
        logging.info("the value to be entered is" +value)
        self.driver.find_element(*locator).send_keys(value, Keys.ENTER)

    def get_text(self, locator):
        return self.driver.find_element(*locator).text

    def move_to_element(self, locator):
        action = ActionChains(self.driver)
        element = self.find_element(locator)
        action.move_to_element(element).perform()

    def move_to_element_and_click(self, locator):
        action = ActionChains(self.driver)
        element = self.find_element(locator)
        action.move_to_element(element).click().perform()
