from django.contrib import admin

from .models import Person, Species, ElectionRetroData,CandidateData

# Register your models here.
admin.site.register(Person)
admin.site.register(Species)
admin.site.register(ElectionRetroData)
admin.site.register(CandidateData)