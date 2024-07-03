from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By


class SearchResults(BasePage):
    def __init__(self) -> None:
        super().__init__()

    def click_first_item(self):
        first_item = self.driver.find_element(By.XPATH, '//*[@id="search"]/div[1]/a[2]')
        first_item.click()
       
