from django.http import HttpResponse
from django.shortcuts import render, reverse, redirect
from django.views import generic
from competence.models import Competence, Bundle
# Create your views here.

class CompetenceList(generic.ListView):
    template_name="comp_qty/home.html"
    model=Competence 
    
    def get_context_data(self,*args, **kwargs):
        context=super().get_context_data(*args, **kwargs)
        context['name']="competence"
        return context
        

def competenceCreate(request):
    if request.method=="POST":
        name=request.POST.get('obj_name')
        competence=Competence.objects.create(name=name)
        return competenceList(request)
    
def competenceList(request):
    competences=Competence.objects.all() 
    context={
        'object_list':competences,
        'name':'competence'
    }
    return render(request, 'comp_qty/list.html', context)


def contextList(request, context):
    return render(request, 'comp_qty/list.html', context)  
      
def testcomp(request):
    return render(request, 'test.html',{})
 


def competenceUpdate(request,pk=None):
    competence=Competence.objects.get(pk=pk)
    if request.method=="POST":
        competence.name=request.POST.get('obj_name')
        competence.save()
        context={'obj':competence,'name':'competence'}
        return render(request, 'comp_qty/item.html', context)    
    context={'obj':competence,'name':'competence'}
    return render(request, 'comp_qty/update.html', context)
    

def deleteCompetence(request, pk):
    competence=Competence.objects.get(pk=pk)
    competence.delete()
    return competenceList(request)
    


#GROUP CODES 

#HOME
def bundlesHome(request):
    context={'bundles':Bundle.objects.all()}
    return render(request, 'competence/bundle/home.html', context)


def bundle_create(request):
    text=request.POST.get('bundle_name')
    Bundle.objects.create(name=text)
    return bundle_list(request)
  

def bundle_list(request):
    context={
        'bundles':Bundle.objects.all()
    }
   
    return render(request,'competence/bundle/partials/list.html',context) 

def bundle_competence(request,pk):
    # bundle=Bundle.objects.get(pk=pk) 
    # competences=bundle.competences.all()
    competences=Bundle.objects.get(pk=pk).competences.all()
    context={'object_list':competences}
    return contextList(request, context)
    # return HttpResponse(context)
    
    