from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def should_not_be_products_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS_DIV)


    def should_be_message_empty_basket(self) -> None:
        message = self.browser.find_element(*BasketPageLocators.EMPTY_BASKET_MESSAGE)
        assert "Your basket is empty" in message.text
