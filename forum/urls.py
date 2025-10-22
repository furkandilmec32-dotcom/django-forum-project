from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('forums/', views.ForumListView.as_view(), name='forum_list'),
    path('forums/<int:pk>/', views.ForumDetailView.as_view(), name='forum_detail'),
]
from django.urls import path
from . import views

from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('forums/', views.ForumListView.as_view(), name='forum_list'),
    path('forums/<int:pk>/', views.ForumDetailView.as_view(), name='forum_detail'),
    path('forums/<int:forum_pk>/threads/new/', views.ThreadCreateView.as_view(), name='thread_create'),
    path('threads/<int:pk>/', views.ThreadDetailView.as_view(), name='thread_detail'),
    path('threads/<int:thread_pk>/reply/', views.ReplyCreateView.as_view(), name='reply_create'),
]