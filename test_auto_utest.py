import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

class suite_utest(unittest.TestCase):
    def setUp(self):
        service = Service('C:\\chrome_driver\\chromedriver.exe')
        self.driver = webdriver.Chrome(service=service)



    def test_form(self):
        driver = self.driver
        driver.get('https://utest.com/')
        driver.maximize_window()
        time.sleep(1)
        buttom_join = driver.find_element(By.XPATH, '/html/body/ui-view/unauthenticated-container/div/div/unauthenticated-header/div/div[3]/ul[2]/li[2]/a')
        time.sleep(1)
        buttom_join.click()
        time.sleep(1)
        cam_f_name = driver.find_element(By.XPATH,'//*[@id="firstName"]')
        cam_f_name.send_keys('cholo')
        cam_f_name.send_keys(Keys.TAB)
        time.sleep(1)
        cam_f_last_name = driver.find_element(By.XPATH,'//*[@id="lastName"]')
        cam_f_last_name.send_keys('gilbert')
        cam_f_last_name.send_keys(Keys.TAB)
        time.sleep(1)
        cam_f_email = driver.find_element(By.XPATH,'//*[@id="email"]')
        cam_f_email.send_keys('alda092021@gmail.com')
        cam_f_email.send_keys(Keys.TAB)
        time.sleep(1)
        camp_mounth = driver.find_element(By.XPATH,'//*[@id="birthMonth"]')
        time.sleep(1)
        camp_mounth = Select(camp_mounth)
        time.sleep(1)
        camp_mounth.select_by_value('number:5')
        time.sleep(1)
        camp_day = driver.find_element(By.XPATH,'//*[@id="birthDay"]')
        time.sleep(1)
        camp_day = Select(camp_day)
        camp_day.select_by_value('number:5')
        time.sleep(1)
        camp_year = driver.find_element(By.XPATH,'//*[@id="birthYear"]')
        time.sleep(1)
        camp_year = Select(camp_year)
        time.sleep(1)
        camp_year.select_by_value('number:1995')
        time.sleep(1)
        buttom_next_location = driver.find_element(By.XPATH,'//*[@id="regs_container"]/div/div[2]/div/div[2]/div/form/div[2]/a/span')
        buttom_next_location.click()
        time.sleep(3)
        button_zip_code = driver.find_element(By.XPATH,'//*[@id="zip"]')
        button_zip_code.send_keys('507')
        time.sleep(1)
        button_next_device = driver.find_element(By.XPATH,'//*[@id="regs_container"]/div/div[2]/div/div[2]/div/form/div[2]/div/a/span')
        button_next_device.click()
        time.sleep(3)
        camp_mobile_device = driver.find_element(By.XPATH,'//*[@id="mobile-device"]/div[1]/div[2]/div/div[1]/span')
        camp_mobile_device.click()
        time.sleep(2)
        selection_device = driver.find_element(By.XPATH,'/html/body/ui-view/main/section/div/div[2]/div/div[2]/div/div[1]/div[3]/div[2]/div[1]/div[2]/div/ul/li/div[5]/span/div') # Use the full XPATH for have find the element
        selection_device.click()
        time.sleep(1)
        camp_model_device = driver.find_element(By.XPATH,'//*[@id="mobile-device"]/div[2]/div[2]/div/div[1]/span/span[1]')
        camp_model_device.click()
        time.sleep(1)
        selection_model = driver.find_element(By.XPATH,'/html/body/ui-view/main/section/div/div[2]/div/div[2]/div/div[1]/div[3]/div[2]/div[2]/div[2]/div/ul/li/div[18]/span/div')
        selection_model.click()
        time.sleep(1)
        camp_operating = driver.find_element(By.XPATH,'//*[@id="mobile-device"]/div[3]/div[2]/div/div[1]/span')
        camp_operating.click()
        time.sleep(1)
        selection_sys = driver.find_element(By.XPATH,'/html/body/ui-view/main/section/div/div[2]/div/div[2]/div/div[1]/div[3]/div[2]/div[3]/div[2]/div/ul/li/div[10]/span/div')
        selection_sys.click()
        time.sleep(1)
        button_last_step = driver.find_element(By.XPATH,'//*[@id="regs_container"]/div/div[2]/div/div[2]/div/div[2]/div/a/span')
        button_last_step.click()
        time.sleep(1)
        camp_pass = driver.find_element(By.XPATH,'//*[@id="password"]')
        camp_pass.send_keys('juanfong092010*PUCCA')
        camp_pass_con = driver.find_element(By.XPATH,'//*[@id="confirmPassword"]')
        time.sleep(1)
        camp_pass_con.send_keys('juanfong092010*PUCCA')
        time.sleep(1)
        toggle_read_term = driver.find_element(By.XPATH,'//*[@id="regs_container"]/div/div[2]/div/div[2]/div/form/div[5]/label/span[1]')
        toggle_read_term.click()
        time.sleep(1)
        toggle_read_priv = driver.find_element(By.XPATH,'//*[@id="regs_container"]/div/div[2]/div/div[2]/div/form/div[6]/label/span[1]')
        toggle_read_priv.click()
        time.sleep(1)
        buttom_complete = driver.find_element(By.XPATH,'//*[@id="laddaBtn"]/span')
        buttom_complete.click()
        time.sleep(4)




    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()

