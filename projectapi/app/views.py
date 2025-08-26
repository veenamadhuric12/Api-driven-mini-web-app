from django.shortcuts import render,redirect
import requests
from . models import Weather
from .serialisers import WeatherSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

def index(request):
    weather_data = None
    if request.method == "POST":
        city = request.POST.get("city")
        if city:
            response = requests.get(f"https://goweather.herokuapp.com/weather/{city}")
            if response.status_code == 200:
                data = response.json()
                print(data)
                weather_data = {
                    "city": city.title(),
                    "temperature": data.get("temperature", "N/A"),
                    "wind":data.get("wind","N/A"),
                    "description": data.get("description", "N/A")
                }

                serializer = WeatherSerializer(data = weather_data)
                if serializer.is_valid():
                    serializer.save()
    
    return render(request, 'index.html',{"weather":weather_data})
def display(request):
    weathers = Weather.objects.all().order_by("-timestamp")
    return render(request,'display.html',{"weathers":weathers})

@api_view(['GET'])
def serial(request):
    weathers = Weather.objects.all().order_by("-timestamp")
    serializer = WeatherSerializer(weathers, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


