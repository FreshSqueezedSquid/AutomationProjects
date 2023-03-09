from selenium.webdriver.common.by import By
from PageObjects.LoginPage import LoginPage


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    select_language = (By.CSS_SELECTOR, "#js-link-box-en")
    login_button = (By.CSS_SELECTOR, "#pt-login-2")
    star_icon = (By.CSS_SELECTOR, ".mw-ui-button.mw-ui-quiet.mw-ui-icon.mw-ui-icon-element.mw-ui-icon-star.mw-ui-icon-wikimedia-star.mw-ui-icon-small")

    def getLanguage(self):
        return self.driver.find_element(*HomePage.select_language)

    def goToLogin(self):
        self.driver.find_element(*HomePage.login_button).click()
        loginPage = LoginPage(self.driver)
        return loginPage
