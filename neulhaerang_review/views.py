from django.core import serializers
from django.db.models import Count, Sum, Value
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from rest_framework.response import Response
from rest_framework.views import APIView

from member.models import Member
from neulhaerang.models import Byeoljji, Neulhaerang, NeulhaerangDonation, BusinessPlan, NeulhaerangParticipants
from neulhaerang_review.models import NeulhaerangReview, NeulhaerangReviewTag, ReviewInnerTitle, ReviewInnerContent, \
    ReviewInnerPhotos, FundUsageHistory, NeulhaerangReviewReply, ReviewReplyLike, NeulhaerangReviewLike
from static_app.models import Badge
from workspace.pagenation import Pagenation
from workspace.serializers import NeulhaerangSerializer, PagenatorSerializer, NeulhaerangReviewSerializer, \
    NeulhaerangReviewReplySerializer

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




class NeulhaerangReviewDetailView(View):
    def get(self, request, neulhaerang_review_id):
        my_email = request.session.get('member_email')
        review_post = NeulhaerangReview.objects.get(id=neulhaerang_review_id)
        neulhaerang_id = review_post.neulhaerang_id
        post_badge = Badge.objects.filter(category_id=review_post.neulhaerang.category_id)[0]
        # post_writer_thumb = NeulhaerangReview.objects.filter(id=neulhaerang_review_id).values('member__profile_image')[0]
        # business_plan = BusinessPlan.objects.filter(neulhaerang_id=neulhaerang_id).order_by('-created_date')
        fund_usage_history = FundUsageHistory.objects.filter(neulhaerang_review=review_post).order_by('id')
        tags = NeulhaerangReviewTag.objects.filter(neulhaerang_review_id=neulhaerang_review_id).order_by('id')
        inner_title_query = ReviewInnerTitle.objects.filter(neulhaerang_review_id=neulhaerang_review_id)
        content_query = ReviewInnerContent.objects.filter(neulhaerang_review_id=neulhaerang_review_id)
        photo_query = ReviewInnerPhotos.objects.filter(neulhaerang_review_id=neulhaerang_review_id).order_by('photo_order')
        review_inner_contents = list(inner_title_query) + list(content_query) + list(photo_query)
        sorted_inner_contents = sorted(review_inner_contents, key=lambda item: item.neulhaerang_content_order)
        byeoljji = Byeoljji.objects.filter(neulhaerang_id=neulhaerang_id).order_by('byeoljji_rank')
        target_amount = Neulhaerang.objects.filter(id=neulhaerang_id)

        amount_sum = NeulhaerangDonation.objects.filter(neulhaerang=neulhaerang_id).aggregate(Sum('donation_amount'))
        if(amount_sum['donation_amount__sum'] is None):
            amount_sum = 0

        likes_count = NeulhaerangReviewLike.objects.filter(neulhaerang_review_id=neulhaerang_review_id).count()
        # participants_count = NeulhaerangParticipants.objects.filter(neulhaerang_id=neulhaerang_id).count()
        reply = NeulhaerangReviewReply.objects.filter(neulhaerang_review_id=neulhaerang_review_id)
        bottom_posts = NeulhaerangReview.objects.exclude(id=neulhaerang_review_id).order_by('?')[0:4]
        #
        if (NeulhaerangReviewLike.objects.filter(member__member_email=my_email, neulhaerang_review_id=neulhaerang_review_id)):
            cheer_status = 'on'
        else:
            cheer_status = ''

        # if(amount_sum['donation_amount__sum'] is None):
        #     amount_sum = {'donation_amount__sum': 0}
        context = {
            'review_post': review_post,
            'post_badge': post_badge,
            'cheer_status': cheer_status,
            # 'neulhaerang_id': neulhaerang_id,
            'neulhaerang_review_id': neulhaerang_review_id,
            # 'post_writer_thumb':post_writer_thumb,
            # 'neulhaerang_review':neulhaerang_review,
            'bottom_posts': bottom_posts,
            'reply_count': reply.count(),
            # 'participants_count' : participants_count,
            'likes_count' : likes_count,
            # 'js_byeoljjies' : serializers.serialize("json",byeoljji),
            'byeoljjies': byeoljji,
            # 'amount_sum': amount_sum,
            # 'target_amount': serializers.serialize("json", target_amount),
            'tags': tags,
            # 'business_plan': serializers.serialize("json",business_plan),
            'fund_usage_history': serializers.serialize("json", fund_usage_history),
            'review_inner_contents': serializers.serialize("json", sorted_inner_contents),
        }
        return render(request,'neulhaerang/review-detail.html', context)


