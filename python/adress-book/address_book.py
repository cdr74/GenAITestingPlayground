# COPILOT: "Create the python selenium tests"
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class TestAddressBook:
    def setup_method(self):
        self.driver = webdriver.Firefox()
        self.vars = {}

    def teardown_method(self):
        self.driver.quit()

    def test_add_contact(self):
        self.driver.get("http://yourwebsite.com/new_contact")
        self.driver.find_element(By.ID, "first_name").send_keys("John")
        self.driver.find_element(By.ID, "last_name").send_keys("Smith")
        self.driver.find_element(By.ID, "phone_number").send_keys("1234567890")
        self.driver.find_element(By.ID, "address").send_keys("123 St")
        self.driver.find_element(By.ID, "submit").click()
        WebDriverWait(self.driver, 10).until(
            EC.text_to_be_present_in_element((By.ID, "success_message"), "Success")
        )
        assert "John Smith" in self.driver.page_source
        assert "1234567890" in self.driver.page_source

    def test_export_contact(self):
        self.driver.get("http://yourwebsite.com/contacts")
        self.driver.find_element(By.LINK_TEXT, "John").click()
        self.driver.find_element(By.ID, "export").click()
        WebDriverWait(self.driver, 10).until(
            EC.text_to_be_present_in_element((By.ID, "success_message"), "Success")
        )

    def test_delete_contact(self):
        self.driver.get("http://yourwebsite.com/contacts")
        self.driver.find_element(By.LINK_TEXT, "John").click()
        self.driver.find_element(By.ID, "delete").click()
        WebDriverWait(self.driver, 10).until(
            EC.text_to_be_present_in_element((By.ID, "success_message"), "Success")
        )
        assert "John Smith" not in self.driver.page_source
