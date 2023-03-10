import time

from selenium.webdriver.common.by import By
from PageObjects.LoginPage import LoginPage


class MainPage:

    def __init__(self, driver):
        self.driver = driver

    select_language = (By.CSS_SELECTOR, "#js-link-box-en")
    login_button = (By.CSS_SELECTOR, "#pt-login-2")
    star_icon = (By.CSS_SELECTOR, ".mw-ui-button.mw-ui-quiet.mw-ui-icon.mw-ui-icon-element.mw-ui-icon-star.mw-ui-icon-wikimedia-star.mw-ui-icon-small")
    user_dropdown = (By.CSS_SELECTOR, "#vector-user-links-dropdown-checkbox")
    logout = (By.XPATH, "//li[@id='pt-logout']//a[@title='Log out']")

    def goToLogin(self):
        self.driver.find_element(*MainPage.login_button).click()
        loginPage = LoginPage(self.driver)
        return loginPage

    def userLogout(self):
        self.driver.find_element(*MainPage.user_dropdown).click()
        time.sleep(1.5)
        self.driver.find_element(*MainPage.logout).click()