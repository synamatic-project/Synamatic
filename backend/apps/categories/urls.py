from django.urls import path        
from .views import categoryList


urlpatterns = [
    path('',categoryList.as_view(), name='categoryList'),
    
]