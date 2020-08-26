import os


from WWSpider.util.getTimeStr import GetTimeStr   #导入获取时间串函数
from WWSpider.util.myLogs import MyLogs
from WWSpider.util.handleTxt import HandleTxt
from requests_html import HTMLSession

class SpiderCommon(object):
    def __init__(self):
        self.timeStr = GetTimeStr()  # 实例化
        self.html_session = HTMLSession()


    def outPutMyLog(self,context):
        mylog = MyLogs(context)
        mylog.runMyLog()


    def outPutErrorMyLog(self,context):
        mylog = MyLogs(context)
        mylog.runErrorLog()

    def createDir(self,filedir):
        filelist = filedir.split("/")
        # print(filelist)
        long = len(filelist)
        # print(long)
        zuhefiledir = filelist[0]
        for i in range(1,long):
            zuhefiledir = zuhefiledir+"/"+filelist[i]
            if os.path.exists(zuhefiledir):
                self.outPutMyLog("已经存在目录：%s" % zuhefiledir)
            else:
                os.mkdir(zuhefiledir)
                self.outPutMyLog("已经创建目录：%s" % zuhefiledir)

    def getUrlResponse(self,hs,url, headers=None,**kwargs):
        for i in range(1,6):
            try:
                url_response = hs.get(url=url, headers=headers,timeout=5, verify=False)
                self.outPutMyLog("请求网址：%s" % url)
                break
            except Exception as e:
                self.outPutErrorMyLog("获取页面请求响应超时异常：%s" % e)
                self.outPutErrorMyLog("第%s次请求响应超时..." % i)
                continue
        return url_response

    #处理403网址


    #处理失败网址
    def handleFailWebUrl(self,fail_url,project_dir,fail_dir,fail_txt):
        mynowdir = str(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        print("当前路径：%s" % mynowdir)
        base_dir = '%s/myproject/%s/%s' % (mynowdir,project_dir,fail_dir)
        self.createDir(base_dir)
        ht = HandleTxt("%s/%s" % (base_dir,fail_txt))
        ht.add_content(fail_url)

    #正则匹配获取变量中的内容
    def get_re_content(self,pipei,content):
        import re
        pipei_from_content = re.findall(pipei,content)
        self.outPutMyLog(pipei_from_content)
        return pipei_from_content

    #根据网址获取网址所有链接的绝对路径作为新的网址链接
    def get_response_absolute_links(self,url_response):
        all_links_list = url_response.html.absolute_links
        print(all_links_list)
        return all_links_list

    # 获取网址的title
    def get_respinse_title(self, url_response):
        title_text_list = []
        text = url_response.content
        text = url_response.text
        # print(text)
        pipei = "<title>.*</title>"
        title_list = self.get_re_content(pipei=pipei, content=text)
        if title_list == None:
            print("没有查找到【<title>.*</title>】相关内容，匹配标题失败")
            return None
        else:
            for title_one in title_list:
                title_one_one = title_one.strip("<title>")  # 去掉<title>
                title_one_two = title_one_one.strip("</title>")  # 去掉</title>
                title_text_list.append(title_one_two)
        print("网址标题列表：")
        print(title_text_list)
        title_text_list_len = len(title_text_list)
        if title_text_list_len > 0:
            print("获取网址标题：")
            print(title_text_list[0])
            return title_text_list[0]
        else:
            return None

    # 根据网址列表，获取网址和title的集合
    def get_url_and_title_dict(self, url_list):
        url_and_title_dict = {}
        url_list_len = len(url_list)
        if url_list_len == 0:
            print("列表长度为0，获取内容")
        else:
            for url_one in url_list:
                try:
                    print("self.html_session:")
                    print(self.html_session)
                    url_response = self.getUrlResponse(hs=self.html_session, url=url_one)

                    url_title = self.get_respinse_title(url_response)
                    if url_title != None:  # 如果title不为空，则保存到字典中
                        url_and_title_dict[url_one] = url_title  # 网址和标题
                except Exception as e:
                    print("获取出错，出错原因：%s" % e)
                    continue  # 继续下次循环

        print("网址及其对应的标题：")
        print(url_and_title_dict)
        import json
        print(json.dumps(url_and_title_dict))  # indent=1代表字节点比父节点前多几个空格

        return url_and_title_dict


if __name__ == "__main__":
    url_list = ['https://3000jl.com']
    sc = SpiderCommon()
    sc.get_url_and_title_dict(url_list=url_list)


