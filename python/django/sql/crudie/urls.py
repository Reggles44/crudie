from django.urls import path
from crudie.views import create, read, update, delete

urlpatterns = [
    path('create', create),
    path('read', read),
    path('update', update),
    path('delete', delete),
]
