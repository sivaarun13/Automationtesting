from maintestcase import user
from selenium import webdriver
import time

"""1. Launch browser
2. Navigate to url 'http://automationexercise.com'
3. Verify that home page is visible successfully
4. Scroll down page to bottom
5. Verify 'SUBSCRIPTION' is visible
6. Scroll up page to top
7. Verify that page is scrolled up and 'Full-Fledged practice website for Automation Engineers' text is visible on screen
"""

class Testcase26(user):
    def __init__(self):
        driver = webdriver.Chrome()
        super().__init__(driver)

    def execute_testcase(self):
        try:
            """Initialize the browser"""
            url = "http://automationexercise.com"
            # self.driver = webdriver.Chrome()
            self.driver.maximize_window()
            self.driver.get(url)

            """Testcase steps """
            self.validate_home_page_is_visible_successfully()
            self.scroll_to_bottom()
            self.verify_headline_is_displayed('Subscription')
            time.sleep(5)
            self.click_arrow_button()
            time.sleep(5)
            self.verify_headline_is_displayed('Full-Fledged practice website for Automation Engineers')

        except Exception as exp:
            print(f'Error during test execution{exp}')

        finally:
            self.driver.quit()

if __name__ == '__main__':
    testcase = Testcase26()
    testcase.execute_testcase()
