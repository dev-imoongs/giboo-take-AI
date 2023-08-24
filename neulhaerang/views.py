from datetime import datetime

from django.core import serializers
from django.db.models import Sum, F, Count, Value
from django.shortcuts import render, redirect
from django.views import View
from rest_framework.response import Response
from rest_framework.views import APIView

from member.models import Member
from neulhaerang.models import Neulhaerang, NeulhaerangDonation, NeulhaerangInnerTitle, NeulhaerangInnerContent, \
    NeulhaerangInnerPhotos, BusinessPlan, NeulhaerangTag, NeulhaerangLike, Byeoljji, NeulhaerangParticipants, \
    NeulhaerangReply, ReplyLike
from neulhaerang_review.models import NeulhaerangReview
from workspace.pagenation import Pagenation, Pagenation
from workspace.serializers import NeulhaerangSerializer, PagenatorSerializer, NeulhaerangReplySerializer


class NeulhaerangDetailView(View):
    def get(self, request, neulhaerang_id):

        post = Neulhaerang.objects.get(id=neulhaerang_id)
        post_writer_thumb = Neulhaerang.objects.filter(id=neulhaerang_id).values('member__profile_image')[0]
        business_plan = BusinessPlan.objects.filter(neulhaerang_id=neulhaerang_id).order_by('-created_date')
        tags = NeulhaerangTag.objects.filter(neulhaerang_id=neulhaerang_id).order_by('-created_date')
        if(NeulhaerangReview.objects.filter(neulhaerang_id=neulhaerang_id)):
            neulhaerang_review = NeulhaerangReview.objects.filter(neulhaerang_id=neulhaerang_id)[0]
        else:
            neulhaerang_review = None
        inner_title_query = NeulhaerangInnerTitle.objects.filter(neulhaerang_id=neulhaerang_id)
        content_query = NeulhaerangInnerContent.objects.filter(neulhaerang_id=neulhaerang_id)
        photo_query = NeulhaerangInnerPhotos.objects.filter(neulhaerang_id=neulhaerang_id).order_by('photo_order')

        contents = list(inner_title_query) + list(content_query) + list(photo_query)

        byeoljji = Byeoljji.objects.filter(neulhaerang_id=neulhaerang_id).order_by('byeoljji_rank')

        sorted_contents = sorted(contents, key=lambda item: item.neulhaerang_content_order)

        target_amount = Neulhaerang.objects.filter(id=neulhaerang_id)
        amount_sum = NeulhaerangDonation.objects.filter(neulhaerang=neulhaerang_id).aggregate(Sum('donation_amount'))
        likes_count = NeulhaerangLike.objects.filter(neulhaerang_id=neulhaerang_id).count()
        participants_count = NeulhaerangParticipants.objects.filter(neulhaerang_id=neulhaerang_id).count()
        reply = NeulhaerangReply.objects.filter(neulhaerang_id=neulhaerang_id)
        bottom_posts = Neulhaerang.objects.all().order_by('-created_date')[0:4]


        if(amount_sum['donation_amount__sum'] is None):
            amount_sum = {'donation_amount__sum': 0}

        context = {
            'neulhaerang_id': neulhaerang_id,
            'post_writer_thumb':post_writer_thumb,
            'neulhaerang_review':neulhaerang_review,
            'bottom_posts': bottom_posts,
            'reply_count': reply.count(),
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
        my_email = request.session.get('member_email')
        replyPage = int(request.GET.get('replyPage'))
        neulhaerang_id = request.GET.get('neulhaerangId')
        replys_queryset = NeulhaerangReply.objects.all().filter(neulhaerang_id=neulhaerang_id)
        pagenator = Pagenation(page=replyPage, page_count=5, row_count=5, query_set=replys_queryset)
        replys = NeulhaerangReplySerializer(pagenator.paged_models, many=True, context={'request': request}).data

        # 베댓을 가져왔는데 3개이상이다 그럼 오더바이 (좋아요 순 , 생성순)으로 최대 3개 가져와 list
        # 3개면 전체 댓글 가져온거 list 최신순으로 한다? 이게 말이댐?
        # 페이지네이터해 list+ list
        if(replyPage==1):
            # count = replys_queryset.annotate(reply_count=Count('replylike')).filter(reply_count__gt = 10).count()
            temps = replys_queryset.annotate(reply_count=Count('replylike')).filter(reply_count__gt = 10).order_by('-reply_count','-created_date').annotate(best_reply=Value(True))
            if(temps.count()>3):
                temps = temps[0:3]
            temp2 = replys_queryset.annotate(reply_count=Count('replylike')).order_by('-created_date')[0:5-temps.count()]
            sum_temp = list(temps)+list(temp2)
            replys = NeulhaerangReplySerializer(sum_temp, many=True, context={'request': request}).data
            datas = {
                'replys':replys,
                'replys_count':replys_queryset.count(),
            }
            return Response(datas)
        datas = {
            'replys':replys,
            'replys_count':replys_queryset.count(),

        }

        return Response(datas)

class NeulhaerangDetailReplyWriteAPIView(APIView):
    def get(self, request):
        my_email = request.session.get('member_email')
        replyCont = request.GET.get('replyCont')
        neulhaerang_id = request.GET.get('neulhaerangId')
        member = Member.objects.get(member_email=my_email)

        NeulhaerangReply.objects.create(member=member, neulhaerang_id=neulhaerang_id, reply_content=replyCont)

        return Response(True)

class NeulhaerangDetailReplyDeleteAPIview(APIView):
    def get(self, request):
        reply_id = request.GET.get('reply_id')
        NeulhaerangReply.objects.get(id=reply_id).delete()
        return Response(True)

class NeulhaerangDetailReplyLikeAPIView(APIView):
    def get(self, request):
        my_email = request.session.get('member_email')
        neulhaerang_reply_id = request.GET.get('reply_id')
        member = Member.objects.get(member_email=my_email)
        neulhaerang_reply = NeulhaerangReply.objects.get(id=neulhaerang_reply_id)
        reply_like = ReplyLike.objects.filter(neulhaerang_reply=neulhaerang_reply, member=member)
        if reply_like:
            reply_like.delete()
        else:
            ReplyLike.objects.create(neulhaerang_reply=neulhaerang_reply, member=member)
        reply_like_count = ReplyLike.objects.filter(neulhaerang_reply=neulhaerang_reply).count()

        return Response(reply_like_count)




class TestView(View):
    def get(self, request):
        return render(request, 'neulhaerang/test.html')
    def post(self, request):
        file = request.FILES
        # NeulhaerangInnerPhotos.objects.create(inner_photo=file.get('file'), neulhaerang_content_order=1, photo_order=1, photo_explanation='설명1',neulhaerang_id=7)
        # Neulhaerang.objects.create(member_id=1,neulhaerang_title=f"이미지 테스트",volunteer_duration_start_date=datetime.now()
        #                            ,volunteer_duration_end_date=datetime.now(),category_id=1, thumbnail_image=file.get('file'))
        # Member.objects.create(member_nickname='임웅빈테스트', member_age=4, member_gender='M', member_role='MEMBER',
        #                       donation_status='open', total_donation_fund=0, total_donation_count=0, donation_level='bronze',
        #                       profile_image=file.get('file'), profile_image_choice='user')
        pass
