from selenium import webdriver
import time
from Util.ObjectMap import find_element,find_elements
from Config.ProjVar import PageElementLocator_file_path
from Util.ParseConfig import read_ini_file_option
import traceback

driver = ""

def is_xpath(exp):
    if ("//" in exp) or ("[") in exp or ("@") in exp:
        return True
    return False


def get_element(driver,locator_exp):
    section_name = locator_exp.split(",")[0]
    option_name = locator_exp.split(",")[1]
    element_locator = read_ini_file_option(PageElementLocator_file_path,section_name,option_name)
    element = find_element(driver,element_locator.split(">")[0],element_locator.split(">")[1])
    return element



def open_browser(browser_name):
    global driver
    if "ie" in browser_name.lower():
        driver = webdriver.Ie(executable_path="d:\\IEDriverServer.exe")
    elif "chrome" in browser_name.lower():
        driver = webdriver.Chrome(executable_path="d:\\chromedriver.exe")
    else:
        driver = webdriver.Firefox(executable_path="d:\\geckodriver.exe")

def visit(url):
    global driver
    driver.get(url)

def input(xpath_exp,content):
    global driver
    if is_xpath(xpath_exp):
        element =driver.find_element_by_xpath(xpath_exp)
        element.send_keys(content)
    else:
        element = get_element(driver,xpath_exp)
        element.send_keys(content)


def click(xpath_exp):
    global drver
    if is_xpath(xpath_exp):
        element = driver.find_element_by_xpath(xpath_exp)
        element.click()
    else:
        element = get_element(driver,xpath_exp)
        element.click()


def sleep(seconds):
    time.sleep(float(seconds))

def assert_word(excepted_word):
    global driver
    assert excepted_word in driver.page_source


def switch_to(xpath_exp):
    global driver
    if is_xpath(xpath_exp):
        driver.switch_to.frame(driver.find_element_by_xpath(xpath_exp))
    else:
        element = get_element(driver,xpath_exp)
        driver.switch_to.frame(element)

def quit():
    global driver
    driver.quit()




if __name__ == "__main__":
    #driver = login("testgloryroad2020","123456789!!")
    #open_browser("ie")
    # open_browser("firefox")
    try:
        open_browser("chrome")
        visit("http://mail.126.com")
        #input("//input[@id='query']","关键字驱动")
        #click("126mail_login,loginPage.loginlink")
        sleep(1)
        switch_to("126mail_login,loginPage.frame")
        input("126mail_login,loginPage.username","testgloryroad2020")
        input("126mail_login,loginPage.password","123456789!!")
        click("126mail_login,loginPage.loginbutton")
        sleep(5)
        assert_word("通讯录")
        click("126mail_homePage,homePage.addressbook")
        sleep(1)
        click("126mail_addContactsPage,addContactsPage.createContactsBtn")
        input("126mail_addContactsPage,addContactsPage.contactPersonName","kely")
        input("126mail_addContactsPage,addContactsPage.contactPersonEmail","1234567@qq.com")
        click("126mail_addContactsPage,addContactsPage.starContacts")
        input("126mail_addContactsPage,addContactsPage.contactPersonMobile","13800138000")
        input("126mail_addContactsPage,addContactsPage.contactPersonComment","重要联系人")
        click("126mail_addContactsPage,addContactsPage.savecontacePerson")
        sleep(5)
    except AssertionError as e:
        print("断言失败")
    except Exception as e:
        print("出现异常了",e)
        print("异常失败")
        traceback.print_exc()
    finally:
        quit()


