from selenium import webdriver
import time
import os


link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.maximize_window()
browser.get(link)

try:
    first_name = browser.find_element_by_css_selector("[name=firstname]").send_keys("Volodiya")
    last_name = browser.find_element_by_css_selector("[name=lastname]").send_keys("Dodikov")
    email = browser.find_element_by_css_selector("[name=email]").send_keys("Dodik@mail.ru")

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, "For_lesson_2.2_step_8.txt")

    Choose_file_button = browser.find_element_by_css_selector("[type=file]")
    Choose_file_button.send_keys(file_path)

    submit_button = browser.find_element_by_css_selector("[type=submit]").click()

finally:
    time.sleep(10)
    browser.quit()
