from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time


link = "http://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()  # open Chrome browser
browser.maximize_window()  # open browser to maximize window
browser.get(link)  # open web site

try:
    num_1 = browser.find_element_by_id("num1")
    x = num_1.text
    num_2 = browser.find_element_by_id("num2")
    y = num_2.text
    summ_num = str(int(x) + int(y))

    select = Select(browser.find_element_by_id("dropdown"))
    select.select_by_value(summ_num)

    submit_button = browser.find_element_by_css_selector("[type=submit]").click()

finally:
    time.sleep(10)
    browser.quit()
