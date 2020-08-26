from django.shortcuts import render, get_object_or_404,redirect

from .modelsnewdev import NodeConfig,ConfigCollectSendCmd,ConfigCollectFactor
from .formsets import NodeConfigFormSet,ConfigCollectSendCmdFormSet
from .forms import NodeConfigForm


def manage_nodeconfig(request):
    if request.method == "POST":
        nodeconfigformset = NodeConfigFormSet(request.POST,request.FILES)
        if nodeconfigformset.is_valid():
            nodeconfigformset.save()  #modelformset_factory有save功能，formset_factory没有save功能
            nodeconfigformset.cleaned_data  #清空数据
            pass
    else:
        nodeconfigformset = NodeConfigFormSet()
    return render(request,'manage_nodeconfigtwotemple.html',{
        'nodeconfigformset':nodeconfigformset,
    })

def nodeconfig_update(request,pk):
    nodeconfig = get_object_or_404(NodeConfig,pk=pk)
    if request.method == "POST":
        nodeconfigform = NodeConfigForm(request.POST,instance=nodeconfig)
        if nodeconfigform.is_valid():
            nodeconfig = nodeconfigform.save()
            configcollectsendcmd_formset = ConfigCollectSendCmdFormSet(request.POST,instance=nodeconfig)
        # nodeconfigformset = NodeConfigFormSet(request.POST,request.FILES)
            if configcollectsendcmd_formset.is_valid():
                configcollectsendcmd_formset.save()  #modelformset_factory有save功能，formset_factory没有save功能
        return redirect('/nodeconfig/')
    else:
        nodeconfigform = NodeConfigForm(instance=nodeconfig)
        configcollectsendcmd_formset = ConfigCollectSendCmdFormSet(instance=nodeconfig)
    return render(request,'nodeconfig/nodeconfig_update.html',{
        'nodeconfigform':nodeconfigform,
        'configcollectsendcmd_formset':configcollectsendcmd_formset,
    })

def nodeconfig_add(request):
    if request.method == "POST":
        nodeconfigform = NodeConfigForm(request.POST)
        if nodeconfigform.is_valid():
            nodeconfig = nodeconfigform.save()
            configcollectsendcmd_formset = ConfigCollectSendCmdFormSet(request.POST,instance=nodeconfig)
        # nodeconfigformset = NodeConfigFormSet(request.POST,request.FILES)
            if configcollectsendcmd_formset.is_valid():
                configcollectsendcmd_formset.save()  #modelformset_factory有save功能，formset_factory没有save功能
        return redirect('/shucaiyidate/nodeconfig/')
    else:
        nodeconfigform = NodeConfigForm()
        configcollectsendcmd_formset = ConfigCollectSendCmdFormSet()
    return render(request,'nodeconfig/nodeconfig_add_temple.html',{
        'nodeconfigform':nodeconfigform,
        'configcollectsendcmd_formset':configcollectsendcmd_formset,
    })





