from django.apps import apps
from django.db.models import query
from utils.models import MakeModelOrQueryset

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
        ''' if model_ame is a string, use the string
        if a queryset was entered then get the name of the object in the queryset'''
        if isinstance(model_name, query.QuerySet):
            return model_name[0].__class__.__name__ 
        return model_name 
        
    def get_model(self, model_name, app_name=None):
        ''' Build a queryset from only the model name
         model name is entered as a string 'model_name' 

         use:
            get_model(model_name, app_name)
         
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
    

class EndPoint:
    '''generate a dictionary of endpoint (urls) and database queryset that will be attached to a template as context data'''
    def __init__(self, model_name, app_name=None, request=None, defaults=False, many=True):
        self.model_name=model_name
        self.query_or_obj = MakeModelOrQueryset(model_name,app_name).queryset
        if defaults:
            self.defaults()
    
    
    
    def new_path(self, key, value):
        ''' a method to set attributes on all endpoint instance 
        use:  action('age', 34) will set attributes age to 34 on an EndPoint instance'''
        if self.__dict__.get(key):
            self.__dict__[key] = value
        else:
            setattr(self,key,value)
        
        return self

    def defaults(self):
        ''' return sets of urls paths that is most likely  to be used to generate endpoints
        this include the create, retreive, update and delete urls '''
        print('...add default paths')
        self.__dict__['create']=f'{self.model_name}:create'
        self.__dict__['retrieve']=f'{self.model_name}:retrieve'
        self.__dict__['updated']=f'{self.model_name}:updated'
        self.__dict__['delete']=f'{self.model_name}:delete'


        return self


    @property
    def context(self):
        ''' return a dictionary of the endpoints generated from the instance dunder __dict__  method'''
        return self.__dict__.copy()
    

    

    def get_model(self, model_name, app_name=None, pk={}):
        ''' Build a queryset from only the model name
         model name is entered as a string 'model_name' 

         use:
            get_model(model_name, app_name)
         
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
        

        
           
        # return self._get_model_obj_or_queryset(model_base,pk)
        return model_base.objects.all()
    

    # def _get_model_obj_or_queryset(self, model, pk, many):
    #     ''' return a queryset from a model name and if is specified, return the model object
    #     if the model object is not found, '''

    #     if many:
    #         queryset =model.objects.all() 
    #         return queryset
    #     elif isinstance(pk, dict) and len(pk) > 0 :
    #         try:
    #             model_object=model.objects.get(pk=pk.get('pk'))
    #             return model_object 
    #         except model_object.DoesNotExistExist:
    #             return None



endpoint=EndPoint("competence", defaults=True)
# endpoint.defaults()
endpoint.new_path('gender','male')
context=endpoint.context
print('ENDPOINT: \n',context)

# print('NEW QUERY \n',MakeModelObjectOrQueryset("competence", pk=5).queryset )
      