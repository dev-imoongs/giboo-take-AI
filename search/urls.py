from django.urls import path

from search.views import SearchFormView, SearchClickView, SearchInputView

app_name = 'search'

urlpatterns = [
    path('form/',SearchFormView.as_view()),
    path('click/',SearchClickView.as_view()),
    path('input/',SearchInputView.as_view()),
]