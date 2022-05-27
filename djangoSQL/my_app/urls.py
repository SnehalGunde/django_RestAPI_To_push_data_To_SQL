from django.urls import include, path

from rest_framework import routers

from my_app.views import PersonViewSet, SpeciesViewSet, CandidateDataViewSet, ElectionRetroDataViewSet, get_data
from . import views 

router = routers.DefaultRouter()
router.register(r'people', PersonViewSet)
router.register(r'species', SpeciesViewSet)
router.register(r'electionData', ElectionRetroDataViewSet)
router.register(r'candidateData', CandidateDataViewSet)
# router.register(r'ImportURL', views.import_csv, name = Importcsv)


urlpatterns = [
   path('', include(router.urls)),
   path('get_data', views.get_data, name = 'get_data')

]