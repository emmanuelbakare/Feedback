from competence.models import Competence, Bundle 
from django.http import JsonResponse 
from utils.build import EndPoints



    
def main():
    comps=Competence.objects.all()
    recs={'data':list(comps.values())}
    return JsonResponse(recs)

if __name__=="__main__":
    main()