
from maintestcase import user
from selenium import webdriver

"""
1. Launch browser
2. Navigate to url 'http://automationexercise.com'
3. Click on 'Products' button
4. Verify user is navigated to ALL PRODUCTS page successfully
5. Enter product name in search input and click search button
6. Verify 'SEARCHED PRODUCTS' is visible
7. Verify all the products related to search are visible
8. Add those products to cart
9. Click 'Cart' button and verify that products are visible in cart
10. Click 'Signup / Login' button and submit login details
11. Again, go to Cart page
12. Verify that those products are visible in cart after login as well
"""

class Testcase20(user):
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
            self.verify_headline_is_displayed('All Products')
            self.search_bar('winter top')
            self.verify_headline_is_displayed('Searched Products')
            self.scroll_down(500)
            self.add_to_cart(5)
            self.view_cart()
            products = self.get_cart_details()
            if products:
                print(products)
            else:
                print("products are not found")
            self.click_menu_items('Signup / Login')
            self.enter_email("ADMIN131120@gmail.com", "login")
            self.enter_password('Domain@123')
            self.click_menu_items('Cart')
            self.get_cart_details()
            products = self.get_cart_details()
            if products:
                print(products)
            else:
                print("products are not found")

        except Exception as exp:
            print(f'Error During Test Execution:{exp}')

        finally:
            self.driver.quit()

if __name__ == '__main__':
    testcase = Testcase20()
    testcase.execute_testcase()
