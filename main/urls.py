from django.urls import path

from main.views import SuggestionChoiceView, MainView, TestView, TestPreView

app_name = 'main'

urlpatterns = [
    path('suggestion-choice/',SuggestionChoiceView.as_view(),name= "suggestion-choice"),
    path('main/',MainView.as_view(),name= 'main'),

    path('test/', TestView.as_view(), name = 'test'),
    path('pretest/', TestPreView.as_view(), name= 'pretest')


]