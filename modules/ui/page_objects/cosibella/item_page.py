from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By
import time


class ItemPage(BasePage):
    def __init__(self) -> None:
        super().__init__()

    def add_item_to_cart(self):
        self.click_element(By.XPATH, '//*[@id="projector_button_basket"]')

    def go_to_cart(self):
        time.sleep(10)
        go_to_cart_btn = self.driver.find_element(By.XPATH, '//*[@id="toBasketToplayer"]/div[4]/a[2]')
        go_to_cart_btn.click()
