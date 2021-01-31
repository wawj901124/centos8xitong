import sys,os
mypath =os.path.dirname(os.path.dirname(os.path.abspath(__file__))) #写入项目路径
sys.path.append(mypath)
import os
import uiautomator2 as u2
import time
from PIL import Image   #导入Image
from PIL import ImageEnhance  #导入ImageEnhance

from WWUiautoamtorTwo.util.comparePictureSSIM import CompareImage   #对比两张图片
from WWUiautoamtorTwo.util.getTimeStr import GetTimeStr  # 导入获取时间串函数
from WWUiautoamtorTwo.util.myLogs import MyLogs


class BaseFrame(object):
    def __init__(self, outdevice=None, apppacakagename=None, isusb=None):
        print(outdevice)
        if outdevice == None:
            # self.d = u2.connect('192.168.199.168')
            self.d = u2.connect_usb('192.168.1.100:5555')
        else:
            self.d = u2.connect_usb(outdevice)

        if apppacakagename == None:
            self.packagename = "com.ahdi.qrindo.wallet"
        else:
            self.packagename = apppacakagename
        self.timeStr = GetTimeStr()  # 实例化
        self.isstartapp = False

    def outPutMyLog(self, context):
        mylog = MyLogs(context)
        mylog.runMyLog()

    def outPutErrorMyLog(self, context):
        mylog = MyLogs(context)
        mylog.runErrorLog()

    # 执行shell命令
    def adbshell(self, order):
        d = self.d
        d.adb_shell(order)
        self.outPutMyLog('输入shell命令:', order, '。\n')

    # 启动app
    def startapp(self):
        self.stopapp()
        self.d.app_start(self.packagename)
        self.outPutMyLog('启动包名为[%s]的应用---------' % self.packagename)
        # self.outPutMyLog('设备信息：', d.device_info)
        self.delaytime(3)

    # 关闭app
    def stopapp(self):
        self.d.app_stop(self.packagename)
        self.outPutMyLog('关闭包名为[%s]的应用---------' % self.packagename)

    # 延时
    def delaytime(self, dalaytime):
        dalaytime = int(dalaytime)
        time.sleep(dalaytime)
        self.outPutMyLog('等待%d秒...' % dalaytime)

    #点击固定点（10，10）
    def clickGuDingDian(self,x,y):
        self.d.click(x,y)
        self.outPutMyLog("点击点[%s,%s]"%(str(x),str(y)))

    # 点击返回按钮
    def clickback(self):
        self.d.press("back")
        self.outPutMyLog('点击返回按键')
        self.delaytime(3)

    # 点击Home按钮
    def clickhome(self):
        self.d.press("home")
        self.outPutMyLog('点击Home按键')
        self.delaytime(3)

    # 元素是否存在
    def ele_is_exist(self, findstyle, styleparame):
        try:
            if findstyle == "resourceId":
                ele = self.d(resourceId=styleparame)
                ele.info
                # self.outPutMyLog("ele.info:%s" % ele.info)
                # self.outPutMyLog("找到元素")
            elif findstyle == "text":
                ele = self.d(text=styleparame)
                ele.info
                # self.outPutMyLog("ele.info:%s"% ele.info)
                # self.outPutMyLog("找到元素")
        except Exception as e:
            # self.outPutMyLog("报错：%s"% e)
            return False
        else:
            return True

    # 查找元素
    def findelement(self, findstyle, styleparame):
        try:
            if findstyle == "resourceId":
                ele = self.d(resourceId=styleparame)
                eletext = self.geteleinfo_text(ele)
                if eletext == "":
                    self.outPutMyLog("定位到resourceId为[%s]的控件。" % styleparame)
                else:
                    self.outPutMyLog("定位到text为[%s]的控件。" % eletext)
                return ele
            elif findstyle == "text":
                ele = self.d(text=styleparame)
                eletext = self.geteleinfo_text(ele)
                if eletext == "":
                    self.outPutMyLog("没有定位到控件。")
                else:
                    self.outPutMyLog("定位到text为[%s]的控件。" % eletext)
                return ele

        except Exception as e:
            self.outPutMyLog("self.isstartappd的值为：%s" % self.isstartapp)
            self.isstartapp = True
            self.outPutMyLog("self.isstartappd的值为：%s" % self.isstartapp)
            self.getScreenshotError()
            self.outPutErrorMyLog("出错原因：定位控件失败.具体原因：%s" % e)
            self.delaytime(3)
            self.isstartapp = True
            self.outPutMyLog("self.isstartappd的值为：%s" % self.isstartapp)

    # 查找到元素并且输入内容
    def findelement_and_input(self, findstyle, styleparame, inputtext):
        ele = self.findelement(findstyle, styleparame)
        self.ele_input(ele, inputtext)

    # 查找到元素并且点击该元素
    def findelement_and_click(self, findstyle, styleparame, outpretoastmessage=None):
        ele = self.findelement(findstyle, styleparame)
        toastmessage = self.ele_click_and_return_toastmessage(ele, outpretoastmessage)
        return toastmessage

    # 查找到元素并且返回enabled属性的状态
    def findelement_and_return_enabledstatus(self, findstyle, styleparame):
        ele = self.findelement(findstyle, styleparame)
        eleinfo_enabled = self.geteleinfo_enabled(ele)
        return eleinfo_enabled

    # 查找到元素并且text内容
    def findelement_and_return_text(self, findstyle, styleparame):
        ele = self.findelement(findstyle, styleparame)
        eleinfo_text = self.geteleinfo_text(ele)
        return eleinfo_text

    # 查找到元素并且返回selected属性状态
    def findelement_and_return_selectedstatus(self, findstyle, styleparame):
        ele = self.findelement(findstyle, styleparame)
        eleinfo_selected = self.geteleinfo_selected(ele)
        return eleinfo_selected

    # 通过ID查找到元素
    def findbyresourceId(self, resourceId):
        d = self.d
        try:
            ele = d(resourceId=resourceId)
            eletext = self.geteleinfo_text(ele)
            if eletext == "":
                self.outPutMyLog("定位到resourceId为[%s]的控件。" % resourceId)
            else:
                self.outPutMyLog("定位到text为[%s]的控件。" % eletext)
            return ele
        except Exception as e:
            self.outPutMyLog("self.isstartappd的值为：%s" % self.isstartapp)
            self.isstartapp = True
            self.outPutMyLog("self.isstartappd的值为：%s" % self.isstartapp)
            self.getScreenshotError()
            self.outPutErrorMyLog("出错原因：定位控件失败.具体原因：%s" % e)
            self.delaytime(3)
            self.isstartapp = True
            self.outPutMyLog("self.isstartappd的值为：%s" % self.isstartapp)

    # 通过ID查找到元素并且输入内容
    def findbyresourceId_and_input(self, resourceId, inputtext):
        ele = self.findbyresourceId(resourceId)
        self.ele_input(ele, inputtext)

    # 通过ID查找到元素并且点击该元素
    def findbyresourceId_and_click(self, resourceId, outpretoastmessage=None):
        ele = self.findbyresourceId(resourceId)
        toastmessage = self.ele_click_and_return_toastmessage(ele, outpretoastmessage)
        return toastmessage

    # 通过ID查找到元素并且返回enabled属性的状态
    def findbyresourceId_and_return_enabledstatus(self, resourceId):
        ele = self.findbyresourceId(resourceId)
        eleinfo_enabled = self.geteleinfo_enabled(ele)
        return eleinfo_enabled

    # 通过ID查找到元素并且text内容
    def findbyresourceId_and_return_text(self, resourceId):
        ele = self.findbyresourceId(resourceId)
        eleinfo_text = self.geteleinfo_text(ele)
        return eleinfo_text

    # 通过ID查找到元素并且返回selected属性状态
    def findbyresourceId_and_return_selectedstatus(self, resourceId):
        ele = self.findbyresourceId(resourceId)
        eleinfo_selected = self.geteleinfo_selected(ele)
        return eleinfo_selected

    # 通过text查找到元素
    def findbytext(self, text):
        d = self.d
        try:
            ele = d(text=text)
            eletext = self.geteleinfo_text(ele)
            if eletext == "":
                self.outPutMyLog("没有定位到控件。")
            else:
                self.outPutMyLog("定位到text为[%s]的控件。" % eletext)
            return ele
        except Exception as e:
            self.outPutMyLog("self.isstartappd的值为：%s" % self.isstartapp)
            self.isstartapp = True
            self.outPutMyLog("self.isstartappd的值为：%s" % self.isstartapp)
            self.getScreenshotError()
            self.outPutErrorMyLog("出错原因：定位控件失败.具体原因：%s" % e)
            self.delaytime(3)

    # 通过text查找到元素并且输入内容
    def findbytext_and_input(self, text, inputtext):
        ele = self.findbytext(text)
        self.ele_input(ele, inputtext)

    # 通过text查找到元素并且点击内容
    def findbytext_and_click(self, text, outpretoastmessage=None):
        ele = self.findbytext(text)
        toastmessage = self.ele_click_and_return_toastmessage(ele, outpretoastmessage)
        return toastmessage

    # 通过text查找到元素并且返回enabled状态
    def findbytext_and_return_enabledstatus(self, text):
        ele = self.findbytext(text)
        eleinfo_enabled = self.geteleinfo_enabled(ele)
        return eleinfo_enabled

    # 通过text查找到元素并且返回enabled状态
    def findbytext_and_return_text(self, text):
        ele = self.findbytext(text)
        eleinfo_text = self.geteleinfo_text(ele)
        return eleinfo_text

    # 通过text查找到元素并且返回selected状态
    def findbytext_and_return_selectedstatus(self, text):
        ele = self.findbytext(text)
        eleinfo_selected = self.geteleinfo_selected(ele)
        return eleinfo_selected

    # 元素中输入内容
    def ele_input(self, ele, inputtext):
        ele.clear_text()
        ele.send_keys(inputtext)
        self.outPutMyLog("输入:%s。" % inputtext)
        self.delaytime(1)

    # 点击元素并返回toast提示信息
    def ele_click_and_return_toastmessage(self, ele, outpretoastmessage=None):
        ele.click()
        self.outPutMyLog("点击该控件。")
        if outpretoastmessage == None:
            self.delaytime(3)
            return None
        else:
            toastmessage = self.getToast()
            self.outPutMyLog("pretoastmessage:", outpretoastmessage)
            return toastmessage

    # 得到元素enabled属性值
    def geteleinfo_enabled(self, ele):
        value = 'enabled'
        eleinfo_enabled = self.geteleinfo_value(ele, value)
        self.outPutMyLog('该控件的enabled属性的值为：%s' % eleinfo_enabled)
        return eleinfo_enabled

    # 得到元素text属性值
    def geteleinfo_text(self, ele):
        value = 'text'
        eleinfo_text = self.geteleinfo_value(ele, value)
        if eleinfo_text != '':
            self.outPutMyLog('该控件的text属性的值为：%s' % eleinfo_text)
        return eleinfo_text

    # 得到元素selected属性值
    def geteleinfo_selected(self, ele):
        value = 'selected'
        eleinfo_selected = self.geteleinfo_value(ele, value)
        if eleinfo_selected != '':
            self.outPutMyLog('该控件的selected属性的值为：%s' % eleinfo_selected)
        return eleinfo_selected

    # 得到元素属性值
    def geteleinfo_value(self, ele, value):
        eleinfo = ele.info
        # self.outPutMyLog('eleinfo:',eleinfo)
        eleinfo_value = eleinfo[value]
        return eleinfo_value

    # 得到toast提示信息
    def getToast(self):
        toastmessage = self.d.toast.get_message(5.0, default="")
        self.outPutMyLog("toastmessage:", toastmessage)
        return toastmessage

    # 得到设备信息
    def getdeviceinfo(self):
        deviceinfo = self.d.device_info
        self.outPutMyLog("deviceinfo:%s" % deviceinfo)
        self.outPutMyLog("deviceinfo类型:%s" % type(deviceinfo))
        return deviceinfo

    # 建立crash监听
    def createwatcher(self):
        d = self.d
        d.watcher('crash').when(text='很抱歉，“QRindo MCH”已停止运行。').click(text="确定")
        d.watcher("crash").triggered
        self.outPutMyLog('d.watcher:', d.watcher)

    # 获取时间串
    def getTimeStr(self):
        tStr = self.timeStr.getTimeStr()
        return tStr

    def getTimeStrNY(self):
        tStrNY = self.timeStr.getTimeStrNY()
        return tStrNY

    #返回当前文件路径的父路径的父路径
    def getCurrentFilePath(self):
        current_path = str(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        return current_path

    # 出错时，获取页面截图
    def getScreenshotError(self):
        d = self.d
        self.outPutMyLog("调用截取图片函数")
        currentny = self.getTimeStrNY()  # 获取当前时间的年月
        tStr = self.getTimeStr()
        # path = "../screenshots/screenpicture_%s.png"% tStr
        firedir = r'%s/media/report/%s/screenshots/' % (
        os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), currentny)
        self.createdir(firedir)
        path = '%s/screenpicture_%s.png' % (firedir, tStr)
        pathaboutmysql = r'media\report\%s\screenshots\screenpicture_%s.png' % (currentny, tStr)
        # path = '%s/screenshots/screenpicture_%s.png'%(str(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),tStr)
        d.screenshot(path)
        self.outPutMyLog("*****")
        # self.outPutMyLog(path)
        self.outPutMyLog(pathaboutmysql)
        self.outPutMyLog("*****")
        return path

    # 正常，获取页面截图
    def getScreenshotNormal(self):
        d = self.d
        self.outPutMyLog("调用截取图片函数")
        tStr = self.getTimeStr()
        # path = "../screenshots/screenpicture_%s.png"% tStr
        current_path = str(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        filepath = '%s/screenshots'% current_path
        self.createdir(filepath)
        path = '%s/screenpicture_%s.png' % (filepath, tStr)
        d.screenshot(path)
        self.outPutMyLog("*****")
        self.outPutMyLog(path)
        self.outPutMyLog("*****")
        return path

    #获取截图中的部分图片,部分图片获取根据左上角点坐标及图片宽和高获取
    def getScreenshotNormalBuFenImage(self,point_x=798,point_y=975,kongjian_width=312,kongjian_height=87):
        wholeimagepath = self.getScreenshotNormal()
        eleimage = self.getBuFenImage(wholeimagepath,point_x,point_y,kongjian_width,kongjian_height)
        return eleimage

    def createdir(self, filedir):
        filelist = filedir.split("/")
        # print(filelist)
        long = len(filelist)
        # print(long)
        zuhefiledir = filelist[0]
        for i in range(1, long):
            zuhefiledir = zuhefiledir + "/" + filelist[i]
            if os.path.exists(zuhefiledir):
                self.outPutMyLog("已经存在目录：%s" % zuhefiledir)
            else:
                os.mkdir(zuhefiledir)
                self.outPutMyLog("已经创建目录：%s" % zuhefiledir)
    #对比两张图片
    def comparePicture(self,acturePic,prePic,prebilv):
        try:
            acture_pic_path = str(acturePic)
            print("实际图片路径：%s"% acture_pic_path)
            pre_pic_path = str(prePic)
            print("参照图片路径：%s"% pre_pic_path)
            ci = CompareImage()
            acture_bilv = ci.compare_image(acture_pic_path, pre_pic_path)
            self.outPutMyLog("图片相似度：%s" % str(acture_bilv))
            bilv = prebilv
            if acture_bilv>=bilv:
                self.outPutMyLog("图片相似度【%s】 比预期相似度【%s】高或一样" % (str(acture_bilv),str(bilv)))
                self.outPutMyLog("返回【True】")
                return True
            else:
                self.outPutMyLog("图片相似度【%s】 比预期相似度【%s】低" % (str(acture_bilv),str(bilv)))
                self.outPutMyLog("返回【False】")
                return False
        except Exception as e:
            self.outPutErrorMyLog("对比出错，原因是【%s】"% str(e))
            return False

    #等待10秒，截图对比，达到一定预期后，点击
    def wait_and_conpate_and_click(self,preimage,prebilv,point_x,point_y):
        self.delaytime(5)  # 等待5秒
        pre_shouye =preimage
        act_shouye_jietu = self.getScreenshotNormal()
        is_continue_one = self.comparePicture(acturePic=act_shouye_jietu, prePic=pre_shouye, prebilv=prebilv)
        is_start_shouye_flag = False
        while_count=1
        while not is_start_shouye_flag:
            if is_continue_one:
                self.clickGuDingDian(point_x,point_y)
                is_start_shouye_flag = True
            else:
                # 重启
                print("等待5秒，再次截图对比")
                self.delaytime(5)
                zaici_act_shouye_jietu = self.getScreenshotNormal()
                is_continue_one = self.comparePicture(acturePic=zaici_act_shouye_jietu, prePic=pre_shouye, prebilv=prebilv)
                if while_count >10:
                    self.outPutMyLog("已经循环判断了10次")
                    self.outPutMyLog("判断是否出现排队")
                    act_paidu_path = self.get_paidui_bufen_image(wholeimagepath=zaici_act_shouye_jietu)
                    current_file_path = self.getCurrentFilePath()
                    pre_paidu_path = '%s/prepicture/paidui.png'%current_file_path
                    is_paidu = self.comparePicture(acturePic=act_paidu_path, prePic=pre_paidu_path, prebilv=0.9)
                    if is_paidu:
                        self.outPutErrorMyLog("显示正在排队，需要重新进行启动应用操作")
                        return '正在排队'
                if while_count >15:
                    self.outPutMyLog("已经循环超过了15次")
                    self.outPutMyLog("等待太久，返回正在排队，用于重启")
                    return '正在排队'
            self.outPutMyLog("完成第%s次循环"%str(while_count))
            while_count=while_count+1

        return act_shouye_jietu



    #等待10秒，截图对比，达到一定预期后，点击,对比的是截取的区域块
    def wait_and_compare_bufenimage_and_click(self,preimage,prebilv,clickpoint_x,clickpoint_y,
                                              jiepingpoint_x,jiepingpoint_y,
                                              jiepingkongjian_width,jiepingkongjian_height,is_for_coutinue=False):
        self.delaytime(5)  # 等待5秒
        pre_shouye =preimage
        act_shouye_jietu = self.getScreenshotNormalBuFenImage(point_x=jiepingpoint_x,
                                                              point_y=jiepingpoint_y,
                                                              kongjian_width=jiepingkongjian_width,
                                                              kongjian_height=jiepingkongjian_height)
        is_continue_one = self.comparePicture(acturePic=act_shouye_jietu, prePic=pre_shouye, prebilv=prebilv)
        is_start_shouye_flag = False
        while_count=1
        while not is_start_shouye_flag:
            if is_continue_one:
                self.clickGuDingDian(clickpoint_x,clickpoint_y)
                is_start_shouye_flag = True
            else:
                # 重启
                print("等待5秒，再次截图对比")
                self.delaytime(5)
                zaici_act_shouye_jietu = self.getScreenshotNormalBuFenImage(point_x=jiepingpoint_x,
                                                              point_y=jiepingpoint_y,
                                                              kongjian_width=jiepingkongjian_width,
                                                              kongjian_height=jiepingkongjian_height)
                is_continue_one = self.comparePicture(acturePic=zaici_act_shouye_jietu, prePic=pre_shouye, prebilv=prebilv)
                if while_count >10:
                    self.outPutMyLog("已经循环判断了10次")
                    self.outPutMyLog("判断是否出现排队")
                    act_paidu_path = self.get_paidui_bufen_image(wholeimagepath=zaici_act_shouye_jietu)
                    current_file_path = self.getCurrentFilePath()
                    pre_paidu_path = '%s/prepicture/paidui.png'%current_file_path
                    is_paidu = self.comparePicture(acturePic=act_paidu_path, prePic=pre_paidu_path, prebilv=0.9)
                    if is_paidu:
                        self.outPutErrorMyLog("显示正在排队，需要重新进行启动应用操作")
                        return '正在排队'
                if while_count >15:
                    self.outPutMyLog("已经循环超过了15次")
                    if is_for_coutinue:
                        self.outPutMyLog("返回继续往下")
                        return '继续往下'
                    self.outPutMyLog("等待太久，返回正在排队，用于重启")
                    return '正在排队'
            self.outPutMyLog("完成第%s次循环" % str(while_count))
            while_count=while_count+1

        return act_shouye_jietu

    #根据坐标截取截图中某一部分
    # 获取控件截图
    def getBuFenImage(self,wholeimagepath,point_x=838,point_y=740,kongjian_width=274,kongjian_height=96):

        pageScreenshotpath = wholeimagepath  # 获取整个页面截图
        # # location = ele.location   #获取验证码x,y轴坐标   #截取了BUSINESS
        # location = ele.location_once_scrolled_into_view  # 获取元素x,y轴坐标   #消除self.driver.execute_script("arguments[0].scrollIntoView();", ele) 对截图的影响 截取了login imgae
        # size = ele.size  # 获取元素的长宽
        # coderange = (int(location['x']), int(location['y']), int(location['x'] + size['width']),
        #              int(location['y'] + size['height']))  # 写成我们需要截取的位置坐标
        coderange = (point_x,point_y,
                     point_x+kongjian_width,
                     point_y+kongjian_height)
        pageScreenshot = Image.open(pageScreenshotpath)  # 打开截图
        imageScreen = pageScreenshot.crop(coderange)  # 使用Image的crop函数，从截图中再次截取我们需要的区域,即验证码区域
        tStr = self.getTimeStr()
        currentfilepath = self.getCurrentFilePath()
        firedir = r'%s/imagefile/ele' % currentfilepath
        self.createdir(firedir)
        eleimage = "%s/%s_ele.png" % (firedir,tStr)
        imageScreen.save(eleimage)  # 保存控件截图
        self.outPutMyLog('获取到的元素的截图路径为：%s' % eleimage)
        return eleimage

    #获取点击进入截图
    def get_dianjijinru_bufen_image(self,wholeimagepath,point_x=798,point_y=975,kongjian_width=312,kongjian_height=87):
        wholeimagepath = self.getScreenshotNormal()
        eleimage = self.getBuFenImage(wholeimagepath,point_x,point_y,kongjian_width,kongjian_height)
        return eleimage

    #获取点击含有今日不再显示的图的x截图
    def get_jinribuzaixianshi_bufen_image(self,wholeimagepath,point_x=298,point_y=806,kongjian_width=190,kongjian_height=50):
        wholeimagepath = self.getScreenshotNormal()
        eleimage = self.getBuFenImage(wholeimagepath,point_x,point_y,kongjian_width,kongjian_height)
        return eleimage

    #获取排队截图内容
    def get_paidui_bufen_image(self,wholeimagepath,point_x=569,point_y=215,kongjian_width=792,kongjian_height=622):
        eleimage = self.getBuFenImage(wholeimagepath,point_x,point_y,kongjian_width,kongjian_height)
        return eleimage

    # #获取  #判断排队，然后杀死应用重启
    # #技能点1处的截图
    # def get_jinengdian_one_bufen_image(self,wholeimagepath):
    #     wholeimagepath = self.getScreenshotNormal()
    #     eleimage = self.getBuFenImage(wholeimagepath,point_x=86,point_y=36,kongjian_width=190,kongjian_height=110)
    #     return eleimage


    #获取技能1的【升级】截图函数
    def get_jineng_one_shengji_image(self):
        wholeimagepath = self.getScreenshotNormal()
        eleimage = self.getBuFenImage(wholeimagepath,point_x=1740,point_y=220,kongjian_width=86,kongjian_height=36)
        return eleimage

    #获取技能1的【当前最高或技能点不足】截图函数
    def get_jineng_one_dangqianzuigao_image(self):
        wholeimagepath = self.getScreenshotNormal()
        eleimage = self.getBuFenImage(wholeimagepath,point_x=1690,point_y=210,kongjian_width=190,kongjian_height=110)
        return eleimage

    #获取技能2的【升级】截图函数
    def get_jineng_two_shengji_image(self):
        wholeimagepath = self.getScreenshotNormal()
        eleimage = self.getBuFenImage(wholeimagepath,point_x=1740,point_y=464,kongjian_width=86,kongjian_height=36)
        return eleimage

    #获取技能2的【当前最高或技能点不足】截图函数
    def get_jineng_two_dangqianzuigao_image(self):
        wholeimagepath = self.getScreenshotNormal()
        eleimage = self.getBuFenImage(wholeimagepath,point_x=1690,point_y=452,kongjian_width=190,kongjian_height=110)
        return eleimage



    #点击技能升级操作，
    def wait_and_conpate_and_click_and_loop_click(self,preimage,prebilv,point_x,point_y,quedingimage):
        shengjihoutu = self.wait_and_conpate_and_click(preimage,prebilv,point_x,point_y)
        if shengjihoutu == '正在排队':
            return '正在排队'

        #对升级后的图进行截图，查看某一区域是否是“确定”按钮，如果是，则点击，并且终止此次循环点击
        act_queding = self.getBuFenImage(wholeimagepath=shengjihoutu)
        is_countinue = True

        while is_countinue:
            self.d.click(point_x,point_y)  #点击
            self.delaytime(2)  #停顿2秒
            dianjihoujietu = self.getScreenshotNormal()
            again_act_queding = self.getBuFenImage(wholeimagepath=dianjihoujietu)   #检查是否有确定图标
            is_same = self.comparePicture(acturePic=quedingimage, prePic=again_act_queding, prebilv=0.95)
            if is_same:
                self.outPutMyLog("出现确定按钮")
                self.d.click(980,785)  #点击确定按钮
                is_countinue=False
            else:
                self.outPutMyLog("没有出现确定按钮，继续循环")
                continue
        # #获取技能区域截图，看是"当前最高",还是"技能点不足"
        # check_jineng_one_jietu = self.getScreenshotNormal()
        # act_jinengdianjietu = self.get_jinengdian_one_bufen_image(wholeimagepath=check_jineng_one_jietu)
        # pre_jineng_one =
        # is_jinengdian = self.comparePicture(acturePic=act_jinengdianjietu, prePic=pre_jineng_one, prebilv=0.95)

        self.outPutMyLog("技能升级完成")


    #处理升级技能1
    def handle_jineng_one(self):

        jinengone_quyu_image = self.get_jineng_one_shengji_image()

        current_file_path = self.getCurrentFilePath()
        pre_shouye = '%s/prepicture/jinnengshengji.png' % current_file_path
        is_click_shengji = self.comparePicture(acturePic=jinengone_quyu_image, prePic=pre_shouye, prebilv=0.9)
        if is_click_shengji:   #如果可以升级，点击升级
            clickpoint_x = 1797
            clickpoint_y =305
            self.clickGuDingDian(clickpoint_x,clickpoint_y)
            self.outPutMyLog('点击升级技能')
            self.delaytime(2)
            return '升级技能1'

        act_jinengdianbuzu_image = self.get_jineng_one_dangqianzuigao_image()
        pre_jinengdianbuzu = '%s/prepicture/jinnengdianbuzu.png' % current_file_path
        is_jinengdianbuzu = self.comparePicture(acturePic=act_jinengdianbuzu_image, prePic=pre_jinengdianbuzu, prebilv=0.9)
        if is_jinengdianbuzu:   #如果是技能点不足，则退出循环
            self.outPutMyLog('节能点已经用完，技能点不足')
            return '技能点不足'

        pre_danqianzuigao = '%s/prepicture/dangqianzuigao.png' % current_file_path
        is_dangqianzuigao = self.comparePicture(acturePic=act_jinengdianbuzu_image, prePic=pre_danqianzuigao, prebilv=0.9)
        if is_dangqianzuigao:   #如果是当前最高，则换下一个人，退出当前循环
            is_xiayige_ren = True
            self.outPutMyLog('当前最高，下一个')
            return '当前最高'
            #升级二技能或者下一个人

        #对比是否存在排队提示
        #整个截图
        whole_image = self.getScreenshotNormal()
        act_paidu_path = self.get_paidui_bufen_image(wholeimagepath=whole_image)
        current_file_path = self.getCurrentFilePath()
        pre_paidu_path = '%s/prepicture/paidui.png' % current_file_path
        is_paidu = self.comparePicture(acturePic=act_paidu_path, prePic=pre_paidu_path, prebilv=0.9)
        if is_paidu:
            self.outPutErrorMyLog("显示正在排队，需要重新进行启动应用操作")
            return '正在排队'

    # 处理升级技能2
    def handle_jineng_two(self):

        jinengone_quyu_image = self.get_jineng_two_shengji_image()  #获取技能二升级区域

        current_file_path = self.getCurrentFilePath()

        pre_shouye = '%s/prepicture/jinengtwo/jinnengshengjitwo.png' % current_file_path
        is_click_shengji = self.comparePicture(acturePic=jinengone_quyu_image, prePic=pre_shouye, prebilv=0.9)
        if is_click_shengji:  # 如果可以升级，点击升级
            clickpoint_x = 1797
            clickpoint_y = 305
            self.clickGuDingDian(clickpoint_x, clickpoint_y)
            self.outPutMyLog('点击升级技能')
            self.delaytime(2)
            return '升级技能2'

        act_jinengdianbuzu_image = self.get_jineng_two_dangqianzuigao_image()
        pre_jinengdianbuzu = '%s/prepicture/jinengtwo/jinengdianbuzutwo.png' % current_file_path
        is_jinengdianbuzu = self.comparePicture(acturePic=act_jinengdianbuzu_image, prePic=pre_jinengdianbuzu,
                                                prebilv=0.9)
        if is_jinengdianbuzu:  # 如果是技能点不足，则退出循环
            self.outPutMyLog('节能点已经用完，技能点不足')
            return '技能点不足'

        pre_danqianzuigao = '%s/prepicture/jinengtwo/jinnengdangqianzuigaotwo.png' % current_file_path
        is_dangqianzuigao = self.comparePicture(acturePic=act_jinengdianbuzu_image, prePic=pre_danqianzuigao,
                                                prebilv=0.9)
        if is_dangqianzuigao:  # 如果是当前最高，则换下一个人，退出当前循环
            is_xiayige_ren = True
            self.outPutMyLog('当前最高，下一个')
            return '当前最高'
            # 升级二技能或者下一个人



    #屏幕亮屏
    def liangping(self):
        self.d.screen_on()
        self.outPutMyLog("点亮屏幕")

    #屏幕灭屏
    def meiping(self):
        self.d.screen_off()
        self.outPutMyLog("熄灭屏幕")

    #获取设备信息
    def get_info_dict(self):
        deivce_info_dict = self.d.info
        self.outPutMyLog("设备信息：%s" %str(deivce_info_dict))
        return deivce_info_dict

    #获取屏幕亮灭平
    def is_liang_ping(self):
        deivce_info_dict = self.get_info_dict()
        is_liang_ping = deivce_info_dict['screenOn']
        if is_liang_ping:
            self.outPutMyLog("屏幕处于亮屏状态")
        else:
            self.outPutMyLog("屏幕处于灭屏状态")
        return is_liang_ping

    #获取屏幕的高和宽
    def get_height_and_width(self):
        height_and_width_list = []
        deivce_info_dict =self.get_info_dict()
        height = deivce_info_dict['displayHeight']
        width = deivce_info_dict['displayWidth']
        self.outPutMyLog("设备高：%s" % str(height))
        self.outPutMyLog("设备宽：%s" % str(width))
        height_and_width_list.append(height)
        height_and_width_list.append(width)
        return height_and_width_list

    #从上往下滑动
    def from_up_to_down(self):
        height_and_width_list = self.get_height_and_width()
        height = height_and_width_list[0]
        width = height_and_width_list[1]
        di_x=int(int(width)//2)
        di_y=10
        ding_x=di_x
        ding_y=int(height)-10
        self.d.swipe(di_x, di_y,ding_x,ding_y,2)
        self.outPutMyLog("从顶点【%s,%s】滑动到底点【%s,%s】"%(str(di_x),str(di_y),str(ding_x),str(ding_y)))


    #从下往上滑动
    def from_down_to_up(self):
        height_and_width_list = self.get_height_and_width()
        height = height_and_width_list[0]
        width = height_and_width_list[1]
        di_x=int(int(width)//2)
        di_y=int(height)-10
        ding_x=di_x
        ding_y=10
        self.d.swipe(di_x, di_y,ding_x,ding_y,2)
        self.outPutMyLog("从低点【%s,%s】滑动到顶点【%s,%s】"%(str(di_x),str(di_y),str(ding_x),str(ding_y)))


class CaiJiClass(object):
    def __init__(self,outdevice=None, apppacakagename=None, isusb=None):
        self.outdevice = outdevice
        self.apppacakagename = apppacakagename
        self.bf = BaseFrame(outdevice=self.outdevice, apppacakagename=self.apppacakagename)
        self.returntext = ''

    def jiuRuZhuYe(self):
        bf = self.bf
        bf.outPutMyLog('开始执行')
        is_liangping = bf.is_liang_ping()
        bf.delaytime(2)
        if is_liangping:
            pass
        else:
            bf.liangping()  # 亮屏
            bf.delaytime(2)
            bf.from_down_to_up()  # 上划解锁
            bf.delaytime(2)

        bf.startapp()  # 启动应用
        # 判断是否加载出主页面
        # 截屏
        bf.delaytime(20)  # 等待5秒
        current_file_path = bf.getCurrentFilePath()
        pre_shouye = '%s/prepicture/shouye.png' % current_file_path
        is_paidu_text = bf.wait_and_conpate_and_click(preimage=pre_shouye, prebilv=0.9, point_x=10, point_y=10)  # 首页点击
        if str(is_paidu_text) == '正在排队' or str(is_paidu_text) == '重新启动':
            bf.outPutErrorMyLog("正在排队，重新开始")
            self.returntext = '重新主循环'
            return '重新主循环'

        bf.delaytime(20)  # 等待5秒
        # 进入游戏点击
        pre_shouye = '%s/prepicture/jinruyouxi.png' % current_file_path
        is_paidu_text = bf.wait_and_compare_bufenimage_and_click(preimage=pre_shouye, prebilv=0.9,
                                                                 clickpoint_x=936, clickpoint_y=1000,
                                                                 jiepingpoint_x=798,
                                                                 jiepingpoint_y=975,
                                                                 jiepingkongjian_width=312,
                                                                 jiepingkongjian_height=87)  # 点击进入游戏
        if str(is_paidu_text) == '正在排队' or str(is_paidu_text) == '重新启动':
            bf.outPutErrorMyLog("正在排队，重新开始")
            self.returntext = '重新主循环'
            return '重新主循环'

        bf.delaytime(20)  # 等待5秒

        # 有三个登录领取礼包
        for i in range(0, 5):
            bf.clickGuDingDian(1809, 251)
            bf.delaytime(2)
            bf.clickGuDingDian(1855, 86)
            bf.delaytime(2)
            bf.clickGuDingDian(1855, 86)
            bf.delaytime(2)

        # # 秘密召唤1
        # bf.delaytime(20)  #等待5秒
        # #秘密召唤
        # pre_shouye = '%s/prepicture/jinribuzaixianshi.png'%current_file_path
        # is_paidu_text = bf.wait_and_compare_bufenimage_and_click(preimage=pre_shouye,prebilv=0.9,
        #                                                          clickpoint_x=1740,clickpoint_y=240,
        #                                                          jiepingpoint_x=298,
        #                                                          jiepingpoint_y=806,
        #                                                          jiepingkongjian_width=190,
        #                                                          jiepingkongjian_height=50)     #点击秘密召唤中的x,关闭图片
        # if str(is_paidu_text) == '正在排队':
        #     bf.outPutErrorMyLog("正在排队，重新开始")
        #     continue

        for i in range(0, 2):  # 给2次，点击弹出的弹框
            # 突破200万，中秋祭典
            # 中秋祭典
            bf.delaytime(5)  # 等待5秒
            # 中秋祭典
            pre_shouye = '%s/prepicture/jinribuzaixianshi.png' % current_file_path
            is_paidu_text = bf.wait_and_compare_bufenimage_and_click(preimage=pre_shouye, prebilv=0.9,
                                                                     clickpoint_x=1740, clickpoint_y=240,
                                                                     jiepingpoint_x=298,
                                                                     jiepingpoint_y=806,
                                                                     jiepingkongjian_width=190,
                                                                     jiepingkongjian_height=50,
                                                                     is_for_coutinue=True)  # 点击中秋祭典中的x,关闭图片
            if str(is_paidu_text) == '正在排队':
                bf.outPutErrorMyLog("正在排队，重新开始")
                break  # 终止for循环

        if str(is_paidu_text) == '正在排队':
            bf.outPutErrorMyLog("正在排队，重新开始")
            self.returntext = '重新主循环'
            return '重新主循环'

        self.returntext = ''

    def caiJi(self):


        # # 激进的圣光
        # bf.delaytime(5)  #等待5秒
        # #激进的圣光
        # pre_shouye = '%s/prepicture/jinribuzaixianshi.png'%current_file_path
        # is_paidu_text = bf.wait_and_compare_bufenimage_and_click(preimage=pre_shouye,prebilv=0.9,
        #                                                          clickpoint_x=1740,clickpoint_y=240,
        #                                                          jiepingpoint_x=298,
        #                                                          jiepingpoint_y=806,
        #                                                          jiepingkongjian_width=190,
        #                                                          jiepingkongjian_height=50)   #点击激进的圣光中x,关闭图片
        # if str(is_paidu_text) == '正在排队':
        #     bf.outPutErrorMyLog("正在排队，重新开始")
        #     continue

        # # # 升级祝福礼
        # bf.delaytime(5)  #等待5秒
        # # #升级祝福礼
        # pre_shouye = '%s/prepicture/shengjizhufuli.png'%current_file_path
        # is_paidu_text =bf.wait_and_conpate_and_click(preimage=pre_shouye, prebilv=0.8,point_x=1800,point_y=267)   #点击升级祝福礼
        # if is_paidu_text == '正在排队':
        #     bf.outPutErrorMyLog("正在排队，重新开始")
        #     continue
        bf = self.bf
        current_file_path = bf.getCurrentFilePath()
        # 采收
        bf.delaytime(5)  # 等待5秒
        # 采收
        pre_shouye = '%s/prepicture/caishou.png' % current_file_path
        is_paidu_text = bf.wait_and_compare_bufenimage_and_click(preimage=pre_shouye, prebilv=0.7,
                                                                 clickpoint_x=892, clickpoint_y=1005,
                                                                 jiepingpoint_x=938,
                                                                 jiepingpoint_y=930,
                                                                 jiepingkongjian_width=96,
                                                                 jiepingkongjian_height=34)  # 点击采收
        if str(is_paidu_text) == '正在排队':
            bf.outPutErrorMyLog("正在排队，重新开始")
            self.returntext = '重新主循环'
            return '重新主循环'
        bf.delaytime(5)  # 等待5秒
        bf.d.click(1009, 808)  # 撤去采收完成的弹框
        self.returntext = ''

    def miePing(self):
        bf =self.bf
        bf.meiping()
        bf.stopapp()
        self.returntext = ''


    def caiJiDef(self):
        self.jiuRuZhuYe()
        self.caiJi()
        self.miePing()

    def shengJiJiNeng(self):
        bf = self.bf
        current_file_path = bf.getCurrentFilePath()
        # 英雄头像
        # 点击英雄头像
        bf.delaytime(5)  # 等待5秒
        # 英雄头像
        pre_shouye = '%s/prepicture/yingxiongtouxiang.png' % current_file_path
        is_paidu_text = bf.wait_and_conpate_and_click(preimage=pre_shouye, prebilv=0.1, point_x=138,
                                                      point_y=295)  # 点击英雄头像
        if str(is_paidu_text) == '正在排队':
            bf.outPutErrorMyLog("正在排队，重新开始")
            self.returntext = '重新主循环'
            return '重新主循环'

        # 技能
        # 点击技能
        bf.delaytime(5)  # 等待5秒
        # 技能
        pre_shouye = '%s/prepicture/jineng.png' % current_file_path
        is_paidu_text = bf.wait_and_conpate_and_click(preimage=pre_shouye, prebilv=0.1, point_x=136,
                                                      point_y=535)  # 点击技能
        if str(is_paidu_text) == '正在排队':
            bf.outPutErrorMyLog("正在排队，重新开始")
            self.returntext = '重新主循环'
            return '重新主循环'

        #点击技能
        #点击技能1
        count_xunhuan = 1
        for i in range(0,20):
            jineng_one_result = bf.handle_jineng_one()
            if str(jineng_one_result) == '技能点不足':
                break  #退出循环
            if str(jineng_one_result) == '升级技能1':
                continue #继续循环
            if str(jineng_one_result) == '当前最高':
                bf.outPutMyLog("继续下一个技能或者下一个人")
                bf.outPutMyLog("暂且升级继续二技能")
                break  #退出一技能处理循环
            if str(jineng_one_result) == '正在排队':
                self.returntext = '重新主循环'
                return '重新主循环'
            count_xunhuan = count_xunhuan +1

        #点击技能2
        for i in range(count_xunhuan,20):
            jineng_two_result = bf.handle_jineng_two()
            if str(jineng_two_result) == '技能点不足':
                break  #退出循环
            if str(jineng_two_result) == '升级技能2':
                continue #继续循环
            if str(jineng_two_result) == '当前最高':
                bf.outPutMyLog("继续下一个技能或者下一个人")
                bf.outPutMyLog("暂且升级继续二技能")
                break  #退出一技能处理循环
            if str(jineng_two_result) == '正在排队':
                self.returntext = '重新主循环'
                return '重新主循环'
            count_xunhuan = count_xunhuan +1

        #一个人的技能1和技能2处理完成后
        self.returntext = ''   #设置位正常结束



        # is_while_break = False
        # while True:   #出现技能点不足时，就终止升级技能循环
        #     # 点击第一个人
        #     first_x = 477
        #     forst_y = 962
        #     bf.clickGuDingDian(first_x, forst_y)
        #     bf.delaytime(2)  # 等2秒
        #
        #     # 升级一技能
        #     # 点击升级一技能，直到
        #     bf.delaytime(5)  # 等待5秒
        #     # 升级一技能
        #     #点击技能升级前判断
        #     pre_shouye = '%s/prepicture/jinnengshengji.png' % current_file_path
        #     # quedingimage = '%s/prepicture/queding.png' % current_file_path
        #     is_paidu_text = bf.wait_and_compare_bufenimage_and_click(preimage=pre_shouye, prebilv=0.9,
        #                                                          clickpoint_x=1740, clickpoint_y=220,
        #                                                          jiepingpoint_x=86,
        #                                                          jiepingpoint_y=36,
        #                                                          jiepingkongjian_width=190,
        #                                                          jiepingkongjian_height=110)  # 点击一技能
        #
        #
        #
        #     pre_shouye = '%s/prepicture/jinnengshengji.png' % current_file_path
        #     # quedingimage = '%s/prepicture/queding.png' % current_file_path
        #     is_paidu_text = bf.wait_and_compare_bufenimage_and_click(preimage=pre_shouye, prebilv=0.9,
        #                                                          clickpoint_x=1740, clickpoint_y=220,
        #                                                          jiepingpoint_x=86,
        #                                                          jiepingpoint_y=36,
        #                                                          jiepingkongjian_width=190,
        #                                                          jiepingkongjian_height=110)  # 点击一技能
        #     is_paidu_text = bf.wait_and_conpate_and_click_and_loop_click(preimage=pre_shouye, prebilv=0.1, point_x=1797,
        #                                                                  point_y=305, quedingimage=quedingimage)
        #     if str(is_paidu_text) == '正在排队':
        #         bf.outPutErrorMyLog("正在排队，重新开始")
        #         self.returntext = '重新主循环'
        #         return '重新主循环'
        #
        #
        #     # 升级一技能之判断一技能是否达到最高
        #     pre_shouye = '%s/prepicture/dangqianzuigao.png' % current_file_path
        #     quedingimage = '%s/prepicture/queding.png' % current_file_path
        #     is_paidu_text = bf.wait_and_compare_bufenimage_and_click(preimage=pre_shouye, prebilv=0.9,
        #                                                          clickpoint_x=1797, clickpoint_y=305,
        #                                                          jiepingpoint_x=1690,
        #                                                          jiepingpoint_y=210,
        #                                                          jiepingkongjian_width=190,
        #                                                          jiepingkongjian_height=110)  # 点击一技能
        #
        #     is_paidu_text = bf.wait_and_conpate_and_click_and_loop_click(preimage=pre_shouye, prebilv=0.1, point_x=1797,
        #                                                                  point_y=305, quedingimage=quedingimage)
        #     if str(is_paidu_text) == '正在排队':
        #         bf.outPutErrorMyLog("正在排队，重新开始")
        #         self.returntext = '重新主循环'
        #         return '重新主循环'
        #
        #     # 升级二技能
        #     # 点击升级二技能，直到
        #     bf.delaytime(5)  # 等待5秒
        #     # 升级一技能
        #     pre_shouye = '%s/prepicture/shengjijinengone.png' % current_file_path
        #     quedingimage = '%s/prepicture/queding.png' % current_file_path
        #     is_paidu_text = bf.wait_and_conpate_and_click_and_loop_click(preimage=pre_shouye, prebilv=0.1, point_x=1797,
        #                                                                  point_y=505, quedingimage=quedingimage)
        #     if str(is_paidu_text) == '正在排队':
        #         bf.outPutErrorMyLog("正在排队，重新开始")
        #         self.returntext = '重新主循环'
        #         return '重新主循环'
        #
        #
        #     # 滑动
        #     di_x = 1497
        #     di_y = 506
        #     ding_x = di_x
        #     ding_y = 155
        #     bf.d.swipe(di_x, di_y, ding_x, ding_y, 2)
        #
        #     # 升级三技能
        #     # 点击升级一技能，直到
        #     bf.delaytime(500)  # 等待5秒
        #     # 升级一技能
        #     pre_shouye = '%s/prepicture/shengjijinengone.png' % current_file_path
        #     quedingimage = '%s/prepicture/queding.png' % current_file_path
        #     is_paidu_text = bf.wait_and_conpate_and_click_and_loop_click(preimage=pre_shouye, prebilv=0.9, point_x=1797,
        #                                                                  point_y=305, quedingimage=quedingimage)
        #     if str(is_paidu_text) == '正在排队':
        #         bf.outPutErrorMyLog("正在排队，重新开始")
        #         self.returntext = '重新主循环'
        #         return '重新主循环'
        #
        #     # 回去滑动
        #     di_x = 1497
        #     di_y = 155
        #     ding_x = di_x
        #     ding_y = 506
        #     bf.d.swipe(di_x, di_y, ding_x, ding_y, 2)


    def shengJiJiNengDef(self):
        self.jiuRuZhuYe()
        self.shengJiJiNeng()
        self.miePing()



if __name__ == "__main__":

    while True:

        outdevice = "192.168.1.100:5555"
        apppacakagename = "com.superhgame.rpg.emma"

        while True:
            try:
                #采集
                cjc = CaiJiClass(outdevice=outdevice,apppacakagename=apppacakagename)
                cjc.caiJiDef()
                is_continue_text =cjc.returntext
                if is_continue_text == '重新主循环':
                    continue

                #升级技能点
                cjc = CaiJiClass(outdevice=outdevice,apppacakagename=apppacakagename)
                cjc.shengJiJiNengDef()
                is_continue_text =cjc.returntext
                if is_continue_text == '重新主循环':
                    continue
            except Exception as e:
                print("采集或升级技能出错，原因【%s】"%str(e))
                continue
            else:
                print('采集或升级技能成功完成')
                break  #终止循环
        print("即将睡一小时，准备下次循环")
        time.sleep(3600)#睡一小时


































