from . import views
from django.urls import path
from .views import PostCreate, PostList, PostDetail, PostLike, PostUpdate, PostDelete

urlpatterns = [
    path('', views.PostList.as_view(), name="home"),
    path('post/create/', PostCreate.as_view(), name="post_create"),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path('post/<slug:slug>/update/', PostUpdate.as_view(), name='post_update'),
    path('post/<slug:slug>/delete/', PostDelete.as_view(), name='post_delete'),
]