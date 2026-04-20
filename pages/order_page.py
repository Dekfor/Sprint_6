from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators
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
        self.wait_clickable(OrderPageLocators.METRO_FIRST_OPTION)
        self.click(OrderPageLocators.METRO_FIRST_OPTION)

    @allure.step("Нажать Далее")
    def click_next(self):
        self.click(OrderPageLocators.NEXT_BUTTON)

    @allure.step("Выбрать дату доставки")
    def select_date(self):
        self.type(OrderPageLocators.DATE_INPUT, "31.01.2999")
        self.click(OrderPageLocators.BACKGROUND)

    @allure.step("Выбрать срок аренды")
    def select_rent_period(self):
        self.click(OrderPageLocators.RENT_DROPDOWN)
        self.wait_visible(OrderPageLocators.RENT_OPTION)
        self.click(OrderPageLocators.RENT_OPTION)

        self.click(OrderPageLocators.BACKGROUND)

    @allure.step("Выбрать цвет")
    def select_color(self):
        self.click(OrderPageLocators.COLOR_OPTION)

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