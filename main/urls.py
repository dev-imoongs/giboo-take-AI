from django.urls import path

from main.views import SuggestionChoiceView, MainView, MainGetNeulhaerangsByPagedRandomAPIView, \
    MainGetNeulhajangByPagedRandomAPIView

app_name = 'main'

urlpatterns = [
    path('suggestion-choice/',SuggestionChoiceView.as_view(),name= "suggestion-choice"),
    path('main/',MainView.as_view(),name= 'main'),


    path('get-neulhaerangs-by-paged/',MainGetNeulhaerangsByPagedRandomAPIView.as_view()),
    path('get-neulhajang-slider/',MainGetNeulhajangByPagedRandomAPIView.as_view()),

]