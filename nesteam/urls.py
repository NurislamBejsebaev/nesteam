from django.contrib import admin
from django.urls import path, include
from rest_framework.schemas import get_schema_view
from django.views.generic import TemplateView
from games.views import *
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'genre', GenreViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api_schema/', get_schema_view(title='API Schema', description='test'), name='api_schema'),
    path('docs/', TemplateView.as_view(
        template_name='docs.html',
        extra_context={'schema_url': 'api_schema'}
    ),
         name='swagger-ui'),
    path('games/', include('games.urls')),
    path('users/', include('usersapp.urls')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('auth/', include('djoser.urls.jwt')),
    path('collections/', include('collection.urls')),
    path('', include(router.urls)),
]
