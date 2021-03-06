from django.urls import path, include 
from competence import views
from competence import views_bundles

app_name="competence"
urlpatterns = [
    # path('', views.CompetenceList.as_view(), name="competence"),
    path('', views.competenceList, name="competence"),
    path('test/', views.testcomp, name="test"),
    path('create/', views.competenceCreate, name="create"),
    path('<int:pk>/', include([
        path('', views.competenceUpdate, name='update'),
        path('delete/', views.deleteCompetence, name="delete"),
    ])),
    
    # COMPETENCE BUNDLES--
    path('bundles/',include([
        path('', views_bundles.bundle_list, name='bundles'),
        path('create/', views_bundles.bundle_create, name='bundle-create'), # create a new bundle
        path('<int:pk>/delete/', views_bundles.bundle_delete, name='bundle-delete'),
        path('<int:pk>/update/', views_bundles.bundle_update, name='bundle-update'),
        path('<int:pk>/retrieve/', views_bundles.bundle_retrieve, name='bundle-retrieve'),
        
        path('<int:pk>/add/', views_bundles.bundle_competences_add, name='bundle-competences-add'),
        path('competence/<int:competenceid>/delete/', views_bundles.bundle_competence_remove, name='bundle-competence-remove'),
        # path('<int:bundleid>/competence/<int:competeceid>/', views_bundles.bundle_competence_remove, name='bundle-competence-remove'),
        
        # path('<int:pk>/', views_bundles.bundle_competences, name='bundle-competences'),
           
    ])),
    
]


#HTMX
urlpatterns+=[
    path('list/', views.competenceList, name="list"),
]