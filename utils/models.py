from django.db import models
from django.apps import apps

class BaseModel(models.Model):
    created=models.DateTimeField(auto_now_add=True)
    modified=models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True

class MakeQueryset:
    
    def __init__(self, model_name,app_name=None):
        self._queryset=self.get_queryset(model_name, model_name)
        
    
    @property
    def queryset(self):
        return self._queryset

    
    # @queryset.setter
    # def queryset(self, model_name):
    #     self._queryset=self.get_queryset(model_name, model_name)
        # self._queryset=model_name
         
    # @queryset.setter
    # def queryset(self, model_name,app_name=None):
    #     if not self._queryset:
    #         print('creating new query', model_name)
    #         model_name=model_name.lower()
    #         if app_name is None or len(app_name)==0:
    #             model_base=apps.get_model(model_name, model_name)
    #         else:
    #             model_base=apps.get_model(app_name,model_name)
    #         self._queryset=model_base.objects.all()
    #     else:
    #         print('query already exist',self._queryset )
    #         self._queryset=self.queryset
            
            
            
        
        
    def get_queryset(self, model_name,app_name=None):
        
        # if self._queryset is not None:
        #     print('object already exist')
        #     return self._queryset
        print("making new object")
        # if the app_name is same name as the model_name or app_name is not inputed    
        # model_name=model_name.lower()
        if app_name is None or len(app_name)==0:
            model_base=apps.get_model(model_name, model_name)
        else:
            model_base=apps.get_model(app_name,model_name)
        return model_base.objects.all()
    
   