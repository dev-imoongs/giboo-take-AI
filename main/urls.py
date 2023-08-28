from django.urls import path

from main.views import SuggestionChoiceView, MainView, MainGetNeulhaerangsByPagedRandomAPIView, \
    MainGetNeulhajangByPagedRandomAPIView, MainGetTagNeulhaerangsRandomAPIView, \
    MainGetTagClickNeulhaerangsRandomAPIView, \
    MainGetNeulhaerangReviewSlideAPIView, MainGetOneRandomNeulhaerangByTagAPIView, MainGetMemberRankingAPIView

app_name = 'main'

urlpatterns = [
    path('suggestion-choice/',SuggestionChoiceView.as_view(),name= "suggestion-choice"),
    path('main/',MainView.as_view(),name= 'main'),


    path('get-neulhaerangs-by-paged/',MainGetNeulhaerangsByPagedRandomAPIView.as_view()),
    path('get-neulhajang-slider/',MainGetNeulhajangByPagedRandomAPIView.as_view()),
    path('get-tag-neulhaerangs/',MainGetTagNeulhaerangsRandomAPIView.as_view()),
    path('get-click-tag-neulhaerangs/',MainGetTagClickNeulhaerangsRandomAPIView.as_view()),
    path('get-review-slide/',MainGetNeulhaerangReviewSlideAPIView.as_view()),
    path('get-random-tag-one-neulhaerang/',MainGetOneRandomNeulhaerangByTagAPIView.as_view()),
    path('get-member-ranking/',MainGetMemberRankingAPIView.as_view()),

]