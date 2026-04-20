from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators
from selenium.webdriver.common.by import By
import allure

class OrderPage(BasePage):

    @allure.step("Заполнить персональные данные")
    def fill_personal_info(self, name, lastname, address, phone):
        self.type(OrderPageLocators.NAME, name)
        self.type(OrderPageLocators.LASTNAME, lastname)
        self.type(OrderPageLocators.ADDRESS, address)

        self.select_metro()
        self.type(OrderPageLocators.PHONE, phone)

    @allure.step("Выбрать метро")
    def select_metro(self):
        self.click(OrderPageLocators.METRO)

        first_option = (By.CSS_SELECTOR, ".select-search__option")
        self.wait_clickable(first_option)
        options = self.find_elements(first_option)
        options[0].click()

    @allure.step("Нажать Далее")
    def click_next(self):
        self.click(OrderPageLocators.NEXT_BUTTON)

    @allure.step("Выбрать дату доставки")
    def select_date(self):
        self.type(OrderPageLocators.DATE_INPUT, "31.01.2999")
        self.click((By.CSS_SELECTOR, ".App_App__15LM-"))

    @allure.step("Выбрать срок аренды")
    def select_rent_period(self):
        self.click(OrderPageLocators.RENT_DROPDOWN)
        option = (By.CSS_SELECTOR, ".Dropdown-option")
        self.wait_visible(option)

        options = self.find_elements(option)
        options[0].click()
        self.click((By.CSS_SELECTOR, ".App_App__15LM-"))

    @allure.step("Выбрать цвет")
    def select_color(self):
        option = (By.CSS_SELECTOR, "label.Checkbox_Label__3wxSf")
        self.click(option)

    @allure.step("Нажать заказать")
    def click_order(self):
        self.click(OrderPageLocators.ORDER_BUTTON)

    @allure.step("Подтвердить заказ")
    def confirm_order(self):
        self.click(OrderPageLocators.CONFIRM_BUTTON)

    @allure.step("Получить текст подтверждения")
    def get_confirm_text(self):
        return self.get_text(OrderPageLocators.CONFIRM_TEXT)
    
    @allure.step("Ожидание модалки успешности заказа")
    def wait_success_modal(self):
        self.wait_visible(OrderPageLocators.SUCCESS_HEADER)
        
    @allure.step("Получить текст успешности заказа")
    def get_success_text(self):
        return self.get_text(OrderPageLocators.SUCCESS_HEADER)
    
    @allure.step("Обновить страницу")
    def refresh_page(self):
        self.refresh_page()