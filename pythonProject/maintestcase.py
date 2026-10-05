from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


class user:

    def __init__(self, driver):
        self.driver = driver

    def wait_for_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def validate_home_page_is_visible_successfully(self):
        locator = (By.XPATH, "//a/img[@alt='Website for automation practice']")
        home = self.wait_for_element(locator)
        if home.is_displayed():
            print("Home page was successfully displayed")
        else:
            print("Home page was not displayed")

    def click_menu_items(self, menu_items):
        locator = (By.XPATH, f"//a[contains(.,'{menu_items}')]")
        self.wait_for_element(locator)
        self.driver.find_element(*locator).click()

    def enter_name(self, name):
        locator = (By.XPATH, f"//input[@name='name']")
        self.wait_for_element(locator)
        self.driver.find_element(*locator).send_keys(name)

    def enter_email(self, email, email_type):
        locator = (By.XPATH,f"//input[@data-qa='{email_type}-email']")
        self.wait_for_element(locator)
        self.driver.find_element(*locator).send_keys(email)

    def enter_password(self, password):
        locator = (By.NAME, "password")

        self.wait_for_element(locator)
        self.driver.find_element(*locator).send_keys(password)

    def Day_Month_year(self, days, months, years):
        day_locator = (By.NAME, "days")
        month_locator = (By.NAME, "months")
        year_locator = (By.NAME, "years")
        Select(
            self.wait_for_element(day_locator)
        ).select_by_visible_text(days)

        Select(
            self.wait_for_element(month_locator)
        ).select_by_visible_text(months)

        Select(
            self.wait_for_element(year_locator)
        ).select_by_visible_text(years)

    def scroll_down(self, pixels=500):
        self.driver.execute_script(
            f"window.scrollBy(0, {pixels});"
        )
    def Checkbox(self, name):
        locator = (By.XPATH, f"//input[@name='{name}']")
        self.wait_for_element(locator)
        element = self.driver.find_element(*locator)
        if not element.is_selected():
            element.click()

    def enter_details(
        self,
        first_name,
        last_name,
        company,
        address,
        address_2,
        country,
        state,
        city,
        zipcode,
        mobile_number
    ):

        locator = (By.NAME, "first_name")
        self.wait_for_element(locator).send_keys(first_name)

        locator = (By.NAME, "last_name")
        self.wait_for_element(locator).send_keys(last_name)

        locator = (By.NAME, "company")
        self.wait_for_element(locator).send_keys(company)

        locator = (By.NAME, "address1")
        self.wait_for_element(locator).send_keys(address)

        locator = (By.NAME, "address2")
        self.wait_for_element(locator).send_keys(address_2)

        locator = (By.NAME, "country")
        Select(
            self.wait_for_element(locator)
        ).select_by_visible_text(country)

        locator = (By.NAME, "state")
        self.wait_for_element(locator).send_keys(state)

        locator = (By.NAME, "city")
        self.wait_for_element(locator).send_keys(city)

        locator = (By.NAME, "zipcode")
        self.wait_for_element(locator).send_keys(zipcode)

        locator = (By.NAME, "mobile_number")
        self.wait_for_element(locator).send_keys(mobile_number)


    def submit_button(self, submit_button):
        locator = (By.XPATH, f"//button[contains(text(),'{submit_button}')]")
        self.wait_for_element(locator)
        self.driver.find_element(*locator).click()

    def radio_button(self, radio):
        locator = (By.XPATH, f"//input[@value='{radio}']")
        self.wait_for_element(locator)
        self.driver.find_element(*locator).click()

    def verify_headline_is_displayed(self, headline):
        locator = (By.XPATH,f"//h2[contains(.,'{headline}')]")
        element = self.wait_for_element(locator)
        if element.is_displayed():
            print(f"{headline} was successfully displayed")
        else:
            print(f"{headline} was not displayed")

    def click_continue(self):
        locator = (By.XPATH,"//a[contains(text(),'Continue')]")
        self.wait_for_element(locator)
        self.driver.find_element(*locator).click()

    def validate_logged_in_as_username(self, user_name):
        locator = (By.XPATH, f"//a/b[contains(text(),'{user_name}')]")
        element = self.wait_for_element(locator)
        if element.is_displayed():
            print(f"Username {user_name} was successfully validated")
        else:
            print(f"Username {user_name} was not validated")

    # def enter_login_email(self, email):
    #     locator = (By.XPATH, "//input[@data-qa='login-email']")
    #     self.wait_for_element(locator)
    #     self.driver.find_element(*locator).send_keys(email)

    def validate_Your_email_or_password_is_incorrect_is_visible(self):
        locator = (By.XPATH, "//p[contains(text(),'Your email or password is incorrect!')]")
        element = self.wait_for_element(locator)
        if element.is_displayed():
            print(f"Email or password is incorrect is visible")
        else:
            print(f"Email or password is incorrect is not visible")

    def validate_email_address_already_exists(self):
        locator = (By.XPATH, "//p[contains(text(),'Email Address already exist!')]")
        element = self.wait_for_element(locator)
        if element.is_displayed():
            print(f"Email Address already exist! is visible")
        else:
            print(f"Email Address already exist! is not visible")

    def enter_subject(self, subject):
        locator = (By.XPATH, f"//input[@data-qa='subject']")
        self.wait_for_element(locator)
        self.driver.find_element(*locator).send_keys(subject)

    def enter_message(self, message):
        locator = (By.XPATH, f"//textarea[@name='message']")
        self.wait_for_element(locator)
        self.driver.find_element(*locator).send_keys(message)

    def upload_file(self, file_path):
        locator = (By.XPATH, "//input[@type='file' and @name='upload_file']")
        self.wait_for_element(locator)
        self.driver.find_element(*locator).send_keys(file_path)

    def input_submit(self):
        locator = (By.XPATH, "//input[@name='submit']")
        self.wait_for_element(locator)
        self.driver.find_element(*locator).click()

    def click_alert(self):
        alert = WebDriverWait(self.driver, 5).until(EC.alert_is_present())
        print("Alert message:", alert.text)
        alert.accept()
        print("Alert accepted")

    def validate_success_message(self):
        locator = (By.XPATH, "//div[contains(text(),'Success! Your details have been submitted successfully.')]")
        element = self.wait_for_element(locator)
        if element.is_displayed():
            print(f"Success message was successfully displayed")
        else:
            print(f"Success message was not displayed")

    def click_home(self):
        locator = (By.XPATH, "//a[@class='btn btn-success']")
        self.wait_for_element(locator)
        self.driver.find_element(*locator).click()

    def enter_contact_email(self, email):
        locator = (By.XPATH, "//input[@data-qa='email']")
        self.wait_for_element(locator)
        self.driver.find_element(*locator).send_keys(email)

    def click_product(self,product_number):
        locator = (By.XPATH, f"//a[@href = '/product_details/{product_number}']")
        self.wait_for_element(locator)
        self.driver.find_element(*locator).click()

    def get_product_details(self):

        product_name = self.wait_for_element(
            (By.XPATH, "//div[@class='product-information']//h2")
        ).text

        category = self.wait_for_element(
            (By.XPATH, "//div[@class='product-information']//p[contains(text(),'Category:')]")
        ).text

        price = self.wait_for_element(
            (By.XPATH, "//div[@class='product-information']//span[contains(text(),'Rs.')]")
        ).text

        availability = self.wait_for_element(
            (By.XPATH, "//div[@class='product-information']//p[.//b[contains(text(),'Availability:')]]")
        ).text

        condition = self.wait_for_element(
            (By.XPATH, "//div[@class='product-information']//p[.//b[contains(text(),'Condition:')]]")
        ).text

        brand = self.wait_for_element(
            (By.XPATH, "//div[@class='product-information']//p[.//b[contains(text(),'Brand:')]]")
        ).text

        return {
            "product_name": product_name,
            "category": category,
            "price": price,
            "availability": availability,
            "condition": condition,
            "brand": brand
        }

    def search_bar(self, search):
        locator = (By.XPATH, "//input[@name='search']")
        self.wait_for_element(locator)
        self.driver.find_element(*locator).send_keys(search)
        locator = (By.XPATH, "//button[@id='submit_search']")
        self.wait_for_element(locator)
        self.driver.find_element(*locator).click()

    def validate_searched_products(self,product_name):
        locator = (By.XPATH, f"//div[@class='productinfo text-center']//p[contains(text(), '{product_name}')]")
        element= self.wait_for_element(locator)
        if element.is_displayed():
            print(f"Product {product_name} was successfully found")
        else:
            print(f"Product {product_name} was not found")

    def subscribe_email(self, susbscribe_email):
        locator = (By.XPATH, f"//input[@id='susbscribe_email']")
        self.wait_for_element(locator)
        self.driver.find_element(*locator).send_keys(susbscribe_email)

    def scroll_to_bottom(self):
        self.driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);")

    def validate_subscription_success(self):
        locator = (By.XPATH,"//*[contains(normalize-space(.), 'You have been successfully subscribed!')]")
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locator))

        if element.is_displayed():
            print("You have been successfully subscribed!")
            return True
        else:
            print("Subscription success message was not displayed")
            return False

    def add_to_cart(self, product_number):
        locator = (By.XPATH, f"(//a[@data-product-id='{product_number}' and contains(@class,'add-to-cart')])[1]")
        element = self.wait_for_element(locator)
        element.click()

    def get_cart_details(self):
        rows = self.driver.find_elements(
            By.XPATH,
            "//table[@id='cart_info_table']//tbody/tr"
        )

        cart_details = []

        for row in rows:
            product_name = row.find_element(
                By.XPATH, ".//td[contains(@class,'cart_description')]//a"
            ).text

            category = row.find_element(
                By.XPATH, ".//td[contains(@class,'cart_description')]//p"
            ).text

            price = row.find_element(
                By.XPATH, ".//td[contains(@class,'cart_price')]//p"
            ).text

            quantity = row.find_element(
                By.XPATH, ".//td[contains(@class,'cart_quantity')]//button"
            ).text

            total = row.find_element(
                By.XPATH, ".//td[contains(@class,'cart_total')]//p"
            ).text

            cart_details.append({
                "Product": product_name,
                "Category": category,
                "Price": price,
                "Quantity": quantity,
                "Total": total
            })

        return cart_details

    def quantity(self, value):
        locator = (By.XPATH, "//input[@name='quantity']")
        element = self.wait_for_element(locator)
        element.clear()
        self.driver.find_element(*locator).send_keys(value)

    def view_cart(self):
        locator = (By.XPATH, "//div[contains(@class,'modal-content')]//a[@href='/view_cart']")
        self.wait_for_element(locator)
        self.driver.find_element(*locator).click()

    def add_to_cart_submit(self):
        locator=(By.XPATH, "//button[@class='btn btn-default cart']")
        self.wait_for_element(locator)
        self.driver.find_element(*locator).click()

    def validate_cart_page(self):
        locator = (By.XPATH, "//li[contains(.,'Shopping Cart')]")
        element = self.wait_for_element(locator)
        if element.is_displayed():
            print(f"Shopping cart was successfully found")
        else:
            print(f"Shopping cart was not found")

    def proceed_to_checkout(self):
        locator = (By.XPATH, "//a[@class = 'btn btn-default check_out']")
        self.wait_for_element(locator)
        self.driver.find_element(*locator).click()

    def click_register(self):
        locator = (By.XPATH, "//div[contains(@class,'modal-content')]//a[@href='/login']")
        self.wait_for_element(locator)
        self.driver.find_element(*locator).click()

    def verify_address_details(self):
        delivery_locator = (By.XPATH, '//ul[@id="address_delivery"]')
        billing_locator = (By.XPATH, '//ul[@id="address_invoice"]')

        delivery_element = self.wait_for_element(delivery_locator)
        billing_element = self.wait_for_element(billing_locator)

        delivery_address = delivery_element.text
        billing_address = billing_element.text

        print("DELIVERY ADDRESS:")
        print(delivery_address)

        print("\nBILLING ADDRESS:")
        print(billing_address)

        return delivery_address, billing_address

    def card_details(self, name_on_card, card_number, cvc, month, year):
        locator = (By.XPATH, f"//input[@name = 'name_on_card']")
        self.wait_for_element(locator)
        self.driver.find_element(*locator).send_keys(name_on_card)

        locator = (By.XPATH, f"//input[@data-qa='card-number']")
        self.wait_for_element(locator)
        self.driver.find_element(*locator).send_keys(card_number)

        locator = (By.XPATH, f"//input[@name='cvc']")
        self.wait_for_element(locator)
        self.driver.find_element(*locator).send_keys(cvc)

        locator = (By.XPATH, f"//input[@name='expiry_month']")
        self.wait_for_element(locator)
        self.driver.find_element(*locator).send_keys(month)

        locator = (By.XPATH, f"//input[@name='expiry_year']")
        self.wait_for_element(locator)
        self.driver.find_element(*locator).send_keys(year)

    def remove_product_from_cart(self, value):
        locator = (By.XPATH, f"//a[@data-product-id='{value}']")
        self.wait_for_element(locator)
        self.driver.find_element(*locator).click()

    def validate_cart_is_empty(self):
        locator = (By.XPATH, "//div[@id = 'cart_info']//b[contains(text(),'Cart is empty!')]")
        cart = self.wait_for_element(locator)
        if cart.is_displayed():
            print(f"cart is empty")
        else:
            print(f"cart is not empty")

    def click_category(self, gender, category):
        locator = (By.XPATH, f"//h4[@class='panel-title']//a[contains(normalize-space(.),'{gender}')]//i[contains(@class,'fa-plus')]")
        self.wait_for_element(locator)
        self.driver.find_element(*locator).click()
        locator = (By.XPATH, f"//div[@id='{gender}']//a[contains(normalize-space(.),'{category}')]")
        self.wait_for_element(locator)
        self.driver.find_element(*locator).click()

    def select_brand(self, brand):
        locator = (By.XPATH, f"//div[@class='brands-name']//a[@href='/brand_products/{brand}']")
        self.wait_for_element(locator)
        self.driver.find_element(*locator).click()

    def validate_brand_products_displayed(self, brand):
        loactor = (By.XPATH, f"//h2[contains(@class,'title') and contains(.,'{brand}')]")
        element=self.wait_for_element(loactor)
        if element.is_displayed():
            print(f"brand {brand} products displayed")
        else:
            print(f"brand {brand} products not displayed")

    def validate_write_your_review_is_visible(self):
        locator = (By.XPATH, '//div[@class="col-sm-12"]//a[@href="#reviews"]')
        element = self.wait_for_element(locator)
        if element.is_displayed():
            print("Write your review is visible")
        else:
            print("Write your review is not visible")

    def enter_review_details(self, name, email, review):
        locator = (By.XPATH, f'//input[@id="name"]')
        self.wait_for_element(locator)
        self.driver.find_element(*locator).send_keys(name)

        locator = (By.XPATH, f'//input[@id="email"]')
        self.wait_for_element(locator)
        self.driver.find_element(*locator).send_keys(email)

        locator = (By.XPATH, f'//textarea[@name="review"]')
        self.wait_for_element(locator)
        self.driver.find_element(*locator).send_keys(review)

    def validate_address_billing_details_and_review_order(self):
        delivery_locator = (By.XPATH, "//ul[@id='address_delivery']")
        billing_locator = (By.XPATH, "//ul[@id='address_invoice']")

        delivery_address = self.wait_for_element(delivery_locator).text
        billing_address = self.wait_for_element(billing_locator).text

        return {
            "delivery_address": delivery_address,
            "billing_address": billing_address
        }

    def download_invoice(self):
        locator = (By.XPATH, "//a[contains(text(),'Download Invoice')]")
        self.wait_for_element(locator)
        self.driver.find_element(*locator).click()

    def click_arrow_button(self):
        locator = (By.XPATH, "//a[@id='scrollUp']")
        self.wait_for_element(locator)
        self.driver.find_element(*locator).click()