from django.urls import path
from . import views


urlpatterns = [
    path('', views.fileUploadView, name="fileupload",),
    path('basicstats/<int:id>/', views.BasicStatView.as_view())
]