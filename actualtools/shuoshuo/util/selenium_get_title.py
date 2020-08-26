import time   #导入时间
import os
import sys
from selenium import webdriver   #导入驱动

class GetUrlTitle:

    def __init__(self,url):
        self.url = url
        self.driver = self.getChromeDriver()

    #使用谷歌浏览器
    def getChromeDriver(self):
        #谷歌浏览器驱动 网址：http://npm.taobao.org/mirrors/chromedriver/

        chrome_options = webdriver.ChromeOptions()   #为驱动加入无界面配置

        chrome_options.add_argument('--headless')   #–headless”参数是不用打开图形界面
        chrome_options.add_argument('--no-sandbox')  #“–no - sandbox”参数是让Chrome在root权限下跑
        chrome_options.add_argument("--kiosk") #全屏启动
        chrome_options.add_argument("--start-maximized")  #全屏启动
        chrome_options.add_argument("--start-fullscreen")  #全屏启动
        #chrome_options.add_argument("--window-size=4000,1600")  #专门应对无头浏览器中不能最大化屏幕的方案
        chrome_options.add_argument("--window-size=1920,1050")  # 专门应对无头浏览器中不能最大化屏幕的方案
        path = r"%s/driver/chromedriver"% str(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))   #配置驱动路径
        print("path:%s" % path)
        # path = r"D:\Users\Administrator\PycharmProjects\webtestdata\TestCaseFunction\driver\chromedriver.exe"  #配置驱动路径
        # option = webdriver.ChromeOptions()
        # option.add_argument('--user-data-dir=C:\\Users\\Administrator\\Local\\Google\\Chrome\\User Data\\Default')  # 设置成用户自己的数据目录
        #                                                             #浏览器输入chrome://version 下个人资料路径就是自己的数据目录
        # chromedriver = webdriver.Chrome(chrome_options=chrome_options)
        chromedriver = webdriver.Chrome(executable_path=path,chrome_options=chrome_options)
        # chromedriver = webdriver.Chrome(executable_path=path)
        # chromedriver = webdriver.Chrome(executable_path=path)
        chromedriver.maximize_window()   #窗口最大化
        # self.delayTime(5)
        chromedriver.implicitly_wait(1)#设置隐形等待时间为1秒
        return  chromedriver

    #打开网址
    def getUrl(self):
        try:
            self.driver.get(self.url)
            print("进入网址：%s"% self.url)
        except Exception as e:
            print("打开网页失败,关闭驱动.问题描述：[%s]" % e)




    def get_title_from_url(self):
        self.getUrl()
        url_title = self.driver.title
        print("【%s】网址的title为【%s】" %(self.url,url_title))
        self.closeBrowse()
        return url_title

    def get_gonggao_title(self,xpath):
        self.getUrl()
        gonggao_content_ele = self.driver.find_element_by_xpath(xpath)
        gonggao_title = gonggao_content_ele.text
        self.closeBrowse()
        print("【%s】网址的文章的title为【%s】" % (self.url, gonggao_title))
        return gonggao_title

    #关闭浏览器
    def closeBrowse(self):
        self.driver.quit()

if __name__ == '__main__':
    url = "http://www.bdgxq.gov.cn/index.php?m=content&c=index&a=show&catid=106&id=5851"
    gut = GetUrlTitle(url=url)
    gut.get_title_from_url()
