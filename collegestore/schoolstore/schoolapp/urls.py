from . import views
from django.urls import path
app_name="schoolapp"
urlpatterns = [
     path('',views.home, name='home'),
     path('login/', views.login, name='login'),
     path('register/', views.register, name='register'),
     path('registerform/', views.registerform, name='registerform'),
     path('firstregister/', views.firstregister, name='firstregister'),
     path('get_json/', views.get_json, name='get_json'),

]
