from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from tkinter import Tk


chrome_options = Options()
chrome_options.add_experimental_option('detach', True)
chrome_options.add_argument('start-maximized')
driver = webdriver.Chrome(options=chrome_options)
sleep(3)
# driver.maximize_window()
# driver.set_window_size(800, 1080)
# driver.set_window_size(1920, 1080)


def google():
    driver.get('https://www.google.com/')
    print(driver.title)
    print(driver.current_url)
    other_langs = driver.find_element(By.ID, 'gws-output-pages-elements-homepage_additional_languages__als')
    lang_link = other_langs.find_elements(By.TAG_NAME, 'a')
    print(lang_link[0].text)
    for x in lang_link:
        print(x.text)
    sleep(2)
    search_field = driver.find_element(By.NAME, 'q')
    data = 'dog'
    search_field.send_keys(data)
    search_field.submit()
    # search_field.send_keys(Keys.CONTROL + 'a')
    # search_field.send_keys(Keys.CONTROL + 'c')
    # search_field.send_keys(Keys.CONTROL + 't')
    # search_field.send_keys(Keys.CONTROL + 'v')
    assert f'q={data}' in driver.current_url
    # print(Tk().clipboard_get())


def searches():
    driver.get('https://www.qa-practice.com/elements/button/simple')
    # button = driver.find_element(By.ID, 'submit-id-submit')
    button = driver.find_element(By.CLASS_NAME, 'btn')
    button.click()
    title = driver.find_element(By.TAG_NAME, 'h1')
    print(title.text)


google()
