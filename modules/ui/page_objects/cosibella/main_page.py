from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By


class MainPage(BasePage):
    URL = "https://cosibella.com.ua/"

    def __init__(self) -> None:
        super().__init__()

    def go_to(self):
        self.driver.get(MainPage.URL)

    def accept_cookies(self):
        search_btn = self.driver.find_element(By.XPATH, '//*[@id="iai_cookie"]/div/div[1]/div[2]/div/a[4]')
        search_btn.click()

    def search_product(self, product):
        search_elem = self.driver.find_element(By.XPATH, '//*[@id="menu_search"]/div/div[1]/input')
        search_elem.send_keys(product)
        btn_elem = self.driver.find_element(By.XPATH, '//*[@id="menu_search"]/div/div[1]/button[1]')
        btn_elem.click()
