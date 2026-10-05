from maintestcase import user
from selenium import webdriver

"""
1. Launch browser
2. Navigate to url 'http://automationexercise.com'
3. Verify that home page is visible successfully
4. Click 'Cart' button
5. Scroll down to footer
6. Verify text 'SUBSCRIPTION'
7. Enter email address in input and click arrow button
8. Verify success message 'You have been successfully subscribed!' is visible
"""

class Testcase11(user):
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
            self.click_menu_items('Cart')
            self.scroll_down(3000)
            self.verify_headline_is_displayed('Subscription')
            self.subscribe_email('pawankalyan18092002@gmail.com')
            self.validate_subscription_success()


        except Exception as exp:
            print(f"Error during test execution: {exp}")

        finally:
            self.driver.quit()

if __name__ == "__main__":
    testcase = Testcase11()
    testcase.execute_testcase()