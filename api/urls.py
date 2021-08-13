"""DRFTutorial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from .views import ArticleListView, ArticleDetailView, UserListView, UserDetailView

app_name = "api"

urlpatterns = [
    path("", ArticleListView.as_view(), name="article-list"),
    # path("/token-revoke", RevokeToken.as_view(), name="revoke-token"),
    path("/users/", UserListView.as_view(), name="user-list"),
    path("/<int:pk>", ArticleDetailView.as_view(), name="article-detail"),
    path("/users/<int:pk>", UserDetailView.as_view(), name="user-detail"),
]
