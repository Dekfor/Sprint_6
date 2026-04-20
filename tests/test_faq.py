import pytest, allure
from pages.faq_page import FaqPage
from data.faq_data import (
    FAQ_ANSWER_0,
    FAQ_ANSWER_1,
    FAQ_ANSWER_2,
    FAQ_ANSWER_3,
    FAQ_ANSWER_4,
    FAQ_ANSWER_5,
    FAQ_ANSWER_6,
    FAQ_ANSWER_7,
)


@allure.feature("FAQ")
class TestFaq:

    @allure.title("Проверка ответов в FAQ")
    @pytest.mark.parametrize("index, expected", [
        (0, FAQ_ANSWER_0),
        (1, FAQ_ANSWER_1),
        (2, FAQ_ANSWER_2),
        (3, FAQ_ANSWER_3),
        (4, FAQ_ANSWER_4),
        (5, FAQ_ANSWER_5),
        (6, FAQ_ANSWER_6),
        (7, FAQ_ANSWER_7),
    ])

    @allure.step("Проверка FAQ по индексу {index}")
    def test_faq(self, driver, index, expected):

        page = FaqPage(driver)

        page.open_question(index)
        answer = page.get_answer(index)

        assert expected in answer