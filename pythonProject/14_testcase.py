from maintestcase import user
from selenium import webdriver

"""1. Launch browser
2. Navigate to url 'http://automationexercise.com'
3. Verify that home page is visible successfully
4. Add products to cart
5. Click 'Cart' button
6. Verify that cart page is displayed
7. Click Proceed To Checkout
8. Click 'Register / Login' button
9. Fill all details in Signup and create account
10. Verify 'ACCOUNT CREATED!' and click 'Continue' button
11. Verify ' Logged in as username' at top
12.Click 'Cart' button
13. Click 'Proceed To Checkout' button
14. Verify Address Details and Review Your Order
15. Enter description in comment text area and click 'Place Order'
16. Enter payment details: Name on Card, Card Number, CVC, Expiration date
17. Click 'Pay and Confirm Order' button
18. Verify success message 'Your order has been placed successfully!'
19. Click 'Delete Account' button
20. Verify 'ACCOUNT DELETED!' and click 'Continue' button
"""

class Testcase14(user):
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
            self.scroll_down(700)
            self.add_to_cart(1)
            self.submit_button('Continue Shopping')
            self.add_to_cart(2)
            self.submit_button('Continue Shopping')
            self.click_menu_items('Cart')
            self.validate_cart_page()
            self.proceed_to_checkout()
            self.click_register()
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
            self.click_menu_items('Cart')
            self.proceed_to_checkout()
            delivery_address, billing_address = self.verify_address_details()

            print("DELIVERY ADDRESS:")
            print(delivery_address)

            print("\nBILLING ADDRESS:")
            print(billing_address)
            self.scroll_down(200)
            self.enter_message('Hi')
            self.proceed_to_checkout()
            self.card_details('Domain', '82545300245', '525', '07', '2052')
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
    testcase = Testcase14()
    testcase.execute_testcase()

