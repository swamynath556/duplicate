from behave.contrib.scenario_autoretry import patch_scenario_with_autoretry
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from behave import fixture
from pages.base import basepage


def before_feature(context, feature):
    for scenario in feature.scenarios:
        if "smoke_test" not in scenario.effective_tags:
            patch_scenario_with_autoretry(scenario, max_attempts=2)


def before_scenario(context, scenario):
    print("Scenario is ")
    service = Service()
    options = webdriver.ChromeOptions()
    context.driver = webdriver.Chrome(service=service, options=options)
    context.driver.maximize_window()


def after_scenario(context, scenario):
    context.driver.close()


def before_step(context, step):
    basepage.attach_screenshot(context, step.name + '---BEFORE_SCREENSHOT---')


def after_step(context, step):
    basepage.attach_screenshot(context, step.name + '---AFTER_SCREENSHOT---')
