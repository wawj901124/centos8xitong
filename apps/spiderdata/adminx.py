import xadmin
from django.utils.safestring import mark_safe   #调用mark_safe这个函数，django可以显示成一个文本，而不是html代码

from .models import SpiderData,SpiderDownLoad,SpiderVideo
from .modelshm import SpiderHMBook
from .modelsurl import SpiderWebUrl,CopySpiderWebUrl

from xadmin.plugins.actions import BaseActionView   #导入ActionView

class MyAction(BaseActionView):
    #这里需要填写三个属性
    action_name = "my_action"  #相当于这个Action的唯一标识，尽量用比较有针对性的名字
    description = (u'Test selected %(verbose_name_plural)s') #描述，出现在Action菜单中，
                            # 可以使用‘%(verbose_name_plural)s’代替Model的名字
    model_perm = 'change'  #该Action所需权限，‘change’为修改更新权限

    #而后实现do_action方法
    def do_action(self, queryset):
        #queryset是包含了已经选择的数据的queryset
        for obj in queryset:
            #obj的操作
            pass
        # return HttpResponse(...)  #返回一个http响应，也可以没有



class SpiderDataAdmin(object):
    # def preview(self,obj):
    #     from django.utils.safestring import mark_safe  # 调用mark_safe这个函数，django可以显示成一个文本，而不是html代码
    #     return mark_safe("<a href='{}'>大图</a>".format(obj.front_cover_img.url))
    # # preview.allow_tags = True
    # preview.short_description = u"大图"


    ziduan = ['id','front_cover_img','video',
              'down_load',


              'add_time','update_time']

    list_display =['id','back_image_data',
                   'is_love','is_check',
                   'down_load_link',
                   # 'preview',
                   'add_time','update_time']#定义显示的字段
    search_fields =  ['splider_title','prenum',]   #定义搜索字段
    list_filter =  ['splider_title','is_love','is_check','prenum',] #定义筛选的字段
    model_icon = 'fa fa-bars '  # 定义图标显示
    ordering = ['-add_time']  # 添加默认排序规则显示排序，根据添加时间倒序排序
    # readonly_fields = ziduan  # 设置某些字段为只为可读  #设置了readonly_fields，再设置exclude，exclude对该字段无效，
    # exclude = ['case_step']  # 设置某些字段为不显示，即隐藏  #readonly_fields和exclude设置会有冲突
    # inlines = [TestCaseInline]  # inlines配和TestCaseInline使用，可以直接在项目页面添加测试用例#只能做一层嵌套，不能进行两层嵌套
    list_editable = ['is_love','is_check',]  # 可以在列表页对字段进行编辑
    refresh_times = [3, 5]  # 对列表页进行定时刷新,配置了3秒和5秒，可以从中选择一个
    list_per_page = 10   #每页设置50条数据，默认每页展示100条数据
    # fk_fields = ['test_project_id',]  #设置显示外键字段，未生效
    list_display_links = []   #设置点击链接进入编辑页面的字段
    # date_hierarchy = 'add_time'   #详细时间分层筛选，未生效
    # show_detail_fields = []   #显示数据详情
    # data_charts = {   #使用网址：https://xadmin.readthedocs.io/en/latest/_modules/xadmin/plugins/chart.html
    #                   # 插件介绍网址：http://www.mamicode.com/info-detail-2403646.html
    #                   #使用网址：https://www.jianshu.com/p/6201e1e9133c
    #     "user_count": {'title': u"页面加载时间", "x-field": "forcount", "y-field": ( 'page_load_time_no_catch', 'dom_load_time_no_catch',),
    #                    "order": ('id',)},
    # }

    #设置内联
    class SpiderVideoInline(object):
        model = SpiderVideo
        exclude = ["add_time","update_time","write_user"]
        extra = 1
        style = 'tab'    #以标签形式展示

    #设置内联
    class SpiderDownLoadInline(object):
        model = SpiderDownLoad
        exclude = ["add_time","update_time","write_user"]
        extra = 1
        style = 'tab'    #以标签形式展示

    inlines = [SpiderVideoInline,SpiderDownLoadInline ]



    def queryset(self):   #重载queryset方法，用来做到不同的admin取出的数据不同
        qs = super(SpiderDataAdmin, self).queryset()   #调用父类
        if self.request.user.is_superuser:   #超级用户可查看所有数据
            return qs
        else:
            qs = qs.filter(write_user=self.request.user)  #否则只显示本用户数据
            return qs   #返回qs



