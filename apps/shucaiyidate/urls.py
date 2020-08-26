from django.urls import  path

from .views import  manage_nodeconfig #导入ClickAndBackView
from .views import nodeconfig_add



urlpatterns = [
    # 漫画图片页面的url配置
    path('managenodeconfig/', manage_nodeconfig, name="manage_node_config"),
    # 配置复制新增测试用例url,namespace指明命名空间，用命名空间做限定

    # 漫画图片页面的url配置
    path('nodeconfigadd/', nodeconfig_add, name="node_config_add"),
    # 配置复制新增测试用例url,namespace指明命名空间，用命名空间做限定


]

app_name = 'shucaiyidate'

