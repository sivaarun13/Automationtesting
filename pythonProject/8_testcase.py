from maintestcase import user
from selenium import webdriver

"""
1. Launch browser
2. Navigate to url 'http://automationexercise.com'
3. Verify that home page is visible successfully
4. Click on 'Products' button
5. Verify user is navigated to ALL PRODUCTS page successfully
6. The products list is visible
7. Click on 'View Product' of first product
8. User is landed to product detail page
9. Verify that detail detail is visible: product name, category, price, availability, condition, brand
"""

class Testcase8(user):
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

            """Testcase steps"""
            self.validate_home_page_is_visible_successfully()
            self.click_menu_items('Products')
            self.verify_headline_is_displayed('All Products')
            self.scroll_down(1000)
            self.click_product(1)
            details = self.get_product_details()
            if details:
                print(details)
            else:
                print("failed to retrieve product details ")


        except Exception as exp:
            print(f"Error during Test Execution:{exp}")

        finally:
            self.driver.quit()

if __name__ == "__main__":
    testcase = Testcase8()
    testcase.execute_testcase()


























# from selenium import webdriver
# import time
# from selenium.webdriver.common.alert import Alert
# from selenium.webdriver.common.by import By
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
# driver.find_element(By.XPATH, "//a[@href='/product_details/1']").click()
#
# product_name = driver.find_element(By.XPATH, "//h2[text()='Blue Top']")
# category = driver.find_element(By.XPATH,"//p[text()='Category: Women > Tops']")
# price = driver.find_element(By.XPATH,"//span[text()='Rs. 500']")
# Availability = driver.find_element(By.XPATH,"//p[contains(text(), 'In Stock')]")
# condition = driver.find_element(By.XPATH,"//p[contains(text(), 'New')]")
# Brand = driver.find_element(By.XPATH,"//p[contains(text(), 'Polo')]")
#
# if product_name.is_displayed():
#     print("Blue Top")
# else:
#     print("Error")
# if category.is_displayed():
#     print("Women > Tops")
# else:
#     print("error")
# if price.is_displayed():
#     print("Rs. 500")
# else:
#     print("error")
# if Availability.is_displayed():
#     print("In Stock")
# else:
#     print("error")
# if condition.is_displayed():
#     print("New")
# else:
#     print("error")
# if Brand.is_displayed():
#     print("polo")
# else:
#     print("error")