import time

from maintestcase import user
from selenium import webdriver

"""
1. Launch browser
2. Navigate to url 'http://automationexercise.com'
3. Verify that home page is visible successfully
4. Click 'Products' button
5. Hover over first product and click 'Add to cart'
6. Click 'Continue Shopping' button
7. Hover over second product and click 'Add to cart'
8. Click 'View Cart' button
9. Verify both products are added to Cart
10. Verify their prices, quantity and total price
"""

class Testcase12(user):
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
            self.click_menu_items('Products')
            time.sleep(5)
            self.scroll_down(500)
            self.add_to_cart(1)
            self.submit_button('Continue Shopping')
            self.add_to_cart(2)
            self.submit_button('Continue Shopping')
            self.click_menu_items('Cart')
            products=self.get_cart_details()
            if products:
                print(products)
            else:
                print("products are not found")

        except Exception as exp:
            print(f"Error during test execution: {exp}")

        finally:
            self.driver.quit()

if __name__=="__main__":
    testcase = Testcase12()
    testcase.execute_testcase()



