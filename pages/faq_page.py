from pages.base_page import BasePage
from locators.faq_locators import FaqLocators
from selenium.webdriver.support import expected_conditions as EC
import allure


class FaqPage(BasePage):

    @allure.step("Открыть вопрос FAQ")
    def open_question(self, index):
        question = self.wait_clickable(FaqLocators.QUESTIONS[index])
        self.scroll_to(question)

        self.click(
        FaqLocators.QUESTIONS[index]
    )

        self.wait_visible(
        FaqLocators.ANSWERS[index]
    )

        self.wait.until(
            EC.visibility_of_element_located(FaqLocators.ANSWERS[index])
        )
        
    @allure.step("Получить ответ FAQ")
    def get_answer(self, index):
        locator = FaqLocators.ANSWERS[index]
        self.wait_visible(locator)
        return self.get_text(locator)