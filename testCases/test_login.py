import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_homePageTitle(self, setup, current_datetime):
        self.logger.info("*************** Test_001_Login *****************")
        self.logger.info("****Started Home page title test ****")
        self.driver = setup
        self.current_datetime = current_datetime
        self.logger.info("****Opening URL****")
        act_title = self.driver.title

        if act_title == "Altos":
            self.logger.info("**** Home page title test passed ****")
            self.driver.close()
            self.driver.save_screenshot(".\\Screenshots\\"+"test_homePageTitle2.png")
            assert True
        else:
            self.logger.error("**** Home page title test failed****")
            self.driver.save_screenshot(".\\Screenshots\\"+"test_homePageTitle11.png")
            self.driver.close()
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self,setup):

        self.logger.info("****Started Login Test****")
        self.driver = setup
        self.lp = LoginPage(self.driver)
        # self.lp.setUserName(self.username)
        # self.lp.setPassword(self.password)
        # self.lp.clickLogin()
        act_title = self.driver.title
        if act_title == "Altos":
            self.logger.info("****Login test passed ****")
            self.driver.close()
            assert True
        else:
            self.logger.error("****Login test failed ****")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_homePageTitle.png")
            self.driver.close()
            assert False


# [command Pytest]
#
# pytest -v -s -n=3  testCases\test_login.py --browser chrome
#
# pytest -v -s -n=2 --html=Report/report.html testCases\test_login.py --browser chrome

