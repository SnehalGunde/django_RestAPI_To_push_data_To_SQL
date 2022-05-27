from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from my_app.serializers import PersonSerializer, SpeciesSerializer, ElectionRetroDataSerializer,CandidateDataSerializer
from my_app.models import Person, Species , CandidateData, ElectionRetroData

import requests
from django.http import JsonResponse

import datetime as dt
import pandas as pd
import os
from django.conf import settings
from django.core.files.storage import FileSystemStorage
#import requests

class PersonViewSet(viewsets.ModelViewSet):
   queryset = Person.objects.all()
   serializer_class = PersonSerializer


class SpeciesViewSet(viewsets.ModelViewSet):
   queryset = Species.objects.all()
   serializer_class = SpeciesSerializer


#class ImportViewURL(viewsets.ModelViewSet):



class ElectionRetroDataViewSet(viewsets.ModelViewSet):
   queryset = ElectionRetroData.objects.all()
   serializer_class = ElectionRetroDataSerializer

class CandidateDataViewSet(viewsets.ModelViewSet):
   queryset = CandidateData.objects.all()
   serializer_class = CandidateDataSerializer

   
        
base_url='https://docs.google.com/spreadsheets/d/1PJDXeDsIACIHBsJOT_FQ3Cl-CgOQoGzKTEsIBSysEik/edit#gid=249491301'
def get_data(request):
    response = requests.get(base_url)
    #"200" response indicates that the request has succeeded.
    if str(response) =="<Response [200]>":
        res_type=response.headers.get('content-type')
        if res_type=='text/html; charset=utf-8':
            data = response.content.decode()
            changed_data=  pd.read_html(data)
            print(type(changed_data))
            # print total number of tables in url
            print(f'Total tables: {len(changed_data)}')
            headers = changed_data[0].iloc[0]
            complete_df = pd.DataFrame(changed_data[0].values[1:], columns=headers)
            print(complete_df)

            CandidateData_Columns=['Candidate Name', 'Candidate ID','Candidate Category']
            CandidateData_df=pd.DataFrame(complete_df[CandidateData_Columns])
            CandidateData_df=CandidateData_df.fillna(0)
            print("*********************")
            print(CandidateData_df)
            CandidateData_df.to_csv('Candidate.csv')
            #CandidateData_df.to_sql('CandidateData',if_exists='append',index=False,con=engine)
            # for i, CandidateData_df in CandidateData_df.itertuples():
            #     print("*********************______________________")
            #     print(CandidateData_df)
            #     obj = CandidateData.objects.create(CandidateName=CandidateData_df.CandidateName, CandidateID=CandidateData_df.CandidateID, CandidateCategory=CandidateData_df.CandidateCategory)
            #     print(type(obj))
            #     obj.save()

            # #Open DB
            # engine = create_engine('sqlite:///db/immo.db', echo=True)
            # sqlite_connection = engine.connect()
            # # Set table name -> mytable
            # mytable = "my_app_candidatedata"
            # #Open df  
            # df = pd.read_csv(CandidateData_df)
            # # Write df to SQLite db
            # df.to_sql(mytable, sqlite_connection, if_exists='fail')

            ElectionRetroData_Columns=['Year','Election Type','AC No','AC Name','Rank','Party Name','Party ID','Alliance','Candidate Name','% votes polled','Total Valid Votes']
            ElectionRetroData_df=pd.DataFrame(complete_df[ElectionRetroData_Columns])
            print("*********************")
            print(ElectionRetroData_df)
            ElectionRetroData_df=ElectionRetroData_df.fillna(0)
            print("*********************")
            print(ElectionRetroData_df)
            ElectionRetroData_df.to_csv('ElectionRetroData_df.csv')

        
 

        # extract data from table and store in SQL db
        # for i in range(0,len(changed_data)):
        #     print("***************************Table :"+ str(i) +" **************************")
        #     num=i
        #     string_data = "df_"+ str(i)
        #     print(string_data)
        #     headers = changed_data[i].iloc[0]
        #     string_data = pd.DataFrame(changed_data[i].values[1:], columns=headers)
        #     for string_data in string_data.itertuples():
        #         obj = CandidateData.objects.create(CandidateName=string_data.candidateName,candidateID=string_data.candidateID,candidateCategory=string_data.candidateCategory)
        #         print(type(obj))
        #         obj.save()
            #establish sql and add tables to the sql
    
    #If response indicates is other than success
    else:
        print("Failed while getting response , " + str(response))

    return JsonResponse({'message': 'Suceesfully added to database'})     

        

 