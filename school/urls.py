from django.urls import path

from .views import SchoolPage

urlpatterns =[
    path('', SchoolPage.as_view(), name='school')
]