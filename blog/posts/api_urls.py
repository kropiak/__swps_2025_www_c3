from django.urls import path, include
from . import api_views

urlpatterns = [
    # path('topics/', api_views.topic_list),
    # path('topics/<int:pk>/', api_views.topic_detail),
    # path('topics/create/', api_views.topic_create),
    # path('topics/search/<str:phrase>/', api_views.topic_search_by_name),
    # path('topicscategories/search/<str:phrase>/', api_views.topic_and_category_search_by_name),
    # # path('categories/', api_views.ca_list),
    # path('categories/', api_views.category_list),
    # path('categories/<int:pk>/', api_views.category_detail),
    path('topics/', api_views.TopicList.as_view()),
    path('posts/', api_views.PostList.as_view()),
    path('posts/<int:pk>/', api_views.PostDetail.as_view()),
]