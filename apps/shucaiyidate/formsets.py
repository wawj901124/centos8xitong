from django.forms import formset_factory,modelformset_factory,inlineformset_factory  #导入 formset
from .forms import NodeConfigForm  #导入form
from .forms import ConfigCollectSendCmdForm
from .modelsnewdev import NodeConfig,ConfigCollectSendCmd,ConfigCollectFactor

# Create your views here.

NodeConfigFormSet = modelformset_factory(NodeConfig,NodeConfigForm,extra=3,max_num=2)  #定义formset
ConfigCollectSendCmdFormSet = inlineformset_factory(NodeConfig,ConfigCollectSendCmd,
                                                    ConfigCollectSendCmdForm,extra=3,
                                                    can_delete=False,max_num=5)