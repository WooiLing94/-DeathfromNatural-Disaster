import json
from django.shortcuts import render
from django.http import HttpResponse
from naturalDisaster.settings import MEDIA_URL,MEDIA_ROOT
from django.conf.urls.static import static
from django.http import HttpResponse
from django.views.generic import TemplateView, View 

import pandas as pd
import numpy as np
import re
import matplotlib as pl
pl.use('Agg')
import matplotlib.pyplot as plt
import plotly
import plotly.graph_objs as go
import json

class HomePageView(TemplateView):
    def get(self,request,**kwargs):
        return render(request, 'combine/index.html', context=None)

class Api(TemplateView):
    def getFlood(request):
        df = pd.read_csv('naturalDisaster.csv')
        df.drop(['Extreme temperature','Mass movement (dry)','Volcanic activity','Drought'], axis = 1, inplace = True)
        df = df[df["Country"].str.contains("income")==False]
        df['Flood'] = pd.to_numeric(df['Flood'],errors='coerce')
        df = df.replace(np.nan, 0)
        df = df[df['Flood']>300]
        x = df['Country']
        y = df['Flood']
        plt.bar(x,y, color = '#c9e9f6')
        plt.title('Number of Deaths from Floods')
        plt.xlabel('Country')
        plt.ylabel('Number of Deaths')
        plt.xticks(fontsize=8)
        plt.yticks(fontsize=8)
        response = HttpResponse(content_type="image/jpeg")
        plt.savefig('media/Floods.png',format="png")
        return HttpResponse('media/Floods.png')

    def getWildfire(request):
        df_Wildfire = pd.read_csv('naturalDisaster.csv')
        df_Wildfire.drop(['Extreme temperature','Mass movement (dry)','Volcanic activity','Drought'], axis = 1, inplace = True)
        df_Wildfire = df_Wildfire[df_Wildfire["Country"].str.contains("income")==False]
        df_Wildfire['Wildfire'] = pd.to_numeric(df_Wildfire['Wildfire'],errors='coerce')
        df_Wildfire = df_Wildfire.replace(np.nan, 0)
        df_Wildfire = df_Wildfire[df_Wildfire['Wildfire']>100]
        x = df_Wildfire['Country']
        y = df_Wildfire['Wildfire']
        plt.bar(x,y, color = '#c9e9f6')
        plt.title('Number of Deaths from Wildfire')
        plt.xlabel('Country')
        plt.ylabel('Number of Deaths')
        plt.xticks(fontsize=8)
        plt.yticks(fontsize=8)
        response = HttpResponse(content_type="image/jpeg")
        plt.savefig('media/Wildfire.png',format="png")
        return HttpResponse('media/Wildfire.png')
    
    def getStorms(request):
        df_Storms = pd.read_csv('naturalDisaster.csv')
        df_Storms.drop(['Extreme temperature','Mass movement (dry)','Volcanic activity','Drought'], axis = 1, inplace = True)
        df_Storms = df_Storms[df_Storms["Country"].str.contains("income")==False]
        df_Storms['Storms'] = pd.to_numeric(df_Storms['Storms'],errors='coerce')
        df_Storms = df_Storms.replace(np.nan, 0)
        df_Storms = df_Storms[df_Storms['Storms'] > 300]
        x = df_Storms['Country']
        y = df_Storms['Storms']
        plt.bar(x,y, color = '#c9e9f6')
        plt.title('Number of Deaths from Storms')
        plt.xlabel('Country')
        plt.ylabel('Number of Deaths')
        plt.xticks(fontsize=8)
        plt.yticks(fontsize=8)
        response = HttpResponse(content_type="image/jpeg")
        plt.savefig('media/Storms.png',format="png")
        return HttpResponse('media/Storms.png')
    
    def getLandslides(request):
        df_Landslides = pd.read_csv('naturalDisaster.csv')
        df_Landslides.drop(['Extreme temperature','Mass movement (dry)','Volcanic activity','Drought'], axis = 1, inplace = True)
        df_Landslides = df_Landslides[df_Landslides["Country"].str.contains("income")==False]
        df_Landslides['Landslides'] = pd.to_numeric(df_Landslides['Landslides'],errors='coerce')
        df_Landslides = df_Landslides.replace(np.nan, 0)
        df_Landslides = df_Landslides[df_Landslides['Landslides'] > 400]
        x = df_Landslides['Country']
        y = df_Landslides['Landslides']
        plt.bar(x,y, color = '#c9e9f6')
        plt.title('Number of Deaths from Landslides')
        plt.xlabel('Country')
        plt.ylabel('Number of Deaths')
        plt.xticks(fontsize=8)
        plt.yticks(fontsize=8)
        response = HttpResponse(content_type="image/jpeg")
        plt.savefig('media/Landslides.png',format="png")
        return HttpResponse('media/Landslides.png')
    
    def getEarthquakes(request):
        df_Earthquakes = pd.read_csv('naturalDisaster.csv')
        df_Earthquakes.drop(['Extreme temperature','Mass movement (dry)','Volcanic activity','Drought'], axis = 1, inplace = True)
        df_Earthquakes = df_Earthquakes[df_Earthquakes["Country"].str.contains("income")==False]
        df_Earthquakes['Earthquakes'] = pd.to_numeric(df_Earthquakes['Earthquakes'],errors='coerce')
        df_Earthquakes = df_Earthquakes.replace(np.nan, 0)
        df_Earthquakes = df_Earthquakes[df_Earthquakes['Earthquakes'] > 400]
        x = df_Earthquakes['Country']
        y = df_Earthquakes['Earthquakes']
        plt.bar(x,y, color = '#c9e9f6')
        plt.title('Number of Deaths from Earthquakes')
        plt.xlabel('Country')
        plt.ylabel('Number of Deaths')
        plt.xticks(fontsize=8)
        plt.yticks(fontsize=8)
        response = HttpResponse(content_type="image/jpeg")
        plt.savefig('media/Earthquakes.png',format="png")
        return HttpResponse('media/Earthquakes.png')
