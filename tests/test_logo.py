from pages.main_page import MainPage
import allure, time


@allure.feature("Логотипы")
@allure.story("Переходы по логотипам")
class TestLogo:

    @allure.title("Переход по логотипу Самоката на главную страницу")
    @allure.step("Тест перехода по логотипу Самоката")
    def test_scooter_logo(self, driver):
        main = MainPage(driver)

        main.click_scooter_logo()

        assert "qa-scooter" in driver.current_url

    @allure.title("Переход по логотипу Яндекса в Дзен")
    @allure.step("Тест перехода по логотипу Яндекса")
    def test_yandex_logo(self, driver):
        main = MainPage(driver)

        main.click_yandex_logo()

        time.sleep(2)

        driver.switch_to.window(driver.window_handles[-1])

        time.sleep(2)

        assert "dzen" in driver.current_url.lower()