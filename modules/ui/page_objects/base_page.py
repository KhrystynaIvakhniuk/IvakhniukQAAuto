from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    driver = None
    
    def __init__(self) -> None:
        if BasePage.driver is None:
            BasePage.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
            BasePage.driver.maximize_window()
        self.driver = BasePage.driver
    
    def close(self):
        self.driver.close()

    def scroll_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def click_element(self, by, value):
        try:
            element = self.wait.until(EC.element_to_be_clickable((by, value)))
            self.scroll_to_element(element)
            element.click()
        except:
            element = self.driver.find_element(by, value)
            self.driver.execute_script("arguments[0].click();", element)
        