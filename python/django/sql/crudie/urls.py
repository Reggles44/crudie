from django.urls import path
from crudie.views import healthcheck, create, read, update, delete

urlpatterns = [
    path("", healthcheck),
    path("create", create),
    path("read/<int:id>", read),
    path("update/<int:id>", update),
    path("delete/<int:id>", delete),
]
