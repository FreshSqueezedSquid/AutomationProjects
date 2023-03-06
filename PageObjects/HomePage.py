from selenium.webdriver.common.by import By
from PageObjects.LoginPage import LoginPage


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    select_language = (By.CSS_SELECTOR, "#js-link-box-en")
    login_button = (By.CSS_SELECTOR, "#pt-login-2")

    def getLanguage(self):
        return self.driver.find_element(*HomePage.select_language)

    def goToLogin(self):
        self.driver.find_element(*HomePage.login_button).click()
        loginPage = LoginPage(self.driver)
        return loginPage