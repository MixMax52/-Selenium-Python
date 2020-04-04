from selenium import webdriver
import time
import math


link = "http://suninjuly.github.io/execute_script.html"
browser = webdriver.Chrome()
browser.maximize_window()
browser.get(link)

try:
    number_x = browser.find_element_by_css_selector("#input_value").text
    question = str(math.log(abs(12*math.sin(int(number_x)))))
    enter_answer = browser.find_element_by_id("answer").send_keys(question)
    checkBox = browser.find_element_by_id("robotCheckbox").click()
    radioButton = browser.find_element_by_id("robotsRule")
    radioButton_view = browser.execute_script("return arguments[0].scrollIntoView(true);", radioButton)
    radioButton.click()
    button_submit = browser.find_element_by_css_selector("[type=submit]")
    scroll_to_button_submit = browser.execute_script("return arguments[0].scrollIntoView(true);", button_submit)
    button_submit.click()

finally:
    time.sleep(20)
    browser.quit()
