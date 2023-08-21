import math


class Pagenation():
    def __init__(self,page,row_count,model,page_count):
        self.page =page
        self.row_count =row_count
        self.offset = (page - 1) * row_count
        self.limit = page * row_count
        self.total = model.objects.all().count()
        self.page_count = page_count
        self.end_page = math.ceil(page / page_count) * page_count
        self.start_page = self.end_page - self.page_count + 1
        self.real_end = math.ceil(self.total / self.row_count)
        self.end_page = self.real_end if self.end_page > self.real_end else self.end_page
        self.has_next = self.real_end>self.end_page
        self.has_prev = self.start_page>1
        self.paged_models = model.objects.all()[self.offset:self.limit]


class CategoryPagenation():
    def __init__(self,page,row_count,model,page_count, category_id=None):
        self.page =page
        self.row_count =row_count
        self.offset = (page - 1) * row_count
        self.limit = page * row_count
        self.total = model.objects.all().count()
        self.page_count = page_count
        self.end_page = math.ceil(page / page_count) * page_count
        self.start_page = self.end_page - self.page_count + 1
        self.real_end = math.ceil(self.total / self.row_count)
        self.end_page = self.real_end if self.end_page > self.real_end else self.end_page
        self.has_next = self.real_end>self.end_page
        self.has_prev = self.start_page>1
        if category_id is not None:
            self.paged_models = model.objects.all().filter(category_id=category_id)[self.offset:self.limit]
        else:
            self.paged_models = model.objects.all()[self.offset:self.limit]
        self.category_id = category_id
