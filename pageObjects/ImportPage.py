import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class ImportPage:
    # Login Page
    IconAltos = "//i[@class='mat-tooltip-trigger fa fa-medkit oa transition x-md ng-star-inserted']"
    ImportAltos = "//h5[text()='Import']"
    Button_RunAll = "//span[text()=' Run All ']"
    Button_Pause_All = "//span[text()=' Pause All ']"
    Button_Stop_All = "//span[text()=' Stop All ']"

    def __init__(self,driver):
        self.driver = driver

    def Run_All(self):
        time.sleep(10)
        self.driver.find_element(By.XPATH, self.IconAltos).click()
        self.driver.find_element(By.XPATH, self.ImportAltos).click()
        self.driver.find_element(By.XPATH, self.Button_RunAll).click()

    def Pause_All(self):
        time.sleep(10)
        self.driver.find_element(By.XPATH, self.IconAltos).click()
        self.driver.find_element(By.XPATH, self.ImportAltos).click()
        self.driver.find_element(By.XPATH, self.Button_RunAll).click()
        self.driver.find_element(By.XPATH, self.Button_Pause_All).click()

    def Stop_All(self):
        time.sleep(10)
        self.driver.find_element(By.XPATH, self.IconAltos).click()
        self.driver.find_element(By.XPATH, self.ImportAltos).click()
        self.driver.find_element(By.XPATH, self.Button_RunAll).click()
        self.driver.find_element(By.XPATH, self.Button_Stop_All).click()
