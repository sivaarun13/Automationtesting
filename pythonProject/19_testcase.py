from maintestcase import user
from selenium import webdriver

"""1. Launch browser
2. Navigate to url 'http://automationexercise.com'
3. Click on 'Products' button
4. Verify that Brands are visible on left side bar
5. Click on any brand name
6. Verify that user is navigated to brand page and brand products are displayed
7. On left side bar, click on any other brand link
8. Verify that user is navigated to that brand page and can see products
"""

class Testcase19(user):
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
            self.scroll_down(500)
            self.verify_headline_is_displayed('Brands')
            self.select_brand('H&M')
            self.validate_brand_products_displayed('H&M')
            self.select_brand('Polo')
            self.validate_brand_products_displayed('Polo')

        except Exception as exp:
            print(f"Error during test execution: {exp}")

        finally:
            self.driver.quit()

if __name__=='__main__':
    testcase = Testcase19()
    testcase.execute_testcase()