class SpiderHMBookAdmin(object):
    # def preview(self,obj):
    #     from django.utils.safestring import mark_safe  # 调用mark_safe这个函数，django可以显示成一个文本，而不是html代码
    #     return mark_safe("<a href='{}'>大图</a>".format(obj.front_cover_img.url))
    # # preview.allow_tags = True
    # preview.short_description = u"大图"


    ziduan = ['id','front_cover_img',


              'add_time','update_time']

    list_display =['id','front_cover_img_data',
                   'all_chapter',
                   'is_love','is_check',
                   # 'preview',
                   'add_time','update_time']#定义显示的字段
    search_fields =  ['splider_title',]   #定义搜索字段
    # list_filter =  ['splider_title','is_love','is_check','prenum',] #定义筛选的字段
    model_icon = 'fa fa-bars '  # 定义图标显示
    ordering = ['-add_time']  # 添加默认排序规则显示排序，根据添加时间倒序排序
    # readonly_fields = ziduan  # 设置某些字段为只为可读  #设置了readonly_fields，再设置exclude，exclude对该字段无效，
    # exclude = ['case_step']  # 设置某些字段为不显示，即隐藏  #readonly_fields和exclude设置会有冲突
    # inlines = [TestCaseInline]  # inlines配和TestCaseInline使用，可以直接在项目页面添加测试用例#只能做一层嵌套，不能进行两层嵌套
    list_editable = ['is_love','is_check',]  # 可以在列表页对字段进行编辑
    refresh_times = [3, 5]  # 对列表页进行定时刷新,配置了3秒和5秒，可以从中选择一个
    list_per_page = 10   #每页设置50条数据，默认每页展示100条数据
    # fk_fields = ['test_project_id',]  #设置显示外键字段，未生效
    list_display_links = []   #设置点击链接进入编辑页面的字段
    # date_hierarchy = 'add_time'   #详细时间分层筛选，未生效
    show_detail_fields = ['id']   #显示数据详情
    show_all_rel_details = True   #关联字段是否在详情页显示
    # data_charts = {   #使用网址：https://xadmin.readthedocs.io/en/latest/_modules/xadmin/plugins/chart.html
    #                   # 插件介绍网址：http://www.mamicode.com/info-detail-2403646.html
    #                   #使用网址：https://www.jianshu.com/p/6201e1e9133c
    #     "user_count": {'title': u"页面加载时间", "x-field": "forcount", "y-field": ( 'page_load_time_no_catch', 'dom_load_time_no_catch',),
    #                    "order": ('id',)},
    # }

    # #设置内联
    # class SpiderVideoInline(object):
    #     model = SpiderVideo
    #     exclude = ["add_time","update_time","write_user"]
    #     extra = 1
    #     style = 'tab'    #以标签形式展示
    #
    # #设置内联
    # class SpiderDownLoadInline(object):
    #     model = SpiderDownLoad
    #     exclude = ["add_time","update_time","write_user"]
    #     extra = 1
    #     style = 'tab'    #以标签形式展示
    #
    # inlines = [SpiderVideoInline,SpiderDownLoadInline ]

    #批量删除
    def patch_delete(self,request,querset):
        for qs_one in querset:
            #批量删除
            #删除所有章节
            from .modelshm import SpiderHMChapterData,SpiderHMChapterImage
            scd_list = SpiderHMChapterData.objects.filter(spiderhmbook_id=qs_one.id)
            scd_list_len = len(scd_list)
            if scd_list_len>0:
                for scd_one in scd_list:
                    sci_list = SpiderHMChapterImage.objects.filter(spiderhmchapterdata_id=scd_one.id)
                    sci_list_len = len(sci_list)
                    if sci_list_len > 0:
                        sci_list.delete()  #批量删除
                sci_list.delete()  #批量删除

        querset.delete()  #批量删除

    patch_delete.short_description = "批量删除"


    actions = [patch_delete,]

    def queryset(self):   #重载queryset方法，用来做到不同的admin取出的数据不同
        qs = super(SpiderHMBookAdmin, self).queryset()   #调用父类
        if self.request.user.is_superuser:   #超级用户可查看所有数据
            return qs
        else:
            qs = qs.filter(write_user=self.request.user)  #否则只显示本用户数据
            return qs   #返回qs

