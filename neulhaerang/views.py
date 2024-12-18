from datetime import datetime
from os.path import exists

from django.core import serializers
from django.db.models import Sum, F, Count, Value, Q, ExpressionWrapper
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views import View
from rest_framework.response import Response
from rest_framework.views import APIView

from customer_center.models import Alarm
from member.models import Member
from neulhaerang.models import Neulhaerang, NeulhaerangDonation, NeulhaerangInnerTitle, NeulhaerangInnerContent, \
    NeulhaerangInnerPhotos, BusinessPlan, NeulhaerangTag, NeulhaerangLike, Byeoljji, NeulhaerangParticipants, \
    NeulhaerangReply, ReplyLike
from neulhaerang_review.models import NeulhaerangReview
from static_app.models import Badge, MemberBadge
from workspace.pagenation import Pagenation, Pagenation
from workspace.serializers import NeulhaerangSerializer, PagenatorSerializer, NeulhaerangReplySerializer

class NeulhaerangListView(View):

    def get(self, request):
        # print(request.session.get("member_email"))
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
            neulhaerang = Neulhaerang.objects.all().filter(category__category_name=category,neulhaerang_status="모금중")
        else:
            neulhaerang = Neulhaerang.objects.all().filter(neulhaerang_status="모금중")

        if(sort == '추천순'):
            neulhaerang = neulhaerang.filter(neulhaerang_status="모금중").annotate(neulhaerang=Count('neulhaeranglike')).order_by('-neulhaerang','-created_date')
        elif(sort == '최신순'):
            neulhaerang = neulhaerang.filter(neulhaerang_status="모금중").order_by('-created_date')
        else:
            neulhaerang = neulhaerang.filter(neulhaerang_status="모금중").order_by('fund_duration_end_date')
        pagenator = Pagenation(page=page, page_count=5, row_count=8, query_set=neulhaerang)
        posts = NeulhaerangSerializer(pagenator.paged_models, many=True).data
        serialized_pagenator= PagenatorSerializer(pagenator).data


        existsPost = False
        if(posts):
            existsPost = True

        datas = {
            "posts":posts,
            "pagenator" : serialized_pagenator,
            "existsPost" : existsPost
        }

        return Response(datas)

