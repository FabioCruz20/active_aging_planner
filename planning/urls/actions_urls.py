from django.urls import path
from planning.views import actions_views

app_name = 'actions'

urlpatterns = [
    path('', actions_views.list_view, name='list'),
    path('new', actions_views.new_view, name='new'),
    path('<int:action_id>/edit', actions_views.edit_view, name='edit'),
    path('<int:action_id>/delete', actions_views.delete, name='delete')
]
