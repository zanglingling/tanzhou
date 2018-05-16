#!/usr/bin/python
# -*- coding:utf-8 -*-


class Paginator(object):
    def __init__(self, totalCount, currentPage, perPageNum=30, maxPage=10):
        # 数据总个数
        self.total_count = totalCount
        # 当前页
        try:
            self.current_page = int(currentPage)
        except Exception as e:
            self.current_page = 1
        # 每页显示的行数
        self.per_page_num = perPageNum
        # 最多显示页数（最好选择奇数）
        self.max_page = maxPage

    # 切片起始
    def start(self):
        return (self.current_page - 1) * self.per_page_num

    # 切片终止
    def end(self):
        return self.current_page * self.per_page_num

    # 总页数
    @property
    def num_pages(self):
        a, b = divmod(self.total_count, self.per_page_num)
        if b == 0:
            return a
        return a + 1

    # 显示页码范围
    def pager_num_range(self):
        if self.num_pages <= self.max_page:  # 总页数小于显示最大页数
            return range(1, self.num_pages)
        part = int(self.max_page / 2)  # 取显示页数的一半
        if self.current_page <= part:  # 当前页小于一半
            return range(1, self.max_page + 1)
        if self.current_page > part:  # 当前页大于一半
            return range(self.num_pages - self.max_page + 1, self.num_pages + 1)
        return range(self.current_page - part, self.current_page + part + 1)  # 总页数大于最大页数



