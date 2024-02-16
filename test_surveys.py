from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait 
from selenium.webdriver.support import expected_conditions as ec 
from selenium.webdriver.common.keys import Keys
import pytest


class Test_Surveys:

    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://tobeto.com/giris")
        self.driver.maximize_window()

    def teardown_method(self): 
        self.driver.quit()

    @pytest.mark.parametrize("email, password", [("....", ".....")])
    def test_successful_login(self, email, password):
        emailInput = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH, "//*[@id='__next']/div/main/section/div/div/div[1]/div/form/input[1]")))
        emailInput.send_keys(email)
        passwordInput = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH, "//*[@id='__next']/div/main/section/div/div/div[1]/div/form/input[2]")))
        passwordInput.send_keys(password)
        loginButton = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH, "//*[@id='__next']/div/main/section/div/div/div[1]/div/form/button")))
        loginButton.click()
        systemMessage = WebDriverWait(self.driver,5).until(ec.presence_of_element_located((By.XPATH, "//*[@id='__next']/div/div[2]/div/div[2]")))
        assert systemMessage.text == "• Giriş başarılı."
        self.driver.execute_script("window.scrollBy(0, 500);") 
        sleep(2)
        #anketlerim Kontrolü
        survey_button = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID, "mySurvey-tab")))
        self.driver.execute_script("window.scrollBy(0, 100);")   
        survey_button.click()
        sleep(3)
        survey_not_btn = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID, "mySurvey-tab-pane")))
        assert survey_not_btn.text == 'Atanmış herhangi bir anketiniz bulunmamaktadır'

