import pymysql

conn_dcloud_base = pymysql.connect(host="192.168.8.205", port=3306, user="root", password="admin123!@#qwe",
                       database="dcloud_base", charset="utf8")
conn_dcloud_data = pymysql.connect(host="192.168.8.205", port=3306, user="root", password="admin123!@#qwe",
                       database="dcloud_data", charset="utf8")

cursor_dcloud_base = conn_dcloud_base.cursor()

cursor_dcloud_data = conn_dcloud_data.cursor()


def connectDcloudBaseMyDBAndSelect(sql):
    cursor_dcloud_base.execute(sql)
    # 数据库提交命令
    # self.conn.commit()  # 执行update操作时需要写这个，否则就会更新不成功
    rs = cursor_dcloud_base.fetchall()  # 获取执行sql后的结果
    # for r in rs:
    #     # print(r)
    #     mn_id = r[0]
    #     break
    # print(mn_id)
    return rs

def connectDcloudDataMyDBAndSelect(sql):
    cursor_dcloud_data.execute(sql)
    # 数据库提交命令
    # self.conn.commit()  # 执行update操作时需要写这个，否则就会更新不成功
    rs = cursor_dcloud_data.fetchall()  # 获取执行sql后的结果
    # for r in rs:
    #     # print(r)
    #     mn_id = r[0]
    #     break
    # print(mn_id)
    return rs




#根据支干/断面名称查询水质类别
#支干/断面名称
# zhigan_name = "昌平区测试设备1号"
zhigan_name ="支干/断面名称20200108105836"
#根据支干/断面查询tb_station表获取对应数据的
mysql_yuju = """
        SELECT * FROM tb_station WHERE NAME='%s'
        """% zhigan_name
# cursor_dcloud_base.execute(mysql_yuju)
# # 数据库提交命令
# # self.conn.commit()  # 执行update操作时需要写这个，否则就会更新不成功
# rs = cursor_dcloud_base.fetchall()  # 获取执行sql后的结果
# for r in rs:
#     # print(r)
#     mn_id = r[0]
#     break

tbStation = connectDcloudBaseMyDBAndSelect(mysql_yuju)[0]
# print(tbStation)
# print("ID:%s" % tbStation[0])
# print("AREA_ID（所属省ID）:%s" % tbStation[1])
# print("CITY_ID（所属流域ID）:%s" % tbStation[2])
# print("MCUSN（MN号）:%s" % tbStation[3])
# print("NAME(支干/断面):%s" % tbStation[4])
# print("UPLOAD_INTERVAL:%s" % tbStation[5])
# print("ADDRESS（站点地址）:%s" % tbStation[6])
#
# print("STANDARD_ID:%s" % tbStation[7])
# print("STANDARD_FILE_NAME（执行标准）:%s" % tbStation[8])
# print("STANDARD_FILE_RUL（执行标准URL路径）:%s" % tbStation[9])
# print("STANDARD_FILE_NEW_NAME:%s" % tbStation[10])
# print("OPERTOR（联系人）:%s" % tbStation[11])
# print("TELEPHONE（联系方式）:%s" % tbStation[12])
# print("file_id（站点图片ID）:%s" % tbStation[13])
#
# print("remarks（备注）:%s" % tbStation[14])
# print("CREATETIME:%s" % tbStation[15])
# print("LONGITUDE:%s" % tbStation[16])
# print("LATITUDE:%s" % tbStation[17])

cityid = tbStation[2]
fileid = tbStation[13]

tbStationid = tbStation[0]
print(tbStationid )
#根据站点ID查询td_real_upload中的数据（实时数据）
mysql_yuju = """
        SELECT FACTOR_CODE,FACTOR_VALUE FROM td_real_update WHERE STATION_ID='%s'
        """% tbStationid
# cursor_dcloud_base.execute(mysql_yuju)
# # 数据库提交命令
# # self.conn.commit()  # 执行update操作时需要写这个，否则就会更新不成功
# rs = cursor_dcloud_base.fetchall()  # 获取执行sql后的结果
# for r in rs:
#     # print(r)
#     mn_id = r[0]
#     break

yinzi_list = connectDcloudBaseMyDBAndSelect(mysql_yuju)
yinzi_jieguo_list = []
for yinzi in yinzi_list:
    # print(yinzi)
    yinzi_code = yinzi[0]
    yinzi_value = yinzi[1]
    # print(yinzi_code)
    #根据因子code查询tb_factor得到因子名称
    mysql_yuju = """
            SELECT FACTOR_NAME FROM tb_factor WHERE FACTOR_CODE='%s'
            """ % yinzi_code
    yinzi_name = connectDcloudBaseMyDBAndSelect(mysql_yuju)[0][0]
    # print(yinzi_name)
    # print(yinzi_value)
    print("%s:%s" % (yinzi_name,yinzi_value))












#