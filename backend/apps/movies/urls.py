from django.urls import path        


urlpatterns = [
    path('',views.movieList.as_view(), name='movieList'),
    
]