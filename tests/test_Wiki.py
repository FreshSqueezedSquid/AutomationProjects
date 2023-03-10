import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from PageObjects.MainPage import MainPage
from TestData.LoginData import LoginData
from TestData.SearchData import SearchData
from utilities.BaseClass import BaseClass
from selenium.webdriver.support import expected_conditions as EC


class TestWiki(BaseClass):

    def test_wiki(self, getLogin, getSearch):

        log = self.getLog()
        wait = WebDriverWait(self.driver, 15)
        log.info("Selecting viewing language")

        mainPage = MainPage(self.driver)
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#pt-login-2")))
        loginPage = mainPage.goToLogin()
        wait.until(EC.element_to_be_clickable(loginPage.getUsername()))
        loginPage.getUsername().send_keys(getLogin["username"])
        loginPage.getPassword().send_keys(getLogin["password"])
        log.info("Logging into account")
        loginPage.sendLogin().click()
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#searchInput")))
        self.searchFunc(getSearch["person"])
        self.searchFunc(getSearch["place"])
        self.searchFunc(getSearch["thing"])
        mainPage.userLogout()
        self.driver.delete_all_cookies()
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".mw-logo")))
        self.driver.find_element(By.CSS_SELECTOR, ".mw-logo").click()
        time.sleep(2)


    @pytest.fixture(params=LoginData.test_login_data)
    def getLogin(self, request):
        return request.param

    @pytest.fixture(params=SearchData.test_search_data)
    def getSearch(self, request):
        return request.param
