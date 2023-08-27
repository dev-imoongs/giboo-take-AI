import math


class Pagenation():
    def __init__(self,page,row_count,page_count,query_set):
        self.page =page
        self.row_count =row_count
        self.offset = (page - 1) * row_count
        self.limit = page * row_count
        if type(query_set)==list:
            self.total = len(query_set)
        else:
            self.total = query_set.count()
        self.page_count = page_count
        self.end_page = math.ceil(page / page_count) * page_count
        self.start_page = self.end_page - self.page_count + 1
        self.real_end = math.ceil(self.total / self.row_count)
        self.end_page = self.real_end if self.end_page > self.real_end else self.end_page
        self.has_next = self.real_end>self.end_page
        self.has_prev = self.start_page>1
        self.has_next_data = self.total>self.limit
        self.paged_models = query_set[self.offset:self.limit]

