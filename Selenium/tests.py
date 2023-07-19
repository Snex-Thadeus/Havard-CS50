import os
import pathlib
import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

from selenium import webdriver

# Finds the Uniform Resourse Identifier of a file
def file_uri(filename):
    return pathlib.Path(os.path.abspath(filename)).as_uri()

# Sets up web driver using Google chrome
driver = webdriver.Chrome()
driver.maximize_window()

wait = WebDriverWait(driver, 10)


# Standard outline of testing class
class WebpageTests(unittest.TestCase):

    def test_title(self):
        """Make sure title is correct"""
        driver.get(file_uri("counter.html"))
        self.assertEqual(driver.title, "Counter")

    def test_increase(self):
        """Make sure header updated to 1 after 1 click of increase button"""
        driver.get(file_uri("counter.html"))
        increase = driver.find_element(By.ID,"increase")
        increase.click()
        self.assertEqual(driver.find_element(By.TAG_NAME,"h1").text, "1")

    def test_decrease(self):
        """Make sure header updated to -1 after 1 click of decrease button"""
        driver.get(file_uri("counter.html"))
        decrease = driver.find_element(By.ID,"decrease")
        decrease.click()
        self.assertEqual(driver.find_element(By.TAG_NAME,"h1").text, "-1")

    def test_multiple_increase(self):
        """Make sure header updated to 3 after 3 clicks of increase button"""
        driver.get(file_uri("counter.html"))
        increase = driver.find_element(By.ID,"increase")
        for i in range(3):
            increase.click()
        self.assertEqual(driver.find_element(By.TAG_NAME,"h1").text, "3")

if __name__ == "__main__":
    unittest.main()