from rest_framework import serializers

from my_app.models import Person, Species, ElectionRetroData, CandidateData

class PersonSerializer(serializers.ModelSerializer):
   class Meta:
       model = Person
       fields = ('name', 'birth_year', 'eye_color', 'species')


class SpeciesSerializer(serializers.ModelSerializer):
   class Meta:
       model = Species
       fields = ('name', 'classification', 'language')

class ElectionRetroDataSerializer(serializers.ModelSerializer):
   class Meta:
       model = ElectionRetroData
       fields = ('year','election_type', 'acNum', 'accName','rank','partyName','partyID','alliance','candidateName','votesPolled','totalValidVotes')

class CandidateDataSerializer(serializers.ModelSerializer):
   class Meta:
       model = CandidateData
       fields = ('candidateName', 'candidateID', 'candidateCategory')
