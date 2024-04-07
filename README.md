# Selenium-Python-Hybrid-Framework-Design
 
### Objectives/Goals of this Framework
    ✅ Customization            -> Tailor the framework precisely depending on the project's needs.
    ✅ Flexibility              -> Combine testing approaches for versatile test scenarios.
    ✅ Reusability              -> Create reusable components for efficient testing.
    ✅ Modularity               -> Break down the application into manageable modules for easier maintenance.
    ✅ Separation of Concerns   -> Keep test scripts, data, and logic separate for clarity.
    ✅ Ease of Maintenance      -> Changes are isolated, making maintenance easier.
    ✅ Scalability              -> Extend the framework to handle larger projects or new features.
    ✅ Integration              -> Seamlessly integrate with CI/CD pipelines and other tools.
    ✅ Cross-Team Collaboration -> Provide a common ground for effective collaboration.
    ✅ Skill Enhancement        -> Boost team skills in testing, programming, and automation.
    ✅ Adaptability             -> Keep automation relevant by integrating new technologies.

### Tools, Packages, Concept, Frameworks Used to build this framework:
    ✅ Selenium WebDriver   -> To interact with web elements and perform actions on web pages.

    ✅ Python               -> To write test scripts and framework code.

    ✅ Pytest or Unittest   -> To organize and run your test cases.

    ✅ Page Object Model    -> A design pattern for organizing code by creating a separate class for each page or component of your application.

    ✅ Test Data Management -> Libraries like yaml or json to manage test data separately from the test scripts.

    ✅ Logging              -> Python's built-in logging module to create detailed logs of test execution.

    ✅ Reporting            -> Libraries like pytest-html, Allure, or custom reporting to generate reports.

    ✅ Version Control      -> Git for version control to keep track of changes.

    ✅ CI/CD Tool           -> Jenkins for automating test execution.

    ✅ IDE                  -> PyCharm.

    ✅ Browser Drivers      -> ChromeDriver, GeckoDriver for Firefox.

    ✅ Package Management   -> Python's package manager, pip to install and manage third-party libraries.

    ✅ OOP                  -> Python's OOP features to structure framework with classes and objects, enhancing modularity.

    ✅ Selectors            -> Techniques for locating web elements on the page, essential for interaction in Selenium.

    ✅ Data Driven          -> Libraries like ddt to enable data-driven testing where the same test case is executed with different inputs.

# Steps to build this framework
### Step 1: Create new Project and install required packages/plugins
###### Go to -> File ->Settings ->Project ->Project Interpreter ->Install the following packages
    ✅ Selenium: Selenium Libraries
    ✅ Pytest: Python Unit Test Framework
    ✅ pytest-html: PyTest Html Report
    ✅ pytest-xdist: Run test parallelly
    ✅ Openpyxl: MS Excel Support
    ✅ Allure-pytest: Generate allure report
    
### Step 2: Create the folder structure
######      Project Name
            ---> Project
                        ---> pageObjects (Package)
                                    ---> page classes those contains locators
                                    
                        ---> testCases (Package)
                                    ---> Contains test classes       
                                    
                        ---> utilities (Package)
                                    ---> Contains base class & other necessary utilities
                                    
                        ---> Configurations (Folder)
                                    ---> Contains setup
                                    
                        ---> Logs (Folder)
                                    ---> Contains logs 
                                    
                        ---> Screenshots (Folder)
                                    ---> Contains screenshots
                                    
                        ---> Reports (Folder)
                                    ---> Contains html report
                                    
                        ---> TestData (Folder)
                                    ---> Contains demo data
                                    
                        ---> Run.bat     //To run with a single click  
                        
