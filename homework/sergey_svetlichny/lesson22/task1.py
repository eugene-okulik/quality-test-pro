# Напишите три теста:
#
# Первый тест
# https://www.demoblaze.com/index.html
#
# откройте товар в новой вкладке
# Перейдите на вкладку с товаром
# Добавьте товар в корзину
# Закройте вкладку с товаром
# На начальной вкладке откройте корзину
# Убедитесь, что в корзине тот товар, который вы добавляли

# Второй тест
# https://demoqa.com/menu# выбрать Main item2 -> SUB SUB List -> Sub Sub Item 2 - здесь никакого ассерта не получится
# # сделать
#
# Третий тест
# На странице https://demoqa.com/dynamic-properties нажать на первую кнопку тогда, когда она станет enabled.
# И здесь тоже никакого ассерта сделать не получится.

# Да, там беда с ним какая-то приключилась.
# Давай тогда такое задание вместо того:
# На странице https://the-internet.herokuapp.com/dynamic_controls нажать кнопку enable и ввести текст в поле после того
# как это поле станет доступным для ввода


import time

from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = Options()
# chrome_options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=chrome_options)
driver.implicitly_wait(10)


def test_put_in_cart():
    driver.get('https://www.demoblaze.com/index.html')
    links = driver.find_elements(By.XPATH, "//div[@class='card-block']/h4/a")
    link = links[0]
    good_name_to_open = link.text
    print(good_name_to_open)
    ActionChains(driver).key_down(Keys.CONTROL).click(link).key_up(Keys.CONTROL).perform()
    driver.switch_to.window(driver.window_handles[1])
    driver.find_element(By.LINK_TEXT, 'Add to cart').click()
    WebDriverWait(driver, 5).until(EC.alert_is_present(), 'Timed out waiting for simple alert to appear')
    alert = Alert(driver)
    print(alert.text)
    alert.accept()
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    driver.find_element(By.LINK_TEXT, 'Cart').click()
    good_name_in_cart = driver.find_element(By.XPATH, "//*[@class='success']/td[2]").text
    print(good_name_in_cart)
    assert good_name_in_cart == good_name_to_open


def test_opening_demoqa():
    try:
        driver.get('https://demoqa.com/menu#')
    except Exception as e:
        print("The site is unavailable, error: ", e)


def test_wait_for_input_enabling():
    driver.get('https://the-internet.herokuapp.com/dynamic_controls')
    driver.find_element(By.XPATH, "//button[contains(text(),'Enable')]").click()
    text_input = driver.find_element(By.XPATH, "//input[@type='text']")
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable(text_input), 'Timed out waiting for text_input enabled')
    text_input.send_keys('Inputted text')


def test_open_menu_with_action_chains():
    driver.get('https://demoqa.com/menu#')
    main_item2 = driver.find_element(By.XPATH, "//a[contains(text(),'Main Item 2')]")
    sub_sub_list = driver.find_element(By.XPATH, "//a[contains(text(),'SUB SUB LIST »')]")
    sub_sub_item2 = driver.find_element(By.XPATH, "//a[contains(text(),'Sub Sub Item 2')]")
    actions = ActionChains(driver)
    actions.move_to_element(main_item2)
    actions.move_to_element(sub_sub_list)
    actions.click(sub_sub_item2)
    actions.perform()
