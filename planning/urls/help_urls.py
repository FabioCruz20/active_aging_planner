from django.urls import path
from planning.views import help_views


app_name = 'help'

urlpatterns = [
    path('', help_views.help_topics, name='index'),
]