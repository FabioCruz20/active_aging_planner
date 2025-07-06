from django.urls import path, include

urlpatterns = [
    path('projects/', include('planning.urls.projects_urls')),
    path('actions/', include('planning.urls.actions_urls')),
    path('levels/', include('planning.urls.levels_urls')),
]