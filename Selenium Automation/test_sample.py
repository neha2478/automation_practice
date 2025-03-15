# tests/test_sample.py
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

class TestSampleWebsite(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Set up the Chrome driver
        cls.driver = webdriver.Chrome()
        cls.driver.get('http://127.0.0.1:8000/')  # Adjust the URL as needed

    @classmethod
    def tearDownClass(cls):
        # Close the browser window
        cls.driver.quit()

    def test_home_page(self):
        # Test the home page content
        self.assertIn('Welcome to the Sample Website', self.driver.page_source)

    def test_form_submission(self):
        # Test form submission
        input_field = self.driver.find_element(By.ID, 'inputData')
        submit_button = self.driver.find_element(By.XPATH, '//button[text()="Submit"]')
        input_field.send_keys('Test Data')
        submit_button.click()
        time.sleep(2)  # Wait for the form to submit and page to reload
        # Add assertions to verify the form submission
        # For example, check if a success message appears
        # success_message = self.driver.find_element(By.ID, 'successMessage')
        # self.assertTrue(success_message.is_displayed())

    def test_json_data_display(self):
        # Test if JSON data is displayed
        json_data_div = self.driver.find_element(By.ID, 'jsonData')
        self.assertTrue(json_data_div.is_displayed())
        # Optionally, verify the content of the JSON data
        # json_content = json_data_div.text
        # self.assertIn('John Doe', json_content)

if __name__ == '__main__':
    unittest.main()
