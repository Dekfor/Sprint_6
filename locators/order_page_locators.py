from selenium.webdriver.common.by import By


class OrderPageLocators:

    NAME = (By.XPATH, "//input[@placeholder='* Имя']")
    LASTNAME = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO = (By.CLASS_NAME, "select-search__input")
    METRO_FIRST_OPTION = (By.CSS_SELECTOR, ".select-search__option")
    PHONE = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")

    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")

    DATE_INPUT = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    RENT_DROPDOWN = (By.CLASS_NAME, "Dropdown-control")
    RENT_OPTION = (By.CSS_SELECTOR, ".Dropdown-option")
    COLOR_OPTION = (By.CSS_SELECTOR, "label.Checkbox_Label__3wxSf")

    ORDER_BUTTON = (By.XPATH, "//button[contains(@class,'Button_Middle') and contains(text(),'Заказать')]")
    CONFIRM_BUTTON = (By.XPATH, "//button[text()='Да']")

    CONFIRM_TEXT = (By.XPATH, "//div[contains(@class,'Order_ModalHeader')]")
    SUCCESS_HEADER = (By.CLASS_NAME, "Order_ModalHeader__3FDaJ")

    BACKGROUND = (By.CSS_SELECTOR, ".App_App__15LM-")
