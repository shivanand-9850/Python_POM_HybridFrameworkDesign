import pytest
from selenium import webdriver
from pageObjects.ImportPage import ImportPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_003_Login:
    logger = LogGen.loggen()

    @pytest.mark.regression
    @pytest.mark.sanity
    def test_Run_All(self, setup,current_datetime):
        self.logger.info("****Started Login Test****")
        self.driver = setup
        self.current_datetime = current_datetime
        self.lp = ImportPage(self.driver)
        self.lp.Run_All()
        act_title = self.driver.title
        if act_title == "Import":
            self.logger.info("****Login test passed ****")
            self.driver.close()
            assert True
        else:
            self.logger.error("****Login test failed ****")
            self.driver.save_screenshot(".\\Screenshots\\" "Run_All.png")
            self.driver.close()
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_Pause_All(self, setup, current_datetime):
        self.logger.info("****Started Login Test****")
        self.driver = setup
        self.current_datetime = current_datetime
        self.lp = ImportPage(self.driver)
        self.lp.Run_All()
        # self.lp.Pause_All()
        act_title = self.driver.title
        if act_title == "Import":
            self.logger.info("****Login test passed ****")
            self.driver.close()
            assert True
        else:
            self.logger.error("****Login test failed ****")
            self.driver.save_screenshot(".\\Screenshots\\" + "Pause_All.png")
            self.driver.close()
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_Stop_All(self, setup, current_datetime):
        self.logger.info("****Started Login Test****")
        self.driver = setup
        self.current_datetime = current_datetime
        self.lp = ImportPage(self.driver)
        self.lp.Run_All()
        # self.lp.Stop_All()
        act_title = self.driver.title
        if act_title == "Import":
            self.logger.info("****Login test passed ****")
            self.driver.close()
            self.driver.save_screenshot(".\\Screenshots\\" + "Stop_All.png")
            assert True

        else:
            self.logger.error("****Login test failed ****")
            self.driver.save_screenshot(".\\Screenshots\\" + "Stop_All.png")
            self.driver.close()
            assert False