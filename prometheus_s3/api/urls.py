from django.urls import path
from . import views


#URLConf
urlpatterns = [
    path('save/', views.save),
    path('create/', views.create),
]