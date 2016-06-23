from selenium import webdriver
from django.test import TestCase
import os

class SignupTests(TestCase):
    driver = webdriver.PhantomJS()
    
    def teardown(self):
        self.driver.quit()
        
    def login(self, driver, user, password):
        driver.find_element_by_id("id_username").send_keys(user)
        driver.find_element_by_id("id_password").send_keys(password)
        driver.find_element_by_id("login").click()
        
    def signup(self, driver, user, password):
        page_url = "http://" + os.getenv('C9_HOSTNAME') + "/accounts/register" 
        
        driver.get(page_url)
        driver.find_element_by_id("id_username").send_keys(user)
        driver.find_element_by_id("id_password1").send_keys(password)
        driver.find_element_by_id("id_password2").send_keys(password)
        driver.find_element_by_id("register").click()
        
    def test_new_user(self):
        page_url = "http://" + os.getenv('C9_HOSTNAME') + "/game/"
        accounts_url = "http://" + os.getenv('C9_HOSTNAME') + "/" +"accounts/"

        self.driver.set_window_size(1120, 550)
        
        self.driver.get(page_url)
        self.driver.find_element_by_id('signup').click();
        self.assertEqual(accounts_url + 'register/', self.driver.current_url)
        
        self.signup(self.driver, 'test2', 'test')
        self.assertRegexpMatches(self.driver.current_url, accounts_url + 'login' + '.*')
        
        self.login(self.driver, 'test2', 'test')
        self.assertEqual(page_url, self.driver.current_url)