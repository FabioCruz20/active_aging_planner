from django.urls import path
from planning.views import profiles_views as views

app_name = 'profiles'

urlpatterns = [
    path('', views.profile_view, name='profile'),
]