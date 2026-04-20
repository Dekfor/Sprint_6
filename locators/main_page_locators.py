from selenium.webdriver.common.by import By


class MainPageLocators:

    ORDER_BUTTON_HEADER = (By.XPATH, "//button[text()='Заказать']")
    ORDER_BUTTON_FOOTER = (By.XPATH, "(//button[text()='Заказать'])[2]")
    SCOOTER_LOGO = (By.XPATH, "//a[contains(@class, 'Header_LogoScooter')]")
    YANDEX_LOGO = (By.XPATH, "//a[contains(@href, 'yandex')]")
    COOKIE_BUTTON = (By.ID, "rcc-confirm-button")