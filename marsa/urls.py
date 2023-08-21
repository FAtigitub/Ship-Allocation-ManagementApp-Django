from django.contrib import admin
from django.urls import path,include
from marsa import views



app_name = 'marsa'
urlpatterns = [  
    path('admin/', admin.site.urls),
    path('', views.loginPage, name='login'),
    path('home/', views.homeView, name='home')
]
