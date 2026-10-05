from maintestcase import user
from selenium import webdriver

"""1. Launch browser
2. Navigate to url 'http://automationexercise.com'
3. Click on 'Products' button
4. Verify user is navigated to ALL PRODUCTS page successfully
5. Click on 'View Product' button
6. Verify 'Write Your Review' is visible
7. Enter name, email and review
8. Click 'Submit' button
9. Verify success message 'Thank you for your review.'
"""

class Testcase21(user):
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
            self.scroll_down(500)
            self.click_product(2)
            self.scroll_down(500)
            self.validate_write_your_review_is_visible()
            self.scroll_down(500)
            self.enter_review_details('Domain', 'Domain@gmail.com', 'hi')
            self.scroll_down(200)
            self.submit_button('Submit')

        except Exception as exp:
            print(f'Error During test execution{exp}')

        finally:
            self.driver.quit()

if __name__ == '__main__':
    testcase = Testcase21()
    testcase.execute_testcase()