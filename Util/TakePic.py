from Config.ProjVar import *
from Util.DateAndTime import *
from Util.Dir import *
from selenium import webdriver


def take_pic(driver):
    try:
        file_path = make_time_dir()
        pic_path = os.path.join(file_path,TimeUtil().get_chinesetime()+".png")
        result = driver.get_screenshot_as_file(pic_path)
        print(result)
    except IOError as e:
        print(e)


if __name__ == "__main__":
    driver = webdriver.Chrome(executable_path= "d:\chromedriver.exe")
    driver.get("https://www.weibo.com")
    time.sleep(10)
    take_pic(driver)











