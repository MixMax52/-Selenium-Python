import math
from selenium import webdriver
import time


result = str(math.ceil(math.pow(math.pi, math.e)*10000))
link = "http://suninjuly.github.io/find_link_text"

try:
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.get(link)

    # find text of task
    link = browser.find_element_by_partial_link_text(result)
    link.click()

    # fill in the form
    input1 = browser.find_element_by_name("first_name")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_name("last_name")
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_class_name("city")
    input3.send_keys("Smolensk")
    input4 = browser.find_element_by_id("country")
    input4.send_keys("Russia")
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    time.sleep(20)
finally:
    browser.quit()
