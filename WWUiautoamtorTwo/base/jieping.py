from PIL import Image   #导入Image

def getBuFenImage(wholeimagepath,point_x=298,point_y=806,kongjian_width=190,kongjian_height=50):
    pageScreenshotpath = wholeimagepath  # 获取整个页面截图
    # # location = ele.location   #获取验证码x,y轴坐标   #截取了BUSINESS
    # location = ele.location_once_scrolled_into_view  # 获取元素x,y轴坐标   #消除self.driver.execute_script("arguments[0].scrollIntoView();", ele) 对截图的影响 截取了login imgae
    # size = ele.size  # 获取元素的长宽
    # coderange = (int(location['x']), int(location['y']), int(location['x'] + size['width']),
    #              int(location['y'] + size['height']))  # 写成我们需要截取的位置坐标
    coderange = (point_x, point_y,
                 point_x + kongjian_width,
                 point_y + kongjian_height)
    pageScreenshot = Image.open(pageScreenshotpath)  # 打开截图
    imageScreen = pageScreenshot.crop(coderange)  # 使用Image的crop函数，从截图中再次截取我们需要的区域,即验证码区域
    # tStr = self.getTimeStr()
    # currentfilepath = self.getCurrentFilePath()
    # firedir = r'%s/imagefile/ele' % currentfilepath
    # self.createdir(firedir)
    eleimage = "elejinribuzaixianshi.png"
    imageScreen.save(eleimage)  # 保存控件截图
    # self.outPutMyLog('获取到的元素的截图路径为：%s' % eleimage)
    return eleimage


getBuFenImage(wholeimagepath=r'D:\PycharmProjects\centos8xitong\WWUiautoamtorTwo\prepicture\mimizhaohuanone.png')