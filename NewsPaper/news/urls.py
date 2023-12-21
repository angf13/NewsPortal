from django.urls import path
from .views import PostList, PostDetail, PostSearch, NewsCreate, NewsDelete, NewsUpdate, ArticlesUpdate, ArticlesDelete

ArticlesDelete

urlpatterns = [
    path('', PostList.as_view(), name='news'),
    path('search/', PostSearch.as_view()),
    path('<int:pk>', PostDetail.as_view(), name='separate_news'),
    path('create/', NewsCreate.as_view(), name='news_create'),
    path('<int:pk>/edit/', NewsUpdate.as_view(), name='news_edit'),
    path('<int:pk>/delete/', NewsDelete.as_view(), name='news_delete'),
    path('articles/create/', NewsCreate.as_view(), name='articles_create'),
    path('articles/<int:pk>/edit/', ArticlesUpdate.as_view(), name='articles_edit'),
    path('articles/<int:pk>/delete/', ArticlesDelete.as_view(), name='articles_delete'),

]
