import inspect
import logging
import time
import pytest
from selenium.webdriver.common.by import By



@pytest.mark.usefixtures("setup")
class BaseClass:

    # Allows a screenshot to be taken at any point in the booking process to help troubleshoot what is going wrong
    def takeScreenshot(self):
        self.driver.save_screenshot('screenshot.png')

    def searchFunc(self, data):
        # finds search input and enters topic/text to be searched
        self.driver.find_element(By.CSS_SELECTOR, "#searchInput").send_keys(data)
        # clicks the search button
        self.driver.find_element(By.XPATH, "//form[@id='searchform']//button[@class='cdx-button "
                                           "cdx-button--action-default cdx-button--type-normal cdx-button--framed "
                                           "cdx-search-input__end-button'][normalize-space()='Search']").click()
        # saves article to view later....click the 'star' icon
        self.driver.find_element(By.CSS_SELECTOR, ".mw-ui-button.mw-ui-quiet.mw-ui-icon.mw-ui-icon-element.mw-ui-icon"
                                                  "-star.mw-ui-icon-wikimedia-star.mw-ui-icon-small").click()
        time.sleep(1.5)

    # Creates a log of testing events
    def getLog(self):
        loggerName = inspect.stack()[1][3]  # Gets the name of the class / method from where this method is called
        logger = logging.getLogger(loggerName)
        # formatter will produce...201-19-02-17 12:40:14,798 : ERROR: <testcasename>: Fatal error in submitting credit card payment on step 4. Cannot continue...using for formatting error logs
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler = logging.FileHandler('logfile.log')
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)  # filehandler object
        logger.setLevel(logging.DEBUG)
        return logger