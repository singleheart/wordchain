from selenium import webdriver
from django.test import TestCase
import os

class FirstTests(TestCase):
    def test_play_with_no_login(self):
        page_url = "http://" + os.getenv('C9_HOSTNAME') + "/"
        print(page_url)

        driver = webdriver.PhantomJS()
        driver.set_window_size(1120, 550)
        
        driver.get(page_url)
        driver.find_element_by_id("play").click()
        self.assertEqual(page_url+"accounts/login/?next=/game/", driver.current_url)
        driver.quit()
