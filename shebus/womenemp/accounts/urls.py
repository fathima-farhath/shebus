from django.urls import path
from . import views
app_name = 'accounts'
urlpatterns = [
    path('',views.home,name='home'),
    path('login/',views.user_login,name='login'),
    path('reg/',views.reg,name='reg'),
]