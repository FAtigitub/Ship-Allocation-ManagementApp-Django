from django.contrib import admin
from django.urls import path, include
from marsa import views
from django.conf.urls.static import static
from django.conf import settings
app_name = 'marsa'

from marsa import views

urlpatterns = [  
    path('admin/', admin.site.urls),
    path('', views.loginPage, name='login'),
    path('home/', views.homeView, name='home')
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)