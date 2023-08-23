from django.db.models import Count
from django.shortcuts import render
from django.views import View
from rest_framework.response import Response
from rest_framework.views import APIView

from neulhaerang_review.models import NeulhaerangReview
from workspace.pagenation import Pagenation
from workspace.serializers import NeulhaerangSerializer, PagenatorSerializer, NeulhaerangReviewSerializer


# Create your views here.
class NeulhaerangReviewDetailView(View):
    def get(self, request, neulhaerang_review_id):
        post = NeulhaerangReview.objects.get(id=neulhaerang_review_id)
        context = {
            'post':post,
        }
        return render(request,'neulhaerang/review-detail.html',context)


class NeulhaerangReviewListView(View):
    def get(self,request):
        def get(self, request):
            if request.GET.get("page") is not None:
                page = request.GET.get("page")
            else:
                page = 1

        return render(request,'neulhaerang/review-list.html')

class NeulhaerangReviewListAPIView(APIView):
    def get(self, request):
        page = int(request.GET.get("page"))
        sort = request.GET.get("sort")

        neulhaerang_review = NeulhaerangReview.objects.all()

        if(sort == '추천순'):
            neulhaerang_review = neulhaerang_review.annotate(review_like_count=Count('neulhaerangreviewlike')).order_by('-review_like_count','-created_date')
        elif(sort == '최신순'):
            neulhaerang_review = neulhaerang_review.order_by('-created_date')
        #
        pagenator = Pagenation(page=page, page_count=5, row_count=8, query_set=neulhaerang_review)
        posts = NeulhaerangReviewSerializer(pagenator.paged_models, many=True).data
        serialized_pagenator = PagenatorSerializer(pagenator).data


        datas = {
            "posts": posts,
            "pagenator": serialized_pagenator
        }

        return Response(datas)

