from selenium import webdriver
from django.test import TestCase
import os

class FirstTests(TestCase):
    def test_play_with_no_login(self):
        page_url = "http://" + os.getenv('C9_HOSTNAME') + "/"

        driver = webdriver.PhantomJS()
        driver.set_window_size(1120, 550)
        
        driver.get(page_url)
        driver.find_element_by_id("play").click()
        self.assertEqual(page_url+"accounts/login/?next=/game/", driver.current_url)
        driver.quit()
        
    def login(self, driver):
        page_url = "http://" + os.getenv('C9_HOSTNAME') + "/" 
        
        driver.get(page_url + "accounts/login/?next=/game/")
        driver.find_element_by_id("id_username").send_keys("test")
        driver.find_element_by_id("id_password").send_keys("test")
        driver.find_element_by_id("login").click()
        
    def test_play_with_login(self):
        driver = webdriver.PhantomJS()
        driver.set_window_size(1120, 550)
        
        self.login(driver)
        
        page_url = "http://" + os.getenv('C9_HOSTNAME') + "/"
        driver.get(page_url)
        driver.find_element_by_id("play").click()
        self.assertEqual(page_url + "game/", driver.current_url)
        
        driver.quit()