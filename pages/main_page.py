from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
import allure


class MainPage(BasePage):

    @allure.step("Нажать верхнюю кнопку Заказать")
    def click_order_header(self):
        self.click(MainPageLocators.ORDER_BUTTON_HEADER)

    @allure.step("Нажать нижнюю кнопку Заказать")
    def click_order_footer(self):
        self.click(MainPageLocators.ORDER_BUTTON_FOOTER)

    @allure.step("Клик по лого Самоката")
    def click_scooter_logo(self):
        self.click(MainPageLocators.SCOOTER_LOGO)

    @allure.step("Клик по лого Яндекса")
    def click_yandex_logo(self):
        self.click(MainPageLocators.YANDEX_LOGO)

    @allure.step("Закрыть модалку cookie")
    def close_cookie(self):
        try:
            self.click(MainPageLocators.COOKIE_BUTTON)
        except:
            pass