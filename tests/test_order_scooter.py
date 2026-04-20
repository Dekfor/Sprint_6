import pytest, allure
from pages.main_page import MainPage
from pages.order_page import OrderPage

@allure.feature("Заказ самоката")
@allure.story("Полный флоу заказа")
class TestOrderFlow:

    @allure.title("Позитивный сценарий заказа самоката")
    @pytest.mark.parametrize("entry, name, lastname, address, phone", [
        ("header", "Дмитрий", "Тестович", "Москва", "89999999999"),
        ("footer", "Алексей", "Петров", "Подольск", "88888888888")
    ])
    @allure.step("Проверка полного сценария заказа")
    def test_order_flow(self, driver, entry, name, lastname, address, phone):

        main = MainPage(driver)
        main.close_cookie()
        order = OrderPage(driver)

        if entry == "header":
            main.click_order_header()
        else:
            main.click_order_footer()

        order.fill_personal_info(name, lastname, address, phone)
        order.click_next()

        order.select_date()
        order.select_rent_period()
        order.select_color()


        order.click_order()
        assert "Хотите оформить заказ" in order.get_confirm_text()

        order.confirm_order()
        order.wait_success_modal()
        assert "Заказ оформлен" in order.get_success_text()