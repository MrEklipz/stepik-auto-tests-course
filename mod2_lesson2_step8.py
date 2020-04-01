from selenium import webdriver
import time
import os

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input_fname = browser.find_element_by_name("firstname")
    input_fname.send_keys("Ivan")
    
    input_lname = browser.find_element_by_name("lastname")
    input_lname.send_keys("Petrov")
    
    input_email =browser.find_element_by_name("email")
    input_email.send_keys("123@abc.abc")
    
    file_send = browser.find_element_by_id("file")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'text.txt')
    file_send.send_keys(file_path)
    
    input_button = browser.find_element_by_css_selector("button.btn")
    input_button.click()
    
finally:
    time.sleep(10)
    browser.quit()
