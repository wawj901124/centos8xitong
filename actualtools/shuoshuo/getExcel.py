class GlobalVar:
    #模板标题字段对应列数
    id = '0'
    webproject = '1'
    testpage = '2'
    testcasetitle = '3'
    isclicklastpage = '4'
    selectxpath = '5'
    selectoptiontextxpath = '6'
    selectinputxpath = '7'
    selectinputselectonexpath = '8'
    selectinputtext = '9'
    isfind = '10'
    colnum = '11'
    checktext = '12'
    add_time = '13'

from db_tools.util.operation_excel import OperationExcel   #导入OperationExcel
from db_tools.importsearchdata.importexceldata.dataconfig.exceldata_config import  *      #导入


class GetData:
    def __init__(self,file_name=None,sheet_id=None):
        self.file_name = file_name
        self.sheet_id = sheet_id
        self.opera_excel = OperationExcel(self.file_name,self.sheet_id)   #实例化
        self.global_var = GlobalVar()   #实例化


    #去获取excel行数，就是我们的case个数
    def get_case_lines(self):
        return self.opera_excel.get_lines()

    # 获取id
    def get_id(self,row):
        col = int(self.global_var.id)  #获取id所在的列数
        id = self.opera_excel.get_cell_value(row, col)   #获取指定单元格的内容
        return id

    # 获取webproject
    def get_webproject(self,row):
        col = int(self.global_var.webproject)  #获取webproject所在的列数
        webproject = self.opera_excel.get_cell_value(row, col)   #获取指定单元格的内容
        return webproject

    #获取testpage
    def get_testpage(self,row):
        col = int(self.global_var.testpage)  #获取testpage所在的列数
        testpage = self.opera_excel.get_cell_value(row, col)   #获取指定单元格的内容
        return testpage

    # 获取testcasetitle
    def get_testcasetitle(self,row):
        col = int(self.global_var.testcasetitle)  #获取testcasetitle所在的列数
        testcasetitle = self.opera_excel.get_cell_value(row, col)   #获取指定单元格的内容
        return testcasetitle

    # 获取isclicklastpage
    def get_isclicklastpage(self,row):
        col = int(self.global_var.isclicklastpage)  #获取isclicklastpage所在的列数
        isclicklastpage = self.opera_excel.get_cell_value(row, col)   #获取指定单元格的内容
        if isclicklastpage == "TRUE":
            return "1"
        elif isclicklastpage == "True":
            return "1"
        elif isclicklastpage == "true":
            return "1"
        elif isclicklastpage == u"是":
            return "1"
        elif isclicklastpage == u"点击":
            return "1"
        elif isclicklastpage == "FALSE":
            return "0"
        elif isclicklastpage == "False":
            return "0"
        elif isclicklastpage == "false":
            return "0"
        elif isclicklastpage == u"否":
            return "0"
        elif isclicklastpage == u"不是":
            return "0"
        elif isclicklastpage == u"不点击":
            return "0"
        return isclicklastpage


    # 获取selectxpath
    def get_selectxpath(self,row):
        col = int(self.global_var.selectxpath)  #获取selectxpath所在的列数
        selectxpath = self.opera_excel.get_cell_value(row, col)   #获取指定单元格的内容
        if selectxpath == u"空":
            return None
        elif selectxpath == "":
            return None
        elif selectxpath == " ":
            return None
        return selectxpath

    #获取selectoptiontextxpath
    def get_selectoptiontextxpath(self,row):
        col = int(self.global_var.selectoptiontextxpath)  #获取selectoptiontextxpath所在的列数
        selectoptiontextxpath = self.opera_excel.get_cell_value(row, col)   #获取指定单元格的内容
        if selectoptiontextxpath == u"空":
            return None
        elif selectoptiontextxpath == "":
            return None
        elif selectoptiontextxpath == " ":
            return None
        return selectoptiontextxpath

    # 获取selectinputxpath
    def get_selectinputxpath(self,row):
        col = int(self.global_var.selectinputxpath)  #获取selectinputxpath所在的列数
        selectinputxpath = self.opera_excel.get_cell_value(row, col)   #获取指定单元格的内容
        if selectinputxpath == u"空":
            return None
        elif selectinputxpath == "":
            return None
        elif selectinputxpath == " ":
            return None
        return selectinputxpath

    # 获取selectinputselectonexpath
    def get_selectinputselectonexpath(self,row):
        col = int(self.global_var.selectinputselectonexpath)  #获取selectinputselectonexpath所在的列数
        selectinputselectonexpath = self.opera_excel.get_cell_value(row, col)   #获取指定单元格的内容
        if selectinputselectonexpath == u"空":
            return None
        elif selectinputselectonexpath == "":
            return None
        elif selectinputselectonexpath == " ":
            return None
        return selectinputselectonexpath

    # 获取selectinputtext
    def get_selectinputtext(self,row):
        col = int(self.global_var.selectinputtext)  #获取selectinputtext所在的列数
        selectinputtext = self.opera_excel.get_cell_value(row, col)   #获取指定单元格的内容
        if selectinputtext == u"空":
            return None
        elif selectinputtext == "":
            return None
        elif selectinputtext == " ":
            return None
        return selectinputtext

    #获取isfind
    def get_isfind(self,row):
        col = int(self.global_var.isfind)  #获取isfind所在的列数
        isfind = self.opera_excel.get_cell_value(row, col)   #获取指定单元格的内容
        if isfind == "TRUE":
            return "1"
        elif isfind == "True":
            return "1"
        elif isfind == "true":
            return "1"
        elif isfind == u"是":
            return "1"
        elif isfind == u"有":
            return "1"
        elif isfind == "FALSE":
            return "0"
        elif isfind == "False":
            return "0"
        elif isfind == "false":
            return "0"
        elif isfind == u"否":
            return "0"
        elif isfind == u"没有":
            return "0"
        return isfind

    # 获取colnum
    def get_colnum(self,row):
        col = int(self.global_var.colnum)  #获取colnum所在的列数
        colnum = self.opera_excel.get_cell_value(row, col)   #获取指定单元格的内容
        return colnum

    # 获取checktext
    def get_checktext(self,row):
        col = int(self.global_var.checktext)  #获取checktext所在的列数
        checktext = self.opera_excel.get_cell_value(row, col)   #获取指定单元格的内容
        return checktext

    # # 获取write_comments
    # def get_write_comments(self,row):
    #     col = int(self.global_var.write_comments)  #获取write_comments所在的列数
    #     write_comments = self.opera_excel.get_cell_value(row, col)   #获取指定单元格的内容
    #     return write_comments
    #
    # # 获取write_user
    # def get_write_user(self,row):
    #     col = int(self.global_var.write_user)  #获取write_user所在的列数
    #     write_user = self.opera_excel.get_cell_value(row, col)   #获取指定单元格的内容
    #     return write_user
    #
    # #获取write_case_time
    # def get_write_case_time(self,row):
    #     col = int(self.global_var.write_case_time)  #获取write_case_time所在的列数
    #     write_case_time = self.opera_excel.get_cell_value(row, col)   #获取指定单元格的内容
    #     return write_case_time
    #
    # # 获取ex_result
    # def get_ex_result(self,row):
    #     col = int(self.global_var.ex_result)  #获取ex_result所在的列数
    #     ex_result = self.opera_excel.get_cell_value(row, col)   #获取指定单元格的内容
    #     return ex_result
    #
    # #获取write_case_time
    # def get_test_comments(self,row):
    #     col = int(self.global_var.test_comments)  #获取test_comments所在的列数
    #     test_comments = self.opera_excel.get_cell_value(row, col)   #获取指定单元格的内容
    #     return test_comments
    #
    # # 获取test_user
    # def get_test_user(self,row):
    #     col = int(self.global_var.test_user)  #获取test_user所在的列数
    #     test_user = self.opera_excel.get_cell_value(row, col)   #获取指定单元格的内容
    #     return test_user