import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_alert_accept(browser):
    browser.get("https://the-internet.herokuapp.com/javascript_alerts")

    browser.find_element(By.XPATH, "//button[text()= 'Click for JS Alert']").click()

    alert = browser.switch_to.alert
    time.sleep(1)

    alert.accept()

    result_text = browser.find_element(By.ID, "result").text
    assert result_text == "You successfully clicked an alert"

def test_alert_dismiss(browser):
    browser.get("https://the-internet.herokuapp.com/javascript_alerts")
    browser.find_element(By.XPATH, "//button[text()= 'Click for JS Confirm']").click()
    alert = browser.switch_to.alert
    time.sleep(1)

    alert.dismiss()

    result_text = browser.find_element(By.ID, "result").text
    assert result_text == "You clicked: Cancel"

def test_alert_send_text(browser):

    browser.get("https://the-internet.herokuapp.com/javascript_alerts")
    browser.find_element(By.XPATH, "//button[text()= 'Click for JS Prompt']").click()
    alert = browser.switch_to.alert
    time.sleep(1)

    alert.send_keys("Welcome to my Junior QA")
    alert.accept()

    result_text = browser.find_element(By.ID, "result").text
    assert "Welcome to my Junior QA" in result_text



