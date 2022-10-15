from django.http import HttpResponse
from django.shortcuts import render, reverse
from django.urls import reverse_lazy 
from django.views import generic
from competence.models import Competence, Bundle

from utils.build import EndPoints
# Create your views here.

 
def getContext(obj_list=None, target="#obj_list",dtarget="#obj_list"):
    context={
        'object_list':obj_list,
        'name':'competence',
        'target':target,
        'delete_target':dtarget,
        'create':'competence:bundle-create',
        'retrieve':'quality:list',
        'update':'competence:update',
        'delete':'competence:delete',
    }
    
    return context     

def competenceCreate(request):
    if request.method=="POST":
        name=request.POST.get('form_name')
        competence=Competence.objects.create(name=name)
        return competenceList(request)
    

def testcomp(request):
    return render(request, 'test.html',{})
 


def competenceUpdate(request,pk=None):
    competence=Competence.objects.get(pk=pk)
    context=getContext(target="#child_list")
    context['obj2']=competence
    if request.method=="POST":
        competence.name=request.POST.get('obj_name')
        competence.save()
        return render(request, 'comp_qty/item.html', context)    
    return render(request, 'comp_qty/update.html', context)
    
def deleteCompetence(request, pk):
    competence=Competence.objects.get(pk=pk)
    competence.delete()
    return competenceList(request)
    
def competenceList(request, target="#child_list", dtarget="#obj_list" ):
    # context={
    #     'object_list':obj_list,
    #     'name':'competence',
    #     'target':target,
    #     'delete_target':dtarget,
    #     'create':'competence:bundle-create',
    #     'retrieve':'quality:list',
    #     'update':'competence:update',
    #     'delete':'competence:delete',
    # }
    endpoints=EndPoints("competence",defaults=True)
    endpoints.new_path('target',target)
    endpoints.new_path('create','competence:bundle-create') 
    endpoints.new_path('delete_target',dtarget)
    endpoints.new_path('retrieve','quality:list')
    context=endpoints.context
    print('CONTEXT \n ',context)
    if request.htmx:
        return render(request, 'comp_qty/list.html', context)
    return  render(request, 'comp_qty/home.html', context)
 

# def get_endpoints(request):
#     makequery=MakeQueryset("competence")
#     competences=makequery.queryset
#     return EndPoints(model_name=competences, request=request)
    
 

