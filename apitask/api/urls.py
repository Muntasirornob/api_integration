from django.urls import path 
from .import views 
urlpatterns = [
    path('submit',views.submitForm),
    path('collectoken',views.collect_token),
    path('submitfile',views.upload_file),
]