class SpiderWebUrlAdmin(object):
    # def preview(self,obj):
    #     from django.utils.safestring import mark_safe  # 调用mark_safe这个函数，django可以显示成一个文本，而不是html代码
    #     return mark_safe("<a href='{}'>大图</a>".format(obj.front_cover_img.url))
    # # preview.allow_tags = True
    # preview.short_description = u"大图"


    ziduan = ['id','web_url','url_title'

              'add_time','update_time']

    list_display =['id',
                   'is_check',
                   'html_web_url',
                   'modify_web_url',
                   'modify_url_title',
                   'is_spider',

                   'url_title',
                   'add_time','update_time']#定义显示的字段
    free_query_filter = False  #无论是否允许自由搜索，该值默认为True,
                              #如果能够进行自由搜索，用户可以通过传输带参数的url执行自定义的搜索
                              #比如：http://192.168.1.103:8000/spiderdata/spiderweburl/?_p_url_title__contains=%E8%B1%86%E8%94%BB
    search_fields = ['web_url','url_title','modify_web_url','modify_url_title']   #定义搜索字段
    list_filter = ['is_check','web_url','url_title','modify_web_url','modify_url_title']  #定义筛选的字段

    model_icon = 'fa fa-bars '  # 定义图标显示
    ordering = ['-add_time']  # 添加默认排序规则显示排序，根据添加时间倒序排序
    # readonly_fields = ziduan  # 设置某些字段为只为可读  #设置了readonly_fields，再设置exclude，exclude对该字段无效，
    # exclude = ['case_step']  # 设置某些字段为不显示，即隐藏  #readonly_fields和exclude设置会有冲突
    # inlines = [TestCaseInline]  # inlines配和TestCaseInline使用，可以直接在项目页面添加测试用例#只能做一层嵌套，不能进行两层嵌套
    list_editable = ['is_check','modify_web_url','modify_url_title','is_spider']  # 可以在列表页对字段进行编辑
    refresh_times = [3, 5]  # 对列表页进行定时刷新,配置了3秒和5秒，可以从中选择一个
    list_per_page = 10   #每页设置50条数据，默认每页展示100条数据
    # fk_fields = ['test_project_id',]  #设置显示外键字段，未生效
    list_display_links = ['id']   #设置点击链接进入编辑页面的字段
    # date_hierarchy = 'add_time'   #详细时间分层筛选，未生效
    # show_detail_fields = []   #显示数据详情
    # data_charts = {   #使用网址：https://xadmin.readthedocs.io/en/latest/_modules/xadmin/plugins/chart.html
    #                   # 插件介绍网址：http://www.mamicode.com/info-detail-2403646.html
    #                   #使用网址：https://www.jianshu.com/p/6201e1e9133c
    #     "user_count": {'title': u"页面加载时间", "x-field": "forcount", "y-field": ( 'page_load_time_no_catch', 'dom_load_time_no_catch',),
    #                    "order": ('id',)},
    # }

    show_bookmarks = True   #设置启用或停用书签
    #书签
    list_bookmarks = [
        {
            'title':'Female', #书签的名称
            'query':{'is_check':False,},  #过滤参数，是标准的queryset过滤
            # 'order':('-add_time'), #排序参数，
            # 'cols':('url_title'),   #显示的列
            # 'search':'Tom' #搜素的参数，指定搜索的内容
        },
    ]

    # #设置内联
    # class SpiderVideoInline(object):
    #     model = SpiderVideo
    #     exclude = ["add_time","update_time","write_user"]
    #     extra = 1
    #     style = 'tab'    #以标签形式展示
    #
    # #设置内联
    # class SpiderDownLoadInline(object):
    #     model = SpiderDownLoad
    #     exclude = ["add_time","update_time","write_user"]
    #     extra = 1
    #     style = 'tab'    #以标签形式展示
    #
    # inlines = [SpiderVideoInline,SpiderDownLoadInline ]
    #批量处理命令
    #批量复制
    # def patch_copy(self,request,querset):  #此处的querset为选中的数据
    #     querset = querset.order_by('id')  #按照id顺序排序
    #     for qs_one in querset:
    #         #新建实体并复制选中的内容
    #         new_tagcontent = TagContent()
    #         new_tagcontent.config_project = qs_one.config_project
    #         new_tagcontent.tag_name = qs_one.tag_name
    #         new_tagcontent.is_root = qs_one.is_root
    #         new_tagcontent.tag_level = qs_one.tag_level
    #         new_tagcontent.tag_text = qs_one.tag_text
    #         new_tagcontent.tag_father = qs_one.tag_father
    #         if self.request.user.is_superuser:  # 超级用户则不保存user
    #             pass
    #         else: #否则保存user为当前用户
    #             new_tagcontent.write_user = self.request.user
    #         new_tagcontent.save()      #保存数据
    #         #获取刚保存的数据的id
    #         newadd = TagContent.objects.filter(config_project = qs_one.config_project).order_by('-add_time')
    #         for new_last in newadd:
    #             newaddid = new_last.id
    #             break
    #
    #         #获取TagAttrib中相应的内容
    #         old_tagattrib_all =TagAttrib.objects.filter(tagcontent_id=qs_one.id).order_by('add_time')
    #         for old_tagattrib_one in old_tagattrib_all:
    #             new_tagattrib = TagAttrib()
    #             new_tagattrib.tagcontent_id = newaddid
    #             new_tagattrib.tag_value_name = old_tagattrib_one.tag_value_name
    #             new_tagattrib.tag_value_text = old_tagattrib_one.tag_value_text
    #             if self.request.user.is_superuser:  # 超级用户则不保存user
    #                 pass
    #             else:  # 否则保存user为当前用户
    #                 new_tagattrib.write_user = self.request.user
    #             new_tagattrib.save()   #保存数据库


    # #批量删除
    # def patch_delete(self,request,querset):
    #     for qs_one in querset:
    #         #删除
    #         qs_one.delete()

    #批量更改为已看
    def patch_update_is_check (self,request,querset):
        for qs_one in querset:
            #更改为已看
            qs_one.is_check = True
            qs_one.save()

    # #批量设置用户名
    # def patch_set_user(self,request,querset):
    #     for qs_one in querset:
    #         #先设置关联用户名
    #         old_sjyzs = ShuJuYinZi.objects.filter(shangbaoshuju_id=qs_one.id)
    #         for old_tagattrib_one in old_sjyzs:
    #             old_tagattrib_one.w
    #         #再删除本体
    #         qs_one.delete()


    # patch_copy.short_description = "批量复制"
    # patch_delete.short_description = "批量删除"
    patch_update_is_check.short_description = "批量更改为已看"

    actions=[patch_update_is_check]


    def queryset(self):   #重载queryset方法，用来做到不同的admin取出的数据不同
        qs = super(SpiderWebUrlAdmin, self).queryset()   #调用父类
        if self.request.user.is_superuser:   #超级用户可查看所有数据
            qs = qs.filter(is_spider=False)
            qs = qs.filter(is_check=False)
            return qs
        else:
            qs = qs.filter(write_user=self.request.user)  #否则只显示本用户数据
            qs = qs.filter(is_spider=False)
            qs = qs.filter(is_check=False)
            return qs   #返回qs

