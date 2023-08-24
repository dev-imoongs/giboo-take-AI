from django.urls import path

from search.views import SearchFormView, SearchClickView, SearchInputView, ShowTagAPIView

app_name = 'search'

urlpatterns = [
    path('form/',SearchFormView.as_view(),name='form'),
    path('click/<str:category_name>',SearchClickView.as_view(),name='click'),
    path('input/',SearchInputView.as_view(),name='input'),
    # API View
    path('tag/', ShowTagAPIView.as_view(), name='tag')
]