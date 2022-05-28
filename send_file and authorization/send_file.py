from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math
import os


link = "http://suninjuly.github.io/file_input.html"



try:
    driver = webdriver.Chrome(
        executable_path=r"D:\Microsoft VS Code\VS projects\selenium\stepik_course\chromdriver\chromedriver.exe")

    driver.get(link)

    text_buttons = driver.find_elements_by_class_name("form-control")

    text_button1 = text_buttons[0]
    text_button1.send_keys("Den")

    text_button2 = text_buttons[1]
    text_button2.send_keys("Smekta")

    text_button3 = text_buttons[2]
    text_button3.send_keys("1241313@mail.ru")

    with open("selenium/stepik_course/text.txt", "w", encoding='utf8') as file:
        file.write("text")

    file_path = os.path.join(r"D:\Microsoft VS Code\VS projects\selenium\stepik_course", 'text.txt')

    file_button = driver.find_element_by_id("file").send_keys(file_path)
    
    submit = driver.find_element_by_tag_name("button").click()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    driver.quit()

# не забываем оставить пустую строку в конце файла
