import pytest
from modules.ui.page_objects.cosibella.main_page import MainPage
from modules.ui.page_objects.cosibella.search_results_page import SearchResults
from modules.ui.page_objects.cosibella.item_page import ItemPage
from modules.ui.page_objects.cosibella.cart_page import CartPage
import time


@pytest.mark.ui_cart
def test_try_add_product_to_cart():
    main_page = MainPage()
    main_page.go_to()
    main_page.accept_cookies()
    main_page.search_product("spf")

    search_results = SearchResults()
    search_results.click_first_item()

    item_page = ItemPage()
    time.sleep(10)
    item_page.add_item_to_cart()
    item_page.go_to_cart()
    
    cart_page = CartPage()
    assert cart_page.check_text("Замовлення")


@pytest.mark.ui_cart
def test_check_quantity():
    cart_page = CartPage()
    current_quantity = cart_page.verify_quantity()
    expected_quantity = 1
    assert current_quantity == expected_quantity

    
@pytest.mark.ui_cart
def test_try_increase_product():
    cart_page = CartPage()
    cart_page.add_one_more_product()
    time.sleep(5)
    current_quantity = cart_page.verify_quantity()
    expected_quantity = 2
    assert current_quantity == expected_quantity


@pytest.mark.ui_cart
def test_delete_product():
    cart_page = CartPage()
    cart_page.delete_product()
    assert cart_page.check_text("Ваш кошик порожній.")




