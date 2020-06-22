from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
import traceback
import time



def find_element(driver,locate_method,locate_exp):
    try:
        element = WebDriverWait(driver,10).until (lambda x:x.find_element(locate_method,locate_exp))
    except TimeoutException as e:#捕获NoSuchElementException异常
        print(traceback.print_exc())

    return element


def find_elements(driver,locate_method,locate_exp):
    try:
        elements = WebDriverWait(driver, 10).until(lambda x: x.find_elements(locate_method, locate_exp))
    except TimeoutException as e:  # 捕获NoSuchElementException异常
        print(traceback.print_exc())

    return elements


if __name__ == "__main__":
    driver = webdriver.Chrome(executable_path = "d:\\chromedriver.exe")
    driver.get("https://www.sogou.com")
    input_box = find_element(driver,"id","query")
    input_elements = find_elements(driver, "xpath", "//input")
    # input_box.send_keys("北京加油")
    print(len(input_elements))
    time.sleep(3)
    driver.quit()

