from django.db import models

from member.models import Member
from static_app.models import Category
from workspace.models import Period

class Neulhaerang(Period):
    fund_duration_start_date = models.DateField(null=True, blank=False)
    fund_duration_end_date = models.DateField(null=True, blank=False)
    neulhaerang_duration = models.IntegerField(null=False, blank=False, default=0)
    volunteer_duration_start_date = models.DateField(null=False, blank=False)
    volunteer_duration_end_date = models.DateField(null=False, blank=False)
    participants_max_count = models.IntegerField(null=False, blank=False, default=0)
    target_amount = models.IntegerField(null=False, blank=False, default=0)
    target_amount_alternatives_plan = models.CharField(max_length=1000, null=False, blank=False)
    message_to_admin = models.CharField(max_length=1000, null=False, blank=False)
    neulhaerang_title = models.CharField(max_length=60, null=False, blank=False)
    thumbnail_image = models.ImageField(null=False, blank=False, upload_to='neulhaerang/thumbnail/%Y/%m/%d')
    participants_openchat_link = models.CharField(max_length=500, null=False, blank=False)
    neulhaerang_status = models.CharField(max_length=100, null=False, blank=False)
    rejected_message = models.CharField(max_length=1000, null=True, blank=False)
    member = models.ForeignKey(Member, null=False, blank=False, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, null=False, blank=False, on_delete=models.CASCADE)

    class Meta:
        db_table = 'tbl_neulhaerang'
        ordering = ["-id"]

class BusinessPlan(Period):
    plan_name = models.TextField(null=False, blank=False)
    plan_amount = models.IntegerField(null=False, blank=False, default=0)
    neulhaerang = models.ForeignKey(Neulhaerang, null=False, blank=False, on_delete=models.CASCADE)

    class Meta:
        db_table = 'tbl_business_plan'
        ordering = ["-id"]

class NeulhaerangLike(Period):
    member = models.ForeignKey(Member, null=False, blank=False, on_delete=models.CASCADE)
    neulhaerang = models.ForeignKey(Neulhaerang, null=True, blank=False, on_delete=models.SET_NULL)

    class Meta:
        db_table = 'tbl_neulhaerang_like'
        ordering = ["-id"]

class NeulhaerangTag(Period):
    tag_name = models.CharField(max_length=50,null=False, blank=False)
    tag_type = models.IntegerField(null=False, blank=False, default=0)
    neulhaerang = models.ForeignKey(Neulhaerang, null=False, blank=False, on_delete=models.CASCADE)

    class Meta:
        db_table = 'tbl_neulhaerang_tag'
        ordering = ["-id"]

class NeulhaerangInnerTitle(Period):
    inner_title_text = models.TextField(null=False, blank=False)
    neulhaerang_content_order = models.IntegerField(null=False, blank=False, default=0)
    neulhaerang = models.ForeignKey(Neulhaerang, null=False, blank=False, on_delete=models.CASCADE)

    class Meta:
        db_table = 'tbl_neulhaerang_inner_title'
        ordering = ["-id"]

class NeulhaerangInnerContent(Period):
    inner_content_text = models.TextField(null=False, blank=False)
    neulhaerang_content_order = models.IntegerField(null=False, blank=False, default=0)
    neulhaerang = models.ForeignKey(Neulhaerang, null=False, blank=False, on_delete=models.CASCADE)

    class Meta:
        db_table = 'tbl_neulhaerang_inner_content'
        ordering = ["-id"]

class NeulhaerangInnerPhotos(Period):
    inner_photo = models.ImageField(null=False, blank=False, upload_to='neulhaerang/innerphoto/%Y/%m/%d')
    neulhaerang_content_order = models.IntegerField(null=False, blank=False, default=0)
    photo_order = models.IntegerField(null=False, blank=False, default=0)
    photo_explanation = models.TextField(null=False, blank=False)
    neulhaerang = models.ForeignKey(Neulhaerang, null=False, blank=False, on_delete=models.CASCADE)

    class Meta:
        db_table = 'tbl_neulhaerang_inner_photos'
        ordering = ["-id"]

class NeulhaerangDonation(Period):
    donation_amount = models.IntegerField(null=False, blank=False, default=0)
    donation_content = models.CharField(max_length=500, null=False, blank=False)
    donation_anonymous = models.CharField(max_length=100, null=False, blank=False)
    neulhaerang = models.ForeignKey(Neulhaerang, null=True, blank=False, on_delete=models.SET_NULL)
    member = models.ForeignKey(Member, null=False, blank=False, on_delete=models.CASCADE)
    class Meta:
        db_table = 'tbl_neulhaerang_donation'
        ordering = ["-id"]

class NeulhaerangParticipants(Period):
    neulhaerang = models.ForeignKey(Neulhaerang, null=True, blank=False, on_delete=models.SET_NULL)
    member = models.ForeignKey(Member, null=False, blank=False, on_delete=models.CASCADE)
    class Meta:
        db_table = 'tbl_neulhaerang_participants'
        ordering = ["-id"]

class NeulhaerangReply(Period):
    reply_content = models.CharField(max_length=1000, null=False, blank=False)
    member = models.ForeignKey(Member, null=False, blank=False, on_delete=models.CASCADE)
    neulhaerang = models.ForeignKey(Neulhaerang, null=True, blank=False, on_delete=models.SET_NULL)
    donation = models.ForeignKey(NeulhaerangDonation, null=True, blank=False, on_delete=models.CASCADE)
    class Meta:
        db_table = 'tbl_neulhaerang_reply'
        ordering = ["-id"]

class ReplyLike(Period):
    member = models.ForeignKey(Member, null=False, blank=False, on_delete=models.CASCADE)
    neulhaerang_reply = models.ForeignKey(NeulhaerangReply, null=False, blank=False, on_delete=models.CASCADE)
    class Meta:
        db_table = 'tbl_reply_like'
        ordering = ["-id"]

class Byeoljji(Period):
    byeoljji_name = models.CharField(max_length=100, null=False, blank=False)
    byeoljji_img = models.ImageField(null=True, blank=False, upload_to='neulhaerang/byeoljji/%Y/%m/%d')
    byeoljji_rank = models.IntegerField(null=False, blank=False, default=0)
    byeoljji_count = models.IntegerField(null=False, blank=False, default=0)
    neulhaerang = models.ForeignKey(Neulhaerang, null=False, blank=False, on_delete=models.CASCADE)
    class Meta:
        db_table = 'tbl_byeoljji'
        ordering = ["-id"]

class MemberByeoljji(Period):
    member = models.ForeignKey(Member, null=False, blank=False, on_delete=models.CASCADE)
    byeoljji = models.ForeignKey(Byeoljji, null=True, blank=False, on_delete=models.SET_NULL)

    class Meta:
        db_table = 'tbl_member_byeoljji'
        ordering = ["-id"]