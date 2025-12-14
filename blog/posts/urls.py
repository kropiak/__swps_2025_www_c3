from django.urls import path
from . import views


urlpatterns = [
    path('welcome', views.welcome_view),
    path('topics', views.topic_list),
    path('categories', views.category_list),
    path('categories/<int:id>', views.category_detail),
]
