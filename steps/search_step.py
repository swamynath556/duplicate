from behave import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from pages.search_page import search

from pages.HomePage import HomePage


@given("User opens the main page")
def step_impl(context):
    HomePage(context).navigate_to_amazon_page(context.config.userdata['env'])


@when('User searches with value :{value}')
def step_impl(context,value):
    HomePage(context).search_with_value(value)


@then('User should get results related to {value}')
def step_impl(context,value):
    search(context).verify_search_results(value)