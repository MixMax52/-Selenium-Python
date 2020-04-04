from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

browser = webdriver.Chrome()
browser.maximize_window()
browser.implicitly_wait(15)
browser.get("http://suninjuly.github.io/explicit_wait2.html")

try:
    price_house = browser.find_element_by_id("price")
    nice_price = EC.text_to_be_present_in_element((By.ID, "price"), "$100")

    WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )


    assert "successful" in nice_price.text

    book_button = browser.find_element_by_id("book").click()

finally:
    time.sleep(5)
    browser.quit()
