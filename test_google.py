from selenium import webdriver  # Import webdriver
import unittest  # Library for tests
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time

from config import CHROME_WEBDRIVER_PATH


class GoogleSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(CHROME_WEBDRIVER_PATH)


    def test_find_titles(self):
        self.driver.get('https://www.google.com/')
        input_field = self.driver.find_element_by_id('lst-ib')

        input_field.send_keys('python')
        input_field.send_keys(Keys.ENTER)

        time.sleep(2)

        titles = self.driver.find_elements_by_class('r')
        for title in titles:
            assert "python" in title.text.lower()

    def test_find_titles2(self):
        self.driver.get('https://www.google.com/search?q=python')
        input_field = self.driver.find_element_by_xpath('/html/body/div/div[3]/form/div[2]/div/div[1]/div/div[1]/input')
        assert len(input_field)>0

        input_field = input_field[0]
        input_field.send_keys('python')

        time.sleep(1)

        input_field.send_keys(Keys.DOWN)
        input_field.send_keys(Keys.ENTER)

        time.sleep(2)

        title = self.driver.find_elements_by_class_name('r')
        assert title is not None

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
