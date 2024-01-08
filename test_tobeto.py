from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait 
from selenium.webdriver.support import expected_conditions as ec 
from time import sleep
import pytest
from constants import globalConstants as c

class Test_TobetoLogin():
    def setup_method(self): 
        self.driver = webdriver.Chrome()
        self.driver.get(c.BASE_URL)
        self.driver.maximize_window() 

    def teardown_method(self):
        self.driver.quit()


    @pytest.mark.parametrize("email, password", [("fogacap180@ubinert.com", "abc123456")])
    def test_valid_login(self, email, password):

        firstLoginButton = self.driver.find_element(By.CSS_SELECTOR,c.FIRST_LOGIN_BUTTON)
        firstLoginButton.click()

        emailInput = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.NAME,c.EMAIL_NAME)))
        emailInput.send_keys(email)

        loginButton = self.driver.find_element(By.XPATH,c.LOGIN_BUTTON_XPATH)
        loginButton.click()

        passwordInput = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.NAME,c.PASSWORD_NAME)))
        passwordInput.send_keys(password)

       

        loginMessage = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.CSS_SELECTOR,c.LOGIN_MESSAGE_CSS)))
        assert loginMessage.text == "• Giriş başarılı."

    @pytest.mark.parametrize("email, password", [("fogacap180@ubinert.com", "")])
    def test_invalid_login(self, email, password):

        firstLoginButton = self.driver.find_element(By.CSS_SELECTOR,c.FIRST_LOGIN_BUTTON)
        firstLoginButton.click()

        emailInput = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.NAME,c.EMAIL_NAME)))
        emailInput.send_keys(email)

        passwordInput = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.NAME,c.PASSWORD_NAME)))
        passwordInput.send_keys("")


        loginButton = self.driver.find_element(By.XPATH,c.LOGIN_BUTTON_XPATH)
        loginButton.click()

        errorMessage = self.driver.find_element(By.XPATH,c.ERROR_MESSAGE_XPATH)
        assert errorMessage.text == c.USERNAME_PASSWORD_DONT_MATCH

    @pytest.mark.parametrize("email, password", [("fogacap180@ubinert.com", "abc")])
    def test_invalid_login(self, email, password):

        firstLoginButton = self.driver.find_element(By.CSS_SELECTOR,c.FIRST_LOGIN_BUTTON)
        firstLoginButton.click()

        emailInput = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.NAME,c.EMAIL_NAME)))
        emailInput.send_keys(email)

        passwordInput = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.NAME,c.PASSWORD_NAME)))
        passwordInput.send_keys(password)

        loginButton = self.driver.find_element(By.XPATH,c.LOGIN_BUTTON_XPATH)
        loginButton.click()

    
        errorMessage = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.CSS_SELECTOR,c.ERROR_MESSAGE_CSS)))
        assert errorMessage.text == "• Geçersiz e-posta veya şifre."

    



    
        
