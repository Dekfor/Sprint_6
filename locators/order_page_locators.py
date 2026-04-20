from selenium.webdriver.common.by import By


class OrderPageLocators:

    NAME = (By.XPATH, "//input[@placeholder='* Имя']")
    LASTNAME = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO = (By.CLASS_NAME, "select-search__input")
    PHONE = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")

    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")
    DATE_INPUT = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    RENT_DROPDOWN = (By.CLASS_NAME, "Dropdown-control")

    ORDER_BUTTON = (By.XPATH, "//button[contains(@class,'Button_Middle') and contains(text(),'Заказать')]")
    CONFIRM_BUTTON = (By.XPATH, "//button[text()='Да']")

    CONFIRM_TEXT = (By.XPATH, "//div[contains(@class,'Order_ModalHeader')]")
    SUCCESS_HEADER = (By.CLASS_NAME, "Order_ModalHeader__3FDaJ")
