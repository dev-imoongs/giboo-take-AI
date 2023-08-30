from django.urls import path

from search.views import SearchFormView, SearchClickView, SearchInputView, ShowTagAPIView, ShowCategoryAPIView, ShowSearchListOfTagView, ShowSearchListOfCategoryView, ShowSearchListOfKeywordView, ShowSearchListOfTagAPIView, ShowSearchListOfCategoryAPIView

app_name = 'search'

urlpatterns = [
    path('form/',SearchFormView.as_view(),name='form'),
    path('click/',SearchClickView.as_view(),name='click'),
    path('input/',SearchInputView.as_view(),name='input'),
    path('tag/result/<str:tag_name>/<str:tag_type>/', ShowSearchListOfTagView.as_view(), name='tag-result'),
    path('category/result/<str:category_name>/', ShowSearchListOfCategoryView.as_view(), name='category-result'),
    path('keyword/result/', ShowSearchListOfKeywordView.as_view(), name='keyword-result'),

    # API View
    path('tag/', ShowTagAPIView.as_view(), name='tag'),
    path('category/', ShowCategoryAPIView.as_view(), name='category'),
    path('tag/api/', ShowSearchListOfTagAPIView.as_view(), name='tag-api'),
    path('category/api/', ShowSearchListOfCategoryAPIView.as_view(), name='category-api')
]