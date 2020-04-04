from selenium import webdriver
import math
import time


browser = webdriver.Chrome()
browser.maximize_window()
link = "http://suninjuly.github.io/get_attribute.html"
browser.get(link)

try:
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    value_chest = browser.find_element_by_id("treasure")
    x = value_chest.get_attribute("valuex")
    answer = calc(x)


    enter_answer = browser.find_element_by_id("answer")
    enter_answer.send_keys(answer)

    checkBox = browser.find_element_by_id("robotCheckbox").click()
    radioButton = browser.find_element_by_id("robotsRule").click()
    Submit_button = browser.find_element_by_css_selector("[type=submit]").click()

finally:
    time.sleep(10)
    browser.quit()
