from django.urls import path
from planning.views import papers_views


app_name = 'papers'

urlpatterns = [
    path('', papers_views.list_papers, name='index'),
    path('new/', papers_views.create_paper, name='new'),
    path('<int:paper_id>/edit/', papers_views.edit_paper, name='edit'),
    path('<int:paper_id>/delete/', papers_views.delete_paper, name='delete'),
]