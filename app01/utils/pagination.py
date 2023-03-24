from django.utils.safestring import mark_safe
from django .http.request import QueryDict
import copy

"""
Page tools defined by ourselves

# 1. Filter out all data from database based on our needs
queryset = models.TableName.objects.all()

context = {
    "queryset": page_object.page_queryset, # data after split pages
    "page_string": page_object.html() # generate page numbers 
    }
    return render(request, '.html', context)
    
In .html page
    
    {% for obj in queryset %}
        {{ obj.xx }}
    {% endfor %}
    
    <ul class="pagination">
        {{ page_string }}
    </ul>
    
"""

class Pagination(object):

    def __init__(self, request, queryset, page_param="page", page_size = 15, plus = 5):

        query_dict = copy.deepcopy(request.GET)
        query_dict._mutable = True
        self.query_dict = query_dict





        page = request.GET.get(page_param, "1")
        if page.isdecimal():
            page = int(page)
        else:
            page = 1
        self.page = page
        self.page_size = page_size
        self.start = (page - 1) * page_size
        self.end = page * page_size
        self.page_queryset = queryset[self.start:self.end]
        total_count = queryset.count()
        total_page_count, div = divmod(total_count, page_size)
        if div:
            total_page_count += 1
        self.total_page_count = total_page_count
        self.plus = plus
        self.page_param = page_param

    def html(self):
        print(self.total_page_count)
        if self.total_page_count <= 2 * self.plus + 1:
            start_page = 1
            end_page = self.total_page_count
        else:
            # When the page < plus
            if self.page <= self.plus:
                start_page = 1
                end_page = 2 * self.plus + 1
            else:
                # When the page + plus > total page number
                if self.page + self.plus > self.total_page_count:
                    start_page = self.total_page_count - 2 * self.plus
                    end_page = self.total_page_count
                else:
                    start_page = self.page - self.plus
                    end_page = self.page + self.plus

        # PageNumber
        page_str_list = []

        self.query_dict.setlist(self.page_param, [1])

        # First page
        if self.total_page_count:
            first = '<li><a href="?{}">First</a><li>'.format(self.query_dict.urlencode())
            page_str_list.append(first)

        # Previous page
        if self.page > 1:
            self.query_dict.setlist(self.page_param, [self.page - 1])
            prev = '<li><a href="?{}">Previous</a><li>'.format(self.query_dict.urlencode())
        else:
            self.query_dict.setlist(self.page_param, [1])
            prev = '<li><a href="?{}">Previous</a><li>'.format(self.query_dict.urlencode())
        page_str_list.append(prev)

        for i in range(start_page, end_page + 1):
            self.query_dict.setlist(self.page_param, [i])
            if i == self.page:
                ele = '<li class="active"><a href="?{}">{}</a><li>'.format(self.query_dict.urlencode(), i)
            else:
                ele = '<li><a href="?{}">{}</a><li>'.format(self.query_dict.urlencode(), i)
            page_str_list.append(ele)

        # Next page
        if self.page < self.total_page_count:
            self.query_dict.setlist(self.page_param, [self.page + 1])
            next = '<li><a href="?{}">Next</a><li>'.format(self.query_dict.urlencode())
        else:
            self.query_dict.setlist(self.page_param, [self.total_page_count])
            next = '<li><a href="?{}">Next</a><li>'.format(self.query_dict.urlencode())
        page_str_list.append(next)

        if self.total_page_count:
            # Last page
            self.query_dict.setlist(self.page_param, [self.total_page_count])
            last = '<li><a href="?{}">Last</a><li>'.format(self.query_dict.urlencode())
            page_str_list.append(last)

        page_string = mark_safe("".join(page_str_list))

        return page_string
"""
<li><a href="/num/list?page=1">1</a></li>
<li><a href="/num/list?page=2">2</a></li>
<li><a href="/num/list?page=3">3</a></li>
<li><a href="/num/list?page=4">4</a></li>
<li><a href="/num/list?page=5">5</a></li>
"""