from selenium import webdriver
from django.test import TestCase
import os

class LoginTests(TestCase):
        
    def login(self, driver, user, password):
        page_url = "http://" + os.getenv('C9_HOSTNAME') + "/" 
        
        driver.get(page_url + "accounts/login/")
        driver.find_element_by_id("id_username").send_keys(user)
        driver.find_element_by_id("id_password").send_keys(password)
        driver.find_element_by_id("login").click()
        
    def test_false_user(self):
        page_url = "http://" + os.getenv('C9_HOSTNAME') + "/" +"accounts/login/"

        driver = webdriver.PhantomJS()
        driver.set_window_size(1120, 550)
        
        driver.get(page_url)
        self.login(driver, "nobody", "None")
        self.assertEqual(page_url, driver.current_url)
        driver.quit()