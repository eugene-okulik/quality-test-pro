# Напишите программу, которая зайдет на страницу https://demoqa.com/automation-practice-form и полностью заполнит форму
# (кроме загрузки файла) и нажмет Submit. Небольшая особенность
# Страничка эта немного кривая, иногда реклама перекрывает элементы и по ним невозможно кликнуть (но сейчас, смотрю,
# вообще реклама пропала). Если бы это было приложение, которое мы тестируем, это был бы баг. Но работаем с тем, что
# есть.
# И для нас это даже плюс, нужно найти как выкрутиться. Обойти это можно уменьшив размер экрана браузера - тогда
# элементы
# перераспределяются и становятся доступны. Но если реклама так и не появится, то ничего на странице не мешает.
# После отправки вам будет отображено окошко с тем что вы ввели. Получите со страницы содержимое этого окошка и
# распечатайте (выведите на экран).


from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webelement import WebElement

chrome_options = Options()
chrome_options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=chrome_options)


def input_text_is_in_results():
    driver.get('https://demoqa.com/automation-practice-form')
    driver.implicitly_wait(1)
    googleAds = driver.find_elements(By.XPATH, "//*[@width='728']")
    # print(len(googleAds))
    while len(googleAds) != 0:
        driver.refresh()
        driver.implicitly_wait(1)
        googleAds = driver.find_elements(By.XPATH, "//*[@width='728']")
        # print(len(googleAds))
    driver.execute_script("window.scrollBy(0,500)")
    stateField: WebElement = driver.find_element(By.XPATH, '//*[@id="state"]/div/div[2]/div')
    ActionChains(driver).move_to_element(stateField).click().perform()
    driver.find_element(By.XPATH, "//*[contains(text(),'Haryana')]").click()
    driver.find_element(By.XPATH, '//*[@id="city"]/div').click()
    cityField = driver.find_element(By.XPATH, "//*[contains(text(),'Karnal')]")
    ActionChains(driver).move_to_element(cityField).click().perform()
    driver.find_element(By.ID, "firstName").send_keys("Ivan")
    driver.find_element(By.ID, "lastName").send_keys("Petrov")
    driver.find_element(By.ID, "userEmail").send_keys("test@mailforspam.com")
    driver.find_element(By.ID, "userNumber").send_keys("1234567890")
    driver.find_element(By.ID, "dateOfBirthInput").clear()
    driver.find_element(By.ID, "dateOfBirthInput").send_keys(Keys.CONTROL + "A")
    driver.find_element(By.ID, "dateOfBirthInput").send_keys("04 Oct 1988")
    driver.find_element(By.ID, "lastName").click()
    radioM: WebElement = driver.find_element(By.XPATH, "//input[@value='Male']")
    ActionChains(driver).move_to_element(radioM).click().perform()
    SubjField = driver.find_element(By.ID, "subjectsInput")
    SubjField.send_keys("Social")
    SubjField.send_keys(Keys.ARROW_DOWN)
    SubjField.send_keys(Keys.ENTER)
    for i in range(1, 4):
        checkb: WebElement = driver.find_element(By.XPATH, "//input[@value='" + str(i) + "']")
        ActionChains(driver).move_to_element(checkb).click().perform()
    driver.find_element(By.XPATH, "//textarea").send_keys("Warsaw, Poland")
    SubjField.send_keys(Keys.ENTER)
    infoFull = driver.find_elements(By.XPATH, "//tr/td")
    counter = 0
    for x in infoFull:
        if counter % 2 == 0:
            print(x.text + " : ", end='')
        else:
            print(x.text)
        counter += 1


input_text_is_in_results()
