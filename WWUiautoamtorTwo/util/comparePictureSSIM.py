#安装skimage
#pip install -i https://pypi.tuna.tsinghua.edu.cn/simple scikit-image
#或 pip install scikit-image
#pip install -i https://pypi.tuna.tsinghua.edu.cn/simple opencv-python
#3.6 安装 cv2 :https://blog.csdn.net/ethan_sui/article/details/105515624
# pip install -i https://pypi.tuna.tsinghua.edu.cn/simple opencv-python==3.4.2.16
# pip install opencv-contrib-python==3.4.2.16
#注意，图片路径中不要包含中文，否则会报错(-215:Assertion failed)

from skimage.measure import compare_ssim
import cv2

class CompareImage():

    def compare_image(self, path_image1, path_image2):

        imageA = cv2.imread(path_image1)
        imageB = cv2.imread(path_image2)

        grayA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)
        grayB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)

        (score, diff) = compare_ssim(grayA, grayB, full=True)
        print("SSIM: {}".format(score))
        return score

if __name__ == '__main__':
    acture_pic_path = "D:\PycharmProjects\centos8xitong\WWUiautoamtorTwo\prepicture\jinruyouxi.png"
    pre_pic_path = "D:\PycharmProjects\centos8xitong\WWUiautoamtorTwo\screenshots\screenpicture_20201003155605.png"

    compare_image = CompareImage()
    compare_image.compare_image(acture_pic_path, pre_pic_path)