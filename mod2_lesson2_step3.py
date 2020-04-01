from selenium import webdriver
from selenium.webdriver.support.ui import Select
import math
import time

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    num1 = browser.find_element_by_id("num1").text
    num2 = browser.find_element_by_id("num2").text

    final_value = str(int(num1)+ int(num2))
    print(final_value)

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(final_value)

    input_button = browser.find_element_by_tag_name("button").click()

    
finally:
    time.sleep(10)
    browser.quit()
