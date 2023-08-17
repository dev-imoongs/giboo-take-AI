from django.urls import path

from neulhaerang.views import NeulhaerangListView

app_name = 'neulhajang'

urlpatterns = [
    path('list/', NeulhaerangListView.as_view())
]