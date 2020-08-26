
from actualtools.shuoshuo.util.get_date import GetData
from actualtools.shuoshuo.util.selenium_get_title import GetUrlTitle


class GetResult:
    def __init__(self,file_name=None,sheet_id=None,title_xpath=None):
        self.file_name = file_name
        self.sheet_id = sheet_id
        self.title_xpath = title_xpath
        self.get_date = GetData(self.file_name,self.sheet_id)



    def run(self):
        #获取行数
        num_count = self.get_date.get_case_lines()
        for i in range(1, num_count):  #从第二行开始获取数据，第一行为标题
            yuan_title = self.get_date.get_title(i)
            print(yuan_title)
            # 1.获取表中的url
            url = self.get_date.get_url(i)
            print(url)
            #2.通过selenium获取到title
            gut = GetUrlTitle(url=url)
            selenium_title = gut.get_gonggao_title(xpath=self.title_xpath)
            #3.将title与原title做对比
            if yuan_title == selenium_title:
                com_result = "相同"
            else:
                com_result = "不一致"
            #4.将获取都的title和对比结果写入到excel表中
            self.get_date.write_selenium_title(row=i,value=selenium_title)
            self.get_date.write_com_result(row=i,value=com_result)
        pass


if __name__ == '__main__':
    file_name=r"D:\PycharmProjects\shangbaogongju\actualtools\shuoshuo\myexcel\dataresult.xls"
    sheet_id = 0
    title_xpath = "/html/body/div[5]/div[2]/div/div/div/div[1]"   #文章标题的xpath路径
    gr = GetResult(file_name=file_name,sheet_id=sheet_id,title_xpath=title_xpath)
    gr.run()
