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
    """
    Use to Save the data in s3 bucket
    Example: http://127.0.0.1:8000/api/save/?url=localhost:9090&path=/home/baibhav/Downloads/prometheus_new/prometheus-2.52.0.linux-amd64/data/
    """
    url = request.GET.get("url", None)
    response = requests.post(f"http://{url}/api/v1/admin/tsdb/snapshot")
    path = request.GET.get("path", None)
    data = response.json()
    print(path)
    upload(data["data"]["name"], f'{url}/{data["data"]["name"]}', path) 
    return Response(data)

@api_view([GET])
def create(request):
    """
    Use to download the data from s3 bucket to local system
    Example: http://127.0.0.1:8000/api/save/?url=localhost:9090&path=/home/baibhav/Downloads/prometheus_new/prometheus-2.52.0.linux-amd64/data/
    """
    url = request.GET.get("url", None)
    date = request.GET.get("date", None)
    download(url, date)
    return Response("")
    

