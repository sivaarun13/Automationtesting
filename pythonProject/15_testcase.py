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
12. Verify Address Details and Review Your Order
13. Enter description in comment text area and click 'Place Order'
14. Enter payment details: Name on Card, Card Number, CVC, Expiration date
15. Click 'Pay and Confirm Order' button
16. Verify success message 'Your order has been placed successfully!'
17. Click 'Delete Account' button
18. Verify 'ACCOUNT DELETED!' and click 'Continue' button
"""

class Testcase15(user):
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
            self.enter_name("Domain")
            self.enter_email("ADMIN131120@gmail.com", "signup")
            self.submit_button("Signup")
            self.radio_button("Mr")
            self.scroll_down(500)
            self.enter_password("Domain")
            self.Day_Month_year("23", "August", "2000")
            self.scroll_down(500)
            self.Checkbox("newsletter")
            self.enter_details(
                "Domain",
                "Admin",
                "Commvault",
                "Bangame Tech Park",
                "Tin Factory",
                "India",
                "Karnataka",
                "Bangalore",
                "561203",
                "8932487301283"
            )
            self.scroll_down(500)
            self.submit_button("Create Account")
            self.verify_headline_is_displayed("Account Created")
            self.click_continue()
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
            self.scroll_down(200)
            self.submit_button('Pay and Confirm Order')
            self.click_continue()
            self.click_menu_items('Delete Account')
            self.verify_headline_is_displayed("Account Deleted!")
            self.click_continue()

        except Exception as exp:
            print(f"Error during test execution: {exp}")

        finally:
            self.driver.quit()

if __name__ == "__main__":
    testcase = Testcase15()
    testcase.execute_testcase()
