from django.urls import path
from . import views


urlpatterns = [
    path('', views.fileUploadView, name="fileupload",),
    path('basic-analysis/<int:f_id>', views.BasicStatView.as_view()),
    path('advanced-analysis/<int:f_id>', views.AdvancedAnalysisView.as_view()),
    path('usercount/<int:f_id>', views.UserCountView.as_view()),
]