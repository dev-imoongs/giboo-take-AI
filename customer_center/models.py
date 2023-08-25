from django.db import models

from member.models import Member
from neulhaerang.models import Neulhaerang
from neulhaerang_review.models import NeulhaerangReview
from neulhajang.models import Neulhajang
from workspace.models import Period


# Create your models here.
class Inquery(Period):
    inquery_title = models.TextField(null=False, blank=False)
    inquery_content = models.TextField(null=False, blank=False)
    response_status = models.CharField(max_length=50, null=False, blank=False)
    member = models.ForeignKey(Member, null=False, on_delete=models.CASCADE)
    class Meta:
        db_table = 'tbl_inquery'
        ordering = ["-id"]

class InqueryResponse(Period):
    response_content = models.TextField(null=False, blank=False)
    admin = models.ForeignKey(Member, null=False, on_delete=models.CASCADE)
    inquery = models.ForeignKey(Inquery, null=False, on_delete=models.CASCADE)
    class Meta:
        db_table = 'tbl_inquery_response'
        ordering = ["-id"]


class Alarm(Period):
    message = models.TextField(null=False, blank=False)
    isChecked = models.CharField(max_length=30, null=False, blank=False)
    member = models.ForeignKey(Member, null=False, on_delete=models.CASCADE)
    type = models.TextField()
    reference_id = models.IntegerField(null=False, default=0)

    class Meta:
        db_table = 'tbl_alarm'
        ordering = ["-id"]