# 상세보기
class NeulhaerangDetailView(View):
    def get(self, request, neulhaerang_id):
        my_email = request.session.get('member_email')
        #이메일 검사
        if(my_email):
            my_member = Member.objects.get(member_email=my_email)
        else:
            my_member = ""

        post = Neulhaerang.objects.get(id=neulhaerang_id)
        post_writer_thumb = Neulhaerang.objects.filter(id=neulhaerang_id).values('member__profile_image')[0]
        post_badge = Badge.objects.filter(category_id=post.category_id)[0]
        business_plan = BusinessPlan.objects.filter(neulhaerang_id=neulhaerang_id).order_by('-created_date')
        tags = NeulhaerangTag.objects.filter(neulhaerang_id=neulhaerang_id).order_by('id')
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
        bottom_posts = Neulhaerang.objects.exclude(id=neulhaerang_id).filter(neulhaerang_status="모금중").order_by('?')[0:4]

        neulhaerang_participants = NeulhaerangParticipants.objects.filter(member__member_email=my_email, neulhaerang_id=neulhaerang_id)
        if(neulhaerang_participants):
            check_my_participate = 'on'
        else:
            check_my_participate = ''

        if(NeulhaerangLike.objects.filter(member__member_email=my_email, neulhaerang_id=neulhaerang_id)):
            cheer_status = 'on'
        else:
            cheer_status = ''
        if(amount_sum['donation_amount__sum'] is None):
            amount_sum = {'donation_amount__sum': 0}
        print(post.neulhaerang_status)
        context = {
            'my_member': my_member,
            'post_badge': post_badge,
            'cheer_status': cheer_status,
            'check_my_participate': check_my_participate,
            'neulhaerang_id': neulhaerang_id,
            'post_writer_thumb': post_writer_thumb,
            'neulhaerang_review': neulhaerang_review,
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

# 댓글
class NeulhaerangDetailReplyAPIView(APIView):
    exclude_id_list = []
    def get(self, request):
        my_email = request.session.get('member_email')
        replyPage = int(request.GET.get('replyPage'))
        neulhaerang_id = request.GET.get('neulhaerangId')
        check_donate_reply = request.GET.get('checkDonateReply')

        if(check_donate_reply == "전체"):
            replys_queryset = NeulhaerangReply.objects.all().filter(neulhaerang_id=neulhaerang_id)
        else:
            replys_queryset = NeulhaerangReply.objects.all().filter(neulhaerang_id=neulhaerang_id,donation__isnull=False)
        replys_count = replys_queryset.count()
        if(replyPage==1):
            first_page_replys_id = []
            best_replys = replys_queryset.annotate(reply_count=Count('replylike')).filter(reply_count__gt = 3).order_by('-reply_count','-created_date').annotate(best_reply=Value(True))
            best_replys_count = best_replys.count()

            if(best_replys_count>3):
                best_replys = best_replys[0:3]

            for best_reply in best_replys.values('id'):
                first_page_replys_id.append(best_reply['id'])

            normal_replys = replys_queryset.exclude(id__in=first_page_replys_id)[0:5-best_replys_count]

            for normal_reply in normal_replys.values('id'):
                first_page_replys_id.append(normal_reply['id'])
            NeulhaerangDetailReplyAPIView.exclude_id_list = first_page_replys_id
            total_replys = list(best_replys)+list(normal_replys)
            replys = NeulhaerangReplySerializer(total_replys, many=True, context={'request': request}).data
            pagenator = Pagenation(page=replyPage, page_count=5, row_count=5, query_set=replys_queryset)
            serialized_pagenator = PagenatorSerializer(pagenator).data
            datas = {
                'replys':replys,
                'replys_count':replys_count,
                'serialized_pagenator':serialized_pagenator,
            }
            return Response(datas)
        else:
            replys_queryset = replys_queryset.exclude(id__in=NeulhaerangDetailReplyAPIView.exclude_id_list)
            pagenator = Pagenation(page=replyPage-1, page_count=5, row_count=5, query_set=replys_queryset)
            replys = NeulhaerangReplySerializer(pagenator.paged_models, many=True, context={'request': request}).data
            serialized_pagenator = PagenatorSerializer(pagenator).data
            datas = {
                'replys':replys,
                'replys_count':replys_count,
                'serialized_pagenator':serialized_pagenator

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

class NeulhaerangDetailLikeAPIView(APIView):
    def get(self, request):
        my_email = request.session.get('member_email')
        neulhaerang_id = request.GET.get('neulhaerangId')
        member = Member.objects.get(member_email=my_email)
        neulhaerang = Neulhaerang.objects.get(id=neulhaerang_id)
        neulhaerang_like = NeulhaerangLike.objects.filter(member=member, neulhaerang=neulhaerang)
        if neulhaerang_like:
            neulhaerang_like.delete()
        else:
            NeulhaerangLike.objects.create(member=member, neulhaerang=neulhaerang)
        neulhaerang_like_count = NeulhaerangLike.objects.filter(neulhaerang=neulhaerang).count()

        return Response(neulhaerang_like_count)

class NeulhaerangDetailParticipateAPIView(APIView):
    def get(self, request):
        my_email = request.session.get('member_email')
        neulhaerang_id = request.GET.get('neulhaerangId')
        member = Member.objects.get(member_email=my_email)
        neulhaerang = Neulhaerang.objects.get(id=neulhaerang_id)
        neulhaerang_participate = NeulhaerangParticipants.objects.filter(member=member, neulhaerang=neulhaerang)
        neulhaerang_participate_max = Neulhaerang.objects.filter(id=neulhaerang_id).values('participants_max_count')[0]
        neulhaerang_participate_count = NeulhaerangParticipants.objects.filter(neulhaerang=neulhaerang).count()
        check_toast = False
        if(neulhaerang_participate):
            neulhaerang_participate.delete()
        elif(neulhaerang_participate_max['participants_max_count'] > neulhaerang_participate_count):
            NeulhaerangParticipants.objects.create(member=member, neulhaerang=neulhaerang)
        else:
            check_toast = True
        neulhaerang_participate_count = NeulhaerangParticipants.objects.filter(neulhaerang=neulhaerang).count()
        datas = {
            'check_toast':check_toast,
            'neulhaerang_participate_count':neulhaerang_participate_count,
            'neulhaerang_participate_max':neulhaerang_participate_max
        }

        return JsonResponse(datas)

class NeulhaerangDetailRealtimeFundAmountAPIView(APIView):
    def get(self, request):
        neulhaerang_id = request.GET.get('neulhaerangId')
        post = Neulhaerang.objects.filter(id=neulhaerang_id).values()
        post_donation_sum = NeulhaerangDonation.objects.filter(neulhaerang_id=neulhaerang_id).aggregate(sum=Sum('donation_amount'))

        datas={
            'post':post[0],
            'post_donation_sum':post_donation_sum['sum'],
        }
        return JsonResponse(datas)


class SuccessPayment(APIView):
    def get(self, request):
        my_email = request.session.get('member_email')
        neulhaerang_id = int(request.GET.get('neulhaerangId'))
        category_id = Neulhaerang.objects.get(id=neulhaerang_id).category_id
        donation_content = request.GET.get('donationContent')
        donation_amount = int(request.GET.get('donationAmount'))
        donation_anonymous = request.GET.get('donationAnonymous')
        member = Member.objects.get(member_email=my_email)
        member_nickname = member.member_nickname
        #
        if(donation_anonymous == '비공개'):
            member_nickname = '익명의 기부천사'

        if(not donation_content):
            donation_content = '응원합니다'
        donation = NeulhaerangDonation.objects.create(member=member, donation_amount=donation_amount,
                                                      donation_content=donation_content,donation_anonymous=donation_anonymous,
                                                      neulhaerang_id=neulhaerang_id)
        NeulhaerangReply.objects.create(reply_content=donation_content, member=member, donation=donation, neulhaerang_id=neulhaerang_id)
        MemberBadge.objects.create(member=member,badge_id=category_id)
        neulhaerang = Neulhaerang.objects.get(id=neulhaerang_id)
        message = f'회원님이 작성한 늘해랑:{neulhaerang.neulhaerang_title}에 \n' \
                  f'{member_nickname}님이 {donation_amount:,}원을 기부했어요.'
        Alarm.objects.create(member=neulhaerang.member, type='neulhaerang', reference_id=neulhaerang_id, message=message)


        if(member.total_donation_fund<2000):
            member.donation_level = 'silver'
        elif(member.total_donation_fund<5000):
            member.donation_level = 'gold'
        elif(member.total_donation_fund<150000):
            member.donation_level = 'platinum'
        elif(member.total_donation_fund<500000):
            member.donation_level = 'diamond'


        member.total_donation_fund += donation_amount
        member.total_donation_count += 1
        member.save()

        return Response(True)

class NeulhaerangEndStatusAPIView(APIView):
    def get(self, request):
        neulhaerang_id = request.GET.get('neulhaerangId')
        post = Neulhaerang.objects.filter(id=neulhaerang_id,).annotate(donation_sum=Sum('neulhaerangdonation__donation_amount')).values()

        datas = {
            'post': list(post),
        }

        return JsonResponse(datas)



class TestView(View):
    def get(self, request):
        Neulhaerang.objects.filter(neulhaeranglike__member__member_email='email').annotate(member_nickname=F('member__member_nickname'))
        return render(request, 'neulhaerang/test.html')
    def post(self, request):
        file = request.FILES
        print(file.get('file'))
        # NeulhaerangInnerPhotos.objects.create(inner_photo=file.get('file'), neulhaerang_content_order=1, photo_order=1, photo_explanation='설명1',neulhaerang_id=7)
        # Neulhaerang.objects.create(member_id=1,neulhaerang_title=f"이미지 테스트",volunteer_duration_start_date=datetime.now()
        #                            ,volunteer_duration_end_date=datetime.now(),category_id=1, thumbnail_image=file.get('file'))
        # Member.objects.create(member_nickname='임웅빈테스트', member_age=4, member_gender='M', member_role='MEMBER',
        #                       donation_status='open', total_donation_fund=0, total_donation_count=0, donation_level='bronze',
        #                       profile_image=file.get('file'), profile_image_choice='user')
        pass
