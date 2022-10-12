from django.urls import path

from . import views

app_name = 'diary'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:diary_id>/', views.detail, name='detail'),
    path('diary/write/', views.diary_write, name='diary_write'),
]