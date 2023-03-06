from selenium.webdriver.common.by import By


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    username = (By.CSS_SELECTOR, "#wpName1")
    password = (By.CSS_SELECTOR, "#wpPassword1")
    login = (By.CSS_SELECTOR, "#wpLoginAttempt")

    def getUsername(self):
        return self.driver.find_element(*LoginPage.username)

    def getPassword(self):
        return self.driver.find_element(*LoginPage.password)

    def sendLogin(self):
        return self.driver.find_element(*LoginPage.login)
