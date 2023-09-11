from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


chrome_options = Options()
chrome_options.add_experimental_option('detach', True)
chrome_options.add_argument('start-maximized')
driver = webdriver.Chrome(options=chrome_options)
driver.implicitly_wait(3)
sleep(3)


def searches():
    driver.get('https://www.qa-practice.com/')
    driver.find_element(By.PARTIAL_LINK_TEXT, 'Simple').click()
    # button = driver.find_element(By.CSS_SELECTOR, '[class="btn btn-primary"]')
    button = driver.find_element(By.XPATH, '//input[@type="submit"]')
    print(button.id)
    print(button.get_attribute('value'))
    print(button.value_of_css_property('background-color'))
    print(button.tag_name)
    button.click()
    title = driver.find_element(By.CSS_SELECTOR, 'h1')
    print(title.text)
    print(title.get_attribute('innerText'))
    hidden = driver.find_element(By.NAME, 'csrfmiddlewaretoken')
    print(hidden.is_displayed())
    button = driver.find_element(By.XPATH, '//input[@type="submit"]')
    print(button.is_displayed())
    driver.get('https://www.qa-practice.com/elements/button/disabled')
    button = driver.find_element(By.XPATH, '//input[@type="submit"]')
    print(button.is_enabled())
    select_element = driver.find_element(By.ID, 'id_select_state')
    dropdown = Select(select_element)
    dropdown.select_by_value('enabled')


def states():
    driver.get('https://demoqa.com/dynamic-properties')
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, 'visibleAfter'))).click()
    # driver.find_element(By.ID, 'visibleAfter').click()


def switch_tabs():
    driver.get('https://www.qa-practice.com/elements/new_tab/link')
    driver.find_element(By.ID, 'new-page-link').click()
    tabs = driver.window_handles
    driver.switch_to.window(tabs[1])
    result = driver.find_element(By.ID, 'result-text')
    print(result.text)
    driver.close()
    driver.switch_to.window(tabs[0])
    driver.find_element(By.ID, 'new-page-link').click()


switch_tabs()
