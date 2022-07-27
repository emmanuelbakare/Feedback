from django.apps import apps
from django.db.models import query
from utils.models import MakeQueryset

class EndPoints:
    
    def __init__(self, model_name, request=None, pk=None):
        self.object_list=self.get_model(model_name)
        # if request: 
        #     self.url=request.build_absolute_uri
        self.url= request.build_absolute_uri if request is not None else ''
        self.__mname= EndPoints.getname(model_name)
        self.target=f'#child_list'
        self.delete_target=f"#obj_list"
        self.create=f'{self.name.lower()}:create'
        self.retrieve=f'{self.name.lower()}:list'
        self.update=f'{self.name.lower()}:update'
        self.delete=f'{self.name.lower()}:delete'
    
    
    @staticmethod
    def getname(model_name):
        ''' if string name is entered as string name the use the string
        if a queryset was entered then get the name of the object in the queryset'''
        if isinstance(model_name, query.QuerySet):
            return model_name[0].__class__.__name__ 
        return model_name 
        
    def get_model(self, model_name, app_name=None):
        ''' Build a queryset from only the model name
         model name is entered as a string 'model_name' 
         
         argument:
            model_name:str|queryset: a queryset instance or name of the model-system generates the QuerySet
            app_name: the app name  (created with manage.py startapp app_name)
        
         returns:
            queryset
            '''
        #if model_name is a queryset return it if not build the queryset from the model_name    
        if isinstance(model_name, query.QuerySet):
            return model_name
        
        # if the app_name is same name as the model_name or app_name is not inputed    
        model_name=model_name.lower()
        if app_name is None or len(app_name)==0:
            model_base=apps.get_model(model_name, model_name)
        else:
            model_base=apps.get_model(app_name,model_name)
        return model_base.objects.all()
            
          
    def get_context(self):
        return {
            'object_list':self.object_list,
            'url':self.url,
            'name':self.name,
            'target':self.target,
            'delete_target':self.delete_target,
            'create':self.create,
            'retrieve':self.retrieve,
            'update':self.update,
            'delete':self.delete,
        
        }
    
    @property
    def name(self):
        # return self.__mname.title()
        if isinstance(self.object_list, query.QuerySet):
            return self.object_list[0].__class__.__name__ 
        return self.__mname
    
    # @property
    # def model(self):
    #     return self._model
    
    # @model.setter
    # def model(self, value):
    #     if isinstance(value,object):
    #         setattr(self.)
        
        
# p=EndPoints(model_name="Competence")
# print(f"\n{'*'*5}{p.name} DATA {'*'*5}")
# print(p.get_context())     
   
# p2=EndPoints(model_name="Quality")
# print(f"\n{'*'*5}{p2.name} DATA {'*'*5}")
# print(p2.get_context())        