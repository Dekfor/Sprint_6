from pages.base_page import BasePage
from locators.faq_locators import FaqLocators
from selenium.webdriver.support import expected_conditions as EC
import time


class FaqPage(BasePage):

    def open_question(self, index):
        question = self.wait_clickable(FaqLocators.QUESTIONS[index])
        self.scroll_to(question)

        time.sleep(0.5)
        self.wait.until(EC.element_to_be_clickable(FaqLocators.QUESTIONS[index]))

        question.click()

        self.wait.until(
            EC.visibility_of_element_located(FaqLocators.ANSWERS[index])
        )

    def get_answer(self, index):
        return self.get_text(FaqLocators.ANSWERS[index])