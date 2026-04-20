from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators
from selenium.webdriver.common.by import By


class OrderPage(BasePage):

    def fill_personal_info(self, name, lastname, address, phone):
        self.type(OrderPageLocators.NAME, name)
        self.type(OrderPageLocators.LASTNAME, lastname)
        self.type(OrderPageLocators.ADDRESS, address)

        self.select_metro()
        self.type(OrderPageLocators.PHONE, phone)

    def select_metro(self):
        self.click(OrderPageLocators.METRO)

        first_option = (By.CSS_SELECTOR, ".select-search__option")
        self.wait_clickable(first_option)
        self.driver.find_elements(*first_option)[0].click()

    def click_next(self):
        self.click(OrderPageLocators.NEXT_BUTTON)

    def select_date(self):
        self.type(OrderPageLocators.DATE_INPUT, "31.01.2999")
        self.click((By.CSS_SELECTOR, ".App_App__15LM-"))

    def select_rent_period(self):
        self.click(OrderPageLocators.RENT_DROPDOWN)
        option = (By.CSS_SELECTOR, ".Dropdown-option")
        self.wait_visible(option)

        self.driver.find_elements(*option)[0].click()
        self.click((By.CSS_SELECTOR, ".App_App__15LM-"))

    def select_color(self):
        option = (By.CSS_SELECTOR, "label.Checkbox_Label__3wxSf")
        self.click(option)
        self.driver.implicitly_wait(0.5)

    def click_order(self):
        self.click(OrderPageLocators.ORDER_BUTTON)

    def confirm_order(self):
        self.click(OrderPageLocators.CONFIRM_BUTTON)

    def get_confirm_text(self):
        return self.get_text(OrderPageLocators.CONFIRM_TEXT)
    
    def wait_success_modal(self):
        self.wait_visible(OrderPageLocators.SUCCESS_HEADER)
        
    def get_success_text(self):
        return self.get_text(OrderPageLocators.SUCCESS_HEADER)
    
    def refresh_page(self):
        self.driver.refresh()