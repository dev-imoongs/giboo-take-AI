from datetime import datetime

from django.core import serializers
from django.db.models import Sum, F, Count
from django.shortcuts import render, redirect
from django.views import View
from rest_framework.response import Response
from rest_framework.views import APIView

from neulhaerang.models import Neulhaerang, NeulhaerangDonation, NeulhaerangInnerTitle, NeulhaerangInnerContent, \
    NeulhaerangInnerPhotos, BusinessPlan, NeulhaerangTag, NeulhaerangLike, Byeoljji, NeulhaerangParticipants, \
    NeulhaerangReply, ReplyLike
from workspace.pagenation import Pagenation, Pagenation
from workspace.serializers import NeulhaerangSerializer, PagenatorSerializer, NeulhaerangReplySerializer


class NeulhaerangDetailView(View):
    def get(self, request, neulhaerang_id):

        post = Neulhaerang.objects.get(id=neulhaerang_id)
        business_plan = BusinessPlan.objects.filter(neulhaerang_id=neulhaerang_id).order_by('-created_date')
        tags = NeulhaerangTag.objects.filter(neulhaerang_id=neulhaerang_id).order_by('-created_date')

        inner_title_query = NeulhaerangInnerTitle.objects.filter(neulhaerang_id=neulhaerang_id)
        content_query = NeulhaerangInnerContent.objects.filter(neulhaerang_id=neulhaerang_id)
        photo_query = NeulhaerangInnerPhotos.objects.filter(neulhaerang_id=neulhaerang_id)

        contents = list(inner_title_query) + list(content_query) + list(photo_query)
        byeoljji = Byeoljji.objects.filter(neulhaerang_id=neulhaerang_id).order_by('byeoljji_rank')
        sorted_contents = sorted(contents, key=lambda item: item.neulhaerang_content_order)
        target_amount = Neulhaerang.objects.filter(id=neulhaerang_id)
        amount_sum = NeulhaerangDonation.objects.filter(neulhaerang=neulhaerang_id).aggregate(Sum('donation_amount'))
        likes_count = NeulhaerangLike.objects.filter(neulhaerang_id=neulhaerang_id).count()
        participants_count = NeulhaerangParticipants.objects.filter(neulhaerang_id=neulhaerang_id).count()
        reply_count = NeulhaerangReply.objects.filter(neulhaerang_id=neulhaerang_id).count()
        bottom_posts = Neulhaerang.objects.all().order_by('-created_date')[0:4]

        if(amount_sum['donation_amount__sum'] is None):
            amount_sum = {'donation_amount__sum': 0}

        context = {
            'neulhaerang_id': neulhaerang_id,
            'bottom_posts': bottom_posts,
            'reply_count': reply_count,
            'participants_count' : participants_count,
            'likes_count' : likes_count,
            'byeoljjies': byeoljji,
            'amount_sum': amount_sum['donation_amount__sum'],
            'target_amount': serializers.serialize("json",target_amount),
            'tags': tags,
            'business_plan': serializers.serialize("json",business_plan),
            'post': post,
            'contents': serializers.serialize("json",sorted_contents),
        }
        return render(request,'neulhaerang/detail.html', context)


class NeulhaerangListView(View):

    def get(self, request):
        if request.GET.get("page") is not None:
            page = request.GET.get("page")
        else :
            page = 1

        return render(request, 'neulhaerang/list.html')
    # def get(self,request):
    #     posts = Neulhaerang.objects.all()[0:8]
    #     donation_list = []
    #     for post in posts:
    #         post_donation = NeulhaerangDonation.objects.filter(neulhaerang=post).aggregate(Sum('donation_amount'))
    #         donation_list.append(post_donation)
    #     print(type(donation_list))
    #


        # combined_data = zip(posts, donation_list)
    #
        # context = {
        #     'posts':serializers.serialize("json",posts),
        #     'fund_now':donation_list,
        #     'combined_data':combined_data,
        # }
    #     return render(request,'neulhaerang/list.html', context)


class NeulhaerangAPIView(APIView):
    def get(self, request):
        page = int(request.GET.get("page"))
        category = request.GET.get("category")
        sort = request.GET.get("sort")

        if(category != '전체'):
            neulhaerang = Neulhaerang.objects.all().filter(category__category_name=category)
        else:
            neulhaerang = Neulhaerang.objects.all()

        if(sort == '추천순'):
            neulhaerang = neulhaerang.annotate(neulhaerang=Count('neulhaeranglike')).order_by('-neulhaerang','-created_date')
        elif(sort == '최신순'):
            neulhaerang = neulhaerang.order_by('-created_date')
        else:
            neulhaerang = neulhaerang.order_by('-fund_duration_end_date','-created_date')

        pagenator = Pagenation(page=page, page_count=5, row_count=8, query_set=neulhaerang)
        posts = NeulhaerangSerializer(pagenator.paged_models, many=True).data
        serialized_pagenator= PagenatorSerializer(pagenator).data

        datas = {
            "posts":posts,
            "pagenator" : serialized_pagenator
        }
        return Response(datas)

class NeulhaerangDetailReplyAPIView(APIView):
    def get(self, request):
        replyPage = int(request.GET.get('replyPage'))

        neulhaerang_id = request.GET.get('neulhaerangId')
        replys_queryset = NeulhaerangReply.objects.all().filter(neulhaerang_id=neulhaerang_id).order_by("-created_date")[0:5]
        # reply_likes = []
        # for reply in replys:
        #     ReplyLike.objects.all().filter(neulhaerang_reply_id=reply.id)

        replys = NeulhaerangReplySerializer(replys_queryset,many=True).data


        datas = {
            'replys':replys,
        }

        return Response(datas)

class NeulhaerangDetailReplyWriteAPIView(APIView):
    def get(self, request):
        replyCont = request.GET.get('replyCont')
        neulhaerang_id = request.GET.get('neulhaerangId')
        NeulhaerangReply.objects.create(member_id='1', neulhaerang_id=neulhaerang_id, reply_content=replyCont)
        return Response(True)



class TestView(View):
    def get(self, request):
        return render(request, 'neulhaerang/test.html')
    def post(self, request):
        file = request.FILES
        # NeulhaerangInnerPhotos.objects.create(inner_photo=file.get('file'), neulhaerang_content_order=1, photo_order=1, photo_explanation='설명1',neulhaerang_id=7)
        # Neulhaerang.objects.create(member_id=1,neulhaerang_title=f"이미지 테스트",volunteer_duration_start_date=datetime.now()
        #                            ,volunteer_duration_end_date=datetime.now(),category_id=1, thumbnail_image=file.get('file'))
