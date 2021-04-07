# app_blog/urls.py
from django.urls import path

from .views import (HomePageView, ArticleDetail, ArticleList,
                    ArticleCategoryList)

urlpatterns = [
    path(r'', HomePageView.as_view(), name='home'),
    path(r'articles', ArticleList.as_view(), name='articles-list'),
    path(r'articles/category/<slug>',
         ArticleCategoryList.as_view(),
         name='articles-category-list'),
    path(r'articles/<year>/<month>/<day>/<slug>',
         ArticleDetail.as_view(),
         name='news-detail'),  #ear=2020, month=02, day=19, slug=pandas-cheat-sheet-python-for-data-science
]

# articles/2020/02/19/pandas-cheat-sheet-python-for-data-science