from django import forms    #导入django中的forms

from .modelsnewdev import NodeConfig,ConfigCollectSendCmd,ConfigCollectFactor

class NodeConfigForm(forms.ModelForm):#定义处理前段“我要学习”表单类,继承ModelForm,ModelForm可以直接save,这个save调用的就是model的save，可以直接保存到数据库
    class Meta:
        model = NodeConfig   #指明转换的QSLoginAndCheck
        fields = "__all__"


class ConfigCollectSendCmdForm(forms.ModelForm):#定义处理前段“我要学习”表单类,继承ModelForm,ModelForm可以直接save,这个save调用的就是model的save，可以直接保存到数据库
    class Meta:
        model = ConfigCollectSendCmd   #指明转换的QSLoginAndCheck
        fields = "__all__"
