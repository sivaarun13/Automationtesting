from maintestcase import user
from selenium import webdriver

"""1. Launch browser
2. Navigate to url 'http://automationexercise.com'
3. Verify that home page is visible successfully
4. Click 'Signup / Login' button
5. Fill all details in Signup and create account
6. Verify 'ACCOUNT CREATED!' and click 'Continue' button
7. Verify ' Logged in as username' at top
8. Add products to cart
9. Click 'Cart' button
10. Verify that cart page is displayed
11. Click Proceed To Checkout
12. Verify that the delivery address is same address filled at the time registration of account
13. Verify that the billing address is same address filled at the time registration of account
14. Click 'Delete Account' button
15. Verify 'ACCOUNT DELETED!' and click 'Continue' button
"""

class Testcase23(user):
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
            entered_details=self.enter_details(
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
            self.click_menu_items('Home')
            self.scroll_down(500)
            self.add_to_cart(1)
            self.view_cart()
            self.validate_cart_page()
            self.proceed_to_checkout()
            extracted_details = self.validate_address_billing_details_and_review_order()
            if entered_details == extracted_details:
                print('Address verification passed: Billing & Delivery details match!')
            else:
                print('Address verification failed: Mismatch found!')
            self.click_menu_items('Delete Account')
            self.click_continue()
            
        except Exception as exp:
            print(f"Error during test execution: {exp}")

        finally:
            self.driver.quit()


if __name__ == '__main__':
    testcase = Testcase23()
    testcase.execute_testcase()
