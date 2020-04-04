from selenium import webdriver
from selenium.webdriver.common.by import By
import time


link = "https://motivity.test.motivationportal.ru/"
browser = webdriver.Chrome()
browser.maximize_window()
browser.implicitly_wait(5)
browser.get(link)

try:
    # Sign in
    email = browser.find_element(By.ID, "login").send_keys("mixmax@start2play.ru")
    password = browser.find_element(By.ID, "password").send_keys("mixmax@start2play.ru")
    submit_button = browser.find_element(By.CSS_SELECTOR, "[class=inlay]").click()

    # find section "the king of the mountain"
    fucking_line = browser.find_element(By.CSS_SELECTOR, "[id=sfToolbarHideButton-429148]>svg").click()
    king_of_the_mountain = browser.find_element(By.XPATH, "//b[text()='Стать царём горы!']")
    browser.execute_script("window.scrollBy(0, 100);", king_of_the_mountain)
    king_of_the_mountain.click()
    time.sleep(2)
finally:
    time.sleep(5)
    browser.quit()
