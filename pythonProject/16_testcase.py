from maintestcase import user
from selenium import webdriver

"""
1. Launch browser
2. Navigate to url 'http://automationexercise.com'
3. Verify that home page is visible successfully
4. Click 'Signup / Login' button
5. Fill email, password and click 'Login' button
6. Verify 'Logged in as username' at top
7. Add products to cart
8. Click 'Cart' button
9. Verify that cart page is displayed
10. Click Proceed To Checkout
11. Verify Address Details and Review Your Order
12. Enter description in comment text area and click 'Place Order'
13. Enter payment details: Name on Card, Card Number, CVC, Expiration date
14. Click 'Pay and Confirm Order' button
15. Verify success message 'Your order has been placed successfully!'
16. Click 'Delete Account' button
17. Verify 'ACCOUNT DELETED!' and click 'Continue' button
"""

class Testcase16(user):
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
            self.click_menu_items('Signup / Login')
            self.enter_email("ADMIN131120@gmail.com", 'login')
            self.enter_password('Domain')
            self.submit_button('Login')
            self.validate_logged_in_as_username("Domain")
            self.scroll_down(700)
            self.add_to_cart(1)
            self.submit_button('Continue Shopping')
            self.add_to_cart(2)
            self.submit_button('Continue Shopping')
            self.click_menu_items('Cart')
            self.validate_cart_page()
            self.proceed_to_checkout()
            delivery_address, billing_address = self.verify_address_details()

            print("DELIVERY ADDRESS:")
            print(delivery_address)

            print("\nBILLING ADDRESS:")
            print(billing_address)
            self.scroll_down(200)
            self.enter_message('Hi')
            self.proceed_to_checkout()
            self.card_details('Arun', '82545300245', '525', '07', '2052')
            self.submit_button('Pay and Confirm Order')
            self.click_continue()
            self.click_menu_items('Delete Account')
            self.verify_headline_is_displayed("Account Deleted")
            self.click_continue()

        except Exception as exp:
            print(f"Error during test execution: {exp}")

        finally:
            self.driver.quit()

if __name__ == "__main__":
    testcase = Testcase16()
    testcase.execute_testcase()
