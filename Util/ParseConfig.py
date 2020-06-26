#定位表达式PageElementLocator.ini在config目录下
import configparser


'''
print(cf.options("butterfly"))
dbname = cf.get("butterfly","dbname")
username = cf.get("butterfly","username")
password = cf.get("butterfly","password")
'''


def read_ini_file_all_sections(ini_file_path):#读取所有的section选项
    cf = configparser.ConfigParser()
    cf.read(ini_file_path,encoding = "utf-8-sig" )#实例化配置文件解析对象
    return cf.sections()

def read_ini_file_sections_all_options(ini_file_path,section_name):#读取某一个section下的所有option选项
    cf = configparser.ConfigParser()
    cf.read(ini_file_path,encoding = "utf-8-sig" )#实例化配置文件解析对象
    return cf.options(section_name)


def read_ini_file_option(ini_file_path,section_name,option_name):#读取section下的某一个soption选项
    cf = configparser.ConfigParser()
    cf.read(ini_file_path,encoding = "utf-8-sig")
    try:
        value = cf.get(section_name,option_name)
    except:
        print("the specific section or the specific option doesn't exit !")
        return None
    else:
        return value



if __name__ == "__main__":
    ini_file_path = r"D:\test\keyword_driven_framework\Config\PageElementLocator.ini"
    print(read_ini_file_all_sections(ini_file_path))
    print(read_ini_file_sections_all_options(ini_file_path,'126mail_login'))
    print(read_ini_file_option(ini_file_path,'126mail_login','loginpage.loginlink'))
