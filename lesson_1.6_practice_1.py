from selenium import webdriver
import time


try:
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.get(link)

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

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(5)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
