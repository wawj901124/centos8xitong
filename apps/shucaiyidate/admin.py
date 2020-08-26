from django.contrib import admin

from .modelsnewdev import NodeConfig,ConfigCollectSendCmd,ConfigCollectFactor



# Register your models here.
class ConfigCollectSendCmdInline(admin.StackedInline):
    model = ConfigCollectSendCmd
    exclude = ["write_user", "add_time", "update_time"]
    extra = 0
    style = 'accordion'  # 以标签形式展示 ，形式有：stacked，one，accordion（折叠），tab（标签），table（表格）

class ConfigCollectFactorInline(admin.StackedInline):
    model = ConfigCollectFactor
    exclude = ["write_user", "add_time", "update_time"]
    extra = 0
    style = 'accordion'  # 以标签形式展示 ，形式有：stacked，one，accordion（折叠），tab（标签），table（表格）


class NodeConfigAdmin(admin.ModelAdmin):
    list_display = ["config_project",
                    "config_file_name",
                    "config_xieyi_num",
                    "config_xieyi_type",
                    "config_version",
                    "config_device",
                    ]  # 定义显示的字段
    inlines = [ConfigCollectSendCmdInline,
               ConfigCollectFactorInline,]
    def get_inline_formsets(self, request, formsets, inline_instances, obj=None):
        pass


admin.site.register(NodeConfig,NodeConfigAdmin)   #在xadmin中注册NodeConfig
