from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from .const import *
from .upload_new import upload
import requests
import os
from .download import download


@api_view([GET])
def save(request):
    # pass
    url = request.GET.get("url", None)
    response = requests.post(f"http://{url}/api/v1/admin/tsdb/snapshot")
    path = request.GET.get("path", None)
    data = response.json()
    upload(data["data"]["name"], f'{url}/{data["data"]["name"]}') 
    return Response(data)

@api_view([GET])
def create(request):
    url = request.GET.get("url", None)
    date = request.GET.get("date", None)
    download(url, date)
    return Response("hello")
    