class CopySpiderWebUrlAdmin(object):
    # def preview(self,obj):
    #     from django.utils.safestring import mark_safe  # 调用mark_safe这个函数，django可以显示成一个文本，而不是html代码
    #     return mark_safe("<a href='{}'>大图</a>".format(obj.front_cover_img.url))
    # # preview.allow_tags = True
    # preview.short_description = u"大图"


    ziduan = ['id','web_url','url_title'

              'add_time','update_time']

    list_display =['id','html_web_url',
                   'modify_web_url',
                   'modify_url_title',
                   'is_spider',
                   'url_title',
                   'add_time','update_time']#定义显示的字段
    search_fields =  ['web_url','url_title','modify_web_url','modify_url_title']   #定义搜索字段
    # list_filter =  ['splider_title','is_love','is_check','prenum',] #定义筛选的字段
    model_icon = 'fa fa-bars '  # 定义图标显示
    ordering = ['-add_time']  # 添加默认排序规则显示排序，根据添加时间倒序排序
    # readonly_fields = ziduan  # 设置某些字段为只为可读  #设置了readonly_fields，再设置exclude，exclude对该字段无效，
    # exclude = ['case_step']  # 设置某些字段为不显示，即隐藏  #readonly_fields和exclude设置会有冲突
    # inlines = [TestCaseInline]  # inlines配和TestCaseInline使用，可以直接在项目页面添加测试用例#只能做一层嵌套，不能进行两层嵌套
    list_editable = ['modify_web_url','modify_url_title','is_spider']  # 可以在列表页对字段进行编辑
    refresh_times = [3, 5]  # 对列表页进行定时刷新,配置了3秒和5秒，可以从中选择一个
    list_per_page = 10   #每页设置50条数据，默认每页展示100条数据
    # fk_fields = ['test_project_id',]  #设置显示外键字段，未生效
    list_display_links = ['id']   #设置点击链接进入编辑页面的字段
    # date_hierarchy = 'add_time'   #详细时间分层筛选，未生效
    # show_detail_fields = []   #显示数据详情
    # data_charts = {   #使用网址：https://xadmin.readthedocs.io/en/latest/_modules/xadmin/plugins/chart.html
    #                   # 插件介绍网址：http://www.mamicode.com/info-detail-2403646.html
    #                   #使用网址：https://www.jianshu.com/p/6201e1e9133c
    #     "user_count": {'title': u"页面加载时间", "x-field": "forcount", "y-field": ( 'page_load_time_no_catch', 'dom_load_time_no_catch',),
    #                    "order": ('id',)},
    # }

    # #设置内联
    # class SpiderVideoInline(object):
    #     model = SpiderVideo
    #     exclude = ["add_time","update_time","write_user"]
    #     extra = 1
    #     style = 'tab'    #以标签形式展示
    #
    # #设置内联
    # class SpiderDownLoadInline(object):
    #     model = SpiderDownLoad
    #     exclude = ["add_time","update_time","write_user"]
    #     extra = 1
    #     style = 'tab'    #以标签形式展示
    #
    # inlines = [SpiderVideoInline,SpiderDownLoadInline ]


    def queryset(self):   #重载queryset方法，用来做到不同的admin取出的数据不同
        qs = super(CopySpiderWebUrlAdmin, self).queryset()   #调用父类
        if self.request.user.is_superuser:   #超级用户可查看所有数据
            qs = qs.filter(is_spider=True)
            return qs
        else:
            qs = qs.filter(write_user=self.request.user)  #否则只显示本用户数据
            qs = qs.filter(is_spider=True)
            return qs   #返回qs

xadmin.site.register(SpiderData, SpiderDataAdmin) #在xadmin中注册SpiderDate
xadmin.site.register(SpiderHMBook, SpiderHMBookAdmin) #在xadmin中注册SpiderHMBook
xadmin.site.register(SpiderWebUrl, SpiderWebUrlAdmin) #在xadmin中注册SpiderWebUrl
xadmin.site.register(CopySpiderWebUrl, CopySpiderWebUrlAdmin) #在xadmin中注册CopySpiderWebUrl