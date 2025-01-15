from django.contrib import admin
from django.urls import path, include
from relationship_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pages/', include('relationship_app.urls')),
    path('', views.home, name='home'), 
]
