import uiautomator2 as u2
import os
import logging
import time

from WWUiautoamtorTwo.util.myLogs import MyLogs
from WWUiautoamtorTwo.util.getTimeStr import GetTimeStr
from WWUiautoamtorTwo.util.comparePictureSSIM import CompareImage

class AdbActionApp:
    def __init__(self,device_name,
                 app_start_active,
                 package_name):
        self.device_name = device_name
        self.app_start_active = app_start_active
        self.d = self.connet_device()
        self.app_package_name = package_name

    def outPutMyLog(self, context):
        mylog = MyLogs(context)
        mylog.runMyLog()

    def outPutErrorMyLog(self, context):
        mylog = MyLogs(context)
        mylog.runErrorLog()

    def delay_time(self,delay_time):
        time.sleep(int(delay_time))
        self.outPutMyLog("等待%s秒"% delay_time)


    def execure_cmd(self,cmdorder):
        order = os.popen(cmdorder)
        order_info = order.read()
        self.outPutMyLog(order_info)

    def connet_device(self):
        d=u2.connect_adb_wifi(self.device_name)
        d = u2.connect_wifi()
        self.outPutMyLog("连接设备【%s】" % self.device_name)
        return d

    def startApp(self):
        adbstartappcmd = "adb shell am start %s" % self.app_start_active
        self.execure_cmd(adbstartappcmd)
        self.delay_time(5)

    def killApp(self):
        package_name = self.app_package_name
        adbkillappcmd = "adb shell am force-stop %s" %package_name
        self.execure_cmd(adbkillappcmd)

    def clickApp(self,click_x,click_y):
        self.d.click(click_x,click_y)
        self.outPutMyLog("点击【%s,%s】" %(click_x,click_y))
        self.delay_time(5)

    def getNowFilePath(self):
        now_file_root_path = os.path.dirname(os.path.abspath(__file__))
        self.outPutMyLog("当前文件所在文件夹路径：%s" % str(now_file_root_path))
        return now_file_root_path

    def getScreenPicture(self):
        gts = GetTimeStr()
        time_str = gts.getTimeStr()
        picture_name = "%s.png"% time_str
        screen_cmd = "adb shell screencap -p /sdcard/gramescreen/%s" %picture_name
        self.execure_cmd(screen_cmd)
        pull_cmd = "adb pull /sdcard/gramescreen/%s ./comparepictures/acturepicture/%s" %(picture_name,picture_name)
        self.execure_cmd(pull_cmd)
        now_file_root_path = self.getNowFilePath()
        acture_picture_path = "%s/comparepictures/acturepicture/%s" % (now_file_root_path,picture_name)
        self.outPutMyLog("需要验证的截图：【%s】" % acture_picture_path)

    def comparePicture(self,acturePic,prePic,prebilv):
        acture_pic_path = acturePic
        pre_pic_path = prePic
        ci = CompareImage()
        acture_bilv = ci.compare_image(acture_pic_path, pre_pic_path)
        self.outPutMyLog("图片相似度：%s" % str(acture_bilv))
        bilv = prebilv
        if acture_bilv>=bilv:
            self.outPutMyLog("图片相似度【%s】 比预期相似度【%s】高或一样" % (str(acture_bilv),str(bilv)))
            return True
        else:
            self.outPutMyLog("图片相似度【%s】 比预期相似度【%s】低" % (str(acture_bilv),str(bilv)))
            return False






if __name__ == '__main__':
    device_name = "192.168.1.100:5555"
    app_start_active = "com.superhgame.rpg.emma/com.prime31.UnityPlayerNativeActivity"
    package_name = "com.superhgame.rpg.emm"
    aaa = AdbActionApp(device_name,app_start_active,package_name)
    # aaa.startApp()
    # aaa.delay_time(15)

    # aaa.getNowFilePath()

    #截图界面
    aaa.getScreenPicture()


    # click_x= 0.428
    # click_y = 0.928
    # aaa.clickApp(click_x,click_y)  #点击当前页面坐标进入下一个页面
    # aaa.delay_time(30)
    # aaa.clickApp(click_x, click_y) #点击当前页面坐标进入下一个页面


