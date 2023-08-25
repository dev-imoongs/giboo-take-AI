from django.urls import path

from neulhajang.views import NeulhajangListView, NeulhajangListAPIView, NeulhajangDetailView

app_name = 'neulhajang'

urlpatterns = [
    path('list/', NeulhajangListView.as_view(), name ='list'),
    path('detail/<int:neulhajang_id>/', NeulhajangDetailView.as_view(), name='detail'),


    #apiview
    path('neulhajang-list-api-view/', NeulhajangListAPIView.as_view(), name='neulhajang-list-api-view'),

]