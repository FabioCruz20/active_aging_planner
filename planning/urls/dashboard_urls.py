from django.urls import path
from planning.views import dashboard_views

app_name = 'dashboard'

urlpatterns = [
    path('', dashboard_views.index_view, name='index'),
]
