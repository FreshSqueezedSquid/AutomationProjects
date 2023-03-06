import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from PageObjects.HomePage import HomePage
from TestData.LoginData import LoginData
from TestData.SearchData import SearchData
from utilities.BaseClass import BaseClass
from selenium.webdriver.support import expected_conditions as EC


class TestWiki(BaseClass):

    def test_wiki(self, getLogin, getSearch):

        log = self.getLog()
        wait = WebDriverWait(self.driver, 45)
        log.info("Selecting viewing language")

        homePage = HomePage(self.driver)
        homePage.getLanguage().click()
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#pt-login-2")))
        loginPage = homePage.goToLogin()
        wait.until(EC.element_to_be_clickable(loginPage.getUsername()))
        loginPage.getUsername().send_keys(getLogin["username"])
        loginPage.getPassword().send_keys(getLogin["password"])
        log.info("Logging into account")
        loginPage.sendLogin().click()
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#searchInput")))
        self.searchTopic(getSearch["person"])
        time.sleep(2)
        self.takeScreenshot()

    @pytest.fixture(params=LoginData.test_login_data)
    def getLogin(self, request):
        return request.param

    @pytest.fixture(params=SearchData.test_search_data)
    def getSearch(self, request):
        return request.param

