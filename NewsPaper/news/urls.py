from django.contrib import admin
from django.urls import path
from .views import PostsList, PostDetail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', PostsList.as_view()),
    path('<int:pk>', PostDetail.as_view())
]