# ----------------------------------------------------------------------
import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "wanwenyc.settings")
django.setup()
# ----------------------------------------------------------------------
#独运行某一个py文件时会出现如下错误：django.core.exceptions.AppRegistryNotReady: Apps aren't loaded yet.，以上内容可以解决此问题,加载django中的App
from spiderdata.modelshm import SpiderHMChapterImage,SpiderHMChapterData
spiderhmchapterdata = SpiderHMChapterData.objects.exclude(id)