from django.db import models

from member.models import Member
from workspace.models import Period
# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=100, null=False, blank=False)
    class Meta:
        db_table = 'tbl_category'

class Badge(models.Model):
    badge_name = models.CharField(max_length=100, null=False, blank=False)
    badge_content = models.TextField(null=False, blank=False)
    badge_image = models.ImageField(null=False, blank=False)
    category = models.ForeignKey(Category, null=False, blank=False, on_delete=models.DO_NOTHING)
    class Meta:
        db_table = 'tbl_badge'

class MemberBadge(Period):
    member = models.ForeignKey(Member, null=False, blank=False, on_delete=models.DO_NOTHING)
    badge = models.ForeignKey(Badge, null=False, blank=False, on_delete=models.DO_NOTHING)
    class Meta:
        db_table = 'tbl_member_badge'
        ordering = ["-id"]

