import pytest
from pages.product_page import ProductPage


@pytest.mark.parametrize('offer_number', [pytest.param(num, marks=pytest.mark.xfail) if num == 7
                                          else num
                                          for num in range(10)])
def test_guest_can_add_product_to_basket(browser, offer_number: int) -> None:
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{offer_number}"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_add_to_basket_button()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.should_item_in_basket()
    page.should_be_msg_about_adding()