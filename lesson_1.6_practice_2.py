from selenium import webdriver
import time


try:
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.get(link)

    # fill in the form
    input_first_name = browser.find_element_by_css_selector(".first_block .form-control.first")
    input_first_name.send_keys("Ivan")
    input_second_name = browser.find_element_by_css_selector(".first_block .form-control.second")
    input_second_name.send_keys("Petrov")
    input_email = browser.find_element_by_css_selector(".first_block .form-control.third")
    input_email.send_keys("Smolensk@mail.ru")
    input_phone = browser.find_element_by_css_selector(".second_block .form-control.first")
    input_phone.send_keys("+79201112233")
    input_address = browser.find_element_by_css_selector(".second_block .form-control.second")
    input_address.send_keys("Town city")

    # sending the form
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # waiting load the page
    time.sleep(5)

    # find result and record it to variable "welcome_text"
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    welcome_text = welcome_text_elt.text

    # check result
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(10)
    browser.quit()
