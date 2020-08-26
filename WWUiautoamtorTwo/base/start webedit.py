import os

# init 所有的已经连接到电脑的设备
a = os.popen("python -m uiautomator2 init")
print(a.read())

#启动 weditor
b = os.popen("python -m weditor")
print(b.read())