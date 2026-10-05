from maintestcase import user
from selenium import webdriver
import traceback
"""
1. Launch browser
2. Navigate to url 'http://automationexercise.com'
3. Verify that home page is visible successfully
4. Click on 'Products' button
5. Verify user is navigated to ALL PRODUCTS page successfully
6. Enter product name in search input and click search button
7. Verify 'SEARCHED PRODUCTS' is visible
8. Verify all the products related to search are visible
"""

class Testcase9(user):
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
            self.click_menu_items('Products')
            self.verify_headline_is_displayed('All Products')
            self.search_bar('Stylish Dress')
            self.scroll_down(500)
            self.verify_headline_is_displayed('Searched Products')
            self.validate_searched_products('Stylish')

        except Exception as exp:
            print(f"Error during test execution: {exp}")
            traceback.print_exc()

        finally:
            self.driver.quit()

if __name__ == "__main__":
    testcase = Testcase9()
    testcase.execute_testcase()






















# from selenium import webdriver
# import time
# from selenium.webdriver.common.alert import Alert
# from selenium.webdriver.common.by import By
#
# search_product = "Blue Tshirt"
#
# driver = webdriver.Chrome()
# driver.get("http://automationexercise.com")
# home = driver.find_element(By.XPATH, "//a/img[@alt='Website for automation practice']")
# if home.is_displayed():
#     print('Home page is visible')
# else:
#     print("Home is not visible")
# driver.find_element(By.XPATH, "//a/i[@class='material-icons card_travel']").click()
# products = driver.find_element(By.XPATH, "//div/h2[@class='title text-center']")
# if products.is_displayed():
#     print("All Products is visible")
# else:
#     print("All Products is not visible")
# driver.find_element(By.XPATH, "//input[@id = 'search_product']").send_keys(search_product)
# driver.find_element(By.XPATH,"//button[@id = 'submit_search']").click()
# # time.sleep(5)
# # search = driver.find_element(By.XPATH, "//div[@class='single-products']")
# # if search.is_displayed():
# #     print("search product is visible")
# # else:
# #     print("search product is not visible")
#
# #last step is doubt