![folder structure](https://github.com/imranalmunyeem/Selenium4-Hybrid-Framework-Design/blob/main/folderstructure.png)

### Step 3: Automate some test cases
    ✅ Create Page Object Class under "pageObjects"
    ✅ Create test classes under "testCases"
    ✅ Create conftest.py under "testcases"

### Step 4: Capture Screenshot on failure
    ✅ Update test cases with screenshots under testcases

### Step 5: Read common values from ini file
    ✅ Add "config.ini" file under "configuration" folder.
    ✅ Create "readProperties.py" utility file under "utilities" package to read common data.
    ✅ Replace the hard coded values in test casess.
            
### Step 6: Add logs to test cases
    ✅ Add "config.ini" file under "configuration" folder.
    ✅ Create "readProperties.py" utility file under "utilities" package to read common data.
    ✅ Replace the hard coded values in test casess.
                     
### Step 7: Create test classes under testCases Package
                --- Conventions you need to follow
                        --- Test class names have to start with "test_" or end with "_test" if you want to treat them as pytests because pytest look for them and run them automatically using this.
                        --- Example: 
                                    test_login

### Step 8: Create test methods inside test classes
                --- Conventions you need to follow
                        --- Test method names have to start with "test_" 
                        --- Example: 
                                   def test_login():
                                   
                                   
### Step 9: How to configure and run pytests?
                --- Click on "Edit Configurations" from right -> '+' -> Python test -> pytest and then select script from directy -> apply -> click on Run 
                      

### Step 10: How to run the tests from terminal?
                --- Open terminal, copy the path of the test package, paste it to the terminal, go to that directory, use command "py.test" //it will run all test
                --- Example: 
                        cd C:\Users\ialmu\PycharmProjects\Selenium-Python-Hybrid-Framework-Design\pytests             // go to directory by using cd
                        C:\Users\ialmu\PycharmProjects\Selenium-Python-Hybrid-Framework-Design\pytests>py.test        // use command py.test
                        C:\Users\ialmu\PycharmProjects\Selenium-Python-Hybrid-Framework-Design\pytests>py.test -v     // To get more information avout test result
                        C:\Users\ialmu\PycharmProjects\Selenium-Python-Hybrid-Framework-Design\pytests>py.test -v -s  // To print all the console logs in terminal
                        
                        
### Step 11: How to run selected Pytests in Terminal from set of Tests?
               --- cd C:\Users\ialmu\PycharmProjects\Selenium-Python-Hybrid-Framework-Design\pytests                                // go to directory by using cd
               --- C:\Users\ialmu\PycharmProjects\Selenium-Python-Hybrid-Framework-Design\pytests>py.test test_testname.py -v -s      // will run specific test


### Step 12: How to run specific method in Terminal from the set of Test methods?
               --- cd C:\Users\ialmu\PycharmProjects\Selenium-Python-Hybrid-Framework-Design\pytests                                // go to directory by using cd
               --- C:\Users\ialmu\PycharmProjects\Selenium-Python-Hybrid-Framework-Design\pytests>py.test -k methodname -v -s       // will run specific method
               
               
### Step 13: Grouping tests with pytest marks to run selected group?
               --- Import pytest, write @pytest.mark.smoke/ or anything
                        --- Example: 
                                    import pytest
                                    @pytest.mark.smoke
                                    def first_test():
                                      print('hello')
                           Here the test will be marked as smoke test which can be run in the terminal
               --- cd C:\Users\ialmu\PycharmProjects\Selenium-Python-Hybrid-Framework-Design\pytests                           // go to directory by using cd
               --- C:\Users\ialmu\PycharmProjects\Selenium-Python-Hybrid-Framework-Design\pytests>py.test -m smoke -v -s       // m stands for mark
               
               
### Step 14: Skip particular test in termnial using mark?
               --- Import pytest, add @pytest.mark.skip
                        --- Example: 
                                    import pytest
                                    @pytest.mark.skip
                                    def first_test():
                                      print('hello')
                           Here the test will be marked as smoke test which can be run in the terminal
               --- cd C:\Users\ialmu\PycharmProjects\Selenium-Python-Hybrid-Framework-Design\pytests                  // go to directory by using cd
               --- C:\Users\ialmu\PycharmProjects\Selenium-Python-Hybrid-Framework-Design\pytests>py.test -v -s       // marked test will be skipped  
               
               
### Step 15: How to make any specific failed test case to run but not to be added to the report?
               --- Import pytest, add @pytest.mark.xfail
                        --- Example: 
                                    import pytest
                                    @pytest.mark.xfail
                                    def first_test():
                                      print('hello')
                           Here the test will be marked as smoke test which can be run in the terminal
               --- cd C:\Users\ialmu\PycharmProjects\Selenium-Python-Hybrid-Framework-Design\pytests                  // go to directory by using cd
               --- C:\Users\ialmu\PycharmProjects\Selenium-Python-Hybrid-Framework-Design\pytests>py.test -v -s       // marked test will be skipped from reporting          
               
### Step16: How to add fixture in pytest to run the same pre-reqired setup before every test?
               --- Import pytest, add @pytest.fixture
                        --- Example: 
                                    import pytest
                                    @pytest.fixture                        // fixture keyword is for excuting before test like launch the browser during test
                                    def setup():
                                    print('I will be executed first')
                                    
                                    def test_fristTest(setup):
                                    print('Steps of driver setup')   
                                     
                                     
### Step 17: How to add fixture in pytest to run the same reqired post-setup after every test?  
               --- Import pytest, add @pytest.fixture
                        --- Example: 
                                    import pytest
                                    @pytest.fixture
                                    def setup():
                                    print('I will be executed first')
                                    yield                                     // yeild keyword is for excuting after test like close the browser after test
                                    print('I will be executed last')
                                    
                                    def test_fristTest(setup):
                                    print('Steps of driver setup')   


### Step 18: How to add "Conftest" file in pytest to run the same pre and post required setup instead of writing them separately in every class?  
               --- Create a class named "conftest.py" under pytests package         // coftest.py name is mandatory
               --- Put the abive pre and post required setup in conftest file             // example browser launch before test and close after test
               
               
### Step 19: Generating HTML reports for Pytest Testcases
               Run below command in terminal
                        --- pip install pytest-html                     // will install html report generator
                        
               Run below command in terminal to run test with report
                        --- py.test -v -s --html=report.html            // will generate report


###  ⚫ Theory

#### ⚫ What is PIP installer Tool?
pip is a package management system used to install and manage software packages written in Python
pip is a recursive acronym that can stand for either "Pip Installs Packages" or "Pip Installs Python.


#### ⚫ Types of Wait in Selenium?
            --- Explicit Waits
                        --- An explicit wait is a code you define to wait for a certain condition to occur before proceeding further in the code.  
                        
                        --- The extreme case of this is time.sleep(), which sets the condition to an exact time period to wait.
                        
                        --- Example:
                                    from selenium import webdriver
                                    from selenium.webdriver.common.by import By
                                    from selenium.webdriver.support.ui import WebDriverWait
                                    from selenium.webdriver.support import expected_conditions as EC

                                    driver = webdriver.Firefox()
                                    driver.get("http://somedomain/url_that_delays_loading")
                                    try:
                                                element = WebDriverWait(driver, 10).until(
                                                EC.presence_of_element_located((By.ID, "myDynamicElement")))
                                    finally:
                                                driver.quit()
                                                
                        --- Expected Conditions:
                                    --- title_is
                                    --- title_contains
                                    --- presence_of_element_located
                                    --- visibility_of_element_located
                                    --- visibility_of
                                    --- presence_of_all_elements_located
                                    --- text_to_be_present_in_element
                                    --- text_to_be_present_in_element_value
                                    --- frame_to_be_available_and_switch_to_it
                                    --- invisibility_of_element_located
                                    --- element_to_be_clickable
                                    --- staleness_of
                                    --- element_to_be_selected
                                    --- element_located_to_be_selected
                                    --- element_selection_state_to_be
                                    --- element_located_selection_state_to_be
                                    --- alert_is_present
                                    
                        --- Custom Wait Command: You can also create custom wait conditions when none of the previous convenience methods fit your requirements.
                        
                        --- Example:
                                    # Wait until an element with id='myNewInput' has class 'myCSSClass'
                                    wait = WebDriverWait(driver, 10)
                                    element = wait.until(element_has_css_class((By.ID, 'myNewInput'), "myCSSClass"))
                                    
            --- Implicit Waits
                        --- It tells WebDriver to poll the DOM for a certain amount of time when trying to find any element not immediately available.
                        
                        --- The default setting is 0 (zero). 
                        
                        --- Once set, the implicit wait is set for the life of the WebDriver object.
                        
                        --- Example:
                                    from selenium import webdriver

                                    driver = webdriver.Firefox()
                                    driver.implicitly_wait(10) # seconds
                                    driver.get("http://somedomain/url_that_delays_loading")
                                    myDynamicElement = driver.find_element_by_id("myDynamicElement")


#### ⚫ What is XPath?
            --- XPath stands for XML Path Language	
            --- XPath uses "path like" syntax to identify and navigate nodes in an XML document


#### ⚫ Types of XPath?
            --- Absolute XPath:
                        --- It is the direct way to find the element, but the disadvantage of the absolute XPath is that if there are any changes made in the path of the element then that XPath gets failed.
                        
                        --- The key characteristic of XPath is that it begins with the single forward slash(/) ,which means you can select the element from the root node.
                        
                        --- Example: /html/body/div[2]/div[1]/div/h4[1]/b/html[1]/body[1]/div[2]/div[1]/div[1]/h4[1]/b[1]
                        
            --- Relative XPath: 
                        --- Relative Xpath starts from the middle of HTML DOM structure.
                        
                        --- It starts with double forward slash (//). 
                        
                        --- It can search elements anywhere on the webpage, means no need to write a long xpath and you can start from the middle of HTML DOM structure.    
                        
                        --- Relative Xpath is always preferred as it is not a complete path from the root element.
                        
                        --- Example: //div[@class='featured-box cloumnsize1']//h4[1]//b[1]
                                             
            
            
#### ⚫ What is page object model in Selenium?
            --- A design pattern in Selenium that creates an object repository for storing all web elements.
            --- Benefits: 
                        --- Easy to read test cases
                        --- Creating reusable code that can share across multiple test cases
                        --- Reducing the amount of duplicated code
                        --- If the user interface changes, the fix needs changes in only one place


#### ⚫ What is page factory model in Selenium?
            --- An inbuilt Page Object Model framework concept for Selenium WebDriver
            --- Benefits: 
                        --- It is very optimized.
                        --- It is used for initialization of Page objects or to instantiate the Page object itself.
                        --- Also used to initialize Page class elements without using “FindElement/s.”
                        --- @FindBy can accept tagName, partialLinkText, name, linkText, id, css, className, xpath as attributes.


#### ⚫ What is PyTest?
            --- PyTest is a testing framework that allows users to write test codes using Python programming language. 
            --- It helps you to write simple and scalable test cases for databases, APIs, or UI. 
            --- PyTest is mainly used for writing tests for APIs. It helps to write tests from simple unit tests to complex functional tests.


#### ⚫ What is PyTest?
            --- Very easy to start with because of its simple and easy syntax.
            --- Can run tests in parallel.
            --- Can run a specific test or a subset of tests
            --- Automatically detect tests
            --- Skip tests
            --- Open source
   
   
#### ⚫ Why Printing is not a good option in Selenium?
            --- It may solve your issues for simple scripts but for complex scripts, the printing approach will fail. Example: test cases
            

#### ⚫ What is Logging?
            --- Python has a built-in module logging which allows writing status messages to a file or any other output streams. The file can contain the information on which part of the code is executed and what problems have been arisen.
            
            
#### ⚫ Types of Logging?
            --- Debug : These are used to give Detailed information, typically of interest only when diagnosing problems.
            --- Info : These are used to confirm that things are working as expected
            --- Warning : These are used an indication that something unexpected happened, or is indicative of some problem in the near future
            --- Error : This tells that due to a more serious problem, the software has not been able to perform some function
            --- Critical : This tells serious error, indicating that the program itself may be unable to continue running


#### ⚫ Several logger objects offered by the module itself   
            Logger.info(msg) : This will log a message with level INFO on this logger.
            Logger.warning(msg) : This will log a message with a level WARNING on this logger.
            Logger.error(msg) : This will log a message with level ERROR on this logger.
            Logger.critical(msg) : This will log a message with level CRITICAL on this logger.
            Logger.log(lvl,msg) : This will Logs a message with integer level lvl on this logger.
            Logger.exception(msg) : This will log a message with level ERROR on this logger.
            Logger.setLevel(lvl) : This function sets the threshold of this logger to lvl. This means that all the messages below this level will be ignored.
            Logger.addFilter(filt) : This adds a specific filter filt into this logger.
            Logger.removeFilter(filt) : This removes a specific filter filt into this logger.
            Logger.filter(record) : This method applies the logger’s filter to the record provided and returns True if the record is to be processed. Else, it will return False.
            Logger.addHandler(hdlr) : This adds a specific handler hdlr to this logger.
            Logger.removeHandler(hdlr) : This removes a specific handler hdlr into this logger.
            Logger.hasHandlers() : This checks if the logger has any handler configured or not. 


