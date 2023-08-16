from django.urls import path

from main.views import SuggestionChoiceView

app_name = 'main'

urlpatterns = [
    path('suggestion-choice',SuggestionChoiceView.as_view()),
]