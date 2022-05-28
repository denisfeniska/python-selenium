from selenium import webdriver
# from selenium.webdriver.support.ui import Select
import time
import math
# import os


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/alert_accept.html"


try:
    driver = webdriver.Chrome(
        executable_path=r"D:\Microsoft VS Code\VS projects\selenium\stepik_course\chromdriver\chromedriver.exe")

    driver.get(link)

    button1 = driver.find_element_by_tag_name("button").click()

    alert = driver.switch_to.alert
    alert.accept()

    x = driver.find_element_by_id("input_value").text
    res = calc(x)

    input_space = driver.find_element_by_id("answer").send_keys(res)

    submit_button = driver.find_element_by_tag_name("button").click()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    driver.quit()

# не забываем оставить пустую строку в конце файла
