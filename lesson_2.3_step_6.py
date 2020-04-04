from selenium import webdriver
import time
import math


link = "http://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Chrome()
browser.maximize_window()
browser.get(link)

try:
    first_button = browser.find_element_by_css_selector("[type=submit]").click()
    second_window = browser.window_handles[1]
    browser.switch_to.window(second_window)

    def calc(number):
        return str(math.log(abs(12*math.sin(int(number)))))

    number = browser.find_element_by_css_selector("[id=input_value]").text
    answer = calc(number)

    answer_line = browser.find_element_by_css_selector("[id=answer]").send_keys(answer)
    submit_button = browser.find_element_by_css_selector("[type=submit]").click()

finally:
    time.sleep(10)
    browser.quit()
