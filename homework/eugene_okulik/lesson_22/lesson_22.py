from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import MoveTargetOutOfBoundsException
from time import sleep


chrome_options = Options()
chrome_options.add_experimental_option('detach', True)
chrome_options.add_argument('start-maximized')
driver = webdriver.Chrome()
driver.implicitly_wait(3)
sleep(3)


def iframes():
    driver.get('https://www.qa-practice.com/elements/iframe/iframe_page')
    iframe = driver.find_element(By.TAG_NAME, 'iframe')
    driver.switch_to.frame(iframe)
    driver.find_element(By.CSS_SELECTOR, '[aria-controls="navbarHeader"]').click()
    sleep(2)
    driver.switch_to.default_content()
    print(driver.find_element(By.CLASS_NAME, 'tab').text)


def jacket():
    driver.get('https://magento.softwaretestingboard.com/')
    women = driver.find_element(By.ID, 'ui-id-4')
    tops = driver.find_element(By.ID, 'ui-id-9')
    jackets = driver.find_element(By.ID, 'ui-id-11')
    # ActionChains(driver).move_to_element(women).move_to_element(tops).click(jackets).perform()
    actions = ActionChains(driver)
    actions.move_to_element(women)
    actions.move_to_element(tops)
    actions.click(jackets)
    actions.perform()
    sleep(2)


def d_nd_element_in_bounds(draggable):

    def _predicate(ec_driver):
        try:
            ActionChains(ec_driver).click_and_hold(draggable).release().perform()
        except MoveTargetOutOfBoundsException:
            return False
        return True

    return _predicate


def d_n_d():
    driver.get('https://www.qa-practice.com/elements/dragndrop/boxes')
    # sleep(2)
    # driver.maximize_window()
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
    drag_me = driver.find_element(By.ID, 'rect-draggable')
    drag_here = driver.find_element(By.ID, 'rect-droppable')

    WebDriverWait(driver, 5).until(d_nd_element_in_bounds(drag_me))
    ActionChains(driver).drag_and_drop(drag_me, drag_here).perform()
    # while True:
    #     try:
    #         actions = ActionChains(driver)
    #         actions.click_and_hold(drag_me)
    #         actions.move_to_element(drag_here)
    #         actions.release(drag_here)
    #         actions.perform()
    #         break
    #     except MoveTargetOutOfBoundsException:
    #         print('!!!!!')
    #         sleep(0.5)

    sleep(2)


def hold_key():
    driver.get('https://www.qa-practice.com/elements/dragndrop/boxes')
    link = driver.find_element(By.LINK_TEXT, 'Boxes')
    ActionChains(driver).key_down(Keys.CONTROL).click(link).key_up(Keys.CONTROL).perform()
    sleep(2)


def alerts():
    driver.get('https://www.qa-practice.com/elements/alert/alert')
    driver.find_element(By.LINK_TEXT, 'Click').click()
    alert = Alert(driver)
    print(alert.text)
    alert.accept()
    driver.save_screenshot('alerts.png')
    sleep(2)


def upload():
    driver.get('https://demoqa.com/upload-download')
    driver.find_element(By.ID, 'uploadFile').send_keys('/home/eugene/tms/sql/subjects.sql')
    sleep(5)


d_n_d()
