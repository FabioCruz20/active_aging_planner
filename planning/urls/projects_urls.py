from django.urls import path
from planning.views import projects_views

app_name = 'projects'

urlpatterns = [
    path('', projects_views.list_view, name='list'),
    path('new', projects_views.new_view, name='new'),
    path('<int:project_id>/edit', projects_views.edit_view, name='edit'),
    path('<int:project_id>/delete', projects_views.delete, name='delete'),
    path('<int:project_id>/manage_levels', projects_views.manage_project_levels_view, name='manage_levels'),
    path('<int:project_id>/manage_actions_matrix', projects_views.manage_actions_matrix_view, name='manage_actions_matrix'),
    path('level/<int:projectlevel_id>/manage_actions', projects_views.manage_level_actions_view, name='manage_actions'),
    path('<int:project_id>/manage-axis-level-actions/<int:axis_id>/<int:level_id>/', 
         projects_views.manage_axis_level_actions_view, name='manage_axis_level_actions'),
    path('action/<int:project_action_id>/tasks/', 
         projects_views.manage_tasks_view, name='manage_tasks'),
    path('action/<int:project_action_id>/tasks/new/', 
         projects_views.create_task_view, name='create_task'),
    path('tasks/<int:task_id>/edit/', 
         projects_views.edit_task_view, name='edit_task'),
    path('tasks/<int:task_id>/delete/', 
         projects_views.delete_task_view, name='delete_task'),
]
