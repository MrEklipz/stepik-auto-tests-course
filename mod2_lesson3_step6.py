from selenium import webdriver
import math
import time

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    troll_button = browser.find_element_by_css_selector("button.trollface")
    troll_button.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x_element = browser.find_element_by_id("input_value").text
    y = calc(x_element)
        
    input_answer = browser.find_element_by_id("answer")
    input_answer.send_keys(y)

    input_button = browser.find_element_by_css_selector("button.btn")
    input_button.click()

    time.sleep(1)
    
finally:
    time.sleep(10)
    browser.quit()
