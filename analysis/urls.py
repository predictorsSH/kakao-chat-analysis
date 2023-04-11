from django.urls import path
from . import views


urlpatterns = [
    path('', views.fileUploadView, name="fileupload",),
    path('basic-analysis/<int:id>', views.BasicStatView.as_view()),
    path('advanced-analysis/<int:id>', views.AdvancedAnalysisView.as_view())
]