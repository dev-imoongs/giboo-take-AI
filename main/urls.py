from django.urls import path

from main.views import SuggestionChoiceView, MainView

app_name = 'main'

urlpatterns = [
    path('suggestion-choice/',SuggestionChoiceView.as_view(),name= "suggestion-choice"),
    path('main/',MainView.as_view(),name= 'main'),

]