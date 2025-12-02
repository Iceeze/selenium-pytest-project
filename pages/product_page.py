from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.common.exceptions import NoSuchElementException


class ProductPage(BasePage):
    def add_to_basket(self) -> None:
        add_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_button.click()

    def should_be_add_to_basket_button(self) -> None:
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON), (
            "Didn't find the add button"
        )

    def should_item_in_basket(self) -> None:
        self.should_cost_equal()
        self.should_name_equal()

    def should_cost_equal(self) -> None:
        item_basket_cost = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL)
        item_product_cost = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        assert item_basket_cost.text == item_product_cost.text, "Prices in basket and in product page isn't equal"

    def should_name_equal(self) -> None:
        items_strong = self.browser.find_elements(*ProductPageLocators.BASKET_STRONG_NAMES)
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        names_equal = False
        for item_strong in items_strong:
            if item_strong.text == product_name:
                names_equal = True
        assert names_equal, "Names of product isn't equal"

    def should_be_success_message(self) -> None:
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        message = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGES).text

        assert product_name in message, "Product name not found on message"

    def should_not_be_success_message(self) -> None:
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGES), "Success messages show up"

    def should_be_disappeared_message(self) -> None:
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGES), "Success message is not disappeared"

    def should_not_be_disappeared_message(self) -> None:
        assert not self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGES), "Success messages is disappeared"
