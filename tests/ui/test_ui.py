import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


@pytest.mark.ui
def test_check_incorrect_username():
    # create an object to control the browser
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    # open a page https://github.com/login
    driver.get("https://github.com/login")

    # find input field to input incorrect email
    login_elem = driver.find_element(By.ID, "login_field")

    # input incorrect email
    login_elem.send_keys("ivakhniuk@mistakenemail.com")

    # find input field to input incorrect password
    pass_elem = driver.find_element(By.ID, "password")

    # input incorrect password
    pass_elem.send_keys("wrong password")

    # find button Sign In
    btn_elem = driver.find_element(By.NAME, "commit")

    # emulate a click with the left mouse button
    btn_elem.click()

    # check page name
    assert driver.title == "Sign in to GitHub · GitHub"

    # close the browser
    driver.close()
