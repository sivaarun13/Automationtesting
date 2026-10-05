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
5. Verify 'New User Signup!' is visible
6. Enter name and email address
7. Click 'Signup' button
8. Verify that 'ENTER ACCOUNT INFORMATION' is visible
9. Fill details: Title, Name, Email, Password, Date of birth
10. Select checkbox 'Sign up for our newsletter!'
11. Select checkbox 'Receive special offers from our partners!'
12. Fill details: First name, Last name, Company, Address, Address2, Country, State, City, Zipcode, Mobile Number
13. Click 'Create Account button'
14. Verify that 'ACCOUNT CREATED!' is visible
15. Click 'Continue' button
16. Verify that 'Logged in as username' is visible
17. Click 'Delete Account' button
18. Verify that 'ACCOUNT DELETED!' is visible and click 'Continue' button
"""

# class Testcase1(user, Alert):
#     def execute_testcase(self):
class Testcase1(user):

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

            """Test case steps"""
            self.validate_home_page_is_visible_successfully()
            self.click_menu_items("Signup / Login")
            self.enter_name("Domain")
            self.enter_email("ADMIN131120@gmail.com", "signup")
            self.submit_button("Signup")
            self.verify_headline_is_displayed("Enter Account Information")
            self.radio_button("Mr")
            self.enter_password("Domain")
            self.scroll_down(500)
            self.Day_Month_year("13", "November", "2000")
            self.scroll_down(500)
            self.Checkbox("newsletter")
            self.scroll_down(700)
            self.enter_details(
                "Domain",
                "Admin",
                "Admin",
                "1234",
                "1234",
                "India",
                "Karnataka",
                "Bangalore",
                "12345",
                "76217392839"
            )
            self.scroll_down(500)
            self.submit_button("Create Account")
            self.verify_headline_is_displayed("Account Created")
            self.click_continue()
            self.validate_logged_in_as_username("Domain")
            # self.click_menu_items("Delete Account")
            # self.verify_headline_is_displayed("Account Deleted")
            # self.click_continue()




        except Exception as exp:
            print(f"Error during test execution: {exp}")

        finally:
            # Ensure browser is closed
            self.driver.quit()


# Run the test case
if __name__ == "__main__":
    testcase = Testcase1()
    testcase.execute_testcase()
