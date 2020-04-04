from selenium import webdriver
import math
import time


link = "http://suninjuly.github.io/math.html"

browser = webdriver.Chrome()
browser.maximize_window()
browser.get(link)

try:
    def calc(x):
      return str(math.log(abs(12*math.sin(int(x)))))

    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)

    answer = browser.find_element_by_id("answer")
    answer.send_keys(y)

    checkBox = browser.find_element_by_id("robotCheckbox").click()
    radioButton = browser.find_element_by_id("robotsRule").click()
    submitButton = browser.find_element_by_css_selector(".btn-default").click()

finally:
    time.sleep(10)
    browser.quit()
