from selenium import webdriver
import math
import time

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    chest = browser.find_element_by_id("treasure")
    valuex = chest.get_attribute("valuex")
    func_answer = calc(valuex)
    print(valuex)
    print(func_answer)
    
    input_answer = browser.find_element_by_id("answer")
    input_answer.send_keys(func_answer)

    input_checkbox = browser.find_element_by_id("robotCheckbox")
    input_checkbox.click()

    input_radio = browser.find_element_by_id("robotsRule")
    input_radio.click()

    input_button = browser.find_element_by_css_selector("button.btn")
    input_button.click()

    time.sleep(1)    
    
finally:
    time.sleep(10)
    browser.quit()
