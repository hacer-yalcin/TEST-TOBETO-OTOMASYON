from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait 
from selenium.webdriver.support import expected_conditions as ec 
from selenium.webdriver.common.keys import Keys
import pytest

class Test_Notification:

    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://tobeto.com/giris")
        self.driver.maximize_window()
        
    def teardown_method(self): 
        self.driver.quit()

    @pytest.mark.parametrize("email, password", [("...", "....")])
    def test_successful_login(self, email, password):
        emailInput = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH, "//*[@id='__next']/div/main/section/div/div/div[1]/div/form/input[1]")))
        emailInput.send_keys(email)
        passwordInput = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH, "//*[@id='__next']/div/main/section/div/div/div[1]/div/form/input[2]")))
        passwordInput.send_keys(password)
        loginButton = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH,  "//*[@id='__next']/div/main/section/div/div/div[1]/div/form/button")))
        loginButton.click()
        systemMessage = WebDriverWait(self.driver,5).until(ec.presence_of_element_located((By.XPATH, "//*[@id='__next']/div/div[2]/div/div[2]")))
        assert systemMessage.text == "• Giriş başarılı."
        self.driver.execute_script("window.scrollBy(0, 500);") 
        sleep(2)
        # Duyuru ve Haber Kontrolü
        notification_button = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID, "notification-tab")))
        notification_button.click()
        sleep(3)
        # Daha fazla göster 
        showmorebutton = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH, "//*[@id='notification-tab-pane']/div/div[4]")))
        showmorebutton.click()
        notifications = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH, "//*[@id='__next']/div/main/div[1]/div")))
        assert notifications.text == "Duyurularım"
        sleep(3)
        # arama butonu 
        search_btn = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID, "search")))
        search_btn.send_keys("Ocak")
        sleep(2)
        filtre_btn = notifications = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH, "//*[@id='__next']/div/main/div[2]/div[2]/div[1]/div")))
        assert 'Ocak' in filtre_btn.text      
        sleep(5)
        # arama butonu temizleme
        search_btn = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID, "search")))
        search_btn.clear()
        sleep(5)
        # Duyuru bulunmamaktadır
        search_btn = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID, "search")))
        search_btn.send_keys("sınav")
        sleep(3)
        search_not_btn = WebDriverWait(self.driver, 5).until(ec.presence_of_element_located((By.XPATH, "//*[@id='__next']/div/main/div[2]/div[2]/div/p")))
        assert search_not_btn.text == 'Bir duyuru bulunmamaktadır.'
        sleep(3)
        # sayfa yenile
        self.driver.get("https://tobeto.com/duyurular")
        self.driver.refresh()
        sleep(5)

        # tür seçme

        type_button = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH, "//*[@id='__next']/div/main/div[2]/div[1]/div/div[2]/button")))
        type_button.click()
        sleep(3)
        type_button = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH, "//*[@id='__next']/div/main/div[2]/div[1]/div/div[2]/ul/li[2]/div")))
        type_button.click()
        
        sleep(2)
        self.driver.get("https://tobeto.com/duyurular")
        self.driver.refresh()
        sleep(5)
       # organizasyon seçme 
        organization_button = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH, "//*[@id='__next']/div/main/div[2]/div[1]/div/div[3]/div[1]/div[1]/div[2]")))
        organization_button.click()
        sleep(3)
        self.driver.get("https://tobeto.com/duyurular")
        self.driver.refresh()
        sleep(5)
       # sıralama butonu
        line_up = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH, "//*[@id='__next']/div/main/div[2]/div[1]/div/div[4]/div[1]/button")))
        line_up.click()
        sleep(3)
        line_up= WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH, "//*[@id='__next']/div/main/div[2]/div[1]/div/div[4]/div[1]/ul/li[2]/a")))
        line_up.click()
        sleep(3)
        line_filtre = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH, "//*[@id='__next']/div/main/div[2]/div[2]/div[1]/div/div[2]/span[1]")))
        assert line_filtre.text == '27.09.2023'
    


     
        
      


    
