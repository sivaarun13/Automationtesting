import time
from selenium.webdriver.common.alert import Alert
from maintestcase import user
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.common.by import By


"""
1. Launch browser
2. Navigate to url 'http://automationexercise.com'
3. Verify that home page is visible successfully
4. Click on 'Signup / Login' button
5. Verify 'Login to your account' is visible
6. Enter incorrect email address and password
7. Click 'login' button
8. Verify error 'Your email or password is incorrect!' is visible
"""

class Testcase3(user):
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

            """Testcase steps"""
            self.validate_home_page_is_visible_successfully()
            self.click_menu_items("Signup / Login")
            self.validate_home_page_is_visible_successfully()
            self.enter_email("domain@gmail.com", "login")
            self.enter_password("admin")
            self.submit_button("Login")
            self.validate_Your_email_or_password_is_incorrect_is_visible()

        except Exception as exp:
            print(f"Error during Test Execution:{exp}")

        finally:
            self.driver.quit()

if __name__ == "__main__":
    testcase = Testcase3()
    testcase.execute_testcase()

