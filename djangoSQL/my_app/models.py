from django.db import models


class Species(models.Model):
   name = models.CharField(max_length=100)
   classification = models.CharField(max_length=100)
   language = models.CharField(max_length=100)


class Person(models.Model):
   name = models.CharField(max_length=100)
   birth_year = models.CharField(max_length=10)
   eye_color = models.CharField(max_length=10)
   species = models.ForeignKey(Species, on_delete=models.DO_NOTHING)

class CandidateData(models.Model):
    candidateName = models.CharField(max_length=100)
    candidateID =models.CharField(max_length=100)	
    candidateCategory =models.CharField(max_length=100)

class ElectionRetroData(models.Model):
    year = models.CharField(max_length=100)
    election_type= models.CharField(max_length=100)
    acNum=models.CharField(max_length=100)
    accName =models.CharField(max_length=100)
    rank =models.CharField(max_length=100)
    partyName =models.CharField(max_length=100)
    partyID = models.CharField(max_length=100)
    alliance =models.CharField(max_length=100)
    candidateName = models.ForeignKey(CandidateData, on_delete=models.DO_NOTHING)
    votesPolled = models.CharField(max_length=100)
    totalValidVotes = models.CharField(max_length=100)

