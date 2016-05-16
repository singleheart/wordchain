from selenium import webdriver
from django.test import TestCase
import socket

class FirstTests(TestCase):
    def test_play_with_no_login(self):
        username, projectname, _ = socket.gethostname().split('-')
        page_url = "http://" + projectname + "-" + username + ".c9.io/"
        print(page_url)

        driver = webdriver.PhantomJS()
        driver.set_window_size(1120, 550)
        
        driver.get(page_url)
        driver.find_element_by_id("play").click()
        self.assertEqual(page_url+"accounts/login/?next=/game/", driver.current_url)
        driver.quit()
