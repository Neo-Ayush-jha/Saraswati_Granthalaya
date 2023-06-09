from django.urls import path,include
from .views import *

urlpatterns = [
    path("",BookView.as_view(),name="Book"),
    path("category/",CategoryView.as_view(),name="Category")
]
