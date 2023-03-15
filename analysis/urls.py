from django.urls import path
from . import views


urlpatterns = [
    path('', views.fileUpload, name="fileupload",),
    path('basicstats/', views.BasicStatView.as_view())
]