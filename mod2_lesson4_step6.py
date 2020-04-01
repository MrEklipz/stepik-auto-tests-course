from selenium import webdriver
import time

try:
    link = "http://suninjuly.github.io/cats.html"
    browser = webdriver.Chrome()
    browser.get(link)

    find_the_button = browser.find_element_by_id("button")
    find_the_button.click()

    time.sleep(1)

finally:
    time.sleep(10)
    browser.quit()

