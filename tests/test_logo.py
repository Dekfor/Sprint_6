from pages.main_page import MainPage
import allure


@allure.feature("Логотипы")
@allure.story("Переходы по логотипам")
class TestLogo:

    @allure.title("Переход по логотипу Самоката на главную страницу")
    @allure.step("Тест перехода по логотипу Самоката")
    def test_scooter_logo(self, driver):
        main = MainPage(driver)

        main.click_scooter_logo()

        assert "qa-scooter" in main.get_current_url()

    @allure.title("Переход по логотипу Яндекса в Дзен")
    @allure.step("Тест перехода по логотипу Яндекса")
    def test_yandex_logo(self, driver):
        main = MainPage(driver)

        main.click_yandex_logo()
        main.switch_to_last_tab()
        main.wait_url_contains("dzen")

        assert "dzen" in main.get_current_url().lower()