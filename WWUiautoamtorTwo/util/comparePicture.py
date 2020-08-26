from PIL import Image
from PIL import ImageChops


def CompareImages(acture_pic_path, pre_pic_path):
    """
    比较图片
    :param path_one: 第一张图片的路径
    :param path_two: 第二张图片的路径
    :return: 相同返回 success
    """
    image_one = Image.open(acture_pic_path)
    image_two = Image.open(pre_pic_path)
    try:
        diff = ImageChops.difference(image_one, image_two)

        if diff.getbbox() is None:
            # 图片间没有任何不同则直接退出
            print("success")
            return True
        else:
            print("ERROR: 匹配失败！")
            return False

    except ValueError as e:
        print("{0}\n{1}".format(e, "图片大小和box对应的宽度不一致!"))
        return False


if __name__ == '__main__':
    acture_pic_path = "D:/PycharmProjects/shangbaogongju/WWUiautoamtorTwo/base/comparepictures/acturepicture/20200613220540.png"
    pre_pic_path = "D:/PycharmProjects/shangbaogongju/WWUiautoamtorTwo/base/comparepictures/prepicture/exception/网络不稳定断线.png"

    CompareImages(
        acture_pic_path, pre_pic_path
    )
