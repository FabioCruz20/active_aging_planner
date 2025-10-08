from django.urls import path, include

urlpatterns = [
    path('projects/', include('planning.urls.projects_urls')),
    path('actions/', include('planning.urls.actions_urls')),
    path('levels/', include('planning.urls.levels_urls')),
    path('papers/', include('planning.urls.papers_urls')),
    path('help/', include('planning.urls.help_urls')),
    path('dashboard/', include('planning.urls.dashboard_urls')),
    path('profile/', include('planning.urls.profiles_urls')),
]