from django.urls import path
from planning.views import levels_views

app_name = 'levels'

urlpatterns = [
    path('', levels_views.list_view, name='list'),
    path('new', levels_views.new_view, name='new'),
    path('<int:level_id>/edit', levels_views.edit_view, name='edit'),
    path('<int:level_id>/delete', levels_views.delete, name='delete')
]
