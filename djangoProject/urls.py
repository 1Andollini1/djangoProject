from django.contrib import admin
from django.urls import path
from rekruto import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('greetings/', views.greetings, name = 'greetings'),
    path('', views.main_info),
]
