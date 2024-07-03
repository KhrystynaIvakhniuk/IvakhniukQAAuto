from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By
import time


class CartPage(BasePage):
    def __init__(self) -> None:
        super().__init__()
 
    def check_text(self, text):
        return text in self.driver.page_source
    
    def verify_quantity(self):
        quantity = self.driver.find_element(By.XPATH, '//*[@id="InputQuantity1"]')
        return int(quantity.get_attribute("value"))

    def add_one_more_product(self):
        # click plus btn
        self.click_element(By.XPATH, '//*[@id="Basket"]/form/div[1]/div[2]/div[5]/div[1]/div/a[2]')
        # click calculate 
        self.click_element(By.XPATH, '//*[@id="Basket"]/form/div[1]/div[2]/div[5]/div[2]/button/span[2]')

    def delete_product(self):
        # select item to delete
        self.click_element(By.XPATH, '//*[@id="Basket"]/form/div[2]/div/div/label')
        time.sleep(5)
        # click delete btn
        self.click_element(By.XPATH, '//*[@id="Basket"]/form/div[2]/div/a')

    