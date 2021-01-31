import uiautomator2 as u2
import os

# d = u2.connect('192.168.1.101') # alias for u2.connect_wifi('10.0.0.1')
d = u2.connect_adb_wifi("192.168.1.100:5555")
print(d.info)

# adbstartappcmd = "adb shell am start com.superhgame.rpg.emma/com.prime31.UnityPlayerNativeActivity"
# # os.popen(adbstartappcmd)
# d.screenshot("10.png")
# 滑动
di_x = 1497
di_y = 506
ding_x = di_x
ding_y = 155
d.swipe(di_x, di_y, ding_x, ding_y, 2)

