import time
from maintestcase import user
from selenium import webdriver

"""
1. Launch browser
2. Navigate to url 'http://automationexercise.com'
3. Verify that home page is visible successfully
4. Click 'View Product' for any product on home page
5. Verify product detail is opened
6. Increase quantity to 4
7. Click 'Add to cart' button
8. Click 'View Cart' button
9. Verify that product is displayed in cart page with exact quantity
"""

class Testcase13(user):
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
            self.click_product(1)
            self.quantity(4)
            self.add_to_cart_submit()
            time.sleep(10)
            self.view_cart()
            products=self.get_cart_details()
            if products:
                print(products)
            else:
                print("No products found")

        except Exception as exp:
            print(f"Error during test execution: {exp}")

        finally:
            self.driver.quit()

if __name__=="__main__":
    testcase=Testcase13()
    testcase.execute_testcase()