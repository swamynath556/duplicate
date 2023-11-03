import logging
import allure


class basepage:

    @staticmethod
    def attach_screenshot(context, name):
        allure.attach(context.driver.get_screenshot_as_png(), name=name, attachment_type=allure.attachment_type.PNG)

    logging.basicConfig(
        format='%(asctime)s %(levelname)-8s %(message)s',
        level=logging.INFO,
        datefmt='%Y-%m-%d %H:%M:%S'
    )
