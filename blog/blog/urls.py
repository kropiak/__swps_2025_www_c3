from django.contrib import admin
from django.urls import path, include
from debug_toolbar.toolbar import debug_toolbar_urls
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('posts/', include('posts.urls')),
    path('', views.index_view),
    path('api-auth/', include('rest_framework.urls')),
] + debug_toolbar_urls()
