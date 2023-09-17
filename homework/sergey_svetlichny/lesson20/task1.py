# Напишите программку, которая заходит на вот эту страницу:
# https://www.qa-practice.com/elements/input/simple, вводит какой-то текст в поле, делает submit , а после этого
# находит элемент, в котором отображается тот текст, который был введен и рапечатывает этот текст.
import random
import string
# import time

from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.options import Options
#
# chrome_options = Options()
# chrome_options.add_experimental_option('detach', True)
# driver = webdriver.Chrome(options=chrome_options)

driver = webdriver.Chrome()


def test_input_text_is_in_results():
    driver.get('https://www.qa-practice.com/elements/input/simple')
    search_input = driver.find_element(By.XPATH, "//input[@name='text_string']")
    text_input = "".join(random.choice(string.ascii_lowercase) for _ in range(10))
    search_input.send_keys(text_input)
    search_input.submit()
    result = driver.find_element(By.XPATH, f"//*[text() = '{text_input}']")
    print(result.text)
    assert text_input == result.text

    # result_area = driver.find_element(By.CLASS_NAME, 'result')
    # input_result = result_area.find_element(By.CLASS_NAME, 'result-text').text
    # time.sleep(1)
    # assert text_input == input_result


test_input_text_is_in_results()
