from django.urls import path

from introduce.views import IntroduceAboutView, IntroduceGibooSuggestionView, IntroducePartnersView, \
    IntroduceStatisticsView

app_name = 'introduce'

urlpatterns = [
    path('about/' ,IntroduceAboutView.as_view(),name="about" ),
    path('giboo-suggestion/',IntroduceGibooSuggestionView.as_view(),name="giboo-suggestion"),
    path('partners/',IntroducePartnersView.as_view(),name="partners"),
    path('statistics/',IntroduceStatisticsView.as_view(),name="statistics"),
]