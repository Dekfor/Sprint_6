from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):

    def click_order_header(self):
        self.click(MainPageLocators.ORDER_BUTTON_HEADER)

    def click_order_footer(self):
        self.click(MainPageLocators.ORDER_BUTTON_FOOTER)

    def click_scooter_logo(self):
        self.click(MainPageLocators.SCOOTER_LOGO)

    def click_yandex_logo(self):
        self.click(MainPageLocators.YANDEX_LOGO)

    def close_cookie(self):
        try:
            self.click(MainPageLocators.COOKIE_BUTTON)
        except:
            pass