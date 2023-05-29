from BaseApp import BasePage
from selenium.webdriver.common.by import by
import logging


class TestSearchLocators:
    LOCATOR_LOGIN_FIELD = (By.XPATH,  """//*[@id="login"]/div[1]/label/input""")
    LOCATOR_PASS_FIELD = (By.XPATH, """//*[@id="login"]/div[2]/label/input""")
    LOCATOR_LOGIN_BTN = (By.CSS_SELECTOR, "button")
    LOCATOR_ERROR_FIELD = (By.XPATH, """//*[@id="app"]/main/div/div/div[2]/h2""")
    LOCATOR_CONTACT_BTN = (By.CSS_SELECTOR, "button")
    LOCATOR_NAME_FIELD = (By.XPATH, "/html/body/div[1]/main/div/div/form/div[1]/label/input")
    LOCATOR_EMAIL_FIELD = (By.XPATH, "/html/body/div[1]/main/div/div/form/div[2]/label/input")
    LOCATOR_CONTENT_FIELD = (By.XPATH, "/html/body/div[1]/main/div/div/form/div[3]/label/span/textarea")
    LOCATOR_CONTACT_US_BTN = (By.CSS_SELECTOR, "button")
    
class OperationsHelper(BasePage):
    def enter_login(self, word):
        logging.info(f"Send {word} to element {TestSearchLocators.LOCATOR_LOGIN_FIELD[1]}")
        login_field = self.find_element(TestSearchLocators.LOCATOR_LOGIN_FIELD)
        login_field.clear()
        login_field.send_keys(word)
        
    def enter_password(self, word):
        logging.info(f"Send {word} to element {TestSearchLocators.LOCATOR_PASS_FIELD[1]}")
        pass_field = self.find_element(TestSearchLocators.LOCATOR_PASS_FIELD)
        pass_field.clear()
        pass_field.send_keys(word)
    
    def click_login_button(self):
        logging.info("Click login button")
        self.find_element(TestSearchLocators.LOCATOR_LOGIN_BTN).click()
        
    def get_error_text(self):
        error_field = self.find_element(TestSearchLocators.LOCATOR_ERROR_FIELD, time=3)
        text = error_field.text
        logging.info(f"Find text {text} in error field {TestSearchLocators.LOCATOR_ERROR_FIELD[1]}")
        return text
        
    def clic_contact_button(self):
        logging.info("Click Contact button")
        self.find_element(TestSearchLocators.LOCATOR_CONTACT_BTN).click()
        
    def enter_your_name(self, name):
        logging.info(f"Send {name} to element {TestSearchLocators.LOCATOR_NAME_FIELD[1]}")
        pass_field = self.find_element(TestSearchLocators.LOCATOR_NAME_FIELD)
        pass_field.clear()
        pass_field.send_keys(name)
        
    def enter_email(self, email):
        logging.info(f"Send {email} to element {TestSearchLocators.LOCATOR_EMAIL_FIELD[1]}")
        pass_field = self.find_element(TestSearchLocators.LOCATOR_EMAIL_FIELD)
        pass_field.clear()
        pass_field.send_keys(email)
        
    def enter_content(self, content):
        logging.info(f"Send {content} to element {TestSearchLocators.LOCATOR_CONTENT_FIELD[1]}")
        pass_field = self.find_element(TestSearchLocators.LOCATOR_CONTENT_FIELD)
        pass_field.clear()
        pass_field.send_keys(content)
        
    def clic_contact_us_button(self):
        logging.info("Click CONTACT US button")
        self.find_element(TestSearchLocators.LOCATOR_CONTACT_US_BTN).click()
        
    def get_alert(self):
        logging.info("Get alert text")
        text = self.get_alert_text()
        logging.info(text)
        return text
        