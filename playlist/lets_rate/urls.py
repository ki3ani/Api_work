from django.urls import path 
from . import views 


urlpatterns = [
    path('',views.home, name="home"),
    path('',views.success, name="success"),
    path('rate/<int:id>',views.rate,name="rate"),
]

