import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class LoginPage:
    # Login Page
    textbox_username_id = "//input[@placeholder='Employee Code']"
    textbox_password_id = "//input[@type='password']"
    button_login_xpath = "//span[@class='mat-button-wrapper']"
    link_logout_linktext1 = "//div[@class='content']"
    link_logout_linktext2 = "//span[text()='LOG OUT']"

    def __init__(self,driver):
        self.driver = driver

    def setUserName(self, username):
        time.sleep(10)
        self.driver.find_element(By.XPATH, self.textbox_username_id).clear()
        self.driver.find_element(By.XPATH, self.textbox_username_id).send_keys(username)


    def setPassword(self, password):
        self.driver.find_element(By.XPATH, self.textbox_password_id).clear()
        self.driver.find_element(By.XPATH, self.textbox_password_id).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.XPATH, self.button_login_xpath).click()
        time.sleep(10)
        # WebDriverWait(self.driver, 10).until(EC.title_is(T))

    def clickLogout(self):
        self.driver.find_element(By.XPATH, self.link_logout_linktext1).click()
        self.driver.find_element(By.XPATH, self.link_logout_linktext2).click()