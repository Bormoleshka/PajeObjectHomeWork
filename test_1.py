from testpage import OperationsHelper
import logging
import yaml




def test_step1(browser):
    logging.info("Test1 Starting")
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.enter_login("test")
    testpage.enter_pass("test")
    testpage.click_login_button()
    assert testpage.get_error_text() == "401"

def test_step2(browser):
    logging.info("Contact button testing")
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.enter_login(testdata["login"])
    testpage.enter_pass(testdata["password"])
    testpage.click_login_button()
    testpage.click_contact_button()
    
def test_step3(browser):
    logging.info("Enter fields testing")
    testpage.enter_your_name(testdata["name"])
    testpage.enter_email(testdata["email"])
    testpage.enter_content(testdata["content"])
    
def test_step4(browser):
    logging.info("CONTACT US button and alert testing")
    testpage.click_contact_us_button()
    assert testdata.get_alert_text() == "Form succesfully submitted"
    return testdata.get_alert_text(text1)


