from django.db import models
from datetime import datetime
from wanwenyc.settings import DJANGO_SERVER_YUMING
from django.contrib.auth import  get_user_model  #导入get_user_model
from testupdatadb.models import UpdateDbData

#第三个就是我们自己创建的包
User = get_user_model()  #get_user_model() 函数直接返回User类，找的是settings.AUTH_USER_MODEL变量的值


#url
class SpiderWebUrl(models.Model):
    web_url = models.CharField(max_length=1500, default="", null=True, blank=True, verbose_name=u"web网址")
    url_title = models.CharField(max_length=1500, default="", null=True, blank=True,verbose_name=u"网站标题")
    modify_web_url = models.CharField(max_length=1500, default="", null=True, blank=True, verbose_name=u"修改后web网址")
    modify_url_title = models.CharField(max_length=1500, default="", null=True, blank=True, verbose_name=u"修改后网站标题")
    is_spider = models.BooleanField(default=False, verbose_name=u"是否可以爬取"
                                                                u"获得新网址")
    is_check = models.BooleanField(default=False, verbose_name=u"是否已看")
    is_already_spider = models.BooleanField(default=False, verbose_name=u"是否已爬取")
    write_user = models.ForeignKey(User, null=True, blank=True, verbose_name=u"用户名", on_delete=models.PROTECT)
    add_time = models.DateTimeField(null=True, blank=True,auto_now_add=True,
                                    verbose_name=u"添加时间")  # datetime.now记录实例化时间，datetime.now()记录模型创建时间,auto_now_add=True是指定在数据新增时, 自动写入时间
    update_time = models.DateTimeField(default=datetime.now, null=True, blank=True,
                                    verbose_name=u"更新时间")  # datetime.now记录实例化时间，datetime.now()记录模型创建时间，auto_now=True是无论新增还是更新数据, 此字段都会更新为当前时间

    class Meta:
        verbose_name = u"网址收录"
        verbose_name_plural=verbose_name

    def __str__(self):
        return str(self.id)

    def html_web_url(self):   #定义点击后跳转到某一个地方（可以加html代码）
        from django.utils.safestring import mark_safe   #调用mark_safe这个函数，django可以显示成一个文本，而不是html代码
        html_all = ""
        web_url_html = "<a href='{}'>原网址：{}</a><br/>".format(self.web_url,self.web_url)
        url_title_html = "<a href='{}'>原标题：{}</a><br/>".format(self.url_title,self.url_title)
        modify_web_url_html = "<a href='{}'>修改后网址：{}</a><br/>".format(self.modify_web_url,self.modify_web_url)
        modify_url_title_html = "<a href='{}'>修改后标题：{}</a><br/>".format(self.modify_url_title,self.modify_url_title)

        html_all = html_all+web_url_html+modify_web_url_html
        return mark_safe(html_all)

    html_web_url.short_description = u"web网址"   #为go_to函数名个名字


class CopySpiderWebUrl(SpiderWebUrl):
    class Meta:
        verbose_name = u"网址收录之可以爬取新网址"
        verbose_name_plural = verbose_name
        proxy = True  #将proxy设置为True,不会再生成一张表，如果不设置为True,就会再生成一张表

                        #将proxy设置为True,不会再生成一张表，同时具有model的属性
    def __str__(self):
        return str(self.id)

    # def html_web_url(self):   #定义点击后跳转到某一个地方（可以加html代码）
    #     from django.utils.safestring import mark_safe   #调用mark_safe这个函数，django可以显示成一个文本，而不是html代码
    #     html_all = ""
    #     web_url_html = "<a href='{}'>原网址：{}</a><br/>".format(self.web_url,self.web_url)
    #     url_title_html = "<a href='{}'>原标题：{}</a><br/>".format(self.url_title,self.url_title)
    #     modify_web_url_html = "<a href='{}'>修改后网址：{}</a><br/>".format(self.modify_web_url,self.modify_web_url)
    #     modify_url_title_html = "<a href='{}'>修改后标题：{}</a><br/>".format(self.modify_url_title,self.modify_url_title)
    #
    #     html_all = html_all+web_url_html+modify_web_url_html
    #     return mark_safe(html_all)
    #
    # html_web_url.short_description = u"web网址"   #为go_to函数名个名字