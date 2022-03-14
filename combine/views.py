from django.shortcuts import render
from django.http import HttpResponse
from naturalDisaster.settings import MEDIA_URL,MEDIA_ROOT
from django.conf.urls.static import static
from django.http import HttpResponse
from django.views.generic import TemplateView, View 

import pandas as pd
import numpy as np
import re
from matplotlib import pyplot as plt
import plotly
import plotly.graph_objs as go

class HomePageView(TemplateView):
    def get(self,request,**kwargs):
        return render(request, 'combine/index.html', context=None)

df = pd.read_csv('naturalDisaster.csv')
df.drop(['Extreme temperature','Mass movement (dry)','Volcanic activity','Drought'], axis = 1, inplace = True)
df = df[df["Country"].str.contains("income")==False]

class Api(TemplateView):
    def getFloods(request):
        df['Flood'] = pd.to_numeric(df['Flood'],errors='coerce')
        df_Flood = df.replace(np.nan, 0)
        df_Flood= df[df['Flood'] > 150]
        x = df['Country']
        y = df['Flood']
        plt.bar(x,y)
        plt.xlabel('Country')
        plt.ylabel('Flood')
        response = HttpResponse(content_type="image/jpeg")
        plt.savefig(response, format="png")
        # plt.savefig('media/floods.png',response, format="png")
        return response

    def getWilfire(request):
        df['Wilfire'] = pd.to_numeric(df['Wilfire'],errors='coerce')
        df_Wilfire = df.replace(np.nan, 0)
        df_Wilfire= df[df['Wilfire'] > 150]
        x = df['Country']
        y = df['Wilfire']
        plt.bar(x,y)
        plt.xlabel('Country')
        plt.ylabel('Wilfire')
        response = HttpResponse(content_type="image/jpeg")
        plt.savefig(response, format="png")
        # plt.savefig('media/Wilfire.png',response, format="png")
        return response
    
    def getStorms(request):
        df['Storms'] = pd.to_numeric(df['Storms'],errors='coerce')
        df_Storms = df.replace(np.nan, 0)
        df_Storms= df[df['Storms'] > 150]
        x = df['Country']
        y = df['Storms']
        plt.bar(x,y)
        plt.xlabel('Country')
        plt.ylabel('Storms')
        response = HttpResponse(content_type="image/jpeg")
        plt.savefig(response, format="png")
        # plt.savefig('media/Storms.png',response, format="png")
        return response
    
    def getLandslides(request):
        df['Landslides'] = pd.to_numeric(df['Landslides'],errors='coerce')
        df_Landslides = df.replace(np.nan, 0)
        df_Landslides= df[df['Landslides'] > 150]
        x = df['Country']
        y = df['Landslides']
        plt.bar(x,y)
        plt.xlabel('Country')
        plt.ylabel('Landslides')
        response = HttpResponse(content_type="image/jpeg")
        plt.savefig(response, format="png")
        # plt.savefig('media/Landslides.png',response, format="png")
        return response
    
    def getEarthquakes(request):
        df['Earthquakes'] = pd.to_numeric(df['Earthquakes'],errors='coerce')
        df_Earthquakes = df.replace(np.nan, 0)
        df_Earthquakes= df[df['Earthquakes'] > 150]
        x = df['Country']
        y = df['Earthquakes']
        plt.bar(x,y)
        plt.xlabel('Country')
        plt.ylabel('Earthquakes')
        response = HttpResponse(content_type="image/jpeg")
        plt.savefig(response, format="png")
        # plt.savefig('media/Earthquakes.png',response, format="png")
        return response
