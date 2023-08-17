from django.urls import path

from search.views import SearchFormView, SearchClickView, SearchInputView

app_name = 'search'

urlpatterns = [
    path('form/',SearchFormView.as_view(),name='form'),
    path('click/',SearchClickView.as_view(),name = 'click'),
    path('input/',SearchInputView.as_view(),name='input'),
]