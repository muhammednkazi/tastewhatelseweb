from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.videos,name="videos"),
    path('handlecomment', views.HandleComment,name="HandleComment"),
    path('<int:id>',views.openvideo,name="VideoPost")
    # <str:slug>,<int:id>
]