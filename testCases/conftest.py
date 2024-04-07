import pytest
from selenium import webdriver
import pytest
from selenium import webdriver
from utilities.readProperties import ReadConfig
import datetime
from pageObjects.LoginPage import LoginPage
BaseURL = ReadConfig.getApplicationURL()
baseURL = ReadConfig.getApplicationURL()
username = ReadConfig.getUseremail()
password = ReadConfig.getPassword()

# @pytest.fixture()
# def setup():
#     driver = webdriver.Chrome()  # Initialize WebDriver instance
#     print(BaseURL)
#     driver.get(BaseURL)
#     driver.maximize_window()
#     yield driver  # Provide the WebDriver instance to the tests
#     driver.quit()  # Quit the WebDriver after tests are done
@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome()
        print(BaseURL)
        driver.get(BaseURL)
        driver.maximize_window()
        lp = LoginPage(driver)
        lp.setUserName(username)
        lp.setPassword(password)
        lp.clickLogin()
        print("Launching chrome browser.........")
        yield driver  # Provide the WebDriver instance to the tests
        driver.quit()  # Quit the WebDriver after tests are done
    elif browser == 'firefox':
        driver = webdriver.Firefox()
        print(BaseURL)
        driver.get(BaseURL)
        driver.maximize_window()
        print("Launching firefox browser.........")
        yield driver  # Provide the WebDriver instance to the tests
        driver.quit()  # Quit the WebDriver after tests are done
    elif browser == 'IE':
        driver = webdriver.IE()
        print(BaseURL)
        driver.get(BaseURL)
        driver.maximize_window()
        print("Launching IE browser.........")
        yield driver  # Provide the WebDriver instance to the tests
        driver.quit()  # Quit the WebDriver after tests are done
    return driver

def pytest_addoption(parser):    # This will get the value from CLI /hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):  # This will return the Browser value to setup method
    return request.config.getoption("--browser")
@pytest.fixture()
def current_datetime():
    # Get current date and time
    current_datetime = datetime.datetime.now()
    # Print current date and time
    print("Current Date and Time:", current_datetime)



########### pytest HTML Report ################

##It is hook for Adding Environment info to HTML Report
# def pytest_configure(config):
#     config._metadata['Project Name'] = 'Altos'
#     config._metadata['Module Name'] = 'Dashbord'
#     config._metadata['Tester'] = 'Shivanand'
#
# # It is hook for delete/Modify Environment info to HTML Report
# @pytest.mark.optionalhook
# def pytest_metadata(metadata):
#     metadata.pop("JAVA_HOME", None)
#     metadata.pop("Plugins", None)