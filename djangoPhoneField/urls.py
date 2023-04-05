from django.contrib import admin
from django.urls import path
from src.views import save_person

urlpatterns = [
    path('', save_person, name='index'),
    path('admin/', admin.site.urls),
]