class NeulhaerangReviewDetailReplyAPIView(APIView):
    exclude_id_list = []
    def get(self, request):
        my_email = request.session.get('member_email')
        replyPage = int(request.GET.get('replyPage'))
        neulhaerang_review_id = request.GET.get('neulhaerangReviewId')
        replys_queryset = NeulhaerangReviewReply.objects.all().filter(neulhaerang_review_id=neulhaerang_review_id)
        if(replyPage==1):
            first_page_replys_id = []
            best_replys = replys_queryset.annotate(reply_count=Count('reviewreplylike')).filter(reply_count__gt = 10).order_by('-reply_count','-created_date').annotate(best_reply=Value(True))
            best_replys_count = best_replys.count()

            if(best_replys_count>3):
                best_replys = best_replys[0:3]

            for best_reply in best_replys.values('id'):
                first_page_replys_id.append(best_reply['id'])

            normal_replys = replys_queryset.exclude(id__in=first_page_replys_id)[0:5-best_replys_count]

            for normal_reply in normal_replys.values('id'):
                first_page_replys_id.append(normal_reply['id'])

            NeulhaerangReviewDetailReplyAPIView.exclude_id_list = first_page_replys_id
            total_replys = list(best_replys)+list(normal_replys)
            replys = NeulhaerangReviewReplySerializer(total_replys, many=True, context={'request': request}).data

            datas = {
                'replys':replys,
                'replys_count':replys_queryset.count(),
            }
            return Response(datas)
        else:
            replys_queryset = replys_queryset.exclude(id__in=NeulhaerangReviewDetailReplyAPIView.exclude_id_list)
            pagenator = Pagenation(page=replyPage-1, page_count=5, row_count=5, query_set=replys_queryset)
            replys = NeulhaerangReviewReplySerializer(pagenator.paged_models, many=True, context={'request': request}).data
            serialized_pagenator = PagenatorSerializer(pagenator).data
            datas = {
                'replys':replys,
                'replys_count':replys_queryset.count(),
                'serialized_pagenator':serialized_pagenator
            }

            return Response(datas)

class NeulhaerangReviewDetailReplyWriteAPIView(APIView):
    def get(self, request):
        my_email = request.session.get('member_email')
        replyCont = request.GET.get('replyCont')
        neulhaerang_review_id = request.GET.get('neulhaerangReviewId')
        member = Member.objects.get(member_email=my_email)

        NeulhaerangReviewReply.objects.create(member=member, neulhaerang_review_id=neulhaerang_review_id, reply_content=replyCont)

        return Response(True)

class NeulhaerangReviewDetailReplyDeleteAPIview(APIView):
    def get(self, request):
        review_reply_id = request.GET.get('reply_id')
        NeulhaerangReviewReply.objects.get(id=review_reply_id).delete()
        return Response(True)

class NeulhaerangReviewDetailReplyLikeAPIView(APIView):
    def get(self, request):
        my_email = request.session.get('member_email')
        review_reply_id = int(request.GET.get('reply_id'))
        member = Member.objects.get(member_email=my_email)
        # review_reply = NeulhaerangReviewReply.objects.get(id=review_reply_id)
        if(review_reply_id is not None):
            review_reply_like = ReviewReplyLike.objects.filter(review_reply_id=review_reply_id, member=member)
        if review_reply_like:
            review_reply_like.delete()
        else:
            ReviewReplyLike.objects.create(review_reply_id=review_reply_id, member=member)
        reply_like_count = ReviewReplyLike.objects.filter(review_reply_id=review_reply_id).count()


        return Response(reply_like_count)

class NeulhaerangReviewDetailLikeAPIView(APIView):
    def get(self, request):
        my_email = request.session.get('member_email')
        neulhaerang_review_id = request.GET.get('neulhaerangReviewId')
        member = Member.objects.get(member_email=my_email)
        neulhaerang = Neulhaerang.objects.get(id=neulhaerang_review_id)
        neulhaerang_review_like = NeulhaerangReviewLike.objects.filter(member=member, neulhaerang_review_id=neulhaerang_review_id)
        if neulhaerang_review_like:
            neulhaerang_review_like.delete()
        else:
            NeulhaerangReviewLike.objects.create(member=member, neulhaerang_review_id=neulhaerang_review_id)
        neulhaerang_review_like_count = NeulhaerangReviewLike.objects.filter(neulhaerang_review_id=neulhaerang_review_id).count()

        return Response(neulhaerang_review_like_count)

class NeulhaerangReviewDetailFundraisingAPIView(APIView):
    def get(self, request):
        neulhaerang_review_id = request.GET.get('neulhaerangReviewId')
        neulhaerang_review = NeulhaerangReview.objects.get(id=neulhaerang_review_id)
        neulhaerang = Neulhaerang.objects.filter(neulhaerangreview=neulhaerang_review).values()
        donation_amount_sum = NeulhaerangDonation.objects.filter(neulhaerang__neulhaerangreview=neulhaerang_review).values()

        datas = {
            'neulhaerang':list(neulhaerang),
            'donation_amount_sum':list(donation_amount_sum),
        }

        return JsonResponse(datas)

class NeulhaerangReviewDetailInputByeoljjiAPIView(APIView):
    def get(self, request):
        neulhaerang_review_id = request.GET.get('neulhaerangReviewId')
        neulhaerang_review = NeulhaerangReview.objects.get(id=neulhaerang_review_id)
        neulhaerang = Neulhaerang.objects.filter(neulhaerangreview=neulhaerang_review).values()
        byeoljji = Byeoljji.objects.filter(neulhaerang__neulhaerangreview=neulhaerang_review).values().order_by('id')

        datas = {
            'neulhaerang': list(neulhaerang),
            'byeoljji':list(byeoljji)
        }

        return JsonResponse(datas)
