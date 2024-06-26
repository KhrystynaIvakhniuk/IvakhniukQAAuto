from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By


class SignInPage(BasePage):
    URL = "https://github.com/login"

    def __init__(self) -> None:
        super().__init__()

    def go_to(self):
        self.driver.get(SignInPage.URL)

    def try_login(self, username, password):
        # find input field to input incorrect email
        login_elem = self.driver.find_element(By.ID, "login_field")
        
        # input incorrect email
        login_elem.send_keys(username)
        
        # find input field to input incorrect password
        pass_elem = self.driver.find_element(By.ID, "password")
        
        # input incorrect password
        pass_elem.send_keys(password)
        
        # find button Sign In
        btn_elem = self.driver.find_element(By.NAME, "commit")
        
        # emulate a click with the left mouse button
        btn_elem.click()

    def check_title(self, expected_title):
        return self.driver.title == expected_title
    