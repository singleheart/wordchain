from selenium import webdriver
from django.test import TestCase

class FirstTests(TestCase):
    def test_play_with_no_login(self):
        page_url = "https://wordchain-lonelywolflee-1.c9users.io/"

        driver = webdriver.PhantomJS()
        driver.set_window_size(1120, 550)
        
        driver.get(page_url)
        driver.find_element_by_id("play").click()
        self.assertEqual("https://wordchain-lonelywolflee-1.c9users.io/accounts/login/?next=/game/", driver.current_url)
        driver.quit()
