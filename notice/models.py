from django.db import models

from member.models import Member
from workspace.models import Period


# Create your models here.
class Notice(Period):
    type = models.CharField(max_length=30, null=False, blank=False)
    notice_title = models.TextField(null=False, blank=False)
    notice_content = models.TextField(null=False, blank=False)
    notice_image = models.ImageField(null=True, blank=False, upload_to='notice/ype')
    admin = models.ForeignKey(Member, null=False, on_delete=models.DO_NOTHING)

    class Meta:
        db_table = 'tbl_notice'
