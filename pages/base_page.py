from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def wait_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def wait_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))
    
    def click(self, locator):
        self.wait_clickable(locator).click()
    
    def scroll_to(self, element):
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            element
    )

    def get_text(self, locator):
        return self.wait_visible(locator).text
    
    def type(self, locator, text):
        element = self.wait_visible(locator)
        element.clear()
        element.send_keys(text)
        
    def get_current_url(self):
        return self.driver.current_url

    def switch_to_last_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])

    def refresh(self):
        self.driver.refresh()

    def find_elements(self, locator):
        return self.driver.find_elements(*locator)
        