from django.db import models

from member.models import Member
from workspace.models import Period


# Create your models here.
class Inquery(Period):
    inquery_title = models.TextField(null=False, blank=False)
    inquery_content = models.TextField(null=False, blank=False)
    response_status = models.CharField(max_length=50, null=False, blank=False)
    member = models.ForeignKey(Member, null=False, on_delete=models.DO_NOTHING)

    class Meta:
        db_table = 'tbl_inquery'


class Inquery_response(Period):
    response_content = models.TextField(null=False, blank=False)
    admin = models.ForeignKey(Member, null=False, on_delete=models.DO_NOTHING)
    inquery = models.ForeignKey(Inquery, null=False, on_delete=models.DO_NOTHING)


class Alram(Period):
    message = models.TextField(null=False, blank=False)
    isChecked = models.CharField(max_length=30, null=False, blank=False)
    page_link = models.CharField(max_length=200, null=True, blank=False)
    member = models.ForeignKey(Member, null=False, on_delete=models.DO_NOTHING)