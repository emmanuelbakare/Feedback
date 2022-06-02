from django.db import models
from utils.models import BaseModel
from datetime import datetime
from accounts.models import Person

# Create your models here.

class Bundle(BaseModel):
    name=models.CharField(max_length=250)
    assessment=models.ManyToManyField(Person, through='Assessment')
  
    
    def __str__(self):
        return self.name
    
    def addCompetence(self, comp ):
        self.competences.add(comp)
        return self

class Competence(BaseModel):
    name=models.CharField(max_length=250)
    bundles=models.ManyToManyField(Bundle, related_name='competences')
   
    
    def __str__(self) -> str:
        return self.name


#this contain a group of bundles assigned to someone who is to be assessed.   
from datetime import datetime
class Assessment(BaseModel):
    assessed = models.ForeignKey(Person, on_delete=models.CASCADE, related_name="assessed")   
    assessor = models.IntegerField()   
    bundle  = models.ForeignKey(Bundle, on_delete=models.CASCADE) 
    start_date = models.DateTimeField(default=datetime.now())
    end_date = models.DateTimeField(default=datetime.now())
    published = models.BooleanField(default=True)
    
    