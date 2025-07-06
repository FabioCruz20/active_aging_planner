from django.urls import path
from planning.views import projects_views

app_name = 'projects'

urlpatterns = [
    path('', projects_views.list_view, name='list'),
    path('new', projects_views.new_view, name='new'),
    path('<int:project_id>/edit', projects_views.edit_view, name='edit'),
    path('<int:project_id>/delete', projects_views.delete, name='delete'),
    path('<int:project_id>/manage_levels', projects_views.manage_project_levels_view, name='manage_levels'),
    path('level/<int:projectlevel_id>/manage_actions', projects_views.manage_level_actions_view, name='manage_actions'),
]
