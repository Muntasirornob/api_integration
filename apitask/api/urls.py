from django.urls import path 
from .import views


urlpatterns = [
    path('submit',views.submit_form,name="submit"),#giving proper names to redirect the pages if necessary
    path('collectoken',views.collect_token,name="collectoken"),
    path('submitfile',views.upload_file,name="submitfile"),
    path('login/', views.login_page, name='login'),
	path('user_login/',views.user_login, name='user_login'),
]
