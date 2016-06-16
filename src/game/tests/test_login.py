from selenium import webdriver
from django.test import TestCase
import os

class LoginTests(TestCase):
        
    def login(self, driver, user, password, nextPage=''):
        page_url = "http://" + os.getenv('C9_HOSTNAME') + "/" 
        
        driver.get(page_url + "accounts/login/" + nextPage)
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
        
    def test_logout(self):
        page_url = "http://" + os.getenv('C9_HOSTNAME') + "/game/"
        accounts_url = "http://" + os.getenv('C9_HOSTNAME') + "/" +"accounts/"

        driver = webdriver.PhantomJS()
        driver.set_window_size(1120, 550)
        
        driver.get(page_url)

        self.login(driver, 'test', 'test', '?next=/game/')
        self.assertEqual(page_url, driver.current_url)
        
        driver.find_element_by_id("logout").click()
        self.assertRegexpMatches(driver.current_url, accounts_url + 'login' + '.*')

        driver.quit()
