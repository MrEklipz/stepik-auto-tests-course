from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    #Далее хотим найти стоимость на странице, дождаться снижения до 100 и нажать кнопку
    price = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"),"$100")) 
    button = browser.find_element_by_id("book")
    button.click()

    browser.execute_script("window.scrollBy(0, 100);")
    #не забываем посчитать математику, ввести значение и нажать кнопку
    x_element = browser.find_element_by_id("input_value").text
    y = calc(x_element)
        
    input_answer = browser.find_element_by_id("answer")
    input_answer.send_keys(y)

    input_button = browser.find_element_by_id("solve")
    input_button.click()

    time.sleep(1)
    
finally:
    time.sleep(10)
    browser.quit()
