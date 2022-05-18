from django.urls import path
from . import views
from .views import PostListView,PostDetailView,PostCreateView,PostUpdateView,PostDeleteView,UserPostListView
urlpatterns = [
    path('', PostListView.as_view(),name='blog-home'),
    path('user/<str:username>', UserPostListView.as_view(),name='user-post'),
    path('post/new', PostCreateView.as_view(),name='post-create'),
    path('post/new2',views.Postnew,name='post2-create'),
    path('post/<slug:slug>/', PostDetailView.as_view(),name='post-detail'),
    path('post/<slug:slug>/update', PostUpdateView.as_view(),name='post-update'),
    path('post/<slug:slug>/delete', PostDeleteView.as_view(),name='post-delete'),
    path('about', views.about,name='blog-about'),

    #path('homee', views.homee, name='homee')
]
