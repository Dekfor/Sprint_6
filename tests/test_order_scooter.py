import allure
from pages.main_page import MainPage
from pages.order_page import OrderPage

@allure.feature("Заказ самоката")
@allure.story("Полный флоу заказа")
class TestOrderFlow:

    @allure.title("Заказ самоката через хедер")
    def test_order_from_header(self, driver):

        main = MainPage(driver)
        main.close_cookie()
        order = OrderPage(driver)

        main.click_order_header()

        order.fill_personal_info(
            "Дмитрий", "Тестович", "Москва", "89999999999"
        )
        order.click_next()

        order.select_date()
        order.select_rent_period()
        order.select_color()

        order.click_order()
        assert "Хотите оформить заказ" in order.get_confirm_text()

        order.confirm_order()
        order.wait_success_modal()
        assert "Заказ оформлен" in order.get_success_text()


    @allure.title("Заказ самоката через футер")
    def test_order_from_footer(self, driver):

        main = MainPage(driver)
        main.close_cookie()
        order = OrderPage(driver)

        main.click_order_footer()

        order.fill_personal_info(
            "Алексей", "Петров", "Подольск", "88888888888"
        )
        order.click_next()

        order.select_date()
        order.select_rent_period()
        order.select_color()

        order.click_order()
        assert "Хотите оформить заказ" in order.get_confirm_text()

        order.confirm_order()
        order.wait_success_modal()
        assert "Заказ оформлен" in order.get_success_text()
